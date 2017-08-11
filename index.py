import gtk

class ReIDWindow(gtk.Window):
	def __init__(self):
		gtk.Window.__init__(self)
		print(dir(gtk.Window.__init__))
		self.button = gtk.Button(label="tmp")
		self.button.connect("clicked",self.on_button_clicked)
		self.add(self.button)
	def on_button_clicked(self, widget):
		print("Hello World")



win = ReIDWindow()
win.connect("delete-event",gtk.main_quit)
win.show_all()
gtk.main()

