import React from "react";
import "./tejus.css";
class App extends React.Component {
  render() {
    return (
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
          <div
            onClick={() => {
              this.props.OnStudyMaterial();
            }}
          >
            Study Material
          </div>
          <div
            onClick={() => {
              this.props.announcement();
            }}
          >
            Announcements
          </div>
          <div
            onClick={() => {
              this.props.OnPractice();
            }}
          >
            Practice
          </div>
          <div
            onClick={() => {
              this.props.Onaddposts();
            }}
          >
            ADD
          </div>
          <div
            onClick={() => {
              this.props.Onaddposts();
            }}
          >
            Account
          </div>
        </div>
      </div>
    );
  }
}
export default App;
