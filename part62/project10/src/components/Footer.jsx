import React, { useContext } from 'react'
import { ThemeDataContext } from '../context/ThemeContext'

const Footer = () => {

  const data = useContext(ThemeDataContext)
  return (
    <div className='w-full h-20 bg-red-500 p-5 absolute bottom-0 text-white flex items-center justify-between px-4'>
      <p>© 2023 My App. All rights reserved.</p>
      <h1>{data}</h1>
    </div>
  )
}

export default Footer