import React, {useState} from 'react';
import { Button } from './Button';
import './Content.css';
import './Gen.css';
import { Link } from "react-router-dom";
import jwt_decode from "jwt-decode"

function Content() {
    const [id, setID] = useState("");
    const [password, setPassword] = useState("");
  
  
    
    function handleIDChange(e) {
        id = e.target.value
        console.log(e.target.value);
      }

      function handlePassChange(e) {
        password = e.target.value
        console.log(e.target.value);
      }

      function storeDate(){
          console.log("ID:"+id);
          console.log("Password"+password);
      }
      
    return (
        <div>

            <div className="banner">
                <img src="/images/Banner.png" />
            </div>

            <form>
                <label for="email"><b>ID: </b></label>
                <input type="text" name="id" required value={id} onChange={e => setID(e.target.value)}></input>
                <br></br>
                <label for="email"><b>Password: </b></label>
                <input type="password" name="password" required value={password} onChange={e => setPassword(e.target.value)}></input>
            </form>
            <br></br>
            


            <div className="footer">
                <Link to={'./signUp'}><Button className='btn' buttonStyle='btn-outline' buttonSize='btn-large'>New Account</Button></Link>
                <Button className='btn' buttonStyle='btn-login' buttonSize='btn-large' onClick={async () => {
            
            const response = await fetch("api/login", {
              method: "POST",
              headers: {
                "Content-Type": "application/json",
                "Authorization": 'Basic ' + window.btoa(id+":"+password),
              },
              body: JSON.stringify({"remember-me": "False"}),
            });

            if (response.ok) {
              console.log("response worked!");
              response.json().then(data => {
                console.log(data);
                try{
                  sessionStorage.setItem('token',data.token);
                  let patientId = jwt_decode(data.token);
                  console.log("Patient id"+patientId['id']);
                  sessionStorage.setItem('id',patientId['id']);
                } catch(error){
                  console.log(error)
                  console.log(data.token)
                }
              })
            }
            window.location.href = "./pats";
          }}>Login</Button>
            </div>

        </div>

    )

}

export default Content