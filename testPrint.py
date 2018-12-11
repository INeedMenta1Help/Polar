from sys import *

class Token:
	t = None
	v = None
	def __init__(self, t, v):
		self.t = t
		self.v = v

class DisplayTok:
	t = "displayTok"
	v = []
	def __init__(self, v):
		self.v = v

	def exe(self):
		for i in range(0, len(self.v)):
			if self.v[i].v == "\n":
				print("NEWLINE")
				print("")
			else:
				print(self.v[i].v)



file = list(open(argv[1], "r").read())
print(file)

toks = []
newToks = []

def lex():
	#LEX
	tok = ""
	global toks
	strState = 0
	varState = 0

	line = 1
	for char in file:
		print(char)
		if char == "\n":
			line += 1
		if char == "\"" and strState == 0:
			strState = 1
			tok = ""
		elif char == "\"" and strState == 1:
			strState = 0
			toks.append(Token("string", tok))
			tok = ""
		else:
			tok += char
			if strState == 0:
				if tok == " ":
					tok = ""
				elif tok == "\n":
					tok = ""
				elif tok == "{":
					toks.append(Token("ident", "{"))
					tok = ""
				elif tok == "}":
					toks.append(Token("ident", "}"))
					tok = ""
				elif tok == "display":
					toks.append(Token("func", "display"))
					tok = ""


					#TESTING#
	##############################################
	for i in range(0, len(toks)):
		print( toks[i].t, ":", toks[i].v )
	print("")
	print("Your File Contains:", line, "Lines")
	###############################################

def readToks():
	global toks
	global newToks
	i = 0
	while i < len(toks):
		if toks[i].t == "func":
			if toks[i].v == "display":
				i += 1
				if toks[i].v == "{":
					i += 1
					tempArr = []
					for j in range(i, len(toks)):
						if toks[j].v == "}":
							i = j
							break
						else:
							tempArr.append(toks[j])

				
					newToks.append(DisplayTok(tempArr))
		i += 1
					#TESTING#
	##############################################
	for i in range(0, len(newToks)):
		print( newToks[i].t )
	print("")
	###############################################

def exe():
	global newToks
	print("\n\n\n\n\n\n\n\n\n")
	print("#    PolaR    #")
	for i in range(0, len(newToks)):
		newToks[i].exe()

def run():
	lex()
	readToks()
	exe()

run()