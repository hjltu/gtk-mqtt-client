#!/usr/bin/env python2.7

"""
	Project name: hjhome
	Copyright (C) 2017  hjltu@ya.ru
	https://launchpad.net/hjhome

	hjhome free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	hjhome is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see <http://www.gnu.org/licenses/>.

	gtk-mqtt.py 23.11.2017 by hjltu
	require python 2.7, mosquitto
"""

import gtk,os,sys

class My:

	mqtt='mosquitto_pub'	# mqtt broker
	mqtt_host='localhost'	# mqtt server
	mqtt_topic='/test/lamp'	# mqtt topic

	pub=mqtt+' -h '+mqtt_host+' -t '+mqtt_topic

	def off(self,widget,bt,i):
		widget.hide()
		bt.show()
		os.system(self.pub+str(i)+' -m 1')

	def on(self,widget,bt,i):
		widget.hide()
		bt.show()
		os.system(self.pub+str(i)+' -m 0')

	def my_op(self,widget,op):
		if op is 1:
			if self.count<9:
				self.count+=1
		if op is 0:
			if self.count>1:
				self.count-=1
		print 'inc',self.count
		file=open('any/count.txt','w')
		print >> file, self.count
		file.close()
		os.execl(sys.executable, 'python', __file__, *sys.argv[1:])

	def __init__(self):

		try:
			self.count=int(file('any/count.txt').read())
		except:
			self.count=1
		print 'count =',self.count

		win=gtk.Window(gtk.WINDOW_TOPLEVEL)
		win.set_position(gtk.WIN_POS_CENTER)
		win.set_border_width(10)
		win.set_title('gtk mqtt client')
		win.connect("destroy",gtk.main_quit)

		vbox=gtk.VBox()
		hbox=gtk.HBox()

		self.bt_on1=gtk.Button()
		self.bt_off1=gtk.Button()
		self.bt_on2=gtk.Button()
		self.bt_off2=gtk.Button()
		self.bt_on3=gtk.Button()
		self.bt_off3=gtk.Button()
		self.bt_on4=gtk.Button()
		self.bt_off4=gtk.Button()
		self.bt_on5=gtk.Button()
		self.bt_off5=gtk.Button()
		self.bt_on6=gtk.Button()
		self.bt_off6=gtk.Button()
		self.bt_on7=gtk.Button()
		self.bt_off7=gtk.Button()
		self.bt_on8=gtk.Button()
		self.bt_off8=gtk.Button()
		self.bt_on9=gtk.Button()
		self.bt_off9=gtk.Button()

		button=((1,'lamp1',self.bt_on1,self.bt_off1),
			(2,'lamp2',self.bt_on2,self.bt_off2),
			(3,'lamp3',self.bt_on3,self.bt_off3),
			(4,'lamp4',self.bt_on4,self.bt_off4),
			(5,'lamp5',self.bt_on5,self.bt_off5),
			(6,'lamp6',self.bt_on6,self.bt_off6),
			(7,'lamp7',self.bt_on7,self.bt_off7),
			(8,'lamp8',self.bt_on8,self.bt_off8),
			(9,'lamp9',self.bt_on9,self.bt_off9))

		for i in button:
			if i[0]<= self.count:
				bbox=gtk.VBox()
				bbox.set_border_width(5)
				txt=gtk.Label(i[1])

				i[2].set_size_request(80,50)
				img_on=gtk.Image()
				img_on.set_from_file('any/lamp-on.png')
				i[2].add(img_on)
				i[2].connect('clicked',self.off,i[3],i[0])

				i[3].set_size_request(80,50)
				img_off=gtk.Image()
				img_off.set_from_file('any/lamp-off.png')
				i[3].add(img_off)
				i[3].connect('clicked',self.on,i[2],i[0])

				bbox.pack_start(txt)
				bbox.pack_start(i[2])
				bbox.pack_start(i[3])
				hbox.pack_start(bbox)

		bbox=gtk.VBox()
		bbox.set_border_width(5)
		txt=gtk.Label('new')

		self.bt_add=gtk.Button()
		self.bt_add.set_size_request(80,15)
		img_add=gtk.Image()
		img_add.set_from_file('any/plus.png')
		self.bt_add.add(img_add)
		self.bt_add.connect("clicked", self.my_op,1)

		self.bt_del=gtk.Button()
		self.bt_del.set_size_request(80,15)
		img_del=gtk.Image()
		img_del.set_from_file('any/minus.png')
		self.bt_del.add(img_del)
		self.bt_del.connect("clicked", self.my_op,0)

		bbox.pack_start(txt)
		bbox.pack_start(self.bt_add)
		bbox.pack_start(self.bt_del)
		hbox.pack_start(bbox)

		vbox.pack_start(hbox)
		win.add(vbox)
		win.show_all()
		self.bt_on1.hide()
		self.bt_on2.hide()
		self.bt_on3.hide()
		self.bt_on4.hide()
		self.bt_on5.hide()
		self.bt_on6.hide()
		self.bt_on7.hide()
		self.bt_on8.hide()
		self.bt_on9.hide()

	def main(self):
		gtk.main()


if __name__=='__main__':

	my=My()
	my.main()
