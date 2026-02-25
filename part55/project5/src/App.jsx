import React from 'react'
import './index.css'
import { useState } from 'react'
import Card from '../components/Card'


const App = () => {
  const [userName, setUserName] = useState('')
  const [Email, setEmail] = useState('')
  const [Address, setAddress] = useState('')
  const [position, setPosition] = useState('')
  const [allUsers, setallUsers] = useState([])
  const handleSubmit = (e) => {
    console.log(userName,Email,Address,position)
    e.preventDefault()
    setUserName('')
    setEmail('')
    setAddress('')
    setPosition('')
    const oldUser = [...allUsers]
    oldUser.push({userName,Email,Address,position})
    setallUsers(oldUser)
    console.log(oldUser)
  }

const deleteHandeler = (index) => {
  const oldUser = [...allUsers]
  oldUser.splice(index,1)
  setallUsers(oldUser)
}




  return (
    <div className="min-h-screen bg-black text-white flex flex-col p-5 ">
      <form className='flex flex-wrap p-2'
        onSubmit={handleSubmit}
      >
        <input
          value={userName}
          className="bg-gray-800 text-xl border-2 px-5 py-2 m-2 w-[45%] text-white font-semibold p-2 rounded"
          type="text"
          placeholder='Name'
          onChange={(e) => setUserName(e.target.value)} />
        <input
          value={Email}
          className="bg-gray-800 text-xl border-2 px-5 py-2 m-2 w-[45%] text-white font-semibold p-2 rounded"
          type="text"
          placeholder='Profile Picture URL'
          onChange={(e) => setEmail(e.target.value)} />
        <input
          value={Address}
          className="bg-gray-800 text-xl border-2 px-5 py-2 m-2 w-[45%] text-white font-semibold p-2 rounded"
          type="text"
          placeholder='Address'
          onChange={(e) => setAddress(e.target.value)} />
        <input
          value={position}
          className="bg-gray-800 text-xl border-2 px-5 py-2 m-2 w-[45%] text-white font-semibold p-2 rounded"
          type="text"
          placeholder='position'
          onChange={(e) => setPosition(e.target.value)} />
        <button onClick = {(idx) => {
          deleteHandeler(idx)
        }} className="bg-blue-500 hover:bg-blue-700 text-white font-semibold active:scale-95 py-2 px-5 rounded m-2 w-[100%]">Create User</button>
      </form>
      <div className="flex flex-wrap gap-5">
        {allUsers.map((user, index) => {
          return   (
    <div className='bg-white w-80 h-90 rounded-lg p-5 m-5 text-black flex items-center p-7 flex-col '>
      <img className='w-20 h-20 object-cover rounded-full border-2 border-gray-300' src={user.Email} alt="" />
      <h1 className='text-2xl font-bold mt-3'>{user.userName}</h1>
      <h3 className='text-gray-500'>{user.position}</h3>
      <p className='text-gray-500 mt-2'>{user.Address}</p>
      <button onClick={() => deleteHandeler(index)} className="bg-red-500 hover:bg-red-700 text-white font-semibold active:scale-95 py-2 px-5 rounded m-2 w-[100%]">Remove</button>

    </div>
  )
        })}
      </div>
    </div>
  )
}
export default App