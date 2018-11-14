from sys import *
file = list(open(argv[1], "r").read())

#Arrays
memSize = 64
mem = [None] * memSize
var = []

def findVar(name):
	for i in range(0, len(var)):
		if name == var[i][0]:
			return var[i][1]
	print(name + " Not Defined - 0 Instead Of Exception!")
	return 0

def changeVar(name, newVar):
	changed = 0
	for i in range(0, len(var)):
		if name == var[i][0]:
			var[i][1] = newVar
			changed = 1
			break

	if changed == 0:
		print("Unable to find Variable: " + name + "\nNo Variable was changed to avoid Exceptions")

def lex():
	toks = []
	tok = ""
	string = False
	comstate = False

	for char in file:
		#print(tok)
		if ((char == " " and comstate == False) or char == "\n" or char == ";") and string == False:
			if (comstate == False and tok != ""):
				toks.append(tok)
			tok = ""
			comstate = False
		elif char == "#":
			comstate = True
			tok = ""
		elif comstate == False:
			if char == "\"":
				tok += char
				string = not string
			else:
				tok += char


	#print(toks)

	lex2(toks)

def lex2(toks):
	adtoks = [] #Advanced Tokens
	for i in range(0, len(toks)):
		if toks[i][0] == "&":
			varname = toks[i][1:]
			adtoks.append(["var", varname])

		elif toks[i][0] == "$":
			adtoks.append(["data", int(toks[i][1:])])

		elif toks[i][0] == "\"":
			adtoks.append(["string", str(toks[i][1:len(toks[i])-1])])

		elif toks[i] == "=":
			adtoks.append(["declare", "="])

#OPERATORS
		elif toks[i] == "==":
			adtoks.append(["op", "=="])

		elif toks[i] == "*":
			adtoks.append(["op", "*"])

		elif toks[i] == "/":
			adtoks.append(["op", "/"])

		elif toks[i] == "+":
			adtoks.append(["op", "+"])

		elif toks[i] == "-":
			adtoks.append(["op", "-"])

#FUNCTIONS
		elif toks[i] == "log:":
			adtoks.append(["func", "log"])


	print(adtoks)
	parse(adtoks)

def parse(toks):
	i = 0
	while i < len(toks):
		#print(toks[i])

		if toks[i][0] == "var":
			if toks[i+1][0] == "declare":
				if toks[i+2][0] == "data":
					var.append([toks[i][1], int(toks[i+2][1])])
					#print("Var: " + toks[i][1] + " Created As: " + toks[i+2][1])
				elif toks[i+2][0] == "string":
					var.append([toks[i][1], str(toks[i+2][1])])
					#print("Var: " + toks[i][1] + " Created As: " + str(toks[i+2][1]))
				elif toks[i+2][0] == "var":
					vardata = findVar(toks[i+2][1])
					var.append([toks[i][1], vardata])
					#print("Var: " + toks[i][1] + " Created As: " + str(vardata))
				else:
					print("Invalid Declaration Of Variable, Cannot Declare As Type: " + toks[i+2][0] + "\nVar Created With 0 To Avoid Exception")
					var.append([toks[i][1], 0])
				i += 2

			#OPERATIONS
			elif toks[i+1][0] == "op":
				if toks[i+1][1] == "*":
					var1 = findVar(toks[i][1])
					if toks[i+2][0] == "var":
						var2 = findVar(toks[i+2][1])
						changeVar(toks[i][1], var1 * var2)
					elif toks[i+2][0] == "data":
						var1 = var1 * toks[i+2][1]
						changeVar(toks[i][1], var1)
					else:
						print("Invalid Operation on Variable: " + str(toks[i][1]) + ". \n" + str(toks[i][1]) + " Has Been kept the same to Avoid Exceptions")
				elif toks[i+1][1] == "/":
					var1 = findVar(toks[i][1])
					if toks[i+2][0] == "var":
						var2 = findVar(toks[i+2][1])
						changeVar(toks[i][1], var1 / var2)
					elif toks[i+2][0] == "data":
						var1 = var1 / toks[i+2][1]
						changeVar(toks[i][1], var1)
					else:
						print("Invalid Operation on Variable: " + str(toks[i][1]) + ". \n" + str(toks[i][1]) + " Has Been kept the same to Avoid Exceptions")
				elif toks[i+1][1] == "+":
					var1 = findVar(toks[i][1])
					if toks[i+2][0] == "var":
						var2 = findVar(toks[i+2][1])
						changeVar(toks[i][1], var1 + var2)
					elif toks[i+2][0] == "data":
						var1 = var1 + toks[i+2][1]
						changeVar(toks[i][1], var1)
					else:
						print("Invalid Operation on Variable: " + str(toks[i][1]) + ". \n" + str(toks[i][1]) + " Has Been kept the same to Avoid Exceptions")
				elif toks[i+1][1] == "-":
					var1 = findVar(toks[i][1])
					if toks[i+2][0] == "var":
						var2 = findVar(toks[i+2][1])
						changeVar(toks[i][1], var1 - var2)
					elif toks[i+2][0] == "data":
						var1 = var1 - toks[i+2][1]
						changeVar(toks[i][1], var1)
					else:
						print("Invalid Operation on Variable: " + str(toks[i][1]) + ". \n" + str(toks[i][1]) + " Has Been kept the same to Avoid Exceptions")


				i += 2



		elif toks[i][0] == "func":
			if toks[i][1] == "log":
				if toks[i+1][0] == "var":
					print(findVar(toks[i+1][1]))
				elif toks[i+1][0] == "string" or toks[i+1][0] == "data":
					print(toks[i+1][1])
				i += 1

		i += 1

lex()


#print(file)
#print(mem)
print(var)