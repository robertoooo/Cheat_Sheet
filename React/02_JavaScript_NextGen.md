## Classes, Properties & Methods
JavaScript - filter, map and reduce
ES6 - arrow functions, template literals, defualt parameters, object literals. rest and spread operators and destructuring assigment.

### ES5
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
### ES6, the constructor will be created in the compilation, this way we do not need to add 'this.' to all variables we create. 
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

## Spread & Rest Operator
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
const newPerson = Object.assign({}, person); //Same as the spread operator


console.log(newPerson)



```
### Rest operator 
```js
// Rest operator is used to have a variable number of arguments
const filter = (...args) => { //Used to have a variable number of arguments
  return args.filter(el => el === 1); // 3 = checks for type and value 
}

console.log(filter(1,2,3));
```

## Deconstructering
Like spread, except here we can pull out one element instead of all.
Possible to do with objects as well.

```js
const numbers = [1,2,3];

[num1, , num3] = numbers; 

console.log(num1,num3);
```
## Reference and Primitive Types
Copying primitive types such as numbers, strings and booleans will copy the value.
Copying reference types such as objects and arrays will copy the pointer and not the actual value.

```js
const person = {
  name: 'Robert'
};

const secondPerson = {
  ...person //Using the spread operator creates a real copy of the value
};

const thirdPerson = {
  person //Copies the pointer
};

person.name = 'Xristina';

console.log(secondPerson) //Logs Robert
console.log(thirdPerson) //Logs Xristina

```

## Array Functions
The array function map executes on each element in the numbers array. Returns a real new array.

```js
const numbers = [1,2,3];

const doubleNumArray = numbers.map((num) =>{
  return num*2; 
});

console.log(numbers); //[1,2,3]
console.log(doubleNumArray); //[2,4,6]

```

## Question mark or conditiional operator
Is a ternary operatir that has three operands.
```js
condition ? value if true : value if false
```
## For loop on an Await function 
```js
for (const <object> of await <listofobject>){
  Object.assig something 
}
```

## Concat and push
```js
//immutably returns a new array with pushed object/list of state.counter
results: state.results.concat(state.counter) 
//mutably pushes state.counter to the state.results array
results: state.results.push(state.counter) 
```
## Filter
```js
//Returns a new array, function as an input and it is executed on each element in the array.
const updatedArray = state.results.filter(result => result.id !== action.resultElId); 
```
