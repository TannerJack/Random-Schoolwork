def my_split(text):
	wordList = []
	wordLen = text.find(' ')
	if wordLen<1:
		if(hasPunct(text)):
			wordList.append(text[:len(text)-1])
			return wordList
			
		else:
			wordList.append(text)
			return wordList
	
	else:
		while wordLen>0 :
			wordLen = text.find(' ') ## Returns -1 if does not exist
			if(wordLen == -1):
				wordList.append(text)
				return wordList

			if(hasPunct(text[:wordLen])):
				wordList.append(text[:wordLen-1])
				text = text[wordLen+1:]
			else:
				wordList.append(text[:wordLen])
				text = text[wordLen+1:]
			
		wordList.append(text)
		return wordList
def count(words):
	dict = {}
	for word in words:
		dict[word] = dict.get(word, 0) + 1
	return dict
				
	
def word_count_similarity(count1, count2):  
	s1Count = count1.values()
	s1 = 0
	s2Count = count2.values()
	s2 = 0
	
	key1 = ""
	key2 = " "
	s3 = 0
	
	
	for int1 in s1Count:
		s1 = s1 + int1*int1
	for int2 in s2Count:
		s2 = s2 + int2*int2
	for key1 in count1.keys():
		for key2 in count2.keys():
			if key1 == key2:
				s3 = s3 + count1.get(key1, 0) * count2.get(key2, 0)
	return s3/float(s1*s2)
def hasPunct(string):
	if "," in string or "." in string or "?" in string or "!" in string:
		return True
	else:
		return False
def best_guess(known_author_counts, unknown_count):
    comp = 0
    authorB = ""
    for author in known_author_counts:
        comp2 = word_count_similarity(known_author_counts.get(author),unknown_count)
        if comp2 > comp:
            comp = comp2
            authorB = author
    return authorB
