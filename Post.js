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
              alt="image"
              className="border-tlr-radius"
            />
          </div>
          <div className="card__content card__padding">
            <div className="card__meta">
              <a href="#">{this.props.heading}</a>
              <time>{this.props.date}</time>
            </div>
            <article className="card__article">
              <h2>
                <a href="#">{this.props.subheading}</a>
              </h2>
              <p>
                {this.props.description.length > 30
                  ? this.props.description + "..."
                  : this.props.description}
              </p>
              {this.props.description.length > 30 ? (
                <span>
                  <a href="#" style={{ color: "blue" }}>
                    Read More
                  </a>
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
                By <a href="#">{this.props.author}</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
