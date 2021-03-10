import React from "react";
import "./tejus.css";
class App extends React.Component {
  render() {
    return (
      <>
        <div className="nav">
          <input type="checkbox" id="nav-check" />
          <div className="nav-header">
            <div className="nav-title">Xavier Student Adda</div>
          </div>
          <div className="nav-btn">
            <label htmlFor="nav-check">
              <span />
              <span />
              <span />
            </label>
          </div>
          <div className="nav-links">
            <a>Study Material</a>
            <a
              href="#"
              onClick={() => {
                this.props.announcement();
              }}
            >
              Announcements
            </a>
            <a
              onClick={() => {
                this.props.OnPractice();
              }}
            >
              Practice
            </a>
            <a href="#">Events</a>
            <a href="#">Time-Table</a>
          </div>
        </div>
      </>
    );
  }
}
export default App;
