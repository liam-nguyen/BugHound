import React from 'react';
import { Link } from 'react-router-dom';

function IndexPage() {
  return (
    <>
      <h2>Welcome to Bughound</h2>
      <ul>
        <li>
          <Link to="/newbug">Enter NEW Bug</Link>
        </li>
        <li>
          <Link to="/view">Update EXISTING Bug</Link>
        </li>
      </ul>
    </>
  );
}

export default IndexPage;
