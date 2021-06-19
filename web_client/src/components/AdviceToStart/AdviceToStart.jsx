import React, { Component } from 'react';
import './styles.css';

class AdviceToStart extends Component {
    constructor(props) {
        super(props);
        this.state = {
            visible: this.props.visible
        }
    }

    componentWillReceiveProps(nextProps) {
        if (nextProps.visible !== this.state.visible) {
            this.setState({visible: nextProps.visible});
        }
    }

    render() {
        if(this.state.visible) {
            return (
                <div className='adviceToStart'>
                <h2>To get started enter the search word in the field</h2>
                </div>
            )
        } else {
            return (null);
        }
    };
}

export default AdviceToStart;
