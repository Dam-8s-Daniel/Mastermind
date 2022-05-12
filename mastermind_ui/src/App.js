import React from "react"
import { useEffect, useState} from "react";
import './App.css';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'
import Header from './pages/header'
import Home from './pages/home'
import Results from './pages/results'
import HowToPlay from './pages/howto'
import Settings from './pages/settings'
import Contact from './pages/contact'

function App() {
  
  useEffect(() => {
    fetch('http://localhost:4000/startgame')
      .then(res => res.json())
      .then(json)
  }, [])
  
  
  
  
  
  
  return (
    
    <Router>
      <div>
        <Header/>
      </div>
      <Routes>
        <Route path='/' element={<Home/>} />
        <Route path='/Results' element={<Results/>} />
        <Route path='/info' element={<HowToPlay/>} />
        <Route path='/settings' element={<Settings/>} />
        <Route path='/contact' element={<Contact/>} />
      </Routes>
      
    </Router>

  );
}

export default App;
