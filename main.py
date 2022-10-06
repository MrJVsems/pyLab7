class ChartDrawer:
    def __init__(self, coord):
        self.__dot_coord = coord

    def add_point(self, x, y):
        self.__dot_coord.append([x, y])
        print(self.__dot_coord)

    def remove_point(self, x, y):
        if [x, y] in self.__dot_coord:
            indx = self.__dot_coord.index([x, y])
            del self.__dot_coord[indx]
            print(self.__dot_coord)

    def get_coord(self):
        print([i for i in self.__dot_coord])


m = ChartDrawer([[1, 2], [2, 3], [3, 5]])
m.add_point(5, 5)
m.get_coord()
m.remove_point(1, 2)