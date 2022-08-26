import logo from "./logo.svg";
import "./App.css";
import HebrewTextForm from "./HebrewTextForm";
import CircularProgress from "@mui/material/CircularProgress";
// import usestate
import { useState } from "react";

function App() {
  const [text, setText] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [outputText, setOutputText] = useState("The output should be here");
  return (
    <div className="App" dir="rtl">
      {/* <h1>מספר-גדר</h1> */}
      <header className="App-header">
        <HebrewTextForm setOutputText={setOutputText} setIsLoading={setIsLoading} />
        <div className="OutputDiv">{isLoading ? <CircularProgress /> : <p>{outputText}</p>}</div>
      </header>
    </div>
  );
}

export default App;
