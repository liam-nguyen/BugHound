import React from 'react';
import ReactDOM from 'react-dom';

import Routes from './Routes';

import './styles/styles.scss';

function App() {
  return <Routes />;
}

ReactDOM.render(<App />, document.getElementById('root'));
