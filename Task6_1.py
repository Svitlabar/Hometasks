import time

from termcolor import colored


class TrafficLight:

    def __init__(self, c):
        self.__color = c

    def running(self):
        for i in range(5):
            print(colored(f"Red", "red").format(self))
            time.sleep(7)
            print(colored(f"Yellow", "yellow").format(self))
            time.sleep(2)
            print(colored(f"Green", "green").format(self))
            time.sleep(8)
            print(colored(f"Yellow", "yellow").format(self))
            time.sleep(2)


device_1 = TrafficLight("Red-Yellow-Green")
print("Device N 1:")
device_1.running()
