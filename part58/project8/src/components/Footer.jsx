import React from 'react'
import { useNavigate } from 'react-router-dom'

const Footer = () => {
  const navigate = useNavigate()
  return (
    <div
    className='bg-red-800 text-xl text-white w-full h-16 flex items-center justify-center absolute bottom-0'>
      <button onClick={() => navigate('/products')} className='bg-blue-700 px-10 py-1 rounded-4xl'>Explore more</button>
    </div>
  )
}

export default Footer