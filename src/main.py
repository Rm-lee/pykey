#!/usr/bin/env python3


import os
import signal
import string
import gi


gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
gi.require_version('AppIndicator3', '0.1') 
from gi.repository import AppIndicator3
gi.require_version('Notify', '0.7')
from gi.repository import Notify


APPINDICATOR_ID = "top_bar_icon"


def main():
	indicator = AppIndicator3.Indicator.new(
			APPINDICATOR_ID,
			os.path.abspath("keyboard.svg"),
			AppIndicator3.IndicatorCategory.SYSTEM_SERVICES)
	indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
	indicator.set_menu(menu_build())
	Notify.init(APPINDICATOR_ID)

	Gtk.main()


def menu_build():

	menu = Gtk.Menu()
	
	

	reload_conf = Gtk.MenuItem("Notification Test")
	reload_conf.connect('activate', systemNotification)
	menu.append(reload_conf)


	device_list = Gtk.Menu()
	list_item = Gtk.MenuItem("Device List")
	test_item = Gtk.MenuItem("device1")
	test_item2 = Gtk.MenuItem("device2")
	test_item3 = Gtk.MenuItem("device3")
	list_item.set_submenu(device_list)

	list_item.get_submenu().append(test_item)
	list_item.get_submenu().append(test_item2)
	list_item.get_submenu().append(test_item3)

	menu.append(list_item)
	

	item_quit = Gtk.MenuItem("Quit")
	item_quit.connect('activate', quit)
	menu.append(item_quit)
	
	menu.show_all()
	
	return menu
	

def systemNotification(source):
	

	
	name = "A System Notification"
	
	Notify.Notification.new("This is ", 
							name,
							None).show()
def quit(source):
	Notify.uninit()
	Gtk.main_quit()


if __name__ == "__main__":
	signal.signal(signal.SIGINT, signal.SIG_DFL)
	main()
