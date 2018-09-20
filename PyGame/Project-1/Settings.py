class Settings:
    framerate = 0
    resolution = (0, 0)

    def __init__(self):
        # self.resolution = (720, 540)  # WIDTH, HEIGHT
        self.resolution = (1280, 720)   # WIDTH, HEIGHT
        self.framerate = 60

    def __init__(self, width, height, framerate):
        self.resolution = (width, height)
        self.framerate = framerate
