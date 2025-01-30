import random

# GET DETERMINER
def get_determiner(quantity):
    """Randomly choosing and returning a determiner."""

    if quantity == 1:
      words = ["a", "one", "the"]
    else:
      words = ["some", "many", "the"]
    word = random.choice(words)
    return word


# GET NOUN
def get_noun(quantity):
    """Randomly choosing and returning a noun."""

    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    word = random.choice(words)
    return word



# GET VERB
def get_verb(quantity, tense):
    """Return a randomly chosen verb based on quantity and tense."""

    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought",
                 "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present":
        if quantity == 1:
            verbs = ["drinks", "eats", "grows", "laughs", "thinks",
                     "runs", "sleeps", "talks", "walks", "writes"]
        else:
            verbs = ["drink", "eat", "grow", "laugh", "think",
                     "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh",
                 "will think", "will run", "will sleep", "will talk",
                 "will walk", "will write"]
    else:
        raise ValueError("Invalid tense. Must be 'past', 'present', or 'future'.")

    return random.choice(verbs)



# GETTING PREPOSITIONS
def get_preposition():
    """Randomly choosing a preposition."""

    words = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", 
             "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", 
             "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    return random.choice(words)



# GETTING ADJECTIVES
def get_adjective():
    """Return a randomly chosen adjective."""
    words = ["big", "small", "red", "blue", "happy", "sad", "fast", "slow", "smart", "kind"]
    return random.choice(words)


# GETTING ADVERBS
def get_adverb():
    """Return a randomly chosen adverb."""
    words = ["quickly", "slowly", "gracefully", "eagerly", "silently", "loudly", "boldly", "happily"]
    return random.choice(words)



# GETTING PREPOSITIONAL PHRASES
def get_prepositional_phrase(quantity):
    """Building and returning a prepositional phrase."""

    preposition = get_preposition()
    determiner = get_determiner(quantity)
    adjective = get_adjective()
    noun = get_noun(quantity)
    return f"{preposition} {determiner} {adjective} {noun}"



# MAKING SENTENCES
def make_sentence(quantity, tense):
   """Build and return a sentence """
   determiner = get_determiner(quantity)
   adjective = get_adjective()
   noun = get_noun(quantity)
   adverb = get_adverb()
   verb = get_verb(quantity, tense)
   prepositional_phrase_1 = get_prepositional_phrase(quantity)
   prepositional_phrase_2 = get_prepositional_phrase(quantity)


   # Capitalize the first word and build the sentence
   sentence = f"{determiner.capitalize()} {adjective} {noun} {adverb} {verb} {prepositional_phrase_1} {prepositional_phrase_2}."
   return sentence


def __main__():
    print(make_sentence(1, "past"))
    print(make_sentence(1, "present"))
    print(make_sentence(1, "future"))
    print(make_sentence(2, "past"))
    print(make_sentence(2, "present"))
    print(make_sentence(2, "future"))

# Executing the program
if __name__ == "__main__":
    __main__()