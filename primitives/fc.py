
# *****************************************************************************************************************************
#
#											Manages core operations data
#
# *****************************************************************************************************************************

class CoreOperations:
	def __init__(self):
		core = """		
				_temp ; ! ?exec @ *wordsize &signmask + >r 0= 2/ c! c@ depth nand r> repeat
			"""																				# core words.
		self.coreList = core.lower().split()												# make a list of words
		self.coreList.sort()																# alphabetical order
		self.coreDictionary = {} 															# convert to dictionary
		for n in range(0,len(self.coreList)):
			self.coreDictionary[self.coreList[n]] = (n+1) * 2

	def getName(self,id):																	# id -> name
		return self.coreList[id]
	def getID(self,word):																	# name -> id
		return self.coreDictionary(word.lower().strip())

	def createFiles(self):
		h = open("__primitives.h","w")														# create any files which depend on IDs
		h.write("/* Automatically generated */\n\n")
		h.write("#ifndef __PRIMITIVES\n#define __PRIMITIVES\n\n")
		h.write("#define COP_COUNT ({0})\n\n".format(len(self.coreList)))
		for name in self.coreDictionary.keys():
			h.write("#define COP_{0} ({1})\n".format(self.toIdentifier(name).upper(),self.coreDictionary[name]))
		h.write("\n#ifdef STATIC_WORD_NAMES\n\n")
		s = ",".join(['"'+x+'"' for x in self.coreList])
		h.write("static const char *__primitives[] = {"+'"",'+s+"};\n")
		h.write("#endif\n\n")
		h.write("#endif\n\n")
		h.close()

	def toIdentifier(self,s):
		s = s.replace("@","_READ_").replace("!","_STORE_").replace("+","_ADD_")				# convert word to valid C identifier
		s = s.replace("-","_SUB_").replace("/","_DIV_").replace(">","_GREATER_")
		s = s.replace("*","_MUL_").replace("<","_LESS_").replace("=","_EQUAL_")
		s = s.replace(";","_RETURN_").replace("$","_SYS_").replace("&","_AMPERSAND_")
		s = s.replace("?","_QUESTION_").replace("__","_")
		s = s[1:] if s[0] == "_" else s
		s = s[:-1] if s[-1] == "_" else s
		return s

c = CoreOperations()
c.createFiles()
