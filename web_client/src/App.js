import React, { Component } from 'react';
import { sendMsg } from './api/index';
import Input from './components/Input/Input'
import Sentence from './components/Sentence/Sentence';
import TopPanel from './components/TopPanel/TopPanel';
import AdviceToStart from './components/AdviceToStart/AdviceToStart'

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: true,
      items: []
    };

    this.sendReqeust = this.sendReqeust.bind(this);
  }

  sendReqeust(event) {
    sendMsg(event.target.value, (res)=> {
      this.setState({items: res});
    })
  }

  componentDidMount() {
    fetch("http://localhost:5000/getjson")
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            isLoaded: true,
            items: result
          });
        },
        // Note: it's important to handle errors here
        // instead of a catch() block so that we don't swallow
        // exceptions from actual bugs in components.
        (error) => {
          this.setState({
            isLoaded: true,
            error
          });
        }
      )
  }

  render() {
    const { error, isLoaded, items } = this.state;
    if (error) {
      return <div>Error: {error.message}</div>;
    } else if (!isLoaded) {
      return <div>Loading...</div>;
    } else {
      return (
        <div>
          <TopPanel/>
          <Input className="InputField" send={this.sendReqeust}/>
          
          <AdviceToStart visible={this.state.items.length == 0 }/>
          <div>
            {items.map(((item) => (
              <Sentence className="post" key={item.number} message={item}/>
            )))}
          </div>
        </div>
      );
    }
  }
}

export default App;
