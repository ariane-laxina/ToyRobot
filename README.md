# ToyRobot
## Overview
The ToyRobot application simulates a toy robot moving on a grid. The robot can be placed at specific coordinates, moved around, and rotated in different directions. 
The application takes user commands to control the robot and provides feedback on its current position and direction.

## Features
Place the robot on the grid at a specific location and direction.
Move the robot forward.
Rotate the robot left or right.
Report the robot’s current position and direction.

## Requirements
Python 3.x

## Setup
1. Clone the Repository
Clone this repository to your local machine using Git:
```sh
git clone https://github.com/yourusername/ToyRobot.git
 ```

Replace https://github.com/yourusername/ToyRobot.git with the actual URL of your repository.

2. Navigate to the Project Directory
Change to the project directory:
```sh
cd ToyRobot
 ```

3. Set Up a Virtual Environment (Optional but recommended)
Create and activate a virtual environment to manage dependencies:

```sh
python -m venv venv
 ```

Activate the virtual environment:

* On Windows:

```sh
venv\Scripts\activate
```

* On macOS/Linux:

```sh
source venv/bin/activate
```

## Commands
Here are the commands you can use to interact with the robot:

* PLACE x,y,face: Place the robot at position (x, y) facing face (NORTH, EAST, SOUTH, WEST).<br/>
* MOVE: Move the robot one step forward in the direction it is facing..<br/>
* LEFT: Turn the robot 90 degrees to the left..<br/>
* RIGHT: Turn the robot 90 degrees to the right..<br/>
* REPORT: Display the robot’s current position and direction.

## Examples
Place the robot at position (0,0) facing SOUTH:

```sh
PLACE 0,0,SOUTH
```

Move the robot forward:

```sh
MOVE
```

Turn the robot left:

```sh
LEFT
```

Report the robot’s position:

```sh
REPORT
```


## Error Handling
* Invalid Position: If a move command results in the robot going out of bounds, an error message will be displayed. <br/>
* Invalid Command: Commands that are not recognized will trigger an error message.

## Contributing
If you want to contribute to the development of this project, please fork the repository and submit a pull request with your changes.
