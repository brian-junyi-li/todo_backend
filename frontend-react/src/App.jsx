import Dashboard from "./components/Dashboard"
import { useState, useEffect } from "react";

function App() {
    const [data, setdata] = useState([])
const [loading, setloading] = useState(true)
const loadingfunction=()=>{
    setloading(false)
}

    useEffect(() => {
        
        fetch("http://localhost:8000/task")
            .then((response) => response.json())
            .then((data) => {
                console.log(data)
                setdata(data)
            })
    }, [loading])

    return (<Dashboard Apidata={data.data} />)


}

export default App

