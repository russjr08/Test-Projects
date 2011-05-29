#!/usr/bin/python
import pygtk
pygtk.require('2.0')
import gtk
import os

class Base:
    def destroy(self, widget, data=None):
        gtk.main_quit() # Close the application
    
    def download(self, widget):
    	text = self.textbox.get_text() # Gets the text from the text box
    	print text # print the text of the textbox in the terminal for debugging purposes, this can be disabled if not wanted.
    	
    	
    	'''Defines and opens a file chooser dialog 
    	to get ready to save file'''
    	chooser = gtk.FileChooserDialog(title="Where to save?", action=gtk.FILE_CHOOSER_ACTION_SAVE, buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL, gtk.STOCK_SAVE,gtk.RESPONSE_OK))
    	chooser.set_default_response(gtk.RESPONSE_OK)
    	response = chooser.run()
    	print chooser.get_filename() # Once again, prints the filepath from the file chooser for debugging purposes, this can be disabled
    	
    	
    	
    	cmd = "wget " + str(text) + " -O " + str(chooser.get_filename()) # The cmd to download the file
    	#cmd2 = "wget " + str(text) R"2>&1 | sed -u 's/.*\ \([0-9]\+%\)\ \+\([0-9.]\+\ [KMB\/s]\+\)$/\1\n# Downloading \2/' | zenity --progress --auto-kill -O " + str(chooser.get_filename()) << I want this to work :(
    	
    	'''Runs the cmd from above and downloads the file to the specified directory in
    	the file chooser'''
    	if response == gtk.RESPONSE_OK:
    		os.popen(cmd)

	chooser.destroy() # Closes the file chooser object
        

    def __init__(self):
    	'''Defines the window and the other properties such as textbox and button
    	also sets up the positioning and the size of the window'''
    	
    	self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    	self.window.set_size_request(600, 100)
    	
    	self.textbox = gtk.Entry(max=0)
    	self.button = gtk.Button("Download")
    	self.button.connect("clicked", self.download) # connect the clicked function of the button to the download function
    	
    	hbox = gtk.HBox()
    	hbox.pack_start(self.textbox)
    	
    	vbox = gtk.VBox()
    	vbox.pack_start(hbox)
    	vbox.pack_start(self.button)
    	
    	#fixed = gtk.Fixed() << If I was going to use a fixed object, this would be how I set it up
    	
    	#fixed.put(self.textbox, 20, 30)
    	#fixed.put(self.button, 30, 60)
    	
    	#self.window.add(fixed)
    	self.window.add(vbox)
    	self.window.show_all()
    	self.window.connect("destroy", self.destroy)
    	self.window.set_icon_from_file("icon.svg")
    	
    def main(self):
    	gtk.main() # Run the main GTK loop
    	
if __name__ == "__main__":
	base = Base()
	base.main()
	print "I need to be run by myself please, I will now exit the app"
	
	em = gtk.MessageDialog(None, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_ERROR, gtk.BUTTONS_CLOSE, "I need to be run myself please, I will now quit this application")
	
	em.run()
	em.destroy
	raise SystemExit()
	
	''' The above defines the main base class and runs it if the program is run
	by itself, and exits the app / throws an error if not'''
