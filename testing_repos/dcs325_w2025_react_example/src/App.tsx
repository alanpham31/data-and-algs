import { useState } from "react";
import NavBar from "./NavBar";
import InfoCarousel from "./InfoCarousel";

import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";

interface DisplayState {
  showHTML: boolean;
  showCSS: boolean;
  showJS: boolean;
}

function App() {
  const [showElements, setShowElements] = useState<DisplayState>({
    showHTML: false,
    showCSS: false,
    showJS: false,
  });

  const toggleHTML = () => {
    setShowElements((prevShowElements) => ({
      ...prevShowElements,
      showHTML: !prevShowElements.showHTML,
    }));
  };

  return (
    <>
      <NavBar toggleFunction={toggleHTML} />
      {
        // useContext so that HTMLCarousel appears and
        // disappears on each click
      }
      {showElements.showHTML && <InfoCarousel />}
    </>
  );
}

export default App;
