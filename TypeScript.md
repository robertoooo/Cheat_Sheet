# TypeScript Cheat Sheet

**To Loop over a Dictionary**
```ts
//To loop over a dictionary
for (let key in myDictionary) {
    let value = myDictionary[key];
    // Use `key` and `value`
}


```


**To Loop over a List**
```ts
//To loop over a list
for (var element in list) {
    console.log(element)
}


```

**Difference between push and add**
> "Push" can return the new length of the array and "Add" returns void.
```ts
 Array.add(array, item)
 Array.push([item1 [item2 [. . . [itemN ]]]])
 ```

**Type of Variable**
```ts
console.log(typeof(variable))
 ```
 
 ---
 
## TypeScript Class & Interface
#### Class
Defning a class named PizzaMaker. 
```ts
class PizzaMaker {
  static create(event: { name: string; toppings: string[] }) {
    return { name: event.name, toppings: event.toppings };
  }
} 
```
PizzaMaker has a static method called create. We can use this method without creating an instance of the class.
We just invoke the method on the class directly.
```ts
const pizza = PizzaMaker.create({
  name: 'Inferno',
  toppings: ['cheese', 'peppers'],
});

console.log(pizza);
// Output: { name: 'Inferno', toppings: [ 'cheese', 'peppers' ] }
```
If PizzaMaker did not define create as a static method, then we would need to create an instance of PizzaMaker
```ts
const pizzaMaker = new PizzaMaker();
```
We get the same output with create and static method. Adding static properties and methods to a class makes them act like a singelton while defning a non-static properties and methods make them act like a factory. 

Unique to TypeScript is the ability to use classes for type-checking. Let's declare a class that defines what a Pizza looks like
```ts
class Pizza {
  constructor(public name: string, public toppings: string[]) {}
}
```
Here we define the class properties from the arguments of the constructor. Pizza can create objects that have a name and a toppings propery.

```ts
const pizza = new Pizza('Inferno', ['cheese', 'peppers']);

console.log(pizza);
// Output: Pizza { name: 'Inferno', toppings: [ 'cheese', 'peppers' ] }
```
The output of new Pizza(...) and PizzaMaker.create(...) is the same. Both approaches yield an object with the same structure.
Therefore we can use the Pizza class to type-check the event argument of PizzaMaker.create(...)
```ts
class Pizza {
  constructor(public name: string, public toppings: string[]) {}
}

class PizzaMaker {
  static create(event: Pizza) {
    return { name: event.name, toppings: event.toppings };
  }
}
```
Now we have a portable construct where we can enforce the same object structure defined in Pizza. 
Append export to the defintion of Pizza and you get access to it from anywhere in your applciation.

Using the Pizza as a class is great if we want to define and create a Pizza, but what if we only want to define a structure of a Pizza but we'd never need to instantiate it? That's when interface comes handy!


#### Interface

