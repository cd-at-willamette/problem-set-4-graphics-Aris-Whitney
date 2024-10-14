########################################
# Name:Aris Whitney
# Collaborators:
# Estimate time spent (hrs):3
########################################

from pgl import GWindow, GRect, GLabel
import random

# Constants
GW_WIDTH = 500                       # Width of window
GW_HEIGHT = 500                      # Height of window
SQUARE_SIZE = 50                     # Width and height of square
SCORE_DX = 10                        # Distance from left of window to origin
SCORE_DY = 10                        # Distance up from bottom of window to baseline
SCORE_FONT = "bold 20pt 'serif'"     # Font for score
SOME_VAL = random.randint(1, 499)
print(SOME_VAL)                      # To calculate random position

def get_r():
    return random.randint(0, SOME_VAL)

def clicky_box():
    # Create a graphics window
    gw = GWindow(GW_WIDTH, GW_HEIGHT)

    # Create a filled colored square
    def my_square(x,y,w,h,color):
        square = GRect(225,225,SQUARE_SIZE, SQUARE_SIZE)
        square.set_filled(True)
        square.set_color("lightblue")
        gw.add(square)
        gw.box=square
        return square
    box=my_square(225,225,50,50,'lightblue')
    # Center the square in the window
    my_square.x = (GW_WIDTH - SQUARE_SIZE) // 2
    my_square.y = (GW_HEIGHT - SQUARE_SIZE) // 2
    

    #initial score
    score = [0]  # Use a list to hold the score
    score_label = GLabel(f"Score: {score[0]}")
    score_label.font = SCORE_FONT
    score_label.x = SCORE_DX
    score_label.y = GW_HEIGHT - SCORE_DY
    gw.add(score_label)

    def on_mouse_down(e):
        # Get mouse coordinates
        mouse_x = e.get_x()
        mouse_y = e.get_y()
        my_square(mouse_x,mouse_y,50,50,'lightblue')


        #mouse coordinates and square position
        print(f"Mouse clicked at: ({mouse_x}, {mouse_y})")
        print(f"Square position: ({my_square.x}, {my_square.y})")

        # Check if the click is inside the square
        if (my_square.x <= mouse_x <= my_square.x + SQUARE_SIZE) and (my_square.y <= mouse_y <= my_square.y + SQUARE_SIZE):
            print("Square clicked!")  
            score[0] += 1  # adds 1 to previous score
            
            # Move the square to a new random position within bounds
            new_x = get_r()
            new_y = get_r()
            
            # Ensure the square is within the bounds
            new_x = min(new_x, GW_WIDTH - SQUARE_SIZE)
            new_y = min(new_y, GW_HEIGHT - SQUARE_SIZE)
            
            my_square.x = new_x
            my_square.y = new_y
        else:
            print("Clicked outside the square.")  
            score[0] = 0  # Reset score if clicked outside
        
        # Update score display
        score_label.text = f"Score: {score[0]}"

    # Add the mouse click event listener
    gw.add_event_listener("click", on_mouse_down)




if __name__ == '__main__':
    clicky_box()
