import React from 'react';
import { Button } from './Button';
import './Content.css';
import './Gen.css';
import { Link } from "react-router-dom";

function Content() {
    return (
        <div>

            <form>
                <label for="email"><b>ID: </b></label>
                <input type="text" name="id" required></input>
                <br></br>
                <label for="email"><b>Password: </b></label>
                <input type="password" name="password" required></input>
            </form>

            <div className="footer">
            <Link to={'./signUp'}><Button className='btn' buttonStyle='btn-acc' buttonSize='btn-large'>New Account</Button></Link>
            <Link to={'./measurements'}><Button className='btn' buttonStyle='btn-login' buttonSize='btn-large'>Login</Button></Link>
            </div>
            
        </div>

    )

}

export default Content