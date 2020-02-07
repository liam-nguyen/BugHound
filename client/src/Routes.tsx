import React from 'react'
import { BrowserRouter, Redirect, Route, Switch } from 'react-router-dom'
import Layout from 'components/Layout'
import Welcome from 'pages/Welcome'

type RouteProps = {
  path: string
}

const MyRoute: React.FC<RouteProps> = ({ children, path }) => {
  return (
    <Route path={path}>
      <Layout>{children}</Layout>
    </Route>
  )
}

function Routes() {
  return (
    <BrowserRouter>
      <Switch>
        <MyRoute path="/">
          <Welcome />
        </MyRoute>
        <Redirect to="/" />
      </Switch>
    </BrowserRouter>
  )
}

export default Routes
