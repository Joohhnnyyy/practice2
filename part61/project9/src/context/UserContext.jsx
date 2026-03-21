import React from 'react'
import { createContext } from 'react'

export const UserDataContext = createContext()

const users = [
  {
    id: 1,
    name: "Ansh",
    email: "ansh@example.com",
    age: 21,
    description: "Computer Science student passionate about AI, web development, and building smart agriculture solutions."
  },
  {
    id: 2,
    name: "Riya",
    email: "riya@example.com",
    age: 22,
    description: "Frontend developer who enjoys creating responsive UI/UX designs and working with React."
  },
  {
    id: 3,
    name: "Aman",
    email: "aman@example.com",
    age: 20,
    description: "Backend enthusiast focused on APIs, databases, and scalable system design."
  },
  {
    id: 4,
    name: "Sneha",
    email: "sneha@example.com",
    age: 23,
    description: "Data analyst skilled in Python, visualization, and extracting insights from data."
  }
];

const UserContext = ({ children }) => {
  return (
    <div>
      <UserDataContext.Provider value={users}>
        {children}
      </UserDataContext.Provider>

    </div>
  )
}

export default UserContext