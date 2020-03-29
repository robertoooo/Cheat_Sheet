## Rendering Content Conditionally
```js
class App extends Component {
  state = {
    persons: [
      { name: 'Betto', age: 29 },
      { name: "Aidin", age: 23 },
      { name: "Marwin", age: 223 }
    ],
    otherState: 'some other value',
    showPersons: false
  } //Managed inside the component

  togglePersonsHandler = () => {
    const doesShow = this.state.showPersons;
    this.setState({showPersons: !doesShow})

  }
  
  
   render() {
    return (
      <div className="App">
        <h1>Hi I am a react</h1>
        <p>This is really working </p>
        
        <button
          onClick={this.togglePersonsHandler}>Show Name</button>
        {
          this.state.showPersons === true ? //if the left side is true do the right side
            <div >
              <Person
                name={this.state.persons[0].name}
                age={this.state.persons[0].age} />
              <Person
                name={this.state.persons[1].name}
                age={this.state.persons[1].age}
                click={this.switchNameHandler.bind(this, 'Abdallah')}
                changed={this.nameChangeHandler} > I like horses</Person>
              <Person
                name={this.state.persons[2].name}
                age={this.state.persons[2].age} />

            </div> : null //elseif, if it is false render null  
        }

      </div>
    );
  }
}

```
