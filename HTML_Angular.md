### HTML Cheat sheet
Input box in the html that triggers a function in typescript.
HTML
```html
Enter choices: fpc272extra low
<input #box1 (keyup.enter)="loadSession([box1.value,box2.value])">
<input #box2 (keyup.enter)="loadSession([box1.value,box2.value])">
<p>{{testClickedInfoList}}</p>
```
The backend code in TypeScript:
```ts
    loadSession(testClickedInfoList: []) { 
        this.testClickedInfoList = testClickedInfoList
        console.log(testClickedInfoList) }	//Logs an array of multiple values
```



The class in the HTML for a picture have an css connected to it, describing at least the size of the picture.

```html

<h2> Welcome {{name}}	</h2>				<!-- Interpolate the name -->
<input type="text" value="Robert">			<!-- Create an input element filled with Robert -->
	In console: $0.getAttribute('value')	<!-- prints Robert--> 
	In console: $0.value					<!-- prints Robert even after changing the value--> 
	
<input [id]="myId" type="text" value="Robert">	
	<!-- Property binding: Binding the value to the id property -->
	[id]="myId" === bind-id = "myId" 
	
<input id="{{myId}}" type="text" value="Robert">	
	<!-- Interpolate id instead of property binding -->
	[id]="myId"
	
##########################################################################

<app-test></app-test>   <!-- Import a HTML to another HTML  -->

<h2 [ngClass]="messageClasses"> Betto </h2>  <!-- Class Binding, prints betto with the attributes of messageClasses  -->
 public messageClasses = {
   "text-success": !this.hasError,
   "text-danger": this.hasError,
   "text-special": this.isSpecial}

<h2 [style.color]="hasError ? 'red' : 'green'">Style Binding </h2> <!-- red if true, else green -->
   <!-- Set the colour of Style Binding depending on the state of hasError -->

<h2 [style.color]="highlightColor">Style Binding 2 </h2>
   <!-- Dynamically bind the color of Style Binding 2 to variable highlightolor -->
   public highlightColor = "orange";

<h2 [ngStyle]="titleStyles" > Style Binding 3 </h2>
   <!-- Use ng to apply multiple styles -->
   public titleStyles = {
       color: "blue",
       fontStyle: "italic"}

<button (click)= "onClick()">Köp en Cheesburger</button>
   <!-- Create a button that listens for a click event
   The event runs the onClick() method which prints it in console -->
   onClick(){console.log('Welcome to Codeevolution')}
```


Template Reference Variable
```html
   <input #myInput type = "text">
   <button (click)="logMessage(myInput.value)">Log</button>
   <!-- Using a reference variable myInput to store the text input
   On click, send the value to method logMessage which prints it to consol-->
   logMessage(value){console.log(value);}
```

Two way binding
```html
 <input [(ngModel)]="name" type = "text">
 {{name}}
 <!-- From the input, the value flows to the class property
 and from the class property the value flows back to the template-->
 
 ```
