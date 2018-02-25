import math

class Turtle:
    def __init__(self, x_position=0, y_position=0, facing=0):
        self.position = (x_position, y_position)
        self.facing = facing % 1
        self.path = [self.position]

    @property
    def facing_angle(self):
        return 2 * math.pi * self.facing

    def turn_left(self, turn):
        """Turn left a `turn` fraction of a full turn."""
        self.facing = (self.facing + turn) % 1

    def turn_right(self, turn):
        """Turn right a `turn` fraction of a full turn."""
        self.facing = (self.facing - turn) % 1

    def go(self, length):
        """Go forward `length` steps."""
        x, y = self.position
        self.position = (
            x + length * math.cos(self.facing_angle),
            y + length * math.sin(self.facing_angle)
        )
        self.path.append(self.position)

