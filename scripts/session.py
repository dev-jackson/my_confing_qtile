

import gi
# version Gtk
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

import os
from libqtile.command import lazy

class SessionOptions:
    
    # Cancel/Exit
    def delete_event(self, widget, event, data=None):
        Gtk.main_quit()
        return False

    # Lagout
    def logout(self, widget):
        lazy.shutdown()

    # Reboot
    def reboot(self, widget):
        os.system("sudo shutdown -r now")
        lazy.shutdown()

    # Shutdown
    def shutdown(self, widget):
        os.system("shutdown -h now")
        lazy.shutdown()

    # Hibernate
    def hibernate(self, widget):
        os.system("sudo hibernate")

    def __init__(self):
        #Create windows
        self.window = Gtk.Window()
        self.window.set_title("Exit? Choose an option:")
        self.window.set_realized(False)
        self.window.set_position(1)
        self.window.connect("delete_event", self.delete_event)
        self.window.set_border_width(20)

        # Create group 
        acc_group = Gtk.AccelGroup()
        self.window.add_accel_group(acc_group)

        # Create box pack widgets
        self.box = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=6
        )
        self.window.add(self.box)

        # Create buttons
        # Button Cancel
        self.btn1 = Gtk.Button.new_with_label("Cancel")
        self.btn1.set_border_width(10)
        self.btn1.connect("clicked", self.delete_event, "closed")
        self.box.pack_start(self.btn1, True, True, 0)
        self.btn1.add_accelerator(
            "clicked", 
            acc_group,
            Gdk.keyval_from_name('Escape'),
            0,
            0
        )
        self.btn1.add_accelerator(
            "clicked",
            acc_group,
            Gdk.keyval_from_name('c'),
            0,
            0
        )
        self.btn1.show()

        # Button log out 
        self.btn2 = Gtk.Button.new_with_label("Lagout")
        self.btn2.set_border_width(10)
        self.btn2.connect("clicked", self.logout)
        self.box.pack_start(self.btn2, True, True, 0)
        self.btn2.add_accelerator(
            "clicked", 
            acc_group,
            Gdk.keyval_from_name('l'),
            0,
            0
        )
        self.btn2.show()

        # Button reboot
        self.btn3 = Gtk.Button.new_with_label("Reboot")
        self.btn3.set_border_width(10)
        self.btn3.connect("clicked", self.reboot)
        self.box.pack_start(self.btn3, True, True, 0)
        self.btn3.add_accelerator(
            "clicked", 
            acc_group,
            Gdk.keyval_from_name('r'),
            0,
            0
        )
        self.btn3.show()

        # Button shutdown
        self.btn4 = Gtk.Button.new_with_label("Shutdown")
        self.btn4.set_border_width(10)
        self.btn4.connect("clicked", self.shutdown)
        self.box.pack_start(self.btn4, True, True, 0)
        self.btn4.add_accelerator(
            "clicked", 
            acc_group,
            Gdk.keyval_from_name('s'),
            0,
            0
        )       
        self.btn4.show()

        # Button hibernate
        self.btn5 = Gtk.Button.new_with_label("Hibernate")
        self.btn5.set_border_width(10)
        self.btn5.connect("clicked", self.hibernate)
        self.box.pack_start(self.btn5, True, True, 0)
        self.btn5.add_accelerator(
            "clicked", 
            acc_group,
            Gdk.keyval_from_name('h'),
            0,
            0
        )       
        self.btn5.show()

        # Show components
        self.box.show()
        self.window.show()

def main():
    Gtk.main()

if __name__ == "__main__":
    run_it = SessionOptions()
    main()
