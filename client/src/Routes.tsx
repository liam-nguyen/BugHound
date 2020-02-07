import React from 'react'
import { BrowserRouter, Redirect, Route, Switch } from 'react-router-dom'
import Layout from './components/Layout'
import Welcome from './pages/Welcome'
import NewBug from './pages/NewBug'
import ViewBug from './pages/ViewBug'

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

        <MyRoute path="/view">
          <ViewBug />
        </MyRoute>

        <Redirect to="/" />
      </Switch>
    </BrowserRouter>
  )
}

export default Routes
