import unittest
from ToyRobot import ToyRobot


class TestToyRobot(unittest.TestCase):

    def setUp(self):
        """Set ToyRobot instance for each test."""
        self.robot = ToyRobot()

    def test_initial_position(self):
        """Test the initial position and direction of the robot."""
        self.assertEqual(self.robot.x, 0)
        self.assertEqual(self.robot.y, 0)
        self.assertEqual(self.robot.face, 'SOUTH')

    def test_place_valid_position(self):
        """Test placing the robot at a valid position."""
        self.robot.place(1, 2, 'EAST')
        self.assertEqual(self.robot.x, 1)
        self.assertEqual(self.robot.y, 2)
        self.assertEqual(self.robot.face, 'EAST')

    def test_place_invalid_position(self):
        """Test placing the robot at an invalid position."""
        self.robot.place(5, 5, 'NORTH')
        # Position is invalid, so it should stay at the initial position
        self.assertEqual(self.robot.x, 0)
        self.assertEqual(self.robot.y, 0)
        self.assertEqual(self.robot.face, 'SOUTH')

    def test_move(self):
        """Test moving the robot forward."""
        self.robot.place(0, 0, 'NORTH')
        self.robot.move()
        self.assertEqual(self.robot.x, 0)
        self.assertEqual(self.robot.y, 1)
        self.assertEqual(self.robot.face, 'NORTH')

    def test_move_out_of_bounds(self):
        """Test moving the robot out of bounds."""
        self.robot.place(0, 4, 'NORTH')
        self.robot.move()
        # Position is invalid, so it should stay at (0,4)
        self.assertEqual(self.robot.x, 0)
        self.assertEqual(self.robot.y, 4)
        self.assertEqual(self.robot.face, 'NORTH')

    def test_turn_right(self):
        """Test turning the robot right."""
        self.robot.place(0, 0, 'NORTH')
        self.robot.right()
        self.assertEqual(self.robot.face, 'EAST')

    def test_turn_left(self):
        """Test turning the robot left."""
        self.robot.place(0, 0, 'NORTH')
        self.robot.left()
        self.assertEqual(self.robot.face, 'WEST')

    def test_report(self):
        """Test the report function."""
        self.robot.place(2, 3, 'SOUTH')
        self.assertEqual(self.robot.report(), 'Toy\'s current position: 2,3,SOUTH')


if __name__ == '__main__':
    unittest.main()