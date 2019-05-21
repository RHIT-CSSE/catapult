class popup:
	__init__(textlists, xlegnth = 300, ylegnth = 200, headtext)
		self.num = len(textlists)
		self.x   = xlegnth
		self.y   = ylegnth
		self.textlists = textlists
		self.win = GraphWin(self.x, self.y, headtext)
	def createboxes(self):
		boxsizex = (self.x - 5)/self.num
		boxsizey = self.y/3
		for i in range(self.num):
			boxstartx = 5 + (boxsizex * i)
			option[i] = Button(self.textlists[i],Point(boxstartx, boxsizey),boxsizex,boxsizey)
