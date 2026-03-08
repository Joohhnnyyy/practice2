import React from 'react'
import { Link } from 'react-router-dom'

const Products = () => {
  return (
    <div>
      <h1  className=' text-6xl flex justify-center font-bold mt-10 mb-10 '>Products</h1>
      <div className='flex flex-col items-center gap-4'>
        <Link to='/products/mens' className='text-2xl font-bold text-blue-500 hover:underline'>Mens Collection</Link>
        <Link to='/products/womens' className='text-2xl font-bold text-blue-500 hover:underline'>Womens Collection</Link>
      </div>
    </div>
  )
}

export default Products