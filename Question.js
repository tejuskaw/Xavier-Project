import React from "react";
import "./Question.css";
class Question extends React.Component {
  render = () => {
    return (
      <div className="Question">
        <div className="head">
          <div>QUESTION NO. {this.props.index}</div>
          <div>Timer time</div>
        </div>
        <div className="question-space">
          <div>this is the question ??</div>
          <hr />
          <div>
            <input type="radio" />
            option1
            <br />
          </div>
          <hr />
          <div>
            <input type="radio" />
            option1
            <br />
          </div>
          <hr />
          <div>
            <input type="radio" />
            option1
            <br />
          </div>
          <hr />
          <div>
            <input type="radio" />
            option1
            <br />
          </div>
        </div>
      </div>
    );
  };
}
export default Question;
