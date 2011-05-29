#!/usr/bin/python
import pygtk
pygtk.require('2.0')
import gtk
import os

class Base:
    def destroy(self, widget, data=None):
        gtk.main_quit() # Close the application
    
    def download(self, widget):
    	text = self.textbox.get_text()
    	print text
    	
    	chooser = gtk.FileChooserDialog(title="Where to save?", action=gtk.FILE_CHOOSER_ACTION_SAVE, buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL, gtk.STOCK_SAVE,gtk.RESPONSE_OK))
    	chooser.set_default_response(gtk.RESPONSE_OK)
    	response = chooser.run()
    	print chooser.get_filename()
    	
    	
    	
    	cmd = "wget " + str(text) + " -O " + str(chooser.get_filename())
    	
    	if response == gtk.RESPONSE_OK:
    		os.popen(cmd)

	chooser.destroy()
        

    def __init__(self):
    	self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    	self.window.set_size_request(600, 100)
    	
    	self.textbox = gtk.Entry(max=0)
    	self.button = gtk.Button("Download")
    	self.button.connect("clicked", self.download)
    	
    	hbox = gtk.HBox()
    	hbox.pack_start(self.textbox)
    	#hbox.pack_start(self.button)
    	
    	vbox = gtk.VBox()
    	vbox.pack_start(hbox)
    	vbox.pack_start(self.button)
    	
    	#fixed = gtk.Fixed()
    	
    	#fixed.put(self.textbox, 20, 30)
    	#fixed.put(self.button, 30, 60)
    	
    	#self.window.add(fixed)
    	self.window.add(vbox)
    	self.window.show_all()
    	self.window.connect("destroy", self.destroy)
    	
    def main(self):
    	gtk.main()
    	
if __name__ == "__main__":
	base = Base()
	base.main()
