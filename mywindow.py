#!/usr/bin/python

import pygtk
pygtk.require('2.0')
import gtk

class Base:

    def destroy(self, widget, data=None):
        gtk.main_quit()
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_size_request(600, 100)
        self.window.set_position(gtk.WIN_POS_CENTER)   
        self.window.show()
        self.window.connect("destroy", self.destroy)
    def main(self):
        gtk.main()
        
if __name__ == "__main__":
    base = Base()
    base.main()
