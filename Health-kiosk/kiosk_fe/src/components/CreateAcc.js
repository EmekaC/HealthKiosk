import React, { useEffect, useState} from 'react';
import { Button } from './Button';
import './CreateAcc.css';
import { Link } from "react-router-dom";
import Select from 'react-select';
import axios from 'axios';


function CreateAcc() {
    //States
    //Patient Info
    const [patId ,setPatId] = useState("");
    const [patName, setpatName] = useState("");
    const [patSurname, setpatSurname] = useState("");
    const [patMobile, setpatMobile] = useState();
    const [patGender, setpatGender] = useState("");
    const [patDOB, setpatDOB] = useState([]);
    const [patAddress, setpatAddress] = useState("");
    const [patCity, setpatCity] = useState("");
    const [patStatus, setpatStatus] = useState("");
    const [patSiblings, setpatSiblings] = useState("");
    const [patEmail, setpatEmail] = useState("");
    const [patPassword, setpatPassword] = useState("");
    const [patDoc, setpatDoc] = useState();
    
    //Next of Kin Info
    const [nokRelationship, setnokRelationship] = useState("");
    const [nokName, setnokName] = useState("");
    const [nokSurname, setnokSurname] = useState("");
    const [nokMobile, setnokMobile] = useState();
    const [nokGender, setnokGender] = useState("");
    const [nokAddress, setnokAddress] = useState("");
    const [nokCity, setnokCity] = useState("");
    const [nokContactHrs, setnokContactHrs] = useState("");

    //Selections
    const [doctors, setDoctor] = useState([])
    const [relationships, setRelationship] = useState([])
    const [genders, setGender] = useState([])
    const [statues, setStatus] = useState([])
    const [state, setUse] = useState("")


     
    async function CreateAccount(){
        await fetch("api/patients/create", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                "id": patId, 
                "name": patName, 
                "surname": patSurname,
                "mobile": patMobile,
                "gender": patGender, 
                "dob": patDOB,
                "address": patAddress, 
                "city": patCity,
                "marital_status" : patStatus,
                "siblings": Number(patSiblings),
                "email": patEmail, 
                "password": patPassword ,
                "doctor": patDoc
            }),
        }).then(response => {
            if(response.ok){
                 fetch("/api/noks/create", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        "relationship": nokRelationship,
                        "name": nokName,
                        "surname": nokSurname,
                        "mobile": nokMobile,
                        "gender": nokGender,
                        "address":nokAddress,
                        "city" : nokCity,
                        "contact_hrs" : nokContactHrs,
                        "patientId": patId   
                    }),
                }).then(response => {
                    if(response.ok){
                        console.log("Ok")
                        alert("Account Successfully created...Redirecting to login");
                        window.location.href = "./";
                    }else{
                        response.json().then(data => console.log(data));
                    }
                })
            }else{
                response.json().then(data => console.log(data));
            }
        }).catch(error => console.log(error));
    }

    async function getSelections(){
        const docs = await axios.get('api/docs')
        const relations = await axios.get('api/relationships')
        const genders =  await axios.get('api/genders')
        const statuses =  await axios.get('api/status')
        const doctors = docs.data.doctors
        const relationships = relations.data.relationships
        const gender = genders.data.genders
        const status = statuses.data.status

        const doctor = doctors.map(d => ({
            "value": d.id,
            "label": "Dr. "+d.name +" "+ d.surname

        }))

        const relationship = relationships.map(d => ({
            "label": d
        }))

        const gen = gender.map(d => ({
            "label": d
        }))

        const stat = status.map(d => ({
            "label": d
        }))

        setDoctor(doctor)
        setRelationship(relationship)
        setGender(gen)
        setStatus(stat)
        setUse(0)
        
    }  
    
    useEffect(()=> {
        console.log("Use Effect Called")
        getSelections();

    },[state])
    
    
    

    return (
       
        <div >
            <div className='title'>New Account Creation</div>
            <br></br>
            <form name='patient' id='patient'>
                <h1>Personal Details</h1>
                <div className='patient'>


                    <label for="id"><b>ID Number</b></label>
                    <input type="text" name="id" required value={patId} onChange={e => setPatId(e.target.value)} pattern="^[0-9]{7}(M|L|G|H){1}$" title="Maltese id card format"></input>
                    <label for="name"><b>Name</b></label>
                    <input type="text" name="name" required value={patName} onChange={e => setpatName(e.target.value)} pattern="^[a-zA-Z ]*$" title="Only letters can be inputted for name"></input>

                    <label for="surname"><b>Surname</b></label>
                    <input type="text" name="surname" required value={patSurname} onChange={e => setpatSurname(e.target.value)} pattern="^[a-zA-Z ]*$" title="Only letters can be inputted for name"></input>

                    <label for="mobile"><b>Mobile</b></label>
                    <input type="text" name="mobile" required value={patMobile} onChange={e => setpatMobile(e.target.value)} pattern="^[79|99|77]{2}[0-9]{6}$" title="Maltese 8 digit mobile numbers are accepted"></input>

                    <label for="gender"><b>Gender</b></label>
                    <Select options={genders} onChange={e => setpatGender(e.label)} />

                    <label width="20px" for="dob"><b>Date of Birth</b></label>
                    <input type="date" required value={patDOB} onChange={e => setpatDOB(e.target.value)}></input>

                    <label for="address"><b>Address</b></label>
                    <input type="text" name="address" required value={patAddress} onChange={e => setpatAddress(e.target.value)} pattern="^\d+\,\s?[A-z \s\-\']+\,+\s?[A-Z]{3}\s\d{4}$" title="Accepted Address format is: building number, street, post code"></input>

                    <label for="city"><b>City</b></label>
                    <input type="text" name="city" required value={patCity} onChange={e => setpatCity(e.target.value)} pattern="^[A-z \-\']+\s?$" title="City"></input>

                    <label for="married"><b>Marital status</b></label>
                    <Select options={statues} onChange={e =>setpatStatus(e.label)}/>

                    <label for="siblings"><b>Siblings</b></label>
                    <div id="siblings" className="radio"name="siblings" >

                    <label for="yes">Yes</label>
                    <input type="radio" id="yes" name="siblings" value="1" onChange={e => setpatSiblings(e.target.value)} ></input><br/>
                    <label for="no">No</label>
                    <input type="radio" id="no" name="siblings" value="0" onChange={e => setpatSiblings(e.target.value)}></input>
                    
                    </div>



                    <label for="email"><b>Email</b></label>
                    <input type="email" name="email" required value={patEmail} onChange={e => setpatEmail(e.target.value)} pattern="(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)" title="Email"></input>

                    <label for="password"><b>Password</b></label>
                    <input type="password" name="password" required value={patPassword} onChange={e => setpatPassword(e.target.value)} pattern="^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[^\w\s]).{8,14}$" title="Password between 8-14 characters long. Must contain a Captial, number and special character."></input>

                    <label for="doc"><b>Doctor</b></label>
                    <Select options={doctors} onChange={e => setpatDoc(e.value)} />

                </div>
                <br></br>
                <h1>Contact Details</h1>
                <div className="contact">
                    <label for="realtion"><b>Relationship</b></label>
                    <Select options={relationships} onChange={e => setnokRelationship(e.label)} />
                    

                    <label for="name"><b>Name</b></label>
                    <input type="text" name="name" required value={nokName} onChange={e => setnokName(e.target.value)} pattern="^[a-zA-Z ]*$" title="Only letters can be inputted for name"></input>

                    <label for="surname"><b>Surname</b></label>
                    <input type="text" name="surname" required value={nokSurname} onChange={e => setnokSurname(e.target.value)} pattern="^[a-zA-Z ]*$" title="Only letters can be inputted for surname"></input>

                    <label for="mobile"><b>Mobile</b></label>
                    <input type="tel" name="mobile" required value={nokMobile} onChange={e => setnokMobile(e.target.value)} pattern="^[79|99|77]{2}[0-9]{6}$" title="Maltese 8 digit mobile numbers are accepted"></input>

                    <label for="gender"><b>Gender</b></label>
                    <Select options={genders} required onChange={e => setnokGender(e.label)} />

                    <label for="address"><b>Address</b></label>
                    <input type="text" name="address" required value={nokAddress} onChange={e => setnokAddress(e.target.value)} pattern="^\d+\,\s?[A-z \s\-\']+\,+\s?[A-Z]{3}\s\d{4}$" title="Accepted Address format is: building number, street, post code"></input>

                    <label for="city"><b>City</b></label>
                    <input type="text" name="city" required value={nokCity} onChange={e => setnokCity(e.target.value)} pattern="^[A-z \-\']+\s?$" title="City"></input>

                    <label for="contactHrs"><b>Contact Hours</b></label>
                    <input type="text" name="contactHrs" value={nokContactHrs} onChange={e => setnokContactHrs(e.target.value)}></input>
                </div>
                <br></br>
                </form>
                <div >
                    <Link to={'./'}><Button className='btn' buttonStyle='btn-cancel' buttonSize='btn-large'>Cancel</Button></Link>
                     <Button className='btn' buttonStyle='btn-login' buttonSize='btn-large' data-toggle="tooltip" data-placement="top" title="Tooltip on top" onClick={async () => {
                        CreateAccount().then(()=> {
                            window.location.reload();
                        });
                        }}>Submit</Button> 
                    
                </div>
            
            <br></br>
        </div>
    )
                    }

export default CreateAcc




