import React from "react"
import {Link} from 'react-router-dom'


export default function header(){
    return(
        <header>
            <nav className="nav">
                <ul className="nav-items">
                    <li><Link to="/">Home</Link></li>
                    <li><Link to="/Results">Results</Link></li>  
                    <li><Link to="/info">How to play</Link></li> 
                    <li><Link to="/settings">Settings</Link></li>
                    <li><Link to="/contact">Contact</Link></li>
                </ul>
            </nav>
        </header>
    )
}