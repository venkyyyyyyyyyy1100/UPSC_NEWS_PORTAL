import nltk
nltk.download('punkt_tab')
from nltk.tokenize import sent_tokenize
text = "This is a test. It works now!"
sentences = sent_tokenize(text)
print(sentences)  # Should output: ['This is a test.', 'It works now!']