import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [status, setStatus] = useState<string>("Checking...")
  useEffect(() => {
    async function checkServerStatus() {
      try {
        const res = await fetch("/api/health")
        if (!res.ok) {
          setStatus("Server is down");
          throw new Error(`Response status: ${res.status}`);
        }

        const result = await res.json()
        console.log(result)
        setStatus(result.status)
      } catch (error) {
        setStatus("Server is down")
        console.error(error);
      }
    }

    checkServerStatus()
  }, []);

  return (
    <>
      <h1>{status}</h1>
    </>
  )
}

export default App
