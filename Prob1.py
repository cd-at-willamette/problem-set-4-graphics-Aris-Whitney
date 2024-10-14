############################################################
# Name:Aris Whitney
# Name(s) of anyone worked with:
# Est time spent (hr): 1
############################################################

from pgl import GWindow, GRect, GOval, GLine, GLabel

# Setting up initial window dimensions. 
# You can change these if you want. They are in number of pixels.
WIDTH = 600
HEIGHT = 600

def draw_image():
    """ Creates a window and draws a student's creation"""
    gw = GWindow(WIDTH, HEIGHT)
    w=WIDTH
    h=HEIGHT
    # Creating the window
    #My rectangle
    rect=GRect(0,0,w//2,h)
    rect.set_filled(True) #fills rect
    rect.set_color('lightblue')#chooses fill color
    gw.add(rect)
    #My oval
    o=GOval(w//4, h//4, w//2, h//2)
    o.set_filled(True)
    o.set_fill_color("purple")
    gw.add(o)
    #My line
    gw.add(GLine(0, h//2, w, h//2))
    #my label
    label=GLabel("Artful Art", w//2-40, h//2)
    gw.add(label)
    
    
    # And now it is your turn! Add your code below! Make sure you meet all the requirements!





if __name__ == '__main__':
    draw_image()

