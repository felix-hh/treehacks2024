'use client'

import Link from "next/link"
import Image from "next/image";
import { useEffect, useState } from 'react';
import styles from "./page.module.css";

export default function Home() {
  // Subtitles array
  const subtitles = [
    "Discover Languages",
    "Explore Cultures",
    "Connect Globally",
  ];

  // State to keep track of the current subtitle
  const [currentSubtitle, setCurrentSubtitle] = useState(subtitles[0]);
  // State to keep track of the current index
  const [index, setIndex] = useState(0);
  const [fade, setFade] = useState(true); // true for fade-in, false for fade-out

  useEffect(() => {
    const changeTextTimeout = setTimeout(() => {
      // Calculate the next index directly here
      const nextIndex = (index + 1) % subtitles.length;
      setIndex(nextIndex); // Update the index state
      setCurrentSubtitle(subtitles[nextIndex]); // Set the next subtitle based on the next index
      setFade(true); // Assuming you want to trigger some fade in effect here
    }, 3000); // Change text every 3 seconds
  
    // Start fade out slightly before changing text
    const fadeOutTimeout = setTimeout(() => setFade(false), 2500);
  
    return () => {
      clearTimeout(fadeOutTimeout);
      clearTimeout(changeTextTimeout);
    };
  }, [index, subtitles.length]); // Depend on `index` instead of `currentSubtitle`
  
  return (
    <main className={styles.main}>
       <div className={styles.center}>
        <Image
          src="/tree.png"
          alt="Treelingo"
          width={200}
          height={200}
          priority
        />
        <p className={styles.title}>Treelingo</p>
        <p className={styles.subtitle}>{currentSubtitle}</p>
      </div>
      <div className="flex items-center justify-center p-4">
        <Link
          aria-label="Next"
          className="rounded-full bg-gray-900 w-10 h-10 flex items-center justify-center shadow-md text-gray-50 hover:bg-gray-900/90 dark:bg-gray-50 dark:text-gray-900 dark:hover:bg-gray-900/10"
          href="#"
        >
          <svg
            className="w-6 h-6"
            fill="none"
            height="24"
            viewBox="0 0 24 24"
            width="24"
            xmlns="http://www.w3.org/2000/svg"
            style={{ stroke: "#2b593e" }}
          >
            <path
              d="M17 12L12 17M12 17L7 12M12 17L12 7"
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
            />
          </svg>
        </Link>
      </div>
    </main>
  )
}
