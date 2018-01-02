""" Utilities to create our bill corpus """
from typing import List
import spacy

NLP = spacy.load('en', disable=['parser', 'ner', 'textcat'])

def txt_to_token(txt : str) -> List[str]:
    """ Converts a plain txt file to a list of occurences: (<stem>, <count>)

    Args:
        txt (str): Plain txt string.
    """
    results = []
    for token in NLP(txt):
        # Ignore numbers, stop words, and punctuation
        if not token.is_alpha or token.is_stop or token.is_punct or token.is_space:
            continue
        results.append( token.lemma_ )

    return results
