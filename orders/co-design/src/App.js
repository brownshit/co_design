import React from 'react';
import { Route, Routes, Link } from 'react-router-dom';
import Main from './Main';
import Html1 from './html1'; // Import Html1 component

function App() {
  return (
    <div>
      <Routes>
        <Route path="/" element={<Main />} />
        <Route path="/html1" element={<Html1 />} />
      </Routes>
    </div>
  );
}

export default App;