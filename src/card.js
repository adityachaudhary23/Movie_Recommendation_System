import React, { useState, useEffect } from "react";
import "./card.css";


function Card(props) {
    console.log(props.movie);
    
    
    return (<div className="card">
        <h1>{props.movie.title}</h1>
        {/* <ul>Genre: {props.movie.genres.map((genre)=><li>{genre.name}</li>
        )}</ul> */}
        {/* {props.genre.map((gen)=><h1>{gen}</h1>)} */}
        <p><b>IMDB Rating: </b>{props.movie.vote_average}</p>
        <p><b>Language: </b>{props.movie.original_language}</p>
        <p><b>Budget: </b>{props.movie.budget}</p>
        <p><b>Tagline: </b> {props.movie.tagline}</p>
        <p><b>Overview:</b> {props.movie.overview}</p>

    </div>);

}

export default Card;