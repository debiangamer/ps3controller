#!/usr/bin/python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import subprocess

class MyWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="PS4 Controller")
		self.box = Gtk.Box(spacing=16)
		self.add(self.box)
		try:
			a = subprocess.check_output(['cat', '/sys/class/power_supply/sony_controller_battery_98:b6:e9:49:7d:06/capacity'])
			power_label = Gtk.Label(label="Power Level Percentage = " + str(int(a)))
		except:
			power_label = Gtk.Label(label="Please connect the  controller")
		self.box.pack_start(power_label, True, True, 0)

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()   