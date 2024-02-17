import together
from openai import OpenAI
import json
import re
import sys
import os
import requests
import pdb

together_keys = ["587b6874cdc4afebe25881d426f72fee9fc845f2c91c9eab6c531df8a1455bf0", "7847ce8b8b7af361110830db9abfcda72ba058eb984b550d600488799cc26258"]
together.api_key = together_keys[0]

open_key = "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"
client = OpenAI(api_key=open_key)

model = "openai" # "openai" or "together
max_question_tries = 10
mini_target_questions = 1
target_questions = 4

categories = ["Grammar and Syntax Analysis", "Contextual Understanding", "Cultural Understanding"]
descriptions = ["Tasks that require the model to identify, correct, or generate examples of grammatical structures in context. This could involve exercises like filling in blanks with the correct form of a verb, identifying and correcting grammatical errors, or explaining the use of different grammatical structures.", "Tasks that require the model to understand and generate language based on context, audience, and purpose. This could involve recognizing and producing requests, understanding indirect speech acts (e.g., inferring that \"It's cold in here\" might be a request to close a window), or determining the appropriateness of certain phrases in specific social contexts.", "Language learning is deeply intertwined with cultural understanding. Tasks could involve understanding cultural references, understanding the cultural connotations of certain phrases or idioms, or generating language that is culturally appropriate for specific scenarios. Focus on tests that utilize cultural phrases and idioms in English, but do not ask for the meaning of the idiom itself. Rather, questions that require an indirect understanding of the idiom. Be creative with the cultural connotations, idioms, or references you include."]
extras = ["Grammar and Syntax Analysis task, which requires a human to solve exercises like filling in blanks with the correct form of a verb, identifying and correcting grammatical errors, or explaining the use of different grammatical structures.", " Contextual Understanding task, which requires a human to generate language based on context, audience, and purpose.", "Cultural Understanding task, which requires a human to explain cultural references, understand cultural connotations of phrases & idioms, and generate language that is culturally appropriate for specific scenarios."]

def create_questions(type_prompt, extra_context):
  global mini_target_questions
  text = f"Write down {mini_target_questions} unique questions to assess a human’s ability to understand language structure and context. Use the following format for your output: \
  [\
  \“Question1\”,\
  \“Question2\”,\
  \“Question3\”,\
  …\
  ]\
  \
  You will be evaluated on how well you actually perform. Your sentence structure and length can be creative; extrapolate based on the question description you are provided. Be both creative and cautious. Remember, you are writing text for a human to answer so make your question completely understandable by a human. Please design your questions to be accessible to someone who is learning English for the first time. Please design your questions using the following description: \
  {type_prompt}"
  if extra_context != "":
    text_2 = f"\nPlease adapt your questions to incorporate the following feature: {extra_context}. Only write down {mini_target_questions} unique questions."
  else:
    text_2 = ""

  return query(text+text_2)

def generate_questions(type_i, extra_context):
  global mini_target_questions

  list_mini_questions = []
  len_questions = 0
  j = 0
  while len_questions != mini_target_questions:
    j += 1
    if j > max_question_tries:
      sys.exit("Failed to generate questions")
    try:
      questions = create_questions(categories[type_i] + ": " + descriptions[type_i], extra_context)
      list_mini_questions = json.loads(questions)
      len_questions = len(list_mini_questions)
    
    except Exception as e:
      print(str(e))
      continue
  
  return list_mini_questions

def evaluate_mult_responses(type_prompt_prefix, questions, answers):
  text1 = f"I will provide you with a series of (question, answer) pairs for a {type_prompt_prefix} You will be asked to determine how accurate the answer is for the question:\n"
  text2 = '[' + ', '.join([f"({questions[i]}, {answers[i]})" for i in range(len(questions))]) + ']\n\n'
  text3 = "Grade on a scale from 1 to 10 where 1 represents a weak answer and 10 represents a very strong answer. Additionally, add a brief explanation for what the human likely misunderstood in question. Use the following format for your output, where each score corresponds to an integer between 1 and 10. \
  [(\"Score=4\", \"Explanation1\"), \n (\"Score=6\", \"Explanation2\"), \n (\"Score=2\", Explanation3\") \n …]."
  text4 = ""
  text = text1 + text2 + text3 + text4
  return query(text)

def parse_scores_and_explanations(score_string):
  pattern = re.compile(r'\(\"Score=(\d+)\", \"([^\"]+)\"\)')
  matches = pattern.findall(score_string)
  scores = [int(match[0]) for match in matches]  # Convert score strings to integers
  explanations = [match[1] for match in matches]
  return scores, explanations

def select_questions(qs, scores, threshold):
  return [i for i in range(len(qs)) if scores[i] <= threshold]

def synthesize_feedback(some_exps):
  text1 = "I will provide you with a series of explanations for why a human made a mistake in answering questions. Subsequently, I will ask you some questions to test your performance! Here are some explanations for you to memorize: \n"
  text2 = '[' + ', '.join([f"({some_exp})" for some_exp in some_exps]) + ']\n\n'
  text3 = "Using these specific examples, are there any common features in the explanations? Please focus on differences that are important for language translation as these questions are being used to train a human to learn the English language. Try to give descriptions that are specific enough that a language model could reliably produce questions that this entity would fail to answer correctly. For each common feature, include how you would design questions to include this common feature in the explanation. Generate the 4 most important common features you notice in a numbered format. Do not include any other text."
  text = text1 + text2 + text3
  synth = query(text)
  split_synth = re.split(r'\n(?=\d\.)', synth)
  return [x[3:] for x in split_synth]

def query_together(text):
  output = together.Complete.create(
    prompt = f"<human>:{text} \n<bot>:", 
    model = "mistralai/Mixtral-8x7B-Instruct-v0.1", 
    max_tokens = 2048,
    temperature = 0.2,
    top_k = 60,
    top_p = 0.6,
    repetition_penalty = 1.1,
    stop = ['<human>', '\n\n']
  )
  return output["output"]["choices"][0]["text"]

def query_openai(text):
  global open_key
  headers = {
    'Authorization': f'Bearer {open_key}',
    'Content-Type': 'application/json',
  }
  data = {
    "model": "gpt-4-turbo-preview",  # Replace with the actual model name for GPT-4 Turbo
    "messages": [
        {"role": "system", "content": text},
    ],
    "temperature": 0.4,
    "max_tokens": 2048
  }
  response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data).json()
  result = response["choices"][0]["message"]["content"]
  return result

def query(text):
  global model
  if model == "openai":
    return query_openai(text)
  elif model == "together":
    return query_together(text)

list_questions = []
list_answers = []
extra_contexts = ["" for _ in range(target_questions//mini_target_questions)]

def model_get_question():
  global list_questions
  list_questions = []

  for k in range(len(categories)):
    cat_questions = []
    for i in range(target_questions//mini_target_questions):
      mini_questions = generate_questions(k, extra_contexts[i])
      cat_questions.extend(mini_questions)
    list_questions.append(cat_questions)

  print(f'[TIME][{datetime.datetime.now()}] Sending new questions to flask app.')
  return list_questions

def model_post_answer(new_answers):
  global list_answers
  list_answers = new_answers[:]

  print(f'[TIME][{datetime.datetime.now()}] Receiving new set of answers from flask app.')

  execute_pipeline()

def execute_pipeline():
  global extra_contexts

  len_scores = 0
  response_scores = None
  response_explains = None
  i = 0
  while len_scores != len(categories) * target_questions:
    i += 1
    if i > 15:
        print("Failed to get scores")
        return

    try:
      # list_scores = single_wrapper(list_questions, list_answers)
      # print(list_scores)
      response_scores = []
      response_explains = []
      
      for k in range(len(categories)):
        response = parse_scores_and_explanations(evaluate_mult_responses(extras[k], list_questions[k], list_answers[target_questions*k:target_questions*(k+1)]))
        response_scores.extend(response[0]) 
        response_explains.extend(response[1]) 
  
      len_scores = len(response_scores)
      
      print("Response scores:", response_scores)
      print("Length:", len(response_scores))

    except:
      continue

  extra_contexts = synthesize_feedback([response_explains[i] for i in range(len(response_scores)) if response_scores[i] <= 5])
  print("New proposed domain:", extra_contexts)
  print("Length:", len(extra_contexts))


l = 0
while False:
  list_questions = []
  for k in range(len(categories)):
    cat_questions = []
    for i in range(target_questions//mini_target_questions):
      mini_questions = generate_questions(k, extra_contexts[i])
      cat_questions.extend(mini_questions)
    list_questions.append(cat_questions)
  
  print("Initial domain:",list_questions)
  print("Length:", len(list_questions))
  
  l += 1
  if l == 3:
    break

  list_answers = ["bear" for _ in range(len(list_questions)*len(list_questions[0]))]
  len_scores = 0
  response_scores = None
  response_explains = None
  i = 0
  while len_scores != len(categories)*target_questions:
    i += 1
    if i > 15:
      sys.exit("Failed to get scores")
    try:
      # list_scores = single_wrapper(list_questions, list_answers)
      # print(list_scores)
      response_scores = []
      response_explains = []
      
      for k in range(len(categories)):
        response = parse_scores_and_explanations(evaluate_mult_responses(extras[k], list_questions[k], list_answers[target_questions*k:target_questions*(k+1)]))
        response_scores.extend(response[0]) 
        response_explains.extend(response[1]) 
  
      len_scores = len(response_scores)
      
      print("Response scores:", response_scores)
      print("Length:", len(response_scores))

    except:
      continue
  extra_contexts = synthesize_feedback([response_explains[i] for i in range(len(response_scores)) if response_scores[i] <= 5])
  print("New proposed domain:", extra_contexts)
  print("Length:", len(extra_contexts))
