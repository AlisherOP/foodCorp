
import react from 'react'
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import Login from "./pages/Login"
import Register from './pages/Register'
import Home from './pages/Home'
import NotFound from './pages/NotFound'
import ProtectedRoute from './components/ProtectedRoute'


function Logout(){
  localStorage.clear()
  return <Navigate to="/login"/>
}

function RegisterAndLogout(){
  localStorage.clear()  
  return <Register />
}



function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* one Route */}
        <Route
          path='/'
          element={
            <ProtectedRoute>
              <Home/>
            </ProtectedRoute>
          }
        />
        {/* another Routes */}
        <Route path='/login' element={<Login/>} />
        {/* another one */}
        <Route path='/logout' element={<Logout />} /> 
        {/* Third Route */}
        <Route path='/register' element={<RegisterAndLogout/>} />
        {/* last but not least */}
        <Route path='*' element={<NotFound />} /> 
      </Routes>
    </BrowserRouter>
  )
}

export default App
