import React from 'react';
import { Route, BrowserRouter, Switch } from 'react-router-dom';

import { Layout } from './components';
import Index from './pages/Index';

const MyRoute = ({ children, exact, path }) => {
  return (
    <Route exact={exact} path={path}>
      <Layout>{children}</Layout>
    </Route>
  );
};

function Routes() {
  return (
    <BrowserRouter>
      <Switch>
        <MyRoute exact path="/">
          <Index />
        </MyRoute>

        {/* <MyRoute path="/newbug">
          <NewBug />
        </MyRoute>

        <MyRoute path="/view">
          <ViewBug />
        </MyRoute> */}
      </Switch>
    </BrowserRouter>
  );
}

export default Routes;
