// pages/about.js

import axios from 'axios';
import React, { useEffect, useState } from 'react';

const AboutPage = () => {
  const [inputValue, setInputValue] = useState(''); // State for the input value
  const [paragraphs, setParagraphs] = useState([]); // State for the list of paragraphs


  useEffect(() => {
    const fetchData = async () => {
      const data = await axios.get('http://localhost:5000/')
      console.log(data)
      setParagraphs([data.data]);
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
    e.preventDefault();
    if (inputValue.trim()) {
      setParagraphs([...paragraphs, inputValue]);
      setInputValue(''); // Clear the input after submission
    }
  };

  return (
    <div>
      <h1>About Us</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={inputValue}
          onChange={handleInputChange}
          placeholder="Enter text for a new paragraph"
        />
        <button type="submit">Add Paragraph</button>
      </form>
      <div>
        {paragraphs.map((paragraph, index) => (
          <p key={index}>{paragraph}</p>
        ))}
      </div>
    </div>
  );
};

export default AboutPage;