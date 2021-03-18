import React from "react";
import Question from "./Question";
class Questions extends React.Component {
  state = {
    arr: [
      <Question index="1" aage={this.aage} />,
      <Question index="2" aage={this.aage} />,
      <Question index="3" aage={this.aage} />,
      <Question index="4" aage={this.aage} />,
      <Question index="5" aage={this.aage} />,
      <Question index="6" aage={this.aage} />,
    ],
    abhi: 0,
  };
  aage = () => {
    if (this.state.abhi === this.state.arr.length - 1) {
      this.setState({ abhi: 0 });
    } else {
      this.setState({ abhi: this.state.abhi + 1 });
    }
  };
  render = () => {
    return (
      <div>
        {this.state.abhi === this.state.arr.length - 1 ? (
          <div>
            <h1>
              BEST OF LUCK FOR FUTURE.... All Questions are succesfully
              submitted
            </h1>
          </div>
        ) : (
          this.state.arr[this.state.abhi]
        )}
        {this.state.abhi === this.state.arr.length - 1 ? (
          <div
            className="end"
            style={{
              display: "flex",
              justifyContent: "space-evenly",
              alignItems: "center",
            }}
          >
            <div>
              <button
                className="kj"
                style={{
                  backgroundColor: "blue",
                  color: "white",
                  cursor: "pointer",
                }}
              >
                Submit
              </button>
            </div>
          </div>
        ) : (
          <div
            className="end"
            style={{
              display: "flex",
              justifyContent: "space-evenly",
              alignItems: "center",
            }}
          >
            <div>
              <button
                className="kj"
                style={{
                  backgroundColor: "blue",
                  color: "white",
                  cursor: "pointer",
                }}
              >
                Submit
              </button>
            </div>
            <div>
              <button
                className="kj"
                style={{
                  backgroundColor: "green",
                  color: "white",
                  cursor: "pointer",
                }}
                onClick={() => {
                  this.aage();
                }}
              >
                Next
              </button>
            </div>
          </div>
        )}
      </div>
    );
  };
}
export default Questions;
