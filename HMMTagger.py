import os
import json

cur_path = os.path.dirname(__file__)

wordTag = {}
wordTagSeq = {}
langlist = ["En", "Hi", "EnDetailed"]

for lang in langlist:
	filename = "WordTag" + lang + ".json"
	new_path = os.path.join(cur_path, "TrainedData", filename)
	with open(new_path, "r") as file:
		wordTag[lang] = json.load(file)

	filename = "WordTagSeq" + lang + ".json"
	new_path = os.path.join(cur_path, "TrainedData", filename)
	with open(new_path, "r") as file:
		wordTagSeq[lang] = json.load(file)

# Get the emission and transition probability
def getProb(word, prevTag, curTag, langcode):
	# Check the transition probability
	if curTag not in wordTagSeq[langcode][prevTag].keys():
		TrProb = 1
	else:
		TrProb = wordTagSeq[langcode][prevTag][curTag]

	# Check the emission probability
	if word not in wordTag.keys():
		EmProb = 1
	elif curTag not in wordTag[word].keys():
		EmProb = 0
	else:
		EmProb = wordTag[word][curTag]

	return EmProb, TrProb


def viterbiAlgorithm(sent, langcode):
	bestEdge = {}
	bestScore = {}
	possibleTags = []
	possibleWords = wordTag[langcode].keys()

	# Add all the possible tags in a list to check later
	for tag in wordTagSeq[langcode]:
		for secondTag in wordTagSeq[langcode][tag]:
			if secondTag not in possibleTags:
				possibleTags.append(tag)

	words = sent.split(" ")
	words = [word for word in words if len(word) != 0]
	words.insert(0, "S")

	# Get the best tag for the first word
	for tag in possibleTags:
		EmProb, TrProb = getProb(words[0], "S", tag, langcode)
		bestScore[(words[0], tag, 0)] = EmProb * TrProb
		bestEdge[(words[0], tag, 0)] = "S"

	for i in range(1, len(words)):
		for curTag in possibleTags:
			tempScore = 0
			if (words[i] in possibleWords) and (
				curTag not in wordTag[langcode][words[i]].keys()
			):
				# If not a possible tag, assign it a probability = 0
				bestScore[(words[i], curTag, i)] = tempScore
			else:
				# If a possible tag, assign it a calculated probability
				for prevTag in possibleTags:
					EmProb, TrProb = getProb(words[i], prevTag, curTag, langcode)
					score = bestScore[(words[i - 1], prevTag, i - 1)] * EmProb * TrProb
					bestScore[(words[i], curTag, i)] = tempScore

					if score > tempScore:
						tempScore = score
						bestScore[(words[i], curTag, i)] = score
						bestEdge[(words[i], curTag, i)] = prevTag

	# Check the best possible tag for the last word
	score = 0
	bestTag = None
	taggedSent = []
	nthWord = words[-1]
	wordsLength = len(words) - 1
	for tag in possibleTags:
		if bestScore[(nthWord, tag, wordsLength)] > score:
			score = bestScore[(nthWord, tag, wordsLength)]
			bestTag = tag
	taggedSent.append((nthWord, bestTag))

	for i in range(len(words) - 2, -1, -1):
		taggedSent.append((words[i], bestEdge[(words[i + 1], bestTag, i + 1)]))
		bestTag = bestEdge[(words[i + 1], bestTag, i + 1)]

	return taggedSent


def tagSentence(sent, langcode):
	taggedSent = viterbiAlgorithm(sent, langcode)
	taggedSent = taggedSent[::-1]
	taggedSent = taggedSent[1:]
	updatedSent = []
	for i in range(0, len(taggedSent)):
		if taggedSent[i][1] == "S":
			updatedSent.append((taggedSent[i][0], "NNP"))
		elif taggedSent[i][1] == "":
			updatedSent.append((taggedSent[i][0], "X"))
		else:
			updatedSent.append(taggedSent[i])

	return updatedSent