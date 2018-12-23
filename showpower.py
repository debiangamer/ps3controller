#!/usr/bin/python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import subprocess

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="PS3 Controller")
        self.box = Gtk.Box(spacing=16)
        self.add(self.box)
        a = subprocess.check_output(['cat', '/sys/class/power_supply/sony_controller_battery_05:34:9e:68:63:25/capacity'])
        label = Gtk.Label("PS3 Controller Power Level = " + a)
        self.box.pack_start(label, True, True, 0)

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()   