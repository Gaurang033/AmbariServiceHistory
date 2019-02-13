import React, { Component } from 'react';
import StatusBarContainer from './containers/StatusBar'

class App extends Component {
  render() {
    return (
      <div style= {{width: 960, margin: 'auto'}}>
        <StatusBarContainer></StatusBarContainer>
      </div>
    );
  }
}

export default App;
