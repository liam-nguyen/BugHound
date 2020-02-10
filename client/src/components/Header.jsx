import React from 'react';
import { Link } from 'react-router-dom';

function Header({ title }) {
  return (
    <header>
      <h1>
        <Link to="/">{title}</Link>
      </h1>
    </header>
  );
}

export default Header;
