// pages/about.js

import { Button, TextField } from '@mui/material';
import axios from 'axios';
import React, { useEffect, useState } from 'react';
// import {MultiPlayer, useMultiAudio} from '../../components/MultiPlayer'
import type { NextPage } from 'next'
import dynamic from 'next/dynamic';
const MultiPlayer = dynamic(() => import('../../components/MultiPlayer'), { ssr: false })


const arr = ["fun"]
// Question component. Takes text as input, provides a text area below
const Question = ({ text, onTextUpdate }) => {
  return (
    <div className="w-full max-w-lg">
      <p>{text}</p>
      <div className="flex items-center space-x-2">
        {/* text input from mui */}
        <TextField className="max-h-[100px] w-full resize-none text-base" placeholder="Type your response here." onChange={(e) => onTextUpdate(e.target.value)} />
      </div>
    </div>
  )
}

const isSSREnabled = () => typeof window === 'undefined';


const updateIdx = (newValue: string, idx: number, answers, setAnswers) => {
  const newAnswers = [...answers];
  newAnswers[idx] = newValue;
  setAnswers([...newAnswers]);
}

const AboutPage = () => {
  if (!isSSREnabled()) {
    console.log('Browser')
  }
  else {
    console.log('Server')
  }
  // const [audios, toggleAudio] = useMultiAudio([
  const urls = [
    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
  ]
  // );

  //   // ### Audio components
  //   const MultiPlayer = ({ urls }) => {
  //   const [players, toggle] = useMultiAudio(urls);

  //   return (
  //     <div>
  //       {players.map((player, i) => (
  //         <Player key={i} player={player} toggle={toggle(i)} />
  //       ))}
  //     </div>
  //   );
  // };

  // const Player = ({ player, toggle }) => (
  //   <div>
  //     <p>Stream URL: {player.url}</p>
  //     <button onClick={toggle}>{player.playing ? "Pause" : "Play"}</button>
  //   </div>
  // );



  const [inputValue, setInputValue] = useState(''); // State for the input value
  const [paragraphs, setParagraphs] = useState([]); // State for the list of paragraphs
  // initialize as array of length 10 empty strings
  const [answers, setAnswers] = useState(Array(10).fill('')); // State for the list of paragraphs

  useEffect(() => {
    const fetchData = async () => {
      const questions = await axios.get('http://localhost:5000/initial_questions')
      console.log(questions)
      setParagraphs(questions.data);
      return
    };
    fetchData()
  }, [])


  // Handler for input change
  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };

  // Handler for form submission
  const handleSubmit = (e) => {
    console.log(answers)
    try {
      const data = axios.post('http://localhost:5000/answers', {
        'submission': answers
      })
        .then(res => {
          console.log("success")
          setParagraphs(res.data)
        })
    } catch (err) {
      console.log(err)
    }


    e.preventDefault();
  };


  return (
    <>
      <div className="flex w-full items-center">
        {/* map questions to component */}
        {paragraphs.map((paragraph, index) => (
          <Question key={index} text={paragraph} onTextUpdate={(newValue) => updateIdx(newValue, index, answers, setAnswers)} />
        ))}
        <Button type="submit" variant="contained" onClick={handleSubmit}>Submit</Button>
      </div>
      {/* audio component (only if no ssr enabled)*/}
      {<MultiPlayer urls={urls} />}
      {/* <audio src={urls[0]} autoPlay controls></audio> */}
      {/* <Button onClick={() => toggleAudio(0)}>Play</Button> */}
    </>
  )
};

export default AboutPage;