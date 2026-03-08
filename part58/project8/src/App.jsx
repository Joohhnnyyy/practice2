import React from 'react'
import { Link,Routes, Route } from 'react-router-dom'
import Home from './pages/Home'
import About from './pages/About'
import Contact from './pages/Contact'
import Navbar from './components/Navbar'
import Test from './pages/Test'
import Notfound from './pages/Notfound'
import Products from './pages/Products'
import Womens from './pages/Womens'
import Mens from './pages/Mens'
import Footer from './components/Footer'

import { Router } from 'react-router-dom'

const App = () => {
  return (
    <div >
      <Navbar />
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/about' element={<About />} />
        <Route path='/contact' element={<Contact />} />
        <Route path='/contact/mens' element={<Mens />} />
        <Route path ='/contact/:Courseid' element={<Test />} />
        <Route path ='/products' element={<Products />} />
        <Route path = '/products/mens' element={<Mens />} />
        <Route path = '/products/womens' element={<Womens />} />
        <Route path='*' element={<Notfound />} />
      </Routes>
      <Footer />
    </div>
  )
}

export default App