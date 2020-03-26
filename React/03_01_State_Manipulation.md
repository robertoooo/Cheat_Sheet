# Two examples, one using the class-based and the other using the use-state-hook state manipulation.

## Class-based state manipulation 
```js

import React, { Component } from 'react';
import './App.css';
import Person from './Person/Person';

class App extends Component {
  state = {
    persons: [
      { name: 'Betto', age: 29},
      { name: "Aidin", age: 23},
      { name: "Marwin", age: 223}
    ]
  } //Managed inside the component
  
  switchNameHandler = () => {
    //console.log('Was clicked!');
    // DONT DO THIS this.state.persons[0].name = "ZAKNABOOT";
    this.setState({persons: [
      { name: 'Betto', age: 29},
      { name: "Adnan", age: 23},
      { name: "Marwin", age: 223}
    ]});
  }
  
  render() {
    return (
      <div className="App">
        <h1>Hi I am a react acho sharmote</h1>
        <p>This is really working </p>
        <button onClick={this.switchNameHandler}>switch Name</button>
        <Person name={this.state.persons[0].name} age={this.state.persons[0].age} />
        <Person name={this.state.persons[1].name} age={this.state.persons[1].age}> I like horses</Person> 
        <Person name={this.state.persons[2].name} age={this.state.persons[2].age} />
      </div>
    );
    // return React.createElement('div',{className: 'App'}, React.createElement('h1',null,'Does this work now?'));
  }
}

export default App;

```
## Use-state-hook state manipulation
```js
import React, { useState } from 'react';
import './App.css';
import Person from './Person/Person';

const App = props => {
  const [personsState, setPersonsState] = useState({
    persons: [
      { name: 'Betto', age: 29 },
      { name: "Adnan", age: 23 },
      { name: "Marwin", age: 223 }
    ]
  });
const [otherState, setOtherState] = useState('some other value')

  console.log(personsState,otherState, setOtherState)
  const switchNameHandler = () => {
    //console.log('Was clicked!');
    // DONT DO THIS this.state.persons[0].name = "ZAKNABOOT";
    setPersonsState({
      persons: [
        { name: 'Betto', age: 29 },
        { name: "Aidin", age: 23 },
        { name: "Marwin", age: 223 }
      ]
    });
  }

  return (
    <div className="App">
      <h1>Hi I am a react</h1>
      <p>This is really working </p>
      <button onClick={switchNameHandler}>switch Name</button>
      <Person name={personsState.persons[0].name} age={personsState.persons[0].age} />
      <Person name={personsState.persons[1].name} age={personsState.persons[1].age}> I like horses</Person>
      <Person name={personsState.persons[2].name} age={personsState.persons[2].age} />
    </div>
  );
  // return React.createElement('div',{className: 'App'}, React.createElement('h1',null,'Does this work now?'));

}

export default App;



```
