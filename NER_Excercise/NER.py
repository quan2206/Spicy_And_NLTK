import spacy

nlp = spacy.load("en_core_web_sm")
print(nlp.pipe_names)

doc = nlp("Tesla Inc is going to acquire twitter for $45 billion")
for ent in doc.ents :
    print(ent.text, "|", ent.label_, "|")