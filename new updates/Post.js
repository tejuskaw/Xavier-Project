import React, { Component } from "react";
import "./Post.css";
export default class Post extends Component {
  render() {
    return (
      <div className="wrapper article">
        <div className="card radius shadowDepth1">
          <div className="card__image border-tlr-radius">
            <img
              src={this.props.image}
              alt="inside"
              className="border-tlr-radius"
            />
          </div>
          <div className="card__content card__padding">
            <div className="card__meta">
              <span>{this.props.heading}</span>
              <time>{this.props.date}</time>
            </div>
            <article className="card__article">
              <h2>
                <span>{this.props.subheading}</span>
              </h2>
              <p>
                {this.props.description.length > 30
                  ? this.props.description + "..."
                  : this.props.description}
              </p>
              {this.props.description.length > 30 ? (
                <span>
                  <span style={{ color: "blue" }}>Read More</span>
                </span>
              ) : (
                ""
              )}
            </article>
          </div>
          <div className="card__action">
            <div className="card__author">
              <img src={this.props.authorimg} alt="user" />
              <div className="card__author-content">
                By <span>{this.props.author}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
