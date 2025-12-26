import curses
from time import sleep
__all__ = ["CursesView"]
from rplife.grid import LifeGrid

class CursesView:
    
    def __init__(self, pattern, gen=10, frame_rate=7, bbox = (0, 0, 40, 40)):
        self.pattern = pattern
        self.gen = gen
        self.frame_rate = frame_rate
        self.bbox = bbox

    def show(self):
        curses.wrapper(self._draw)
        
    
    def _draw(self, screen):
        current_grid = LifeGrid(self.pattern)
        curses.curs_set(0)
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_YELLOW)
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_RED)


        start_col, start_row, end_col, end_row = self.bbox

        

        def draw():
            
            screen.clear()
            screen.addstr(0, 0, current_grid.pattern.name)

            for row in range(start_row, end_row):
                for col in range(start_col, end_col):
                    y = row - start_row + 1
                    x = 2 * (col - start_col)

                    if (row, col) in current_grid.pattern.alive_cells:
                        age = current_grid.ages.get((row, col), 1)

                        if age <= 2:
                            color = curses.color_pair(1)
                        elif age <= 5:
                            color = curses.color_pair(2)
                        else:
                            color = curses.color_pair(3)

                        screen.addstr(y, x, "  ", color)
                    else:
                        screen.addstr(y, x, "  ")

        draw()
        screen.refresh()

        # try:
        #     screen.addstr(0, 0, current_grid.as_string(self.bbox))
        # except curses.error:
        #     raise ValueError(
        #         f"Error: terminal too small for pattern '{self.pattern.name}'"
        #     )

        for _ in range(self.gen):
            current_grid.evolve()
            # screen.addstr(0, 0, current_grid.as_string(self.bbox))
            draw()
            screen.refresh()
            sleep(1 / self.frame_rate)