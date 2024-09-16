class ToyRobot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.face = 'SOUTH'
        self.table_size = 5

    def place(self, x, y, face):
        if self.is_valid_position(x, y):
            self.x = x
            self.y = y
            self.face = face
        else:
            print("Position is not valid")

    def move(self):
        if self.face == "NORTH" and self.is_valid_position(self.x, self.y + 1):
            self.y += 1
        elif self.face == "SOUTH" and self.is_valid_position(self.x, self.y - 1):
            self.y -= 1
        elif self.face == "EAST" and self.is_valid_position(self.x + 1, self.y):
            self.x += 1
        elif self.face == "WEST" and self.is_valid_position(self.x - 1, self.y):
            self.x -= 1
        else:
            print("Position is not valid")

    def is_valid_position(self, x, y):
        return 0 <= x < self.table_size and 0 <= y < self.table_size

    def right(self):
        directions = ["NORTH", "EAST", "SOUTH", "WEST"]
        current_index = directions.index(self.face)
        self.face = directions[(current_index + 1) % 4]

    def left(self):
        directions = ["NORTH", "EAST", "SOUTH", "WEST"]
        current_index = directions.index(self.face)
        self.face = directions[(current_index - 1) % 4]

    def report(self):
        return f"Toy's current position: {self.x},{self.y},{self.face}"


def process_command(command, robot):
    if command.startswith("PLACE"):
        _, position = command.split(" ")
        x, y, face = map(str, position.split(","))
        robot.place(int(x), int(y), face)
    elif command == "MOVE":
        robot.move()
    elif command == "LEFT":
        robot.left()
    elif command == "RIGHT":
        robot.right()
    elif command == "REPORT":
        print(robot.report())
    else:
        print("Command is not valid")


if __name__ == "__main__":
    robot = ToyRobot()

    while True:
        user_input = input("Enter your command: ")
        process_command(user_input, robot)