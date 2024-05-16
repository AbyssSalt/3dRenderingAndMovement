import pygame
from math import sin, cos, radians


class Screen:
    def __init__(self, Dimensions, Plane, Color):
        self.Color = Color
        self.Screen = pygame.display.set_mode(Dimensions)
        self.Dimensions = pygame.display.get_window_size()
        self.Plane = Plane

    def DrawToScreen(self):
        pygame.display.flip()
        self.Screen.fill(self.Color)


class Camera:
    def __init__(self, Position, Rotation):
        self.Rotations = Rotation
        self.Positions = Position

    def Update(self, Movement, Rotate=(0,0,0)):
        self.Positions = [a + b for a, b in zip(self.Positions, Movement)]
        self.Rotations = [a + b for a, b in zip(self.Rotations, Rotate)]

class Poly:
    def __init__(self, Vertices, Color):
        self.Verts = Vertices
        self.Color = Color

    def Draw(self, Camera, Screen):
        CameraRotation = Camera.Rotations
        CameraPosition = Camera.Positions
        ScreenWidth, ScreenHeight = Screen.Dimensions
        ScreenPlane = Screen.Plane

        Csins = [sin(radians(Angle)) for Angle in CameraRotation]
        Ccoss = [cos(radians(Angle)) for Angle in CameraRotation]

        PlaneProjections = []
        Dist = 0
        for Vertex in self.Verts:
            Wx = Vertex[0] - CameraPosition[0]
            Wy = Vertex[1] - CameraPosition[1]
            Wz = Vertex[2] - CameraPosition[2]

            Cx = Wx * Ccoss[1] * Ccoss[2] - Wy * Csins[2] + Wz * Csins[1]
            Cy = Wx * Csins[2] + Wy * Ccoss[0] * Ccoss[2] - Wz * Csins[0]
            Cz = -Wx * Csins[1] + Wy * Csins[0] + Wz * Ccoss[0] * Ccoss[1]

            if Cz > 0.5:
                Sx = ScreenPlane[2] / Cz * Cx + ScreenPlane[0]
                Sy = ScreenPlane[2] / Cz * Cy + ScreenPlane[1]

            if Cz > 5:
                PlaneProjections.append([Sx, Sy])
                Dist += ((Cx)**2 + (Cy) ** 2 + (Cz) ** 2) ** 0.5

        if len(PlaneProjections) > 2 and Dist / len(PlaneProjections) < 1000:
            Dist = (1000 - Dist / len(PlaneProjections)) / 1000
            Color = [Dist * Color for Color in self.Color]
            if sum(Color) != 0:
                pygame.draw.polygon(Screen.Screen, Color, PlaneProjections)