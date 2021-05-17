# text preprocessinggg..............!!!!!!!!!!!!!!!!!!!!!!!!
#

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')
stemmer= PorterStemmer()
 
word_data = "crime is the thunder . it score snow and happiness "
en_stops = set(stopwords.words('english'))
from nltk.tokenize import word_tokenize
tokens = word_tokenize(word_data)
result = [i for i in tokens if not i in en_stops]
print (result)
for word in result:
    print(stemmer.stem(word))