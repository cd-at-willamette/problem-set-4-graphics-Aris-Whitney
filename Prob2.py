########################################
# Name:Aris Whitney
# Collaborators:N/A
# Estimated time spent (hrs):1
########################################

from pgl import GWindow, GRect


WIDTH = 800         
HEIGHT = 600         
BRICK_WIDTH = 40     
BRICK_HEIGHT = 20    
BRICKS_IN_BASE = 15 
def draw_pyramid():
    # Create the graphics window
    gw = GWindow(WIDTH, HEIGHT)

    # Calculate the total height of the pyramid
    total_height = BRICK_HEIGHT * BRICKS_IN_BASE

    # starting y position 
    start_y = (HEIGHT - total_height) // 2

    # Draw the pyramid
    for row in range(BRICKS_IN_BASE):
        # Calculates the number of bricks in this row 
        num_bricks = row + 1  # Increases the number of bricks as we go down

        # starting x position
        start_x = (WIDTH - (BRICKS_IN_BASE * BRICK_WIDTH)) // 2 + (BRICKS_IN_BASE - num_bricks) * (BRICK_WIDTH // 2)
        for brick in range(num_bricks):
            x = start_x + brick * BRICK_WIDTH
            y = start_y + (BRICKS_IN_BASE - 1 - row) * BRICK_HEIGHT  # Position rows from bottom to top
            brick_rect = GRect(x, y, BRICK_WIDTH, BRICK_HEIGHT)
            brick_rect.set_filled(True)
            brick_rect.set_fill_color("brown")
            gw.add(brick_rect)





if __name__ == '__main__':
    draw_pyramid()


















if __name__ == '__main__':
    draw_pyramid()
