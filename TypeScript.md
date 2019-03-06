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
 
 **Add an object from a class**
 The class
 ```ts
 export class car {
    carName: string;
    carID: string;
    carAddons: string[];
}
 ```
 
 Creating the list car_list of objects car
 ```ts
 let car_list: car[] = []  //car_list is a list of cars
 ```
 
 

