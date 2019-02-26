### TypeScript Cheat Sheet

```ts
//To loop over a dictionary
for (let key in myDictionary) {
    let value = myDictionary[key];
    // Use `key` and `value`
}


```

#### Difference between push and add
> "Push" can return the new length of the array and "Add" returns void.
```ts
 Array.add(array, item)
 Array.push([item1 [item2 [. . . [itemN ]]]])
 ```
