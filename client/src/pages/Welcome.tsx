import React from 'react'
import { Link } from 'react-router-dom'

function Welcome() {
  return (
    <>
      Welcome to Bughound
      <ul>
        <li>
          <Link to="/newbug">Enter NEW Bug</Link>
        </li>
        <li>
          <Link to="/view">Update EXISTING Bug</Link>
        </li>
      </ul>
    </>
  )
}

export default Welcome
