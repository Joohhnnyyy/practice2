import React from 'react'

const Nav = () => {
  return (
    <div className='w-full h-20 bg-blue-600 p-5 text-white flex items-center justify-between px-4'>
      <h1 className='text-2xl font-bold'>My App</h1>
      <div className='Options '>
          <button className='mx-4 hover:text-gray-300'>Home</button>
          <button className='mx-4 hover:text-gray-300'>About</button>
          <button className='mx-4 hover:text-gray-300'>Contact</button>
          <button className='mx-4 hover:text-gray-300'>Login</button>
      </div>
    </div>
  )
}

export default Nav