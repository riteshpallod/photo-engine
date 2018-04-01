from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

input_q = input("Enter query => ")

stop_list = set(stopwords.words("english"))
words_tokens = word_tokenize(input_q)
ps = PorterStemmer()	

filtered = [w for w in words_tokens if not w in stop_list]
filtered = []

for w in words_tokens:
	if w not in stop_list:
		filtered.append(ps.stem(w))

print(filtered)

