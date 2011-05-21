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

    def about_window(self, widget):
        # Create an About Window and it's details
        about = gtk.AboutDialog()
        about.set_program_name("A PyGTK App")
        about.set_version("1.0b")
        about.set_copyright("(c) Russell Richardson")
        about.set_comments("This is a PyGTK app that doesn't do much")
        about.set_website("https://github.com/russjr08/Test-Projects")
        about.set_logo(gtk.gdk.pixbuf_new_from_file("icon.svg"))
        about.run()
        about.destroy()

    def __init__(self):
        # Setting up the Window object and it's settings
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_size_request(600, 100)
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.set_title("Insert Awesome Title Here!") # Set the title of the window
        self.window.set_tooltip_text("I am the main window") # Set the tooltip of the window
        self.window.set_icon_from_file("icon.svg") # Set the Window icon to the icon specified

        self.button1 = gtk.Button("Exit") # Define a new button
        self.button1.connect("clicked", self.destroy) # Make the button run the destroy function when clicked
        self.button1.set_tooltip_text("I will close the program if you click me!") # Set the tooltip of the button
        
        self.label1 = gtk.Label("Click Me -->") # Create a new label
        self.about_button = gtk.Button("About") # Create an About Button
        self.about_button.connect("clicked", self.about_window) # Connect the button to run the about window function when clicked
        self.about_button.set_tooltip_text("Open the About Window")

        fixed = gtk.Fixed() # Create a new fixed object
        fixed.put(self.button1, 300, 30) # Add button to fixed object
        fixed.put(self.label1, 200, 35) # Add label to fixed object
        fixed.put(self.about_button, 400, 30) # Add About button to fixed object

        
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
    raise SystemExit
    # If not running by itself, display a message, and close the program