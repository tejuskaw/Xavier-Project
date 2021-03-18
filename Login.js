import React from "react";
import "./login.css";
export default class Login extends React.Component {
  state = {
    signin: true,
  };
  render = () => {
    return (
      <div className="helllo">
        <div className="top-heading">XAVIER STUDENT ADDA</div>
        <div
          className={`container ${
            this.state.signin ? "" : "right-panel-active"
          }`}
          id="container"
        >
          <div className="form-container sign-up-container">
            <form action="#">
              <h1 style={{ marginBottom: "35px" }}>Create Account</h1>
              <input className="input" type="text" placeholder="Name" />
              <input className="input" type="email" placeholder="Email" />
              <input className="input" type="password" placeholder="Password" />
              <button>Sign Up</button>
            </form>
          </div>
          <div className="form-container sign-in-container">
            <form action="#">
              <h1 style={{ marginBottom: "35px" }}>Sign in</h1>
              <input className="input" type="email" placeholder="Email" />
              <input className="input" type="password" placeholder="Password" />
              <a href="#">Forgot your password?</a>
              <button>Sign In</button>
            </form>
          </div>
          <div className="overlay-container">
            <div className="overlay">
              <div className="overlay-panel overlay-left">
                <h1>Welcome Back!</h1>
                <p>
                  To keep connected with us please login with your personal info
                </p>
                <button
                  onClick={() => {
                    this.setState({ signin: true });
                  }}
                  className="ghost"
                  id="signIn"
                >
                  Sign In
                </button>
              </div>
              <div className="overlay-panel overlay-right">
                <h1>Hello, Friend!</h1>
                <p>Enter your personal details and start journey with us</p>
                <button
                  onClick={() => {
                    this.setState({ signin: false });
                  }}
                  className="ghost"
                  id="signUp"
                >
                  Sign Up
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  };
}
