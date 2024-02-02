import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./components/Home";
import Nav from "./components/Nav";


function App() {
  return (
    <div className="">
      <Router>
          <Nav />
          <Routes>
            <Route path="/" element={<Home />} />
          </Routes>

      </Router>
    </div>
  );
}

export default App;
