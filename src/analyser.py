import spacy

# Documented at: https://universaldependencies.org/u/pos/
POS_TAGS = {
    "noun": ["NOUN", "PROPN"],
    "pronoun": ["PRON"],
    "verb": ["VERB", "AUX"],
    "adjective": ["ADJ"],
    "adverb": ["ADV"],
    "determiner": ["DET"],
    "adposition": ["ADP"],
    "conjunction": ["CCONJ", "SCONJ"],
    "particle": ["PART"],
    "interjection": ["INTJ"]
}

class Analyser:
    def __init__(self, model):
        print(f"Loading spaCy ({model})")
        self.npl = spacy.load(model)

    def identify_pos(self, word):
        doc = self.npl(word)

        for token in doc:
            for pos, tags in POS_TAGS.items():
                if token.pos_ in tags:
                    return pos

        return "other" # NUM, PUNCT, SYM, X