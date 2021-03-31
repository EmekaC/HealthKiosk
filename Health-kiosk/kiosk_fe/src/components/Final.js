import React from 'react';

import './Content.css';
import './Gen.css';
import { Link } from "react-router-dom";

function Final() {
    return (
        <div>

            <div className="banner">
                <img src="/images/Banner.png" />
            </div>

            <div className="titlebar">
                <p>The health kiosk has finished taking your readings</p>
            </div>
            <br></br>
            <br></br>
            <br></br>
            <div className="titlebar">

                <p>your results will be sent to you via email</p>
            </div>


        </div>

    )

}

export default Final