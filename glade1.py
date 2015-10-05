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


