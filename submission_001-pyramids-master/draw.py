

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    shape = ['pyramid', 'square', 'triangle']
    while True:
        shape = input("Shape?: ").lower()
        if shape in ['pyramid', 'square', 'triangle']:
            return shape
        

# TODO: Step 1 - get height (it must be int!)
def get_height():
    while True:
            height = input("Height?: ")
            if height.isdigit() and int(height) <= 80:
                return int(height) 
                

# TODO: Step 2
def draw_pyramid(height, outline):
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        if outline:
            if i == 1 or i == height:
                stars = '*' * (2 * i - 1)
            else:
                stars = '*' + ' ' * (2 * (i - 1) - 1) + '*'
        else:
            stars = '*' * (2 * i - 1)
        print(spaces + stars)

# TODO: Step 3
def draw_square(height, outline):
    if outline:
        for i in range(height):
            if i == 0 or i == height - 1:
                print('*' * height)  # Fill the entire row with '*' characters
            else:
                print('*' + ' ' * (height - 2) + '*')
    else:
        for _ in range(height):
            print('*' * height)

# TODO: Step 4
def draw_triangle(height, outline):
    for i in range(1, height + 1):
        if outline:
            if i == 1 or i == height:
                print('*' * i)  # Fill the entire row with '*' characters
            else:
                print('*' + ' ' * (i - 2) + '*')
        else:
            print('*' * i)

# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == 'pyramid':
        draw_pyramid(height, outline)
    elif shape == 'square':
        draw_square(height, outline)
    elif shape == 'triangle':
        draw_triangle(height, outline)

# TODO: Step 5 - get input from the user to draw outline or solid
def get_outline():
    outline_input = input("Outline only? (y/N): ").strip().lower()
    return outline_input == 'y'

if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)