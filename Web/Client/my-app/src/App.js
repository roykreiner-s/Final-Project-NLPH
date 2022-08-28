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
      <h1>
        <u>דקדוקית</u>
      </h1>
      <h3>ברוכים הבאים למערכת שבאה לשפר את רמת הדיוק בדקדוק בשפה העברית</h3>
      <h3>מטרת המערכת הנה להמיר משפטים בעלי מספרים לצורתם המילולית לפי הטיה מגדרית.</h3>
      <header className="App-header">
        <HebrewTextForm setOutputText={setOutputText} setIsLoading={setIsLoading} />
        <div className="OutputDiv">{isLoading ? <CircularProgress /> : <p>{outputText}</p>}</div>
      </header>
    </div>
  );
}

export default App;
