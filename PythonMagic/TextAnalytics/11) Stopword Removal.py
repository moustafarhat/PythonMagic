from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
stop_words = stopwords.words('english')
example_sent = "This is a sample sentence showing the stop words filtration."
word_tokens = word_tokenize(example_sent)
filtered_sentence = [w for w in word_tokens if not w in stop_words]

print(stop_words)

print("-------------------------")
print(filtered_sentence)
