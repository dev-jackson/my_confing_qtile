import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gio
from gi.repository import Gtk
import os
d = Gtk.MessageDialog(
                              modal=True,
                              buttons=Gtk.ButtonsType.OK_CANCEL)
d.props.text = 'Desea apagar el equipo?'
response = d.run()
d.destroy()

# We only terminate when the user presses the OK button
if response == Gtk.ResponseType.OK:
    os.system("sudo -S <<< 'dev537' shutdown -h 0")  
