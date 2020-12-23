from tkinter import *
from figures import get_random_figure
from figure import figure

grid = [0] * 10
for i in range(10):
    grid[i] = [0] * 20  # TODO

root = Tk()
size = 1
WINDOW_HEIGHT = round(root.winfo_screenheight() / 1.8)
WINDOW_WIDTH = round(WINDOW_HEIGHT / 1.5)
rectangle_border_x = WINDOW_WIDTH // (4 * size)
ITEM_SIZE = (WINDOW_WIDTH - 2 * rectangle_border_x) // 10
rectangle_border_y = (WINDOW_HEIGHT - 20 * ITEM_SIZE) // 2
button_start: Button
canvas: Canvas
score = 0
level = 0
level_text: Text
delay = 500


def initialize_window():
    root.title("Tetris")
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    root.resizable(False, False)
    root.mainloop()


def show_menu():
    global button_start
    button_start = Button(text="Begin",
                          background="#555",
                          foreground="#ccc",
                          padx="50",
                          pady="8",
                          font="16",
                          command=initialize_game)
    button_start.place(rely=.7, relx=.5, anchor="c")


def initialize_game():
    global rectangle_border_y, rectangle_border_x
    destroy_menu()
    global canvas
    canvas = Canvas(width=WINDOW_WIDTH, height=WINDOW_HEIGHT,
                    bg='black')
    canvas.pack()

    draw_grid()
    change_level()
    create_figure()


def draw_grid():
    field = canvas.create_rectangle(rectangle_border_x, rectangle_border_y, WINDOW_WIDTH - rectangle_border_x,
                                    WINDOW_HEIGHT - rectangle_border_y, fill='gray')
    for i in range(11):
        canvas.create_line(rectangle_border_x + ITEM_SIZE * i, rectangle_border_y, rectangle_border_x + ITEM_SIZE * i,
                           WINDOW_HEIGHT - rectangle_border_y)
    for i in range(21):
        canvas.create_line(rectangle_border_x, rectangle_border_y + ITEM_SIZE * i, WINDOW_WIDTH - rectangle_border_x,
                           rectangle_border_y + ITEM_SIZE * i)


def create_figure():
    current_figure = get_random_figure()
    current_figure.__cells = []
    for row in range(len(current_figure.__cell_coords[0])):
        for column in range(len(current_figure.__cell_coords[0][row])):
            if current_figure.__cell_coords[0][row][column] == 1:
                current_figure.__cells.append(fill_cell(column, row, current_figure.__color))
    canvas.bind('<Left>', lambda event: move_figure(current_figure, -1, 0))
    canvas.bind('<Right>', lambda event: move_figure(current_figure, 1, 0))

    canvas.focus_set()
    falling_figure(current_figure)


def move_figure(current_figure: figure, x, y):
    if not current_figure.is_falled:
        for cell in current_figure.__cells:
            coordinates = canvas.coords(cell)
            if coordinates[0] <= rectangle_border_x and x < 0:
                return
            if coordinates[2] >= (WINDOW_WIDTH - rectangle_border_x) and x > 0:
                return
            if coordinates[3] >= (WINDOW_HEIGHT - rectangle_border_y) and y != 0:
                return False
        for cell in current_figure.__cells:
            canvas.move(cell, x * ITEM_SIZE, y * ITEM_SIZE)
        return True


def falling_figure(current_figure: figure):
    if move_figure(current_figure, 0, 1):
        root.after(delay, lambda: falling_figure(current_figure))
    else:
        current_figure.is_falled = True
        create_figure()


def destroy_menu():
    button_start.destroy()


def change_level():
    global level_text
    global level
    level += 1
    level_text = Label(text='Level ' + str(level), fg='white', bg='black', width=12, height=1)
    level_text.place(relx=0.19, rely=0.13)


def fill_cell(x, y: int, fill='red'):
    vec1 = get_coordinate_cell(x + 5, y)
    vec2 = get_coordinate_cell(x + 6, y + 1)
    return canvas.create_rectangle(vec1[0], vec1[1], vec2[0], vec2[1], fill=fill)


def get_coordinate_cell(x, y: int):
    vec = (rectangle_border_x + ITEM_SIZE * (x - 1), rectangle_border_y + ITEM_SIZE * (y - 1))
    return vec
