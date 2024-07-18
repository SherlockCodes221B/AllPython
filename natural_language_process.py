import nltk
nltk.download('all')
sentence = 'Sometimes, all you need to do is completely make an ass of yourself and laugh it off to realise that life isn’t so bad after all.'
tokens = nltk.word_tokenize(sentence)
print(tokens)
tagged = nltk.pos_tag(tokens)
print(tokens)