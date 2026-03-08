import React from 'react'
import { Link, NavLink } from 'react-router-dom'

const Navbar = () => {
  return (
    <div className='flex justify-between px-8 py-4 bg-gray-800 text-white'>
      <h2>NavBar</h2>
      <div className='flex gap-4'>
        <input type="text" placeholder="Search..." className='bg-gray-700 text-white placeholder:text-gray-400 border border-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500' />
        <NavLink to='/' style={({isActive}) => ({ color: isActive ? 'red' : 'white' })} className='text-white hover:scale-110'>Home</NavLink>
        <NavLink to='/about' style={({isActive}) => ({ color: isActive ? 'red' : 'white' })} className='text-white hover:scale-110'>About</NavLink>
        <NavLink to='/contact' style={({isActive}) => ({ color: isActive ? 'red' : 'white' })} className='text-white hover:scale-110'>Contact</NavLink>
        <NavLink to='/products' style={({isActive}) => ({ color: isActive ? 'red' : 'white' })} className='text-white hover:scale-110'>Products</NavLink>
      </div>
      <div></div>

    </div>
  )
}

export default Navbar