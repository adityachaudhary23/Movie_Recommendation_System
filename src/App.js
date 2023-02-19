import React from "react"
import Card from "./card.js"
import data from './data.json'
import "./card.css";


function App() {
    return (
        <div className="home">
            <div className="header"><h1>MOVIES</h1></div>

            {data.slice(0, 25).map((movie) => <Card movie={movie} />)}
        </div>
    );
}

export default App;
