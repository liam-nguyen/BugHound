import React from 'react'
import ReactDOM from 'react-dom'
import { Provider } from 'react-redux'

import store from './state/store'
import Routes from './Routes'

function App() {
  return (
    <Provider store={store}>
      <Routes />
    </Provider>
  )
}

ReactDOM.render(<App />, document.getElementById('root'))
