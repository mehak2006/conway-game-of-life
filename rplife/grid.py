import collections

ALIVE = "♥"
DEAD = "‧"


class LifeGrid:
    
    def __init__(self, pattern):
        self.pattern = pattern
        self.ages = {cell: 1 for cell in pattern.alive_cells}

    def evolve(self):
        # Implementation of the evolution logic
        neighbors = {
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1), (1, 0), (1, 1),
        }
        num_neighbors = collections.defaultdict(int)

        for row, col in self.pattern.alive_cells:
            for dr, dc in neighbors:
                neighbor = (row + dr, col + dc)
                num_neighbors[neighbor] += 1

        stay_alive = {cell for cell, num in num_neighbors.items() if num in {2,3}} & self.pattern.alive_cells
        come_alive = {cell for cell, num in num_neighbors.items() if num == 3} - self.pattern.alive_cells

        new_alive = stay_alive | come_alive

        new_ages = {}
        for cell in new_alive:
            if cell in self.ages:
                new_ages[cell] = self.ages[cell] + 1
            else:
                new_ages[cell] = 1

        self.pattern.alive_cells = new_alive
        self.ages = new_ages


    def as_string(self, bbox):
        # Implementation of the string representation
        start_col, start_row, end_col, end_row = bbox
        display = [self.pattern.name.center(2*(end_col - start_col))]
        for row in range(start_row, end_row):
            line = []
            for col in range(start_col, end_col):
                if (row, col) in self.pattern.alive_cells:
                    line.append(ALIVE)
                else:
                    line.append(DEAD)
            display.append(" ".join(line))
        return "\n".join(display)

    def __str__(self):
        # Implementation of the string conversion
        return (
            f"{self.pattern.name } : \n"
            f"Alive Cells: {sorted(self.pattern.alive_cells)}"
        )
