#!/bin/usr/env python3

class App:
	def __init__(self):
		self.type = 'cell phone systems'

	def start(slef):
		print('starting')
class Web:
	def web_service(self):
		print('censored')

class Android(App, Web):
	def get_version(self):
		print('Android version')

class Apple(App):
	def data_service(self):
		print('4G')

app = Apple()
app.start()
app.data_service()

g = Android()
g.web_service()
g.start()


