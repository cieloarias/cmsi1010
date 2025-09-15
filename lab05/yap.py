import random

words = {
    "noun": ["dog", "carrot", "chair", "toy", "rice cake"],
    "verb": ["ran", "barked", "squeaked", "flew", "fell", "whistled"],
    "adjective": ["small", "great", "fuzzy", "funny", "light"],
    "preposition": ["through", "over", "under", "beyond", "across"],
    "adverb": ["barely", "mostly", "easily", "already", "just"],
    "emotions": ["happy", "sad", "angry", "excited", "hopeful"]
}

template = """
    Yesterday the emotions noun
    verb preposition the coach’s
    adjective emotions noun that was
    adverb adjective before
    """


def random_sentence():
    sentence = []
    for token in template.split():
        if token in words:
            sentence.append(random.choice(words[token]))
        else:
            sentence.append(token)
    return " ".join(sentence) + "."


for _ in range(5):
    print(random_sentence())
