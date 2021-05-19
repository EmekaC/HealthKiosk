import React, { Component } from 'react';
import { Button } from './Button';
import './CreateAcc.css';
import { Link } from "react-router-dom";
import Select from 'react-select';
import axios from 'axios';


export default class CreateAcc extends Component {

    constructor(props) {
        super(props)
        this.state = {
            selectOptions: [],
            id: "",
            name: ''
        }
    }

    async getOptions() {
        const res = await axios.get('https://jsonplaceholder.typicode.com/users')
        const data = res.data

        const options = data.map(d => ({
            "value": d.id,
            "label": d.name

        }))

        this.setState({ selectOptions: options })

    }
    handleChange(e) {
        this.setState({ id: e.value, name: e.label })
    }

    componentDidMount() {
        this.getOptions()
    }

    render() {
        console.log(this.state.selectOptions)
        return(
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
                    <select >
                        <option value="Male">Male</option>
                        <option value="Female">Female</option>
                        <option value="Other">Other</option>
                        </select>

                    <label width="20px" for="dob"><b>Date of Birth</b></label>
                    <input type="date" required></input>

                    <label for="address"><b>Address</b></label>
                    <input type="text" name="address" required></input>

                    <label for="city"><b>City</b></label>
                    <input type="text" name="city" required></input>

                    <label for="married"><b>Marital status</b></label>
                    <input type="text" name="married" required></input>

                    <label for="siblings"><b>Siblings</b></label>
                    <div id="siblings" name="siblings">

                    <input type="radio" id="yes" name="siblings" value="yes"></input>
                    <label for="yes">Yes</label><br></br>
                    <input type="radio" id="no" name="siblings" value="no"></input>
                    <label for="female">no</label><br></br>
                    </div>



                    <label for="email"><b>Email</b></label>
                    <input type="email" name="email" required></input>

                    <label for="password"><b>Password</b></label>
                    <input type="password" name="password" required></input>

                    <label for="doc"><b>Doctor</b></label>
                    <Select options={this.state.selectOptions} onChange={this.handleChange.bind(this)} />

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
                    <input type="tel" name="mobile" required></input>

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
                    <input className="submitbtn" type="submit" value="Submit" ></input>
                </div>
            </form>
            <br></br>



        </div>
        )

    }
}




