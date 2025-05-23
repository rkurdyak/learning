from graphing import Window, Point, Line, Cell

def main():
    win = Window(800, 600)
    
    cell1 = Cell(win)
    cell1.draw(0, 100, 0, 100)
    
    
    
    cell2 = Cell(win)
    cell2.draw(500, 300, 500, 200)
    
    win.wait_for_close()

main()