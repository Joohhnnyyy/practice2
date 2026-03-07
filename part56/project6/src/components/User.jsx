import React from 'react'

const User = (props) => {

  const clr1 = Math.floor(Math.random() * 256)
  const clr2 = Math.floor(Math.random() * 256)
  const clr3 = Math.floor(Math.random() * 256)

  const bgColor = `rgb(${clr1}, ${clr2}, ${clr3})`
  return (
    <div style={{ backgroundColor: bgColor }} className=' m-5 p-2 h-100 w-70 rounded-2xl flex  flex-col items-center gap-1 flex-wrap'>
      <h1 className='text-3xl text-white'>{props.elem.name}</h1>
      <h2 className=' text-white text-xl'>{props.elem.email}</h2>
      <h2 className=' text-white text-xl'>{props.elem.phone}</h2>
      <h2 className=' text-white text-xl'>{props.elem.website}</h2>
      <h2 className=' text-white text-xl'>{props.elem.company.name}</h2>
      <h2 className=' text-white text-xl'>{props.elem.company.catchPhrase}</h2>
      <h2 className=' text-white text-xl'>{props.elem.company.bs}</h2>
      <h2 className=' text-white text-xl'>{props.elem.address.street}</h2>


    </div>
  )
}

export default User