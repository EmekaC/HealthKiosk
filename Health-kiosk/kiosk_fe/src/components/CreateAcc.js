import React from 'react';
import { Button } from './Button';
import './CreateAcc.css';
import { Link } from "react-router-dom";

function CreateAcc() {
    return (
        <div >
            <div className='title'>New Account Creation</div>
            <br></br>
            <form name='patient'>
            <h1>Personal Details</h1>
                <div className='patient'>
                
                
                    <label for="id"><b>ID Number</b></label>
                    <input type="text" name="id" required></input>

                    <label for="name"><b>Name</b></label>
                    <input type="text" name="name" required></input>

                    <label for="surname"><b>Surname</b></label>
                    <input type="text" name="surname" required></input>

                    <label for="mobile"><b>Mobile</b></label>
                    <input type="text" name="mobile" required></input>

                    <label for="gender"><b>Gender</b></label>
                    <input type="text" name="gender" required></input>

                    <label width="20px"for="dob"><b>Date of Birth</b></label>
                    <input type="date" required></input>

                    <label for="address"><b>Address</b></label>
                    <input type="text" name="address" required></input>

                    <label for="city"><b>City</b></label>
                    <input type="text" name="city" required></input>

                    <label for="married"><b>Marital status</b></label>
                    <input type="text" name="married" required></input>

                    <label for="siblings"><b>Siblings</b></label>
                    <div id="siblings" name="siblings">
                    
                    <input type="checkbox" id="siblingsY" name="siblingsY" required></input>
                    <label for="siblingsY"><b>Yes</b></label><br></br>
                    <input type="checkbox" id="siblingsN" name="siblingsN" required></input>
                    <label for="siblingsN"><b>No</b></label><br></br>
                    </div>

                    

                    <label for="email"><b>Email</b></label>
                    <input type="email" name="email" required></input>

                    <label for="password"><b>Password</b></label>
                    <input type="password" name="password" required></input>

                </div>
                <br></br>
                <h1>Contact Details</h1>
                <div className="contact">               
                    <label for="realtion"><b>Relationship</b></label>
                    <input type="text" name="realtion" required></input>

                    <label for="name"><b>Name</b></label>
                    <input type="text" name="name" required></input>

                    <label for="surname"><b>Surname</b></label>
                    <input type="text" name="surname" required></input>

                    <label for="mobile"><b>Mobile</b></label>
                    <input type="text" name="mobile" required></input>

                    <label for="gender"><b>Gender</b></label>
                    <input type="text" name="gender" required></input>

                    <label for="address"><b>Address</b></label>
                    <input type="text" name="address" required></input>

                    <label for="city"><b>City</b></label>
                    <input type="text" name="city" required></input>

                    <label for="contactHrs"><b>Contact Hours</b></label>
                    <input type="text" name="contactHrs"></input>
                </div>
                <br></br>
                
                <div >
                    <Link to={'./'}><Button className='btn' buttonStyle='btn-cancel' buttonSize='btn-large'>Cancel</Button></Link>
                    <input type="submit" value="Submit" ></input>
                </div>
            </form>
            <br></br>

            

        </div>


    )

}

export default CreateAcc