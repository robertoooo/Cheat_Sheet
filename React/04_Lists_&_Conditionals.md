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
## Handling Dynamic Content "The JavaScript Way"
Instead of having the condition inside the render method we put the object inside a javascript if statement outside the render method.

```js
render() {

    let persons = null;

    if (this.state.showPersons) {
      persons = (
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

        </div>

      );
    }

    return (
      <div className="App">
        <h1>Hi I am a react acho sharmote</h1>
        <p>This is really working </p>
        <button
          style={style}
          onClick={this.togglePersonsHandler}>Switch Name</button>
        {persons}

      </div>
    );
  }

```

## Update State Immutably
You should alwats update a state in an immutable fashion, meaning create a copy and change it instead of just copying the pointer.
Using the ... spread operator is the preferred way. Persons is a list of objects. 
```js
const persons = this.state.persons.slice(); //Copies the full array instead of copying the pointer
const persons = [...this.state.persons]; //Spreads out the elements in the array into a list of elements, a new array with the objects from the old array
```

## CSS add dynamic Classes
In the css file
```js
.red {
  color: red;
}
.bold {
  font-weight: bold;
}
```
In the class file
```js
import './App.css';
 state = {
    persons: [
      { id: 'ett', name: 'Betto', age: 29 },
      { id: 'tva', name: "Xristina <3, I love you", age: 23 },
      { id: 'tre', name: "Marwin", age: 223 }
    ]}
    
render() {
    if (this.state.persons.length <= 2){
      classes.push('red'); //classes = ['red]
    }
    if (this.state.persons.length <= 1){
      classes.push('bold'); //classes = ['red]
    }
 return (
        <p className={classes.join(' ')}>YAA RABBIII</p>
  )
}
```
