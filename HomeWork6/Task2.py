# Home Work Lesson 6 Task2


class Road:

    def __init__(self, length, width, thickness, asphalt_mass):

        self._length = float(length)
        self._width = float(width)
        self._thickness = int(thickness)
        self._asphalt_mass = int(asphalt_mass)

    def asphalt_sum(self):
        return self._length * self._width * self._asphalt_mass * self._thickness


print(Road(1000, 125, 5, 25).asphalt_sum())
