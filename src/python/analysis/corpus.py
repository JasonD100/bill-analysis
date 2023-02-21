""" Utilities to create our bill corpus """
from typing import List
import spacy

NLP = spacy.load('en_core_web_sm', disable=['parser', 'ner', 'textcat'])
NLP.max_length = 3000000 #or any large value, as long as you don't run out of RAM


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
