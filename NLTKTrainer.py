from nltk.corpus import brown
from nltk.corpus import indian
import json


def WordTagSeqEn():
	engTagSeq = {}
	sents = brown.tagged_sents()

	for sent in sents:
		for i in range(0, len(sent) + 1):
			if i == 0:
				firstTag = "S"
				secondTag = sent[i][1]
			elif i == len(sent):
				firstTag = sent[i - 1][1]
				secondTag = "E"
			else:
				firstTag = sent[i - 1][1]
				secondTag = sent[i][1]
			firstTag = firstTag.split("-")[0]
			firstTag = firstTag.split("+")[0]
			firstTag = firstTag.split("$")[0]
			firstTag = firstTag.split("*")[0]
			secondTag = secondTag.split("-")[0]
			secondTag = secondTag.split("+")[0]
			secondTag = secondTag.split("$")[0]
			secondTag = secondTag.split("*")[0]
			if firstTag not in engTagSeq.keys():
				engTagSeq[firstTag] = {}
			if secondTag not in engTagSeq[firstTag].keys():
				engTagSeq[firstTag][secondTag] = 1
			else:
				engTagSeq[firstTag][secondTag] += 1

	for tag in engTagSeq:
		tagFreq = sum(engTagSeq[tag].values())
		for secondTag in engTagSeq[tag]:
			engTagSeq[tag][secondTag] /= tagFreq

	with open("WordTagSeqEn.json", "w") as file:
		json.dump(engTagSeq, file, indent=1)


def WordTagSeqHi():
	hinTagSeq = {}
	sents = indian.tagged_sents()

	for sent in sents:
		for i in range(0, len(sent) + 1):
			if i == 0:
				firstTag = "S"
				secondTag = sent[i][1]
			elif i == len(sent):
				firstTag = sent[i - 1][1]
				secondTag = "E"
			else:
				firstTag = sent[i - 1][1]
				secondTag = sent[i][1]
			if firstTag not in hinTagSeq.keys():
				hinTagSeq[firstTag] = {}
			if secondTag not in hinTagSeq[firstTag].keys():
				hinTagSeq[firstTag][secondTag] = 1
			else:
				hinTagSeq[firstTag][secondTag] += 1

	for tag in hinTagSeq:
		tagFreq = sum(hinTagSeq[tag].values())
		for secondTag in hinTagSeq[tag]:
			hinTagSeq[tag][secondTag] /= tagFreq

	with open("WordTagSeqHi.json", "w") as file:
		json.dump(hinTagSeq, file, indent=1)


def WordTagEn():
	engTagWords = {}
	sents = brown.tagged_sents(tagset="universal")

	for sent in sents:
		for word in sent:
			currentWord = word[0]
			currentTag = word[1]
			currentTag = currentTag.split("-")[0]
			currentTag = currentTag.split("+")[0]
			currentTag = currentTag.split("$")[0]
			currentTag = currentTag.split("*")[0]
			if currentWord not in engTagWords.keys():
				engTagWords[currentWord] = {}
			if currentTag not in engTagWords[currentWord].keys():
				engTagWords[currentWord][currentTag] = 1
			else:
				engTagWords[currentWord][currentTag] += 1

	for word in engTagWords:
		wordFreq = sum(engTagWords[word].values())
		for tag in engTagWords[word]:
			engTagWords[word][tag] /= wordFreq

	with open("WordTagEn.json", "w") as file:
		json.dump(engTagWords, file, indent=1)


def WordTagHi():
	hinTagWords = {}
	sents = indian.tagged_sents()

	for sent in sents:
		flag = 0
		for word in sent:
			if len(word[0]) > 0 and word[0][0] >= "\u0900" and word[0][0] <= "\u095d":
				flag = 1
				break
		if flag == 1:
			for word in sent:
				currentWord = word[0]
				currentTag = word[1]
				if currentTag != "":
					if currentWord not in hinTagWords.keys():
						hinTagWords[currentWord] = {}
					if currentTag not in hinTagWords[currentWord].keys():
						hinTagWords[currentWord][currentTag] = 1
					else:
						hinTagWords[currentWord][currentTag] += 1

	for word in hinTagWords:
		wordFreq = sum(hinTagWords[word].values())
		for tag in hinTagWords[word]:
			hinTagWords[word][tag] /= wordFreq

	with open("WordTagHi.json", "w") as file:
		json.dump(hinTagWords, file, indent=1)