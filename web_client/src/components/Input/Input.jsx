import React, { Component, useState } from 'react';

import './styles.css';

class Input extends Component {
  constructor(props) {
    super(props);
    this.state = { lastValue: 'Hello' };

    this.handleOnChanged = this.handleOnChanged.bind(this);
    this.handleOnEnter = this.handleOnEnter.bind(this);
  }

  handleOnChanged(event) {
    this.setState({lastValue: event.target.value});
  }

  handleOnEnter(event) {
    if (event.charCode === 13 && event.target.value != "") {
      console.log(event.target.value)
      this.props.send(event);
    }
  }

  render() {
    return (
      <div className={'input'}>
        <input value={this.state.lastValue} 
          onChange={this.handleOnChanged}
          onKeyPress={this.handleOnEnter}
        placeholder="Type sentence enter to Send"/>
      </div>
    );
  };

}

export default Input;
