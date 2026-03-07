import React from 'react'
import './index.css'
import axios, { all } from 'axios'
import { useState } from 'react'
import User from './components/User'
import { useEffect } from 'react'
const App = () => {
  const [allData, setAllData] = useState([])



  async function getData(){
    const {data} =  await axios.get("https://jsonplaceholder.typicode.com/users")
    console.log(data)
    setAllData(data)

    console.log("Data fetched")
  }
  useEffect (function(){
    getData()
  },[])


  return (
    <div className='bg-black' >

      
      <div className = 'flex flex-wrap items-center justify-center gap-5'>
      {allData.map((elem,idx) =>{
        console.log(elem)
        
        return <div key={idx}>  <User elem={elem} /> </div>
      })}

      </div>
    </div>


  )
}

export default App