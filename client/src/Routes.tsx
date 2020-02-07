import React from 'react'
import { BrowserRouter, Route, Switch, Redirect } from 'react-router-dom'
import Layout from './components/Layout'
import Welcome from './pages/Welcome'
import NewBug from './pages/NewBug'

type RouteProps = {
  path: string
  exact?: boolean
}

const MyRoute: React.FC<RouteProps> = ({ children, exact, path }) => {
  return (
    <Route exact={exact} path={path}>
      <Layout>{children}</Layout>
    </Route>
  )
}

function Routes() {
  return (
    <BrowserRouter>
      <Switch>
        <MyRoute exact path="/">
          <Welcome />
        </MyRoute>

        <MyRoute path="/newbug">
          <NewBug />
        </MyRoute>

        <Redirect to="/" />
      </Switch>
    </BrowserRouter>
  )
}

export default Routes
