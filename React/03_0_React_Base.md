## Install the React create app and create an app 
```sh
npm i create-react-app -g #-g for global
create-react-app appname #creates an app
npm start #starts the application
```
To install peer dependencies
```js
npm install -g npm-install-peers
npm-install-peers
```
To see the npm config list
```js
npm config list 
```

## Components
When creating components, you have the choice between **two different ways**:

1. **Functional components** (also referred to as "presentational", "dumb" or "stateless" components

```js 
const cmp = () => { return <div>some JSX</div> } 
```

2. **Class-based components** (also reffered to as "containers", "smart" or "stateful" components)

```js 
class Cmp extends Component { render () { return <div>some JSX</div> } } 
```
## Props & State
Props and state are **CORE concepts** of React. Changes in props and/or state trigger React to render your components and potentially update the DOM in the browser.

#### Props
props allow you to pass data from a parent (wrapping) component to a child (embedded) component.

You can name this argument whatever you want. React will pass one argument to your component function, an object, which contains all the properties set up.
```js
const post = (props) => {
  return (
    <div>
      <h1>{props.title}</h1>
    </div>
  );
}
```

#### State
Whilts props allow you to pass data down the component tree (and hence trigger an UI update), state is used to change the component, state from within. Changes to state also triggers an UI update.

Only class based components can define and use state. You can pass the state down to functional components, but these then can't edit it. 

```js
class NewPost extends Component { // state can only be accessed in a class-based component.
  state = {
    counter: 1
  };
  
  render () { //Needs to be implemented in class-based components. Needs to return some JSX!
    return (
      <div>{this.state.counter}</div>
    );
  }
}
```

