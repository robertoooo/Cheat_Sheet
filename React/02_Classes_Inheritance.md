ES6
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
ES7, the constructor will be created in the compilation, this way we do not need to add 'this.' to all variables we create. 
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
