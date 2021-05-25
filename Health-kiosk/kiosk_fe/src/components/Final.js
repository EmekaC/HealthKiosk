import React, {useEffect} from 'react';
import './Content.css';
import './Gen.css';
import { Link } from "react-router-dom";

function Final() {
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

    useEffect(() => {
        Logout();
        let tID = setTimeout(function () {

			// redirect page.
            window.location.href = './';
            window.clearTimeout(tID);		// clear time out.
            
        }, 5000);
    }, []);

    return (
        <div>

            <div className="result">
                <p>The health kiosk has finished taking your readings</p>

                <p>Your results will be sent to you via email</p>
                <p>You will be automatically logout out in 5 seconds</p>
            </div>

            

        </div>

    )

}

export default Final