import React from "react";
import Header from "./Header";
import Questions from "./Questions";
import Posts from "./Posts";
class App extends React.Component {
  state = {
    current: "questions",
  };

  Onannouncement = () => {
    this.setState({ current: "announcement" });
  };
  OnPractice = () => {
    this.setState({ current: "questions" });
  };
  render() {
    console.log("rendered");
    return (
      <div>
        <Header
          announcement={this.Onannouncement}
          OnPractice={this.OnPractice}
        />
        {this.state.current === "announcement" ? (
          <Posts />
        ) : this.state.current === "questions" ? (
          <Questions />
        ) : (
          "sorry"
        )}
      </div>
    );
  }
}
export default App;
