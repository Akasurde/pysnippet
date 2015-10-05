import sys

try:
    import pygtk
    pygtk.require('2.0')
except:
    pass

try:
    import gtk
    import gtk.glade
except:
    sys.exit(1)


class HelloGTK:
    def __init__(self):
        self.gladefile = 'pygtkhw.glade'
        self.wTree = gtk.glade.XML(self.gladefile)
        dic = {"on_button1_clicked": self.btnHelloWorld_Clicked, 
                "on_MainWindow_destroy": gtk.main_quit}
        self.wTree.signal_autoconnect(dic)
        self.window = self.wTree.get_widget("main")

    def btnHelloWorld_Clicked(self, widget):
        print "Hello World"

def main():
    hwg = HelloGTK()
    gtk.main()

if __name__ == "__main__":
    main()
