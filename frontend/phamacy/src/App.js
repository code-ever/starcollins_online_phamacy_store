import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Header from "./components/Header";
import Navbar from "./components/Navbar";
import Menubar from "./components/Menubar";
import Inflammentry from "./pages/Inflammentry";
import Main from "./pages/Main";
import Footer from "./components/Footer";

function App() {
  return (
    <div className="App">
      <Router>
        <Header />
        <Navbar />
        <Menubar />
        <Routes>
          <Route path="/" element={<Main />} />
          <Route path="Inflammentry" element={<Inflammentry />} />
        </Routes>
        <Footer />
      </Router>
    </div>
  );
}

export default App;
