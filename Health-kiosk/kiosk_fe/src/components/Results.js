import React, {useState} from 'react';
import { Button } from './Button';
import './Results.css';
import './Gen.css';
import { Link } from "react-router-dom";

function Results() {
    
    var updateRate;
    const [heartData, SetHeart] = useState([]);
    const [temp, SetTemperature] = useState([]);

    function startUpdates(functionName){
        updateRate = setInterval(functionName,2000);
    }

    function getHeartUpdates(){  
        fetch("api/heart")
        .then(response => response.json())
        .then((data) => SetHeart(data.results))
        .catch( (error) => console.log(error));
    }

    function getTempretureUpdates(){  
        fetch("/api/temp")
        .then(response => response.json())
        .then((data) => SetTemperature(data.results))
        .catch( (error) => console.log(error));
    }
    function stopInterval(){
        clearInterval(updateRate);
    }

    async function startHeartSensor(){
        startUpdates(getHeartUpdates);
        await fetch("api/heart/start", {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
            },
          }).then((response) => {
            if (response.ok) {
                stopInterval();
                console.log("response worked!");
                response.json().then((data)=>
                console.log(data.results.heartbeat));
                fetch("api/heart/del",{method:"DELETE"});
                alert("Sensor Has Completed Readings");
            }
            else{
                console.log("Error has occured");
            }
          })
    }

    async function startTemperatureSensor(){
        startUpdates(getTempretureUpdates);
        await fetch("/api/temp/start", {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
            },
          }).then((response) => {
            if (response.ok) {
                stopInterval();
                console.log("response worked!");
                response.json().then((data)=>
                console.log(data.results.heartbeat));
                fetch("api/temp/del",{method:"DELETE"});
                alert("Sensor Has Completed Readings");
            }
            else{
                console.log("Error has occured");
            }
          })
    }

    async function saveResults(){
        await fetch("api/results/add", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
              "x-access-token": sessionStorage.getItem('token')
            },
            body: JSON.stringify({
                "id": sessionStorage.getItem('id'), 
                "temperature": temp.temperature, 
                "weight": "0.00", 
                "bloodOx": heartData.oxygen, 
                "heartRate": heartData.heartbeat
            }),
          }).then((response) => response.json())
          .then((data) => {
            console.log(data);
          })
          .catch(error => console.warn(error));
          window.location.href = "./finished";
    }

    async function Logout(){
        await fetch("api/logout", {
            method: "GET",
            headers: {
              "x-access-token": sessionStorage.getItem('token')
            },
          }).then((response) => response.json())
          .then((data) => {
            console.log(data);
          })
          .catch(error => console.warn(error));
    }
          
    return (
        <div>

            <h1 className="title">Instructions and Results</h1>

            <div id="grid-page">
                
                <div className="instructions" >
                    <p> Select a sensor and press the appropriate button to begin taking your readings.</p>
                    <p> The temperature sensor works both with touch and non-contact.</p>
                    <p> The oxometer should be attatched to your finger</p>
                    <p> Press the finish button once you have all your required results</p>
                </div>

                <img src="/images/human.png" className="diagram" />

                <div className="readings" >
                    <div id="grid-line">

                        <button class="btn-cell" onClick={function(event){startTemperatureSensor();}}>Temperature</button>
                        <div class="res-cell">{temp.temperature}°C</div> 
                        <button class="btn-cell" onClick={function(event){startHeartSensor();}}>Blood Oxygen and Heart Rate</button>
                          
                        <div class="res-cell">{heartData.heartbeat} BPM<div>{heartData.oxygen}</div></div>            
                    </div>
                </div>

            </div>
            <div className="footer">
                <Button className='btn' buttonStyle='btn-cancel' buttonSize='btn-large' onClick={function(event){Logout(); window.location.href="./"}}>Cancel</Button>
                <Button className='btns' buttonStyle='btn-login' buttonSize='btn-large' onClick={function(event){saveResults();}}>Finish</Button>
            </div>

        </div>

    )

}

export default Results