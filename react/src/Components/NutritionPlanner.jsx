import React from 'react';
import Navbar from './Home_Components/Navbar';
import ChatbotBox from './Nutrition_Components/ChatbotBox';
import AIPowered from './Nutrition_Components/AIPowered';
import ImageBanner from './message planner banner.svg'; // Import the SVG file

const NutritionPlanner = () => {
  return (
    <div>
      <Navbar />
      <div>
        <img src={ImageBanner} alt="Banner" style={{ width: '100%', height: 'auto' }} />
      </div>
      <div style={{ marginLeft: '13%', padding: '20px', width: '100%', maxWidth: '1000px' }}>
        <ChatbotBox />
      </div>
      <AIPowered />
    </div>
  );
};

export default NutritionPlanner;
