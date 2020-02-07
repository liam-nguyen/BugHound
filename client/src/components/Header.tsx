import React from 'react'
import { Link } from 'react-router-dom'

type HeaderProps = {
  title: string
}

function Header({ title }: HeaderProps) {
  return (
    <header>
      <h1>
        <Link to="/">{title}</Link>
      </h1>
    </header>
  )
}

export default Header
