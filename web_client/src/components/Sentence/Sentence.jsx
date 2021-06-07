import React, { Component } from 'react';
import './styles.css';

class Sentence extends Component {
  constructor(props) {
    super(props);
    this.state = {
      message: this.props.message
    }
  }

  componentWillReceiveProps(nextProps) {
    if (nextProps.message !== this.state.message) {
      this.setState({ message: nextProps.message });
    }
  }
  
  render() {
    return (
      <p className={'sentence'}>
        {this.state.message.left_part_of_sentence}
        <mark className={'emphasis'}>{this.state.message.key_sentence}</mark>
        {this.state.message.right_part_of_sentence}
      </p> 
    );
  };
}

export default Sentence;
