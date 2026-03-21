import React, { use } from 'react'
import { useContext } from 'react'
import { UserDataContext } from '../context/UserContext'

const Sections = () => {

  const data  = useContext(UserDataContext)
  console.log(data)
  return (
    <div className='h-140 w-full bg-amber-500 p-4'>
      <div className='Allcards display flex justify-around  h-full w-full flex-nowrap '>
        <div className='card_1 bg-yellow-100 p-4 h-100 w-70 rounded '>
          <h2 className='text-xl font-bold mb-2'>{data[0]?.name}</h2>
          <p>{data[0]?.description}</p>
          <p>Email: {data[0]?.email}</p>
          <p>Age: {data[0]?.age}</p>
        </div>
        <div className='card_2 bg-yellow-100 p-4 h-100 w-70 rounded '>
          <h2 className='text-xl font-bold mb-2'>{data[1]?.name}</h2>
          <p>{data[1]?.description}</p>
          <p>Email: {data[1]?.email}</p>
          <p>Age: {data[1]?.age}</p>
        </div>
        <div className='card_3 bg-yellow-100 p-4 h-100 w-70 rounded '>
          <h2 className='text-xl font-bold mb-2'>{data[2]?.name}</h2>
          <p>{data[2]?.description}</p>
          <p>Email: {data[2]?.email}</p>
          <p>Age: {data[2]?.age}</p>
        </div>
        <div className='card_4 bg-yellow-100 p-4 h-100 w-70 rounded '>
          <h2 className='text-xl font-bold mb-2'>{data[3]?.name}</h2>
          <p>{data[3]?.description}</p>
          <p>Email: {data[3]?.email}</p>
          <p>Age: {data[3]?.age}</p>
        </div>
        <div>
          </div>
        </div>
      </div>
      
  )
}

export default Sections