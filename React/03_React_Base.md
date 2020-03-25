Install the React create app and create an app 
```sh
npm i create-react-app -g #-g for global
create-react-app appname #creates an app
npm start #starts the application
```

### Components
When creating components, you have the choice between **two different ways**:

1. **Functional components** (also referred to as "presentational", "dumb" or "stateless" components

```js const cmp = () => { return <div>some JSX</div> } ```

2. **Class-based components** (also reffered to as "containers", "smart" or "stateful" components)

```js class Cmp extends Component { render () { return <div>some JSX</div> } } ```
