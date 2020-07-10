
class Car:
    def __init__(self,  color: str, name: str, speed: float = 0,  is_police: bool = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed != 0:
            print(f'car is go - {self.speed}mph')
        else:
            print('Car is stopped')

    def stop(self):
        if self.speed == 0:
            print('car is stopped')
        else:
            print(f'Car is go {self.speed}')

    def turn(self, direction):
        if direction in ('left', 'right'):
            print(f'car turn to {direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def __init__(self, color, name, speed, is_police):
        super().__init__(color, name, speed, is_police)

    def show_speed(self):
        if self.speed > 60:
            print('Alert!')
        else:
            print(f'all right - {self.speed}')


class SportCar(Car):
    def __init__(self, color, name, speed, is_police):
        super().__init__(color, name, speed, is_police)


class WorkCar(Car):
    def __init__(self, color, name, speed, is_police):
        super().__init__(color, name, speed, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'Alert! - {self.speed}')
        else:
            print(f'all right - {self.speed}')


class PoliceCar(Car):
    def __init__(self, color, name, speed, is_police):
        super().__init__(color, name, speed, is_police)
        if self.is_police:
            return print(f'Is Police Car')
        else:
            print(f'Is not Police car')


temp = PoliceCar('red', 'Merthy', 0, True)
# print(f'This Car is Police? - {temp.is_police}')

# temp2 = WorkCar('blue', 'Alex', 0, False)
# print(temp2.show_speed())

print(temp.turn('left'))

print(temp.go())

print()