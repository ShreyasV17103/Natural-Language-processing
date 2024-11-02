import nltk
from nltk.corpus import treebank
from nltk.tag import AffixTagger
#nltk.download('punkt_tab')

sentence = "This is an example sentence My name is shreyas."
tokens = nltk.word_tokenize(sentence)
train_data = treebank.tagged_sents()
affix_tagger = AffixTagger(train_data, affix_length=-2)
tags = affix_tagger.tag(tokens)
print("Tags for the given sentence using affix tagger are: ")
print(tags)
