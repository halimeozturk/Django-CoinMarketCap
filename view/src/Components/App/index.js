import React, { Component } from 'react';

const API = 'http://localhost:8000/';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      count: 0,
    };
  }


  componentDidMount() {
    fetch(API)
      .then(response => response.json())
      .then(_data => 
        this.setState({
          data : _data
        })
      )

    this._interval = setInterval(() => {
      this.setState({count: this.state.count + 1});
      
      fetch(API)
      .then(response => response.json())
      .then(_data => 
        this.setState({
          data : _data
        })
      )
    }, 5000);

    }
  
  componentWillUnmount() {
    clearInterval(this._interval);
}

  render() {
    return (
     <div>
       <table>
         <tbody>
           <tr>
            <td width="1000px"><b>Name</b></td>
            <td width="1000px"><b>Market Cap</b></td>
            <td width="1000px"><b>Price</b></td>
            <td width="1000px"><b>Volume (24h)</b></td>
            <td width="1000px"><b>Change(24h)</b></td>
            <td width="1000px"><b>Price Graph(7d)</b></td>
           </tr>
           {this.state.data.map((item, i) => (
             <tr key={i}>
              <td width="1000px"><li>{item.name}</li></td> 
              <td width="1000px">{item.market_cap}</td>
              <td width="1000px">{item.price}</td>
              <td width="1000px">{item.percent_change_24h}</td>
              <td width="1000px">{item.percent_change_24h}</td>
              <td width="1000px">{item.percent_change_7d}</td> 
              </tr>
           ))}
           </tbody>
        </table>  
       </div>
    );
  }

}

export default App;