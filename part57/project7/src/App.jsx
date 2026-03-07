import React, { use } from 'react'
import './index.css'
import axios, { all } from 'axios'
import { useState } from 'react'
import { useEffect } from 'react'

const App = () => {
  const [counter, setcounter] = useState(0)
  const [Fullname, setFullname] = useState('')
  useEffect(function(){
    getData()

  },[counter])






  async function getData(){
  const result = await axios.get("https://randomuser.me/api/")
  const fullname = result.data.results[0].name.first + " " + result.data.results[0].name.last
  setFullname(fullname)
  }
  
  

  return (
    <div>{counter}
    <br />
    <button className="bg-amber-300 hover:bg-amber-400 text-white font-bold py-2 px-4 border border-amber-500 rounded" onClick={() => {setcounter(counter + 1)}}>Increment</button>
    <br />
    {Fullname}
      </div>
  )
}

export default App