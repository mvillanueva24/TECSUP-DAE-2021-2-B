import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/Nav'
import Container from 'react-bootstrap/Container';
import {Route,Routes,BrowserRouter,Link} from 'react-router-dom';
import App from './App';
import Users from './users';
import Contact from './contact';
import Notfound  from './notfound';

const routing = (
  <div>
    <BrowserRouter>
      <Navbar bg="light" variant="light">
        <Container>
          <Navbar.Brand href="/">Navbar</Navbar.Brand>
            <Nav className="me-auto">
              <Link class="nav-link" to="/">Home</Link>
              <Link class="nav-link" to="/usuarios">Users</Link>
              <Link class="nav-link" to="/contacto">Contact</Link>
            </Nav>
        </Container>
      </Navbar>
      <Routes>
        <Route exact path="/" element={<App />} />
        <Route path="/usuarios/:id" element={<Users />} />
        <Route path="/contacto" element={<Contact />} />
        <Route path="*" element = {<Notfound />} />
      </Routes>
    </BrowserRouter>
  </div>

  /*
  <div>
    <BrowserRouter>
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/usuarios">Users</Link>
        </li>
        <li>
          <Link to="/contacto">Contact</Link>
        </li>
      </ul>
      <Routes>
        <Route exact path="/" element={<App />} />
        < Route path="/usuarios/:id" element={<Users />} />
        <Route path="/contacto" element={<Contact />} />
        <Route path="*" element = {<Notfound />} />
      </Routes>
    </BrowserRouter>
  </div>*/
)


ReactDOM.render(
  routing,
  document.getElementById('root')
);
