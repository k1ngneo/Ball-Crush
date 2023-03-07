from camera import Camera
from vector import Vec2D


class SceneData:
    main_camera = Camera(pos=Vec2D(0.0, 0.0), size=20.0)

    def __init__(self):
        self.balls = []
        self.ball_spawn_interval = 3
        self.amount_of_balls = 5
        self.balls_speed = 10
