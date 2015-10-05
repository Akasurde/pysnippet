from dogtail.utils import run
from dogtail import tree 

run("gedit")

# Get a handle to gedit's application object.
gedit = tree.root.application('gedit')

# Get a handle to gedit's File menu.
filemenu = gedit.menu('File')

# Get a handle to gedit's Save button.
savebutton = gedit.button('Save')

# Click the button
savebutton.click()
