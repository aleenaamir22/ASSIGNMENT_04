import tkinter as tk

CELL_SIZE = 40
GRID_ROWS = 10
GRID_COLS = 10
ERASER_SIZE = 50

class EraserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Canvas Eraser")

        self.canvas = tk.Canvas(root, width=GRID_COLS*CELL_SIZE, height=GRID_ROWS*CELL_SIZE, bg="white")
        self.canvas.pack()

        # Create color grid cells and store their references
        self.cells = []
        for row in range(GRID_ROWS):
            row_cells = []
            for col in range(GRID_COLS):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="red", outline="black")
                row_cells.append(rect)
            self.cells.append(row_cells)

        # Create eraser
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, outline="red", width=2)
        self.canvas.bind("<B1-Motion>", self.move_eraser)

    def move_eraser(self, event):
        # Move eraser to follow the mouse
        x1 = event.x - ERASER_SIZE // 2
        y1 = event.y - ERASER_SIZE // 2
        x2 = x1 + ERASER_SIZE
        y2 = y1 + ERASER_SIZE
        self.canvas.coords(self.eraser, x1, y1, x2, y2)

        # Check for collisions and erase
        for row in self.cells:
            for rect in row:
                coords = self.canvas.coords(rect)
                if self.rects_overlap((x1, y1, x2, y2), coords):
                    self.canvas.itemconfig(rect, fill="white")

    def rects_overlap(self, r1, r2):
        # Check if two rectangles overlap
        return not (r1[2] <= r2[0] or r1[0] >= r2[2] or r1[3] <= r2[1] or r1[1] >= r2[3])

# Run the app
root = tk.Tk()
app = EraserApp(root)
root.mainloop()
