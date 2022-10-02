import React, { useState, useEffect } from 'react'
import BarChart from './charts/Bar.js'


// useState --> state variable wich will contain the data retrieved from the backend 
// it is used to render the data on the page
// useEffect --> will be used to fetch the backend API on the first render

function App() {

  // const [data, setData] = useState([{}])
  // // data is the actual variable
  // // setData is the function to manipulate the state od the data variable

  // useEffect(() => {
  //   fetch("/members").then(
  //     res => res.json()
  //   ).then(
  //     data => {
  //       setData(data)
  //       console.log(data)
  //     }
  //   )

  // }, [])
  return (
    <div>
      {/* {(typeof data.members === 'undefined') ? (
        <p>Loading...</p>
      ) :
        (
          data.members.map((member, i) => (
            <p key={i}>{member}</p>
          ))
        )} */}
      <BarChart />

    </div>
  )
}

export default App
