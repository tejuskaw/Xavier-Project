import React from "react";
import Header from "./Header";
import Questions from "./Questions";
import Posts from "./Posts";
import StudyMaterial from "./StudyMaterial";
import Login from "./Login";
import Addposts from "./Addposts";
class App extends React.Component {
  state = {
    current: "addnew",
    logined: true,
  };
  Onannouncement = () => {
    this.setState({ current: "announcements" });
  };
  OnPractice = () => {
    this.setState({ current: "questions" });
  };
  OnStudyMaterial = () => {
    this.setState({ current: "material" });
  };
  Onaddposts = () => {
    this.setState({ current: "addnew" });
  };
  render = () => {
    return this.state.logined === true ? (
      <div>
        <Header
          announcement={this.Onannouncement}
          OnPractice={this.OnPractice}
          OnStudyMaterial={this.OnStudyMaterial}
          Onaddposts={this.Onaddposts}
        />
        {this.state.current === "announcements" ? (
          <Posts />
        ) : this.state.current === "questions" ? (
          <Questions />
        ) : this.state.current === "material" ? (
          <StudyMaterial />
        ) : this.state.current === "addnew" ? (
          <Addposts />
        ) : (
          ""
        )}
      </div>
    ) : (
      <>
        <Login />
      </>
    );
  };
}
export default App;
