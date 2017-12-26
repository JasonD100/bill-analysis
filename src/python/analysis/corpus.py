""" Utilities to create our bill corpus """
from typing import List
import spacy
from nltk.stem.wordnet import WordNetLemmatizer

NLP = spacy.load('en', disable=['parser', 'ner', 'textcat'])
STEMMER = WordNetLemmatizer()


def txt_to_token(txt : str) -> List[str]:
    """ Converts a plain txt file to a list of occurences: (<stem>, <count>)

    Args:
        txt (str): Plain txt string.
    """
    results = []
    for token in NLP(txt):
        # Ignore numbers, stop words, and punctuation
        if not token.is_ascii or token.is_stop or token.is_punct:
            continue

        results.append( STEMMER.lemmatize( token.lower_ ) )

    return results
