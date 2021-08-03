
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def drive(self):
        print(f"I'm driving a {self.color} {self.model} car")

    def stop(self):
        print('Stop')


toyota = Car('Toyota', 'red')
hyundia = Car('Hynudia', 'purple')

toyota.drive()
hyundia.drive()
