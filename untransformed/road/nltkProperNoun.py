import nltk
import os, sys
from nltk.tag import pos_tag

newpath = (os.path.dirname(os.path.abspath(__file__))) + r'\newFiles'
if not os.path.exists(newpath):
	os.makedirs(newpath)


for n in os.listdir(os.getcwd()):
	if n.endswith(".dat"):
		with open(n) as File1:
			data = File1.read().replace('\n', '')
		WordList = data.split()
		tagged_sent = pos_tag(data.split())
		propernouns = []
		lowerproper = []


		for n,word in enumerate(tagged_sent):
			if n != 0:
				if "." in WordList[n-1]:
					continue
				elif "?" in WordList[n-1]:
					continue
				elif "!" in WordList[n-1]:
					continue
				else:
					if word[1]=='NNP':
						if word[1] not in propernouns:
							propernouns.append(word[0]);
						

		for word in propernouns:
			lowerproper.append(word.lower())

		for n,word in enumerate(WordList):
			word.replace('"','')
			if word in propernouns:
				WordList[n] = 'Proper_Noun';
			if word in lowerproper:
				WordList[n] = 'Proper_Noun';

		NewString = ' '.join(WordList);
		NewFile = newpath + '\%s' % File1.name
		File2 = open(NewFile, 'a')
		File2.write(NewString)
		File2.close()

