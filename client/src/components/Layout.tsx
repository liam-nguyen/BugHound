import React from 'react'
import Header from './Header'

const Layout: React.FC = ({ children }) => {
  return (
    <>
      <Header title="Bughound" />
      <main>{children}</main>
    </>
  )
}

export default Layout
