## Class-based vs Functional Components
![Class vs Functional Components](./pics/ClassVsFunc.png)


## Component Creation Lifecycle
Components Creation Lifecycle with class based components
```js
constructor(props)                      //Call super(props) Do:Set up state Don't: Cause side effects
getDerivedStateFromProps(props,state)   //Do: Sync State Don't: Cause side effects
render()                                //Prepare & structure your JSX Code
  *Render Child Components*
componentDidMount()                     //Do: Cause Side-Effects Don't: Update State Synchronys (triggers re-render)

```
More Class-based Components
```js
componentDidCatch()
componentWillUnmount()

```
## Component Update Lifecycle

```js
getDerivedStateFromProps(props,state)       //Do: Sync State to Props Don't: Cause Side-Effects
shouldComponentUpdate(nextProps,nextState)  //Do: Decide whether to Continue or Not
render()                                    //Prepare & Structure your JSX code
 *Update Child Component Props*             
getSnapshotBeforeUpdate(prevProps,prevState) //Do: Last-minute DOM ops Don't: Cause Side-Effects
componentDidUpdate()                         //Do: Cause Side-Effects Don't Update State (triggers re-render)
```

## useEffect() in Functional components
```js
import React, { useEffect } from 'react';

const cockpit = (props) => {
    useEffect(() => {
        console.log('[Cockpit.js] useEffect', props);
        // HTTP request, updates when component is created and updated
        // Writing something in the person box will update app which will update cockpit
        setTimeout(() => {
            alert('Saved data to cloud!');
        }, 1000)
    }, [props.persons]); //Will only update when persons change, if empty it will only run the first time

    
    return (
        <div>
            <h1>{props.title}</h1>
        </div>
    );
};

export default cockpit; 
```
