import sys
try:
    import pygtk
    pygtk.require("2.0")
except:
    pass
try:
    import gtk
    import gtk.glade
except:
    sys.exit(1)

class pyWine:
    """This is the PyWine application"""

    def __init__(self):
        
        #Set the Glade file
        self.gladefile = "pywine.glade"  
        self.wTree = gtk.glade.XML(self.gladefile, "mainWindow") 

        #Create our dictionay and connect it
        dic = {"on_mainWindow_destroy" : gtk.main_quit
                , "on_AddWine" : self.OnAddWine}
        self.wTree.signal_autoconnect(dic)
        
    def OnAddWine(self, widget):
        """Called when the use wants to add a wine"""
        
        print "OnAddWine"

if __name__ == "__main__":
    wine = pyWine()
    gtk.main()
