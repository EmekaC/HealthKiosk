import React from 'react';
import { Button } from './Button';
import './CreateAcc.css';
import { Link } from "react-router-dom";

function CreateAcc() {
    return (
        <div >
            <div className='titlebar'>New Account Creation</div>
            <br></br>
            <form>
                <div id='acc' className='signup'>
                    <label for="id"><b>ID Number</b></label>
                    <input type="text" name="id" required></input>

                    <label for="name"><b>Name</b></label>
                    <input type="text" name="name" required></input>

                    <label for="surname"><b>Surname</b></label>
                    <input type="text" name="surname" required></input>

                    <label for="email"><b>Email</b></label>
                    <input type="text" name="email" required></input>

                    <label for="password"><b>Password</b></label>
                    <input type="password" name="password" required></input>

                    <label width="20px"for="dob"><b>Date of Birth</b></label>
                    <input type="date" required></input>
                </div>


            </form>
            <div className="footer">
                <Link to={'./'}><Button className='btn' buttonStyle='btn-cancel' buttonSize='btn-large'>Cancel</Button></Link>
                <Button className='btns' buttonStyle='btn-login' buttonSize='btn-large'>Confirm</Button>
            </div>

        </div>


    )

}

export default CreateAcc