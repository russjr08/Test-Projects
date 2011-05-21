#!/usr/bin/python

# import all required things
import pygtk
# We need pygtk / gtk 2.0 and up
pygtk.require('2.0')
import gtk


# Our main class
class Base:

    def destroy(self, widget, data=None):
        # Set up a way to close the actual program process
        gtk.main_quit()
        print "You have closed me"
    def __init__(self):
        # Setting up the Window object and it's settings
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_size_request(600, 100)
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.button1 = gtk.Button("Exit") # Define a new button
        self.button1.connect("clicked", self.destroy) # Make the button run the destroy function when clicked
        
        fixed = gtk.Fixed()
        fixed.put(self.button1, 300, 30)
        
        self.window.add(fixed) # Add the fixed object (containing the button) to the window
        self.window.show_all() # Show the window and all widgets
        self.window.connect("destroy", self.destroy) # Connect the close button to our newly created destroy function above to allow the program to be able to quit it's own process
    def main(self):
        gtk.main() # Main GTK Process
        
if __name__ == "__main__":
    base = Base() # Set up the Base class to the base object
    base.main() # Run the main function in the Base class
else:
    print "I need to be run by myself please, I will now quit this application"
    quit()
    # If not running by itself, display a message, and close the program