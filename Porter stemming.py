import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download('punkt')


def tokenize_and_stem(input_text):
    tokens = word_tokenize(input_text)
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return tokens, stemmed_tokens


input_text = " the Hindu festival of lights, with variations celebrated in other Indian religions such as Jainism and Sikhism.It symbolises the spiritual victory of Dharma over Adharma, light over darkness, good over evil, and knowledge over ignorance.Diwali is celebrated during the Hindu lunisolar months of Ashvin (according to the amanta tradition) and Kartika—between around mid-September and mid-November.The celebrations generally last five or six days"

tokens, stemmed_tokens = tokenize_and_stem(input_text)
print('Original Tokens:', tokens)
print('\nStemmed Tokens:', stemmed_tokens)
