import React, { use } from 'react'
import { useContext } from 'react'
import { ThemeDataContext } from '../context/ThemeContext'
const Nav = () => {

  const [theme, setTheme] = useContext(ThemeDataContext)
  return (
    <div className='w-full h-20 bg-red-500 p-5 text-white flex items-center justify-between px-4'>
      <h1 className='text-2xl font-bold'>My App</h1>
      <div className='Options '>
          <button className='mx-4 hover:text-gray-300'>Home</button>
          <button className='mx-4 hover:text-gray-300'>About</button>
          <button className='mx-4 hover:text-gray-300'>Contact</button>
          <button className='mx-4 hover:text-gray-300'>Login</button>
          <h1>{theme}</h1>
          <button onClick={
            () => setTheme(theme === 'light' ? 'dark' : 'light')
          }className='h-8 w-30 rounded-3xl bg-green-900'>Change theme</button>
      </div>
    </div>
  )
}

export default Nav