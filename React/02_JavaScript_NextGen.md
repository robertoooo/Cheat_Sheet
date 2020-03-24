# Classes, Properties & Methods

### ES6
```javascript
class Human {
  constructor(){
    this.gender = 'male';
  }
  printGender() {
    console.log(this.gender);
  }
}

class Person extends Human {
  constructor() { //Will initially run when the class is called
    super(); //Used to correctly initiate the parrent class, if using constructor
    this.name ='Max';
  }
  printMyName() {
    console.log(this.name);
  }
}

const person = new Person();
person.printMyName();
person.printGender();
```
### ES7, the constructor will be created in the compilation, this way we do not need to add 'this.' to all variables we create. 
```js
class Human {
  gender = 'male';
  
  printGender = () => {
    console.log(this.gender);
  }
}

class Person extends Human {
  name ='Max';
  
  printMyName = () => {
    console.log(this.name);
  }
}

const person = new Person();
person.printMyName();
person.printGender();


```

# Spread & Rest Operator
### Spread Operator for arrays and objects
```js
// Spread Operator array
const oldArray = [1, 2, 3, 4]
const newArray = [...oldArray, 5, 6]; //Appends oldArray to the array instead of appending an array inside the array
console.log(newArray)

//Spread Operator object

const person = {
  name: 'Robert'
};

const newPerson = {
  ...person, //appends person keypair of object inside a new object instead of appending an object inside an object.
  age: 27
}

console.log(newPerson)



```
### Rest operator 
```js
// Rest operator
const filter = (...args) => { //Used to have a variable number of arguments
  return args.filter(el => el === 1); // 3 = checks for type and value 
}

console.log(filter(1,2,3));
```

