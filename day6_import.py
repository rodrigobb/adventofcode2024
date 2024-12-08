
class Guard:
    def __init__(self, position = (0,0), orientation = '^'):
        self.position = position
        self.orientation = orientation
        self.counter = 1

    def can_move(self, map):
        try:
            return (self.orientation == '^' and map[self.position[0]-1][self.position[1]] != '#') or \
                (self.orientation == '>' and map[self.position[0]][self.position[1]+1] != '#') or \
                (self.orientation == 'v' and map[self.position[0]+1][self.position[1]] != '#') or \
                (self.orientation == '<' and map[self.position[0]][self.position[1]-1] != '#')
        except IndexError:
            return True

    def rotate(self) -> bool:
        orientations = ['^', '>', 'v', '<']
        current = orientations.index(self.orientation)
        self.orientation = orientations[(current+1)%4]
        return True

    def move(self, map) -> bool:
        if not self.can_move(map):
            return self.rotate()
        
        if self.orientation == '^':
            self.position = (self.position[0]-1, self.position[1])
        elif self.orientation == '>':
            self.position = (self.position[0], self.position[1]+1)
        elif self.orientation == 'v':
            self.position = (self.position[0]+1, self.position[1])
        elif self.orientation == '<':
            self.position = (self.position[0], self.position[1]-1)
        else:
            return False

        if self.is_in_map(map) and map[self.position[0]][self.position[1]] == '.':
            self.counter += 1
        return True
    
    def is_in_map(self, map) -> bool:
        return self.position[0] >= 0 and self.position[1] >= 0 and \
            self.position[0] < len(map) and self.position[1] < len(map[self.position[0]])

def load_map(filename:str):
    map = []
    guard = None
    line_index = 0
    with open(filename, 'r') as file:
        for line in file:
            map.append([x for x in line if x in ['^', '.', '#']])
            pos = line.find('^')
            if pos > -1:
                guard = Guard((line_index,pos), '^')
            line_index +=1

    return map, guard


