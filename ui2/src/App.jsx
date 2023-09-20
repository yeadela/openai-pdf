import ProtectedRoute from "./components/ProtectedRoute";
import HomePage from "./pages/HomePage";
import SigninPage from "./pages/SigninPage";
// import Home from "./pages/Home";

import { BrowserRouter, Route, Routes } from "react-router-dom";
import "./app.less"
function App() {

  return (
    // <>
    //   <ToastContainer
    //     position="bottom-left"
    //     autoClose={4000}
    //     hideProgressBar={false}
    //     newestOnTop={false}
    //     closeOnClick
    //     rtl={false}
    //     pauseOnHover
    //   />
    <BrowserRouter>
      <Routes>
        <Route path="/" element={
          <ProtectedRoute>
            <HomePage />
          </ProtectedRoute>
        } />
        <Route path="/signin" element={
          <SigninPage />
        } />

      </Routes>
    </BrowserRouter>
    // </>
  );
}

export default App;
