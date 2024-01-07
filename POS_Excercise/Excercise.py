import spacy

nlp = spacy.load("en_core_web_sm")

###Read new story
with open('new_story.txt', 'r') as f :
    news_test = f.read()
print(news_test)

###Extract NOUN and NUM tokens
doc = nlp(news_test)

numeral_tokens = []
noun_tokens = []

for token in doc :
    if token.pos_ == "NOUN":
        noun_tokens.append(token)
    elif token.pos_ == "NUM":
        numeral_tokens.append(token)
print("noun", noun_tokens , "|", "numeral" , numeral_tokens)

count = doc.count_by(spacy.attrs.POS)
print(count)

for k,v in count.items():
    print(doc.vocab[k].text, "|",v)