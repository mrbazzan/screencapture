
class Car:
    def __init__(self, model):
        self.model = model

    def drive(self):
        print("I'm driving")

    def stop(self):
        print('Stop')


toyota = Car('Toyota')
toyota.drive()
