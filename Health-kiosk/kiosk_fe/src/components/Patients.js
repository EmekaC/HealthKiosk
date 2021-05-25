import React, { useEffect, useState }  from 'react';
import './Gen.css';



function Patients() {
    console.log("token:"+sessionStorage.getItem('token'));
    const [patients, setPatients] = useState([]);
  useEffect(() => {
    fetch("api/patients", {
        method: "GET",
        headers: {
          "x-access-token": sessionStorage.getItem('token')
        },
      }).then(response =>
          response.json().then(data => {
          console.log(data)
          setPatients(data.patients);
        })).catch(
          (error) => {
            console.log(error);
          }
        )
  }, []);
  function Hello(){}
    return (
        <div>
          <h1>Token patient id: {sessionStorage.getItem('id')}</h1>
            <h1 className="titlebar">Testing api call</h1>

            <div>
              { typeof patients != 'undefined' ? patients.map(patient => (
                 <li>
                   {patient.id}: {patient.name},{patient.surname}
                </li>
              )): <p>Empty list;</p> }
              
            </div>

        </div>

    )

}

export default Patients