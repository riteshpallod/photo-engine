from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

'''
query pre processing
'''

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def return_tags_from_query(input_q):
	stop_list = set(stopwords.words("english"))
	words_tokens = word_tokenize(input_q)
	ps = PorterStemmer()	

	#filtered = [w for w in words_tokens if not w in stop_list]
	filtered = []

	for w in words_tokens:
		if w not in stop_list and is_number(w) != True:
			filtered.append(ps.stem(w))
	return filtered
	
		
'''
input_q = input("Enter query => ")

stop_list = set(stopwords.words("english"))
words_tokens = word_tokenize(input_q)
ps = PorterStemmer()	

filtered = [w for w in words_tokens if not w in stop_list]
filtered = []

for w in words_tokens:
	if w not in stop_list and is_number(w) != True:
		filtered.append(ps.stem(w))

print(filtered)
'''
