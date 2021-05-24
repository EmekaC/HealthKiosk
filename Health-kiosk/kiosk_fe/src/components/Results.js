import React, { useEffect, useState} from 'react';
import { Button } from './Button';
import './Results.css';
import './Gen.css';
import { Link } from "react-router-dom";

function Results() {
    var t;
    const [results, SetResults] = useState([]);
    function startUpdates(){
       t = setInterval(myFunction,2000);
    }
    function myFunction(){  
        fetch("api/heart")
        .then(response => response.json())
        .then((data) => SetResults(data.results))
        .catch( (error) => console.log(error));
    }
    function stopInterval(){
        clearInterval(t);
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

                        <button class="btn-cell">Temperature</button>
                        <div class="res-cell">Temperature Result</div> 
                        <button class="btn-cell">Blood Oxygen and Pressure</button>
                          
                        <div class="res-cell">Blood Result</div>                  

                    </div>
                </div>

            </div>
            <div className="footer">
            <Button className='btn' buttonStyle='btn-login' buttonSize='btn-large'onClick={async () => {
            startUpdates();
            const response = await fetch("api/heart/start", {
              method: "GET",
              headers: {
                "Content-Type": "application/json",
              },
            });
            if (response.ok) {
              stopInterval();
              console.log("response worked!");
              response.json().then((data)=>
              console.log(data.results.heartbeat));
              fetch("api/heart/del",{method:"DELETE"});
            }
          }}>Start Readings</Button>
                <Link to={'./'}><Button className='btn' buttonStyle='btn-cancel' buttonSize='btn-large'>Cancel</Button></Link>
                <Link to={'./finished'}><Button className='btns' buttonStyle='btn-login' buttonSize='btn-large'>Finish</Button></Link>
            </div>

        </div>

    )

}

export default Results