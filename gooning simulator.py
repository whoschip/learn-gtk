import gi
gi.require_version('Gtk', '4.0')

from gi.repository import Gtk
class page(Gtk.ApplicationWindow):
    def __init__(self, **kargs):
        super().__init__(**kargs, default_width=400, title="gooning simulator")
        self.goon = 0
        # header bar
        header = Gtk.HeaderBar()
        self.set_titlebar(header)
        self.TotalGoonTimes = Gtk.Label(label=f"Total goon times: {self.goon}")
        header.pack_start(self.TotalGoonTimes)
        # grid
        grid = Gtk.Grid()

        # main funtion
        self.button = Gtk.Button(label='GOON')
        grid.attach(self.button, 0, 0, 5, 10)
        self.button.connect('clicked', self.on_button_clicked)

        self.set_child(grid)
    
    def on_button_clicked(self, _widget):
        self.goon += 1
        print('goon-ed')
        print(f'Total goon times: {self.goon}')
        # update the goon time
        self.TotalGoonTimes.set_label(f"Total goon times: {self.goon}")

def on_activate(app):
    win = page(application=app)
    win.present()


app = Gtk.Application(application_id='com.example.App')
app.connect('activate', on_activate)
app.run(None)

# joke pls dont kill me