import React from "react";
import Question from "./Question";
class Questions extends React.Component {
  state = {
    arr: [
      <Question index="8" next={this.next} />,
      <Question index="2" next={this.next} />,
      <Question index="5" next={this.next} />,
    ],
    abhi: 0,
  };
  next = () => {
    console.log("called");
    if (this.state.abhi < this.state.arr.length) {
      this.setState.abhi = this.state.abhi + 1;
    }
  };
  render() {
    return this.state.arr[this.state.abhi];
  }
}
export default Questions;
