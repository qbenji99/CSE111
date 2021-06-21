"""
Programmer: Ben Quiñones
Task: Begin to write and troubleshoot a program that automatically generates English sentences.
Purpose: Prove that you can write and troubleshoot a program that contains multiple functions.
"""
from sentences import get_determiner, get_noun, get_verb, get_prepositional, get_preposition_phrase
import pytest

print()
###############
## BEGINNING ##
###############
def test_get_determiner():
    #
    singular_determiners = ["the", "one"]

    for _ in range(4):
        word = get_determiner(1)

        assert word in singular_determiners

    plural_determiners = ["some", "many"]
    for _ in range(4):
        word = get_determiner(2)

        assert word in plural_determiners
    #

def test_get_noun():
    #
    singular_nouns = ["adult", "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]
    plural_nouns = ["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]
    for _ in range(4):
        word = get_noun(1)

        assert word in singular_nouns

    for _ in range(4):
        word = get_noun(2)

        assert word in plural_nouns
    #

def test_get_verb():
    #
    past_verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]

    for _ in range(4):
        word = get_verb(1,"past")

        assert word in past_verbs
    
    present_singular_verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]

    for _ in range(4):
        word = get_verb(2,"present")

        assert word in present_singular_verbs

    present_plural_verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]

    for _ in range(4):
        word = get_verb(1,"present")

        assert word in present_plural_verbs
    
    future_verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    for _ in range(4):
        word = get_verb(1,"future")

        assert word in future_verbs
    #

def test_get_prepositional():
    #
    prep_phrases = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    for _ in range(4):
        prepositional = get_prepositional()

        assert prepositional in prep_phrases
    #

def test_get_prepositional_phrase():
    #
    prep_phrases = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    singular_determiners = ["the", "one"]
    plural_determiners = ["some", "many"]
    singular_nouns = ["adult", "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]
    plural_nouns = ["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]
    
    for _ in range(4):
        prepositional = get_prepositional()
        determiner = get_determiner(1)
        noun = get_noun(1)

        assert prepositional in prep_phrases

    #

pytest.main(["-v", "--tb=line", "-rN", "test_sentences.py"])

#########
## END ##
#########
print()