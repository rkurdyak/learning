from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        
        self.__canvas = Canvas(self.__root, bg = "white", width = width, height = height)
        self.__canvas.pack(fill = BOTH, expand = 1)
        
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running == True:
            self.redraw()
        print("Window is closed")
    def close(self):
        self.running = False
    
    def draw_line(self, Line, fill_color="black"):
        return Line.draw(self.__canvas, fill_color)
        


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        
    def draw(self, canvas, fill_color):
        canvas.create_line(self.point1.x, self.point1.y,
                           self.point2.x, self.point2.y,
                           fill=fill_color, width=2)

class Cell():
    def __init__(self, win):
        self.__win = win
        self.has_left_wall, self.has_right_wall, self.has_top_wall, self.has_bottom_wall = True, True, True, True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
    
    def draw(self, x1, x2, y1, y2):
        # set cell coordinates to the given values
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        
        if self.has_left_wall:
            # draw a line for the left wall
            left_wall_point1 = Point(self.__x1, self.__y1)
            left_wall_point2 = Point(self.__x1, self.__y2)
            left_wall_line = Line(left_wall_point1, left_wall_point2)
            self.__win.draw_line(left_wall_line)
        if self.has_right_wall:
            # draw a line for the right wall
            right_wall_point1 = Point(self.__x2, self.__y1)
            right_wall_point2 = Point(self.__x2, self.__y2)
            right_wall_line = Line(right_wall_point1, right_wall_point2)
            self.__win.draw_line(right_wall_line)
        
        if self.has_top_wall:
            # draw a line for the top wall
            top_wall_point1 = Point(self.__x1, self.__y2)
            top_wall_point2 = Point(self.__x2, self.__y2)
            top_wall_line = Line(top_wall_point1, top_wall_point2)
            self.__win.draw_line(top_wall_line)
            
        if self.has_bottom_wall:
            # draw a line for the top wall
            bottom_wall_point1 = Point(self.__x1, self.__y1)
            bottom_wall_point2 = Point(self.__x2, self.__y1)
            bottom_wall_line = Line(bottom_wall_point1, bottom_wall_point2)
            self.__win.draw_line(bottom_wall_line)
        