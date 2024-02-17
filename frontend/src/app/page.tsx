'use client'

import AboutPage from '../pages/example/index'; 
// import Image from "next/image";
// import { useEffect, useState } from 'react';
// import styles from "./page.module.css";

// export default function Home() {
//   // Subtitles array
//   const subtitles = [
//     "Discover Languages",
//     "Explore Cultures",
//     "Connect Globally",
//   ];

//   // State to keep track of the current subtitle
//   const [currentSubtitle, setCurrentSubtitle] = useState(subtitles[0]);
//   // State to keep track of the current index
//   const [index, setIndex] = useState(0);
//   const [fade, setFade] = useState(true); // true for fade-in, false for fade-out
//   const [showNewComponent, setShowNewComponent] = useState(false);

//   useEffect(() => {
//     const changeTextTimeout = setTimeout(() => {
//       // Calculate the next index directly here
//       const nextIndex = (index + 1) % subtitles.length;
//       setIndex(nextIndex); // Update the index state
//       setCurrentSubtitle(subtitles[nextIndex]); // Set the next subtitle based on the next index
//       setFade(true); // Assuming you want to trigger some fade in effect here
//     }, 3000); // Change text every 3 seconds
  
//     // Start fade out slightly before changing text
//     const fadeOutTimeout = setTimeout(() => setFade(false), 2500);
  
//     return () => {
//       clearTimeout(fadeOutTimeout);
//       clearTimeout(changeTextTimeout);
//     };
//   }, [index, subtitles.length]); // Depend on `index` instead of `currentSubtitle`

//   const handleArrowClick = () => {
//     setShowNewComponent(true); // Toggle visibility to show NewComponent
//   };
  
//   return (
//     <main className={styles.main}>
//       {!showNewComponent ? (
//         <div className={styles.center}>
//           <Image src="/tree.png" alt="Treelingo" width={200} height={200} priority />
//           <p className={styles.title}>Treelingo</p>
//           <p className={styles.subtitle}>{currentSubtitle}</p>
//         </div>
//       ) : (
//         <AboutPage />
//       )}
//       <div className="flex items-center justify-center p-4">
//         <button onClick={handleArrowClick} className="rounded-full bg-gray-900 w-10 h-10 flex items-center justify-center shadow-md text-gray-50 hover:bg-gray-900/90 dark:bg-gray-50 dark:text-gray-900 dark:hover:bg-gray-900/10">
//           <svg className="w-6 h-6" fill="none" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg" style={{ stroke: "#2b593e" }}>
//             <path d="M17 12L12 17M12 17L7 12M12 17L12 7" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" />
//           </svg>
//         </button>
//       </div>
//     </main>
//   );
// }
import { motion, AnimatePresence } from 'framer-motion';
import Image from "next/image";
import React, { useState, useEffect } from 'react';
import styles from "./page.module.css";

export default function Home() {
  const subtitles = ["Discover Languages", "Explore Cultures", "Connect Globally"];
  const [currentSubtitle, setCurrentSubtitle] = useState(subtitles[0]);
  const [index, setIndex] = useState(0);
  const [showNewComponent, setShowNewComponent] = useState(false);

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentSubtitle(subtitles[(index + 1) % subtitles.length]);
      setIndex(index + 1);
    }, 3000);
    return () => clearInterval(interval);
  }, [index, subtitles]);

  const arrowStyle = {
    transform: showNewComponent ? 'rotate(180deg)' : 'rotate(0deg)',
    transition: 'transform 0.3s ease-in-out',
  };
  // Animation variants for initial and new content
  const containerVariants = {
    hidden: { opacity: 0, y: -20 },
    visible: { opacity: 1, y: 0 },
    exit: { opacity: 0, y: 20 },
  };

  return (
    <main className={styles.main}>
      <AnimatePresence mode='wait'>
        {!showNewComponent ? (
          <motion.div
            key="content"
            initial="hidden"
            animate="visible"
            exit="exit"
            variants={containerVariants}
            transition={{ duration: 0.5 }}
            className={styles.center}
          >
            <Image src="/tree.png" alt="Treelingo" width={200} height={200} priority />
            <p className={styles.title}>Treelingo</p>
            <motion.p
              key={currentSubtitle} // Change key to trigger animation on update
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              transition={{ duration: 0.5 }}
              className={styles.subtitle}
            >
              {currentSubtitle}
            </motion.p>
          </motion.div>
        ) : (
          <motion.div
            key="newComponent"
            initial="hidden"
            animate="visible"
            exit="exit"
            variants={containerVariants}
            transition={{ duration: 0.5 }}
          >
            <AboutPage />
          </motion.div>
        )}
      </AnimatePresence>
      <div className="flex items-center justify-center p-4">
      <button
        onClick={() => setShowNewComponent(!showNewComponent)}
        className="your-custom-class" // Use your custom class here instead of inline styles if preferred
        style={{
          ...arrowStyle,
          background: 'transparent', // Ensures the button background is transparent
          border: 'none', // Removes any border
          boxShadow: 'none', // Removes any shadow effects
        }}
      >
          <svg className="w-6 h-6" fill="none" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg" style={{ stroke: "#2b593e" }}>
             <path d="M17 12L12 17M12 17L7 12M12 17L12 7" strokeLinecap="round" strokeLinejoin="round" strokeWidth="3" />
           </svg>
        </button>
      </div>
    </main>
  );
}
