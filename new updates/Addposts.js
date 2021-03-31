import React from "react";
import "./addpost.css";
//import { post } from "./extra";
import RichTextEditor from "./Hi";
export default class Addposts extends React.Component {
  state = {
    send: false,
  };
  post = () => {
    this.setState({ send: true });
    setTimeout(() => {
      this.setState({ send: false });
    }, 1000);
  };

  render = () => {
    return (
      <div id="wrapper">
        <div id="header" className="noselect">
          New Entry
        </div>
        <div id="content">
          <input id="title" type="text" placeholder="Your title here..." />
          <div id="triangle-bottomright" />

          <RichTextEditor />
          <div id="footer">
            <div id="footer-left">
              <button className="btn btn-primary" onClick={() => this.post()}>
                {this.state.send ? (
                  <i class="fas fa-spinner fa-spin"></i>
                ) : (
                  "Post"
                )}
              </button>
              {/*<i class="fas fa-spinner fa-spin"></i>*/}
              <input
                type="file"
                name="file"
                id="file"
                className="inputfile"
                accept="text/*"
              />
              <label htmlFor="file">
                <i className="fas fa-paperclip" />
              </label>
            </div>
            <div id="footer-right">
              <button className="btn btn-secondary">
                <i className="far fa-trash-alt" />
              </button>
            </div>
          </div>
        </div>
      </div>
    );
  };
}
