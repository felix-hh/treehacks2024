import random

def model_get_question():
  questions = [
    "What is the correct form of the verb 'to be' in the sentence: 'She  a doctor'?", 
    "Correct the grammatical error in this sentence: 'Me and my friend is going to the park.'", 
    "Fill in the blank with the correct form of the verb: 'If I  a millionaire, I would buy a house on the beach.'", 
    "Identify the grammatical structure of this sentence: 'The dog that is barking is mine.'", 
    "Explain the difference between 'I have eaten' and 'I was eating' in terms of grammar and context.", 
    "Correct the sentence if it's grammatically incorrect: 'She don't like apples.'", 
    "What is the past tense of the verb 'run'?", 
    "Which sentence is written in the past tense: 'I run to the store.' or 'I ran to the store.'", 
    "What is the plural form of the word 'child'?", 
    "Identify the subject and predicate in this sentence: 'The cat is sleeping on the couch.'"
    "What is the past tense of read",
    "What is the past perfect tense of run",
    "Explain the difference between 'good' and 'better'",
    "Find the mistake in the following sentence 'I dye my hair blue yesterday'"
  ]
  random.shuffle(questions)
  return questions[:3]

def model_post_answer(answer):
  print(f'Registering submission: {answer}')