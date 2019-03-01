### TypeScript Cheat Sheet

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
 
# TypeScript Class
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
