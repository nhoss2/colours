import React, { useState, useEffect } from "react";
import "./App.css";

function SingleColour({colourData}) {
  return (
    <div className="colour-box" style={{ background: colourData.css }}>
      {colourData.css}
    </div>
  );
}

function App() {
  const [colours, setColours] = useState([]);

  const get_colours = async () => {
    const response = await fetch("/api/get_colours");
    const data = await response.json();
    setColours(data.colours)
  };

  // fetch new colours on load
  useEffect(() => {
    get_colours();
  }, []);

  return (
    <div className="app">
      <h1>Colours app</h1>

      <div id="colours-list">
        {colours.map((colour, i) => {
          return <SingleColour key={i} colourData={colour} />
        })}
      </div>
    </div>
  );
}

export default App;
