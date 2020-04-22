import React from 'react';
import Header from './Header';

function Layout({ children }) {
  return (
    <>
      <Header title="Bughound" />
      <main>{children}</main>
    </>
  );
}

export default Layout;
