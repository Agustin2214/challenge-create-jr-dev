
import axios from 'axios';
import  React, { useEffect, useState } from 'react';


function App() {
  const [contact, setContact] = useState([]);

  const fetchData = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:5000/api/contacts/')
      setContact(response.data)
      console.log(response.data)
    } catch (error) {
      console.log(error)
    }	

  }


useEffect(() => {
  fetchData()
}, [])

  return (
    <div>
      <h1>
        INCIO
      </h1>
      <h2>
        Lista de Contactos
      </h2>
      {
        contact.length > 0 ? contact.map(contact => (
          <ul>
         <li key={contact.fullname}>
           {contact.fullname}
         </li>
         </ul>
        )) : <p>No hay contactos</p>
      }

      
    </div>
  );
         
}

export default App;
