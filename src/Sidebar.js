import React from "react";
import "./sidebar.css";
class App extends React.Component {
  render() {
    return (
      <>
        <nav className="main-menu">
          <div className="scrollbar" id="style-1">
            <ul>
              <li>
                <a href="#">
                  <i className="fa fa-home fa-lg" />
                  <span className="nav-text">Home</span>
                </a>
              </li>
              <li>
                <a href="#">
                  <i className="fa fa-user fa-lg" />
                  <span className="nav-text">Login</span>
                </a>
              </li>
              <li className="darkerlishadow">
                <a href="#">
                  <i className="fa fa-clock-o fa-lg" />
                  <span className="nav-text">News</span>
                </a>
              </li>
              <li className="darkerli">
                <a href="#">
                  <i className="fa fa-desktop fa-lg" />
                  <span className="nav-text">Technology</span>
                </a>
              </li>
              <li className="darkerli">
                <a href="#">
                  <i className="fa fa-plane fa-lg" />
                  <span className="nav-text">Travel</span>
                </a>
              </li>
              <li className="darkerli">
                <a href="#">
                  <i className="fa fa-shopping-cart" />
                  <span className="nav-text">Shopping</span>
                </a>
              </li>
              <li className="darkerli">
                <a href="#">
                  <i className="fa fa-microphone fa-lg" />
                  <span className="nav-text">Film &amp; Music</span>
                </a>
              </li>
              <li className="darkerli">
                <a href="#">
                  <i className="fa fa-flask fa-lg" />
                  <span className="nav-text">Web Tools</span>
                </a>
              </li>
              <li className="darkerli">
                <a href="#">
                  <i className="fa fa-picture-o fa-lg" />
                  <span className="nav-text">Art &amp; Design</span>
                </a>
              </li>
              <li className="darkerli">
                <a href="#">
                  <i className="fa fa-align-left fa-lg" />
                  <span className="nav-text">Magazines</span>
                </a>
              </li>
              <li className="darkerli">
                <a href="#">
                  <i className="fa fa-gamepad fa-lg" />
                  <span className="nav-text">Games</span>
                </a>
              </li>
              <li className="darkerli">
                <a href="#">
                  <i className="fa fa-glass fa-lg" />
                  <span className="nav-text">Life &amp; Style</span>
                </a>
              </li>
              <li className="darkerlishadowdown">
                <a href="#">
                  <i className="fa fa-rocket fa-lg" />
                  <span className="nav-text">Fun</span>
                </a>
              </li>
            </ul>
            <li>
              <a href="#">
                <i className="fa fa-question-circle fa-lg" />
                <span className="nav-text">Help</span>
              </a>
            </li>
            <ul className="logout">
              <li>
                <a href="#">
                  <i className="fa fa-lightbulb-o fa-lg" />
                  <span className="nav-text">BLOG</span>
                </a>
              </li>
            </ul>
          </div>
        </nav>
      </>
    );
  }
}
export default App;
