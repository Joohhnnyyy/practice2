import React from 'react'
import { useParams } from 'react-router-dom'

const Test = () => {
    const id  = useParams()
  console.log(id)
  return (
    <div>
      <h1 className='text-3xl font-bold capitalize whitespace-break-spaces'>{id.Courseid} page</h1>
    </div>
  )
}

export default Test