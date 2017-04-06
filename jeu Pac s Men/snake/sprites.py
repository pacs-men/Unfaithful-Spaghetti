import pygame

#helper class for making static functions
class Callable:
    def __init__(self, anycallable):
        self.__call__ = anycallable

class Apple(pygame.sprite.Sprite):
    #private constants
    _DEFAULT_COLOR = [255, 0, 0] #red
    _DEFAULT_SIZE = [10, 10]
    def __init__(self, color, size, position):
        #parameter validation
        if color == None:
            color = Apple._DEFAULT_COLOR
        if size == None:
            size = Apple._DEFAULT_SIZE
        if position == None:
            raise Exception('Invalid position.')

        #initialization
        self.color = color
        self.size = size
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = position

class Snake(pygame.sprite.Sprite):
    #private constants
    _DEFAULT_COLOR = [0, 255, 0] #green
    _DEFAULT_SIZE = [10, 10] #10px X 10px
    _DEFAULT_POSITION = [30, 30] #space given to tail of length 2

    #-----PRIVATE CLASSES-------------------------------------------------------
    class _SnakeTail(pygame.sprite.Sprite):
        def __init__(self):
            #initialization
            self.tiles = []

        def add_tile(self, color, size, position):
            #creates a new tile
            tile = pygame.Surface(size)
            tile.fill(color)
            rect = tile.get_rect()
            rect.topleft = position

            self.tiles.append({'image':tile, 'rect':rect})

    class _SnakeHead(pygame.sprite.Sprite):
        def __init__(self, color, size, position):
            #initialization
            self.image = pygame.Surface(size)
            self.image.fill(color)
            self.rect = self.image.get_rect()
            self.rect.topleft = position
    #---------------------------------------------------------------------------

    class SnakeMove():
        UP = '1Y'
        DOWN = '-1Y'
        RIGHT = '1X'
        LEFT = '-1X'

        #checks a direction's validity
        def SnakeMove_is_member(direction):
            if direction == Snake.SnakeMove.UP:
                return True
            elif direction == Snake.SnakeMove.DOWN:
                return True
            elif direction == Snake.SnakeMove.RIGHT:
                return True
            elif direction == Snake.SnakeMove.LEFT:
                return True

            return False

        #makes the function 'is_member' a static function
        SnakeMove_is_member = Callable(SnakeMove_is_member)

    def __init__(self, color, size, position):
        #parameter validation
        if color == None:
            color = Snake._DEFAULT_COLOR
        if size == None:
            size = Snake._DEFAULT_SIZE
        if size[0] != size[1]:
            raise Exception('Invalid tile size. Width and height must be equal.')
        if position == None:
            position = Snake._DEFAULT_POSITION

        self.color = color
        self.size = size
        self.head = Snake._SnakeHead(color, size, position)
        self.tail = Snake._SnakeTail()
        tailposition = [(position[0] - size[0]), position[1]]
        self.tail.add_tile(color, size, tailposition)
        tailposition = [(position[0] - 2*size[0]), position[1]]
        self.tail.add_tile(color, size, tailposition)

    def move(self, direction, frame_width, frame_height):
        #parameter validation
        if Snake.SnakeMove.SnakeMove_is_member(direction) != True:
            raise Exception('Invalid movement direction.')

        #initializes new position
        stepsize = self.head.image.get_rect()[2] #gets the size of the head tile
        newheadposition = [self.head.rect.topleft[0], self.head.rect.topleft[1]]
        if direction == Snake.SnakeMove.UP:
            newheadposition[1] = (newheadposition[1]-stepsize)%frame_height
        if direction  == Snake.SnakeMove.DOWN:
            newheadposition[1] = (newheadposition[1]+stepsize)%frame_height
        if direction == Snake.SnakeMove.RIGHT:
            newheadposition[0] = (newheadposition[0]+stepsize)%frame_width
        if direction == Snake.SnakeMove.LEFT:
            newheadposition[0] = (newheadposition[0]-stepsize)%frame_width

        if self.occupies_position(newheadposition):
            return False

        #moves the head to its new position
        newtileposition = self.head.rect.topleft
        self.head.rect.topleft = newheadposition

        #moves the tail tiles to its respective new positions
        for count in range(len(self.tail.tiles)):
            prevtileposition = self.tail.tiles[count]['rect'].topleft
            self.tail.tiles[count]['rect'].topleft = newtileposition
            newtileposition = prevtileposition

        return True

    #checks if this snake's body occupies a given position
    def occupies_position(self, position):
        #parameter validation
        if position[0] == None or position[1] == None:
            return True

        if self.head.rect.topleft[0] == position[0] \
            and self.head.rect.topleft[1] == position[1]:
                return True

        for count in range(len(self.tail.tiles)):
            if self.tail.tiles[count]['rect'].topleft[0] == position[0] \
            and self.tail.tiles[count]['rect'].topleft[1] == position[1]:
                return True

        return False

    def lengthen_tail(self, number, current_direction):
        #parameter validation
        if number is None:
            number = 1
        if Snake.SnakeMove.SnakeMove_is_member(current_direction) != True:
            raise Exception('Invalid movement direction.')

        size = self.size[0]
        color = self.color

        for count in range(number):
            lastindex = len(self.tail.tiles) - 1
            X = self.tail.tiles[lastindex]['rect'].topleft[0]
            Y = self.tail.tiles[lastindex]['rect'].topleft[1]

            #determines position of new tile
            if current_direction == Snake.SnakeMove.UP:
                Y = Y - size + (count*size)
            elif current_direction == Snake.SnakeMove.DOWN:
                Y = Y + size + (count*size)
            elif current_direction == Snake.SnakeMove.RIGHT:
                X = X - size + (count*size)
            elif current_direction == Snake.SnakeMove.LEFT:
                X = X + size + (count*size)

            self.tail.add_tile(color, self.size, [X, Y])