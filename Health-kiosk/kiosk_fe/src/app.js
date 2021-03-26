import React from 'react';
import'./app.css';
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom';
import Home from './components/Pages/Home';
import Sign_up from './components/Pages/Sign_up';
import Measurements from './components/Pages/Measurements';

function app() {
    return(
        
        <Router> 
            <Switch>
                 <Route path='/' component={Home} />
                 <Route path="/page2" component={Sign_up} />
                 <Route path="/page3" component={Measurements} />
             </Switch>
        </Router>
        
    )   

}

export default app;