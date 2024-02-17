// pages/about.js

import { Button, TextField } from '@mui/material';
import axios from 'axios';
import React, { useEffect, useState } from 'react';

const questions = ["What is the correct form of the verb 'to be' in the sentence: 'She  a doctor'?", "Correct the grammatical error in this sentence: 'Me and my friend is going to the park.'", "Fill in the blank with the correct form of the verb: 'If I  a millionaire, I would buy a house on the beach.'", "Identify the grammatical structure of this sentence: 'The dog that is barking is mine.'", "Explain the difference between 'I have eaten' and 'I was eating' in terms of grammar and context.", "Correct the sentence if it's grammatically incorrect: 'She don't like apples.'", "What is the past tense of the verb 'run'?", "Which sentence is written in the past tense: 'I run to the store.' or 'I ran to the store.'", "What is the plural form of the word 'child'?", "Identify the subject and predicate in this sentence: 'The cat is sleeping on the couch.'"]

// Question component. Takes text as input, provides a text area below
const Question = ({ text, onTextUpdate}) => {
  return (
    <div className="w-full max-w-lg">
      <p>{text}</p>
      <div className="flex items-center space-x-2">
        {/* text input from mui */}
        <TextField className="max-h-[100px] w-full resize-none text-base" placeholder="Type your response here." onChange={(e) => onTextUpdate(e.target.value)}/>
      </div>
    </div>
  )
}

const updateIdx = (newValue: string, idx: number, answers, setAnswers) =>  {
  const newAnswers = [...answers];
  newAnswers[idx] = newValue;
  setAnswers([...newAnswers]);
}

const AboutPage = () => {
  const [inputValue, setInputValue] = useState(''); // State for the input value
  const [paragraphs, setParagraphs] = useState([]); // State for the list of paragraphs
  // initialize as array of length 10 empty strings
  const [answers, setAnswers] = useState(Array(10).fill('')); // State for the list of paragraphs


  useEffect(() => {
    const fetchData = async () => {
      // const data = await axios.get('http://localhost:5000/')
      // console.log(data)
      setParagraphs(questions);
      return 
    }
    fetchData()

  }, [])


  // Handler for input change
  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };

  // Handler for form submission
  const handleSubmit = (e) => {
    try {
      const data = axios.post('http://localhost:5000/funkp', {
        'submission': answers
      })
        .then(res => {
          console.log("success")
          console.log(res)
          console.log(res.data)
          setParagraphs([...paragraphs, "response " + res.data])
        })
    } catch (err) { 
      console.log(err)
    }


    e.preventDefault();
    if (inputValue.trim()) {
      setParagraphs([...paragraphs, inputValue]);
      setInputValue(''); // Clear the input after submission
    }
    console.log(answers)
  };


  return (
    <>
          <div className="flex w-full items-center">
        {/* map questions to component */}
        {paragraphs.map((paragraph, index) => (
          <Question key={index} text={paragraph} onTextUpdate = {(newValue) => updateIdx(newValue, index, answers, setAnswers)}/>
        ))}
            <Button type="submit" variant="contained" onClick={handleSubmit}>Submit</Button>
      </div>
    </>
  )
};

export default AboutPage;