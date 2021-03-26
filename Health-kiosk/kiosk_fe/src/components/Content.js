import React from 'react';
import { Button } from './Button';
import './Content.css';
import {Link } from "react-router-dom";

function Content() {
    return(
        <div >
            <img src="/images/Banner.png" />
            <div >
                <div className='info'>ID:
                <input type='text' className='input' id='username'></input>
                </div>
                <br></br>
                <div className='info'>Password: 
                <input type='text' className='input' id='password'></input>
                <br></br>
                <br></br>
                <img src="/images/Myid.png" />
                </div>
                </div>
                <br></br>
            <div>
                <Link to='/page2'><Button className='btns' buttonStyle='btn-outline' buttonSize='btn-large'>New Account</Button></Link>
                
                <Button className='btns' buttonStyle='btn-login' buttonSize='btn-large'>Log In</Button>
            </div>

        </div>

        
    )
    
}

export default Content