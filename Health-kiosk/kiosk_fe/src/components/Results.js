import React from 'react';
import { Button } from './Button';
import './Results.css';
import './Gen.css';
import { Link } from "react-router-dom";

function Results() {
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
                <Link to={'./'}><Button className='btn' buttonStyle='btn-cancel' buttonSize='btn-large'>Cancel</Button></Link>
                <Link to={'./finished'}><Button className='btns' buttonStyle='btn-login' buttonSize='btn-large'>Finish</Button></Link>
            </div>

        </div>

    )

}

export default Results