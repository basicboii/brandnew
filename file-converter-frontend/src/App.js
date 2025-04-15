import React, { useState } from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "./components/login";
import Upload from "./components/Upload";
import Navbar from "./components/Navbar";

const App = () => {
  const [token, setToken] = useState(localStorage.getItem("token"));

  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Login setToken={setToken} />} />
        <Route path="/upload" element={token ? <Upload token={token} /> : <h2>Please login first</h2>} />
      </Routes>
    </Router>
  );
};

export default App;
