import React from 'react';
import'./app.css';
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom';
import Home from './components/Pages/Home';
import SignUp from './components/Pages/SignUp';
import Measurements from './components/Pages/Measurements';
import Exit from './components/Pages/Exit';
import GetPatients from './components/Pages/GetPatients'

function app() {
    return(
        
        <Router> 
            <Switch>
                 <Route path='/' exact component={Home} />
                 <Route path="/signUp" component={SignUp} />
                 <Route path="/measurements" component={Measurements} />
                 <Route path="/finished" component={Exit} />
                 <Route path="/pats" component={GetPatients} />
             </Switch>
        </Router>
        
    )   

}

export default app;