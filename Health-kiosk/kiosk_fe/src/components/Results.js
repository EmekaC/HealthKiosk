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
                    <p> 1. Step on the  plate to measure your weight</p>
                    <p> 2. Attach the oximeter to your finger.</p>
                    <p> 3. Point the Temperature sensor at your forehead</p>
                    <p> 4. Relax while the kiosk takes your readings</p>
                </div>

                <img src="/images/human.png" className="diagram" />

                <div className="readings" >
                    <div id="grid-line">
                        <div class="cell">Temperature</div>
                        <div class="cell">Weight</div>
                        <div class="cell">Blood Pressure</div>
                        
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