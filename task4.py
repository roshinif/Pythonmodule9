import random

class Car:
    def __init__(self, registration_number, max_speed, current_speed=0, travelled_distance=0):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def __str__(self):
        return f"| {self.registration_number:<8} | {self.max_speed:>10} km/h | {self.current_speed:>13} km/h | {self.travelled_distance:>16} km |"

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, time):
        self.travelled_distance += self.current_speed * time  # (d=v*t)

def create_cars(num_cars):
    cars = []
    for i in range(1, num_cars + 1):
        registration_number = f"ABC-{i}"
        max_speed = random.randint(100, 200)
        car = Car(registration_number, max_speed)
        cars.append(car)
    return cars

cars = create_cars(10)

race_complete = False
time_elapsed = 0

while not race_complete:
    time_elapsed += 1
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.drive(1)

    for car in cars:
        if car.travelled_distance >= 10000:
            race_complete = True
            break

print("/  Registration  /  Maximum speed  /  Current speed  /  Travelled distance  /")
print("  " * 75)
for car in cars:
    print(car)
