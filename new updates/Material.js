import React from "react";
import "./material.css";
export default class StudyMaterial extends React.Component {
  render = () => {
    return (
      <div className="product_card article">
        <img
          src="https://source.unsplash.com/featured/?camera"
          className="product_image"
          alt="PRODUCT"
        />
        <section>
          <h1 className="title">{this.props.title}</h1>
          <p className="price">{this.props.branch}</p>
          <p className="price">{this.props.semister}</p>

          <p className="price" style={{ color: "black" }}>
            by -{this.props.author}
          </p>
        </section>
      </div>
    );
  };
}
