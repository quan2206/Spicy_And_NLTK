import spacy
from spacy import displacy
from spacy.tokens import Span
nlp = spacy.load("en_core_web_sm")
print(nlp.pipe_names)

doc = nlp("Tesla Inc is going to acquire twitter Inc for $45 billion")
for ent in doc.ents :
    print(ent.text, "|", ent.label_, "|", spacy.explain(ent.label_))
# print(displacy.render(doc, style="ent"))
print(nlp.pipe_labels)

doc1 = nlp("Michael Bloomberg founded Bloomberg Inc in 1982")
for ent in doc1.ents :
    print(ent.text, "|", ent.label_, "|", spacy.explain(ent.label_))

print("--------------------------------")
### customize the entities 
doc2 = nlp("Tesla is going to acquire Twitter for $45 billion")
print("before \n ", doc2)
for ent in doc2.ents :
    print(ent.text, "|", ent.label_)

s1 = Span(doc, 0, 1, label="ORG")
s2 = Span(doc, 5, 6, label=" ORG")
doc2.set_ents([s1, s2], default="unmodified")
print("after \n", doc2)
for ent in doc2.ents : 
    print(ent.text, "|", ent.label_)
print("--------------------------------")
