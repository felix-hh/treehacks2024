import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './index.css';
import App from './App';

// Import your other components here
import Nutrition from './Components/NutritionPlanner';
import Workout from './Components/WorkoutPlanner';
import Social from './Components/SocialForum';

ReactDOM.render(
  <React.StrictMode>
    <Router>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="/Home" element={<App />} />
        <Route path="/WorkoutPlanner" element={<Workout />} />
        <Route path="/Message" element={<Nutrition />} />
        <Route path="/SocialForum" element={<Social />} />
        {/* Add more Routes for other components as needed */}
      </Routes>
    </Router>
  </React.StrictMode>,
  document.getElementById('root')
);
