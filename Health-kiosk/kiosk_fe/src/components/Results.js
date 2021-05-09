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

            <h1 className="titlebar">Instructions and Results</h1>

            <div>
                <img src="/images/human.png" className="center" />
                <div className="instructions">
                    <p> 1. Step on the  plate to measure your weight</p>
                    <p> 2. Attach the oximeter to your finger.</p>
                    <p> 3. Point the Temperature sensor at your forehead</p>
                    <p> 4. Relax while the kiosk takes your readings</p>
                </div>
                <div className="readings">
                    <div id="grid-line">
                        <div class="cell">Heart Beat</div>
                        <div class="cell">{results.heartbeat}</div>
                        <div class="cell">Blood Oxygen</div>
                        
                        <div class="cell">{results.oxygen}</div>
                        <div class="cell">Test</div>
                        <div class="cell">Test</div>
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