### Arithmetic Arranger
A program that takes a list of addition and subtraction arithmetic calculations and returns them in a specific format, as well as the answers if `True` 
is included as the second argument when the function is called.

### Time Calculator
This is a program that takes a start time and a duration as input and returns the new time - the day of the week can also be added as an optional argument
and the new day will be returned as well. For example, `12:12 PM, 17:15, Saturday` will return `5:27AM, Sunday (next day)` and `01:49 PM, 67:56` will return `9:45 AM (3 days later)`.

### Budget Calculator
A program that uses a category class from which different types of budgeting category classes can be created. The class has various methods involving moving money or checking balances, as well as a method that creates a bar chart based on spending habits.

### Polygon Area Calculator
This program contains a rectangle parent class that creates a shape based on the width and height, as well as a square child class. They have various methods including the ability to check how many times another shape will fit inside and using stars to print the size of the shape within certain boundaries.

### Probability Calculator
Through OOP, this program determines the approximate probability of drawing certain balls randomly from a hat. Various arguments are factored in including 
the number of balls in the draw and the number of experiemnts performed. For example, the following code will return a random number between 0 and 1.
  `hat = Hat(black=6, red=4, green=3). 
  <br/>
  probability = experiment(hat=hat,  
  <br/>
                    expected_balls={"red":2,"green":1},  
                    <br/>
                    num_balls_drawn=5,  
                    <br/>
                    num_experiments=2000)`
