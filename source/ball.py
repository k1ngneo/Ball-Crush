import math

from vector import Vec2D
from ball_widget import BallWidget


class Ball:
    
    class Body:
        MAX_SPEED = 120.0

        def __init__(self, position=Vec2D(0.0, 0.0), radius=1.0, gravity=False):
            self.pos = position
            self.rad = radius
            self.vel = Vec2D(0.0, 0.0)
            self.mass = (4.0 / 3.0) * math.pi * (self.rad**3)

            self.force = Vec2D(0.0, 0.0)
            self.is_gravity_affected = gravity
            self.is_drag_affected = False

    
    def __init__(self, position=Vec2D(0.0, 0.0), radius=1.0):
        self.body = Ball.Body(position, radius)

        self.__widget = BallWidget()
        self.__widget.color = (1.0, 1.0, 1.0, 1.0)
        self.update()

    def update(self):
        from game_screen import GameData
        self.__widget.pos = GameData.main_camera.world_to_clip(self.body.pos).t()
        self.__widget.radius = self.body.rad / GameData.main_camera.size
        self.__widget.update()

    def set_color(self, r, g, b, a):
        self.__widget.color = (r, g, b, a)

    def get_widget(self) -> BallWidget:
        return self.__widget
