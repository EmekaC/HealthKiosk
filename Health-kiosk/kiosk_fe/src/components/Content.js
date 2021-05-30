import React, {useState} from 'react';
import { Button } from './Button';
import './Content.css';
import './Gen.css';
import { Link } from "react-router-dom";
import jwt_decode from "jwt-decode"

function Content() {
    const [id, setID] = useState("");
    const [password, setPassword] = useState("");
    
    function storeDate(){
          console.log("ID:"+id);
          console.log("Password"+password);
      }

      async function Login(){
        await fetch("api/login", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            'Authorization': 'Basic ' + btoa(`${id}:${password}`)
          },
          body: JSON.stringify({"remember-me": "False"}),
        }).then((response) => {
          if (response.ok){
              response.json().then(data => {
              console.log(data);
            try{
              sessionStorage.setItem('token',data.token);
              let patientId = jwt_decode(data.token);
              sessionStorage.setItem('id',patientId['id']);
            } catch(error){
              console.log(error)
              console.log(data.token)
            }})
            window.location.href = "./measurements";
          }
          else{
            alert("Invalid credentials");
            response.json().then(data => console.log(data.statusText));
          }
        })
        .catch(error => console.log(error));
      }
      
    return (
        <div>

            <form>
                <label for="id"><b>ID: </b></label>
                <input type="text" name="id" required value={id} onChange={e => setID(e.target.value)} pattern="^[0-9]{7}(M|L|G|H){1}$" title="Maltese Citizen ID card format"></input>
                <br></br>
                <label for="password"><b>Password: </b></label>
                <input type="password" name="password" required value={password} onChange={e => setPassword(e.target.value)} pattern="^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[^\w\s]).{8,14}$" title="Invalid password"></input>
            </form>
            <br></br>
            


            <div className="footer">
                <Link to={'./signUp'}><Button className='btn' buttonStyle='btn-acc' buttonSize='btn-large'>New Account</Button></Link>
                <Button className='btn' buttonStyle='btn-login' buttonSize='btn-large' onClick={function(event){Login();}}>Login</Button>
            </div>
            
        </div>

    )

}

export default Content