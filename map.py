class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.field = []
        self.create()

    def create(self):
        for i in range(self.height):
            self.field.append([])
            for j in range(self.width):
                self.field[i].append(0)

    def drow_map(self):
        for i in range(self.height):
            print(self.field[i])
