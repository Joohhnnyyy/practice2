import React, { useContext } from 'react'
import { UserDataContext } from '../context/UserContext'

const Footer = () => {

  const data = useContext(UserDataContext)
  return (
    <div className='w-full h-20 absolute bottom-0 bg-gray-800 text-white flex items-center justify-center p-4'>
      <p>&copy; 2023 My App. All rights reserved.</p>
      <p className='ml-4'>Contact: {data[0]?.email}</p>
      <p className='ml-4'>Phone: {data[1]?.email}</p>
      <p className='ml-4'>Address: {data[2]?.email}</p>
      <p className='ml-4'>Email: {data[3]?.email}</p>
    </div>
  )
}

export default Footer