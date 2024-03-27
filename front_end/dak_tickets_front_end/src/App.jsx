import { useState } from 'react'
 
import { Route, Routes} from 'react-router-dom'
import Header from './components/Header'
import Main from './components/Main'
import Footer from './components/Footer'

import './App.css'

function App() {
  

  return (
    < div className='app'>
      <Header />
        <Main />
      <Footer />
    </div>
  )
}

export default App
