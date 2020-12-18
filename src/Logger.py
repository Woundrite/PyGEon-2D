from colorama import *
from datetime import datetime, date
# %T -> Time
# %D -> Date
# %L -> Level
# %C -> Text to be printed 


#Adding custiom dictionary class as the inbuilt class sucks
class Dict():
	def __init__(self, foo = None):
		self.keys = []
		self.values = []

		if foo != None and type(foo) == dict:
			for key, value in foo.items():
				self.keys.append(key)
				self.values.append(value)


	def __str__(self):
		self.returnMain = []
		for i in range(len(self.keys)):
			self.returnMain.append([str(self.keys[i]), str(self.values[i])])

		return str(self.returnMain)

	def __len__(self):
		return len(self.keys)

	def __getitem__(self, i):
		return [self.keys[i], self.values[i]]

	def __setitem__(self, i, val):
		if len(val)==2 and type(val) == tuple:
			if i <= len(keys):
				if type(val) == type(self.keys[0]):
					self.keys[i], self.values[i] = val
				else:
					raise Exception("Cannot append {0} to type {1}".format(type(key), type(self.keys[0])))
		elif len(val)==2 and type(val) == list:
			if i <= len(keys):
				if type(val) == type(self.keys[0]):
					self.keys[i] = val[0]
					self.values[i] = val[1]
				else:
					raise Exception("Cannot append {0} to type {1}".format(type(key), type(self.keys[0])))

	def get(self, key):
		for i in range(len(self.keys)):
			if key == self.keys[i]:
				return self.values[i]

	def append(self,key, value):
		if len(self.keys) != 0:
			if type(key) == type(self.keys[0]):
				self.keys.append(key)
				self.values.append(value)
			else:
				raise Exception("Cannot append {0} to type {1}".format(type(key), type(self.keys[0])))
		else:
			self.keys.append(key)
			self.values.append(value)

class Logger():
	def __init__(self, filename=None):
		#initializing colorama
		init()
		#setting up the supported colors
		self.Reset = "\033[0m"
		self.Bright = "\033[1m"
		self.Dim = "\033[2m"
		#____________________________________________________# 
		self.NormalBright = "\033[22m"
		self.ForeBlack ="\033[30m"
		self.ForeRed = "\033[31m"
		self.ForeGreen = "\033[32m"
		self.ForeYellow = "\033[33m"
		self.ForeBlue = "\033[34m"
		self.ForeMagenta = "\033[35m"
		self.ForeCyan = "\033[36m"
		self.ForeWhite = "\033[37m"
		self.ForeReset = "\033[39m"
		#____________________________________________________#
		self.BackBlack = "\033[40m"
		self.BackRed = "\033[41m"
		self.BackGreen = "\033[42m"
		self.BackYellow = "\033[43m"
		self.BackBlue = "\033[44m"
		self.BackMagenta = "\033[45m"
		self.BackCyan = "\033[46m"
		self.BackWhite = "\033[47m"
		self.BackReset = "\033[49m"
		#____________________________________________________#

		#setting up the dictionary class which holds all critical info
		self.FormatLevelColor = Dict({"info":[self.ForeCyan, "%D | %T | %L | %C"],
								"warn":[self.ForeYellow, "%D | %T | %L | %C"],
								"error":[self.ForeRed, "%D | %T | %L | %C"],
								"text":[self.ForeWhite, "%D | %T | %L | %C"]})
		#Setting up Meanings for custom Infotags
		self.IDMeaning = Dict({"%D":"^".replace("^", str(datetime.now().date())),
							   "%T":"^".replace("^", str(datetime.now().time())),
							   "%L":"%L"})
		
		if filename != None:
			self.IDMeaning.append("%F", filename)
    
	def Log(self, typee, comment):
		for key, value in self.FormatLevelColor:
			if typee.lower() == key:
				comment = self.FormatLevelColor.get(key)[1].replace("%C", comment)
				for k,v in self.IDMeaning:
					if k in comment:
						comment = comment.replace(k, v)
				if "%L" in comment:
					comment = comment.replace("%L", key)
				comment = comment.split("|")
				for comm in comment:
					if comm != comment[-1]:
						print("{0}{1}{2}".format(value[0], comm, self.Reset + " | "), end="")
					else:
						print("{0}{1}{2}".format(value[0], comm, self.Reset))

	def add(self, **kwargs):
		self.color = kwargs.get("Color")
		self.Format = kwargs.get("Format", "%D | %T | %L | %C")
		self.level = kwargs.get("Level")

		self.FormatLevelColor.append(self.level,[self.color, self.Format])