import React, { Component, useState } from 'react';
import { Row } from 'react-bootstrap';

import './styles.css';

class TopPanel extends Component {
  constructor(props) {
    super(props);
  }
  
  render() {
    return (
      <Row className={'topPanel'}>
        {/* <img src='../assets/sheltor_panel_logo.svg'
          className={styles.topLineMargin} /> */}

          <label className={'topLineMargin'}>Context</label>

      </Row>
    );
  };
}

export default TopPanel;