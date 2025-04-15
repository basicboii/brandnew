import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => (
  <nav>
    <Link to="/">Login</Link> | <Link to="/upload">Upload File</Link>
  </nav>
);

export default Navbar;
