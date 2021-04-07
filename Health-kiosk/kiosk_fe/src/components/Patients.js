import React, { useEffect, useState }  from 'react';
import './Gen.css';
import { Link } from "react-router-dom";

function Patients() {
    const [patients, setPatients] = useState([]);

  useEffect(() => {
    fetch("/patients").then(response =>
      response.json().then(data => {
        console.log(data)
        setPatients(data.patients);
      })
    );
  }, []);
    return (
        <div>

            <h1 className="titlebar">Testing api call</h1>

            <div>
            
              {patients.map(patient => (
                 <li>
                   {patient.id}: {patient.name},{patient.surname}
                </li>
               ))} 
            </div>

        </div>

    )

}

export default Patients