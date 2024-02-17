import React from 'react';
import { Carousel } from 'react-responsive-carousel';
import "react-responsive-carousel/lib/styles/carousel.min.css";
import { AiOutlineMail } from 'react-icons/ai';
import { RiMailSendLine } from 'react-icons/ri';
import { FiPenTool } from 'react-icons/fi';

const Body = () => {
  const icons = [<AiOutlineMail size={50} />, <RiMailSendLine size={50} />, <FiPenTool size={50} />];

  const whiteBoxes = [
    { 
      title: 'Revolutionary Email Analysis',
      content: 'Experience the power of Split\'s cutting-edge technology that transcends mere analysis. Our state-of-the-art machine learning algorithms delve deep into your previous emails, decoding the very essence of your unique syntax and style, unraveling the intricacies of your communication prowess.'
    },
    {
      title: 'Unleash the Power of AI-Generated Emails',
      content: 'Unleash the true potential of your email correspondence with Split\'s unparalleled innovation. Our advanced AI seamlessly crafts emails that embody your authentic voice, mimicking your style and linguistic finesse flawlessly. Witness a new era where your digital correspondence is elevated to unprecedented heights.'
    },
    {
      title: 'Master the Art of Style and Tone',
      content: 'Step into a world where your emails resonate effortlessly with every recipient. Through the remarkable prowess of our AI-generated emails, Split ensures that the tone and style adapt seamlessly to every context. Leave a lasting impression with emails that strike the perfect chord, whether it\'s a formal business proposal or a friendly follow-up.'
    },
    {
      title: 'Unwavering Consistency, Unmatched Brilliance',
      content: 'Discover the hallmark of excellence that is synonymous with Split. We guarantee unwavering consistency in every email you send. With our transformative technology, you\'ll witness a symphony of brilliance resonating through every word, leaving recipients captivated by your consistently impressive communication style.'
    },
    {
      title: 'Skyrocket Your Response Rates',
      content: 'Prepare to witness a quantum leap in your email success rates. Split\'s groundbreaking algorithm unlocks unprecedented response rates for your cold emails. Experience the power of up to a 2 times increase in engagement, as your messages break through the noise and captivate your audience with unparalleled finesse.'
    },
    {
      title: 'Unlock Precious Time',
      content: 'Embrace efficiency like never before with Split\'s industry-leading AI. Our cutting-edge technology empowers you to save up to an astounding 34% of your valuable work time. Unshackle yourself from the mundane task of crafting emails, and redirect your energy towards what truly matters – achieving your goals and driving exceptional results.'
    },
  ];
  

  return (
    <div
      style={{
        background: '#305E48',
        height: '100vh',
        width: '100%',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        overflow: 'hidden', // Changed from 'overflowX: hidden' to 'overflow: hidden' to hide vertical scrollbar
      }}
    >
      <Carousel
        showThumbs={false}
        infiniteLoop
        autoPlay
        interval={2000}
        centerMode
        dynamicHeight
        emulateTouch
      >
        {whiteBoxes.map((box, index) => (
          <div
            key={box.title}
            style={{
              backgroundColor: 'white',
              // Height and width adjusted to be less than 100% for smaller screen sizes
              height: '80vh',
              width: '80%',
              margin: '0 auto', // Changed margin to '0 auto' to center the box
              boxShadow: '0 2px 8px rgba(0,0,0,0.2)',
              padding: '1.5em',
              borderRadius: '5px',
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              justifyContent: 'center',
              textAlign: 'center',
            }}
          >
            <div style={{ marginBottom: '0.5em' }}>{icons[index % icons.length]}</div>
            <div>
              <h2>{box.title}</h2>
              <p style={{ fontSize: '2em' }}>{box.content}</p> {/* Increased font size for the card content */}
            </div>
          </div>
        ))}
      </Carousel>
    </div>
  );
};

export default Body;
