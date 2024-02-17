import React from 'react'
import heroImage from "../combined2.png"; // replace this with the path to your image

const Hero = () => {
  return (
    <div 
      style={{
        backgroundImage: `url(${heroImage})`,
        backgroundColor: 'white',
        height: '100vh',
        width: '100%',
        backgroundPosition: 'center',
        backgroundRepeat: 'no-repeat',
        backgroundSize: 'cover',
        overflowX: 'hidden',
      }}
    >
      {/* Put any text/content you want to overlay on the image here */}
    </div>
  )
}

export default Hero
