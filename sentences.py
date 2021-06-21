"""
Programmer: Ben Quiñones
Task: Begin to write and troubleshoot a program that automatically generates English sentences.
Purpose: Prove that you can write and troubleshoot a program that contains multiple functions.
"""
import random as r

print()
###############
## BEGINNING ##
###############
def main():
    #
    #A1
    determiner = get_determiner(1)
    noun = get_noun(1)
    verb = get_verb(1, "past")
    print(f"{determiner} {noun} {verb}")
    #B1
    determiner = get_determiner(0)
    noun = get_noun(0)
    verb = get_verb(0, "past")
    print(f"{determiner} {noun} {verb}")
    #C1
    determiner = get_determiner(1)
    noun = get_noun(1)
    verb = get_verb(1, "present")
    print(f"{determiner} {noun} {verb}")
    #D1
    determiner = get_determiner(0)
    noun = get_noun(0)
    verb = get_verb(0, "present")
    print(f"{determiner} {noun} {verb}")
    #E1
    determiner = get_determiner(1)
    noun = get_noun(1)
    verb = get_verb(1, "future")
    print(f"{determiner} {noun} {verb}")
    #F1
    determiner = get_determiner(0)
    noun = get_noun(0)
    verb = get_verb(0, "future")
    print(f"{determiner} {noun} {verb}")
    #A2
    determiner = get_determiner(1)
    noun = get_noun(1)
    verb = get_verb(1, "past")
    prep_phrase_1, prep_phrase_2, prep_phrase_3 = get_preposition_phrase(1)
    print(f"{determiner} {noun} {verb} {prep_phrase_1} {prep_phrase_2} {prep_phrase_3}")
    #B2
    determiner = get_determiner(0)
    noun = get_noun(0)
    verb = get_verb(0, "past")
    prep_phrase_1, prep_phrase_2, prep_phrase_3 = get_preposition_phrase(0)
    print(f"{determiner} {noun} {verb} {prep_phrase_1} {prep_phrase_2} {prep_phrase_3}")
    #C2
    determiner = get_determiner(1)
    noun = get_noun(1)
    verb = get_verb(1, "present")
    prep_phrase_1, prep_phrase_2, prep_phrase_3 = get_preposition_phrase(1)
    print(f"{determiner} {noun} {verb} {prep_phrase_1} {prep_phrase_2} {prep_phrase_3}")
    #D2
    determiner = get_determiner(0)
    noun = get_noun(0)
    verb = get_verb(0, "present")
    prep_phrase_1, prep_phrase_2, prep_phrase_3 = get_preposition_phrase(0)
    print(f"{determiner} {noun} {verb} {prep_phrase_1} {prep_phrase_2} {prep_phrase_3}")
    #E2
    determiner = get_determiner(1)
    noun = get_noun(1)
    verb = get_verb(1, "future")
    prep_phrase_1, prep_phrase_2, prep_phrase_3 = get_preposition_phrase(1)
    print(f"{determiner} {noun} {verb} {prep_phrase_1} {prep_phrase_2} {prep_phrase_3}")
    #F2
    determiner = get_determiner(0)
    noun = get_noun(0)
    verb = get_verb(0, "future")
    prep_phrase_1, prep_phrase_2, prep_phrase_3 = get_preposition_phrase(0)
    print(f"{determiner} {noun} {verb} {prep_phrase_1} {prep_phrase_2} {prep_phrase_3}")

    print()
    print("Below are randomly generated phrases based on a random number/choice generator!")
    print()

    tense = ["past", "present", "future"]
    z = 6
    while z != 0:
        quantity = r.randint(0,1)
        tense_choice = r.choice(tense)
        determiner = get_determiner(quantity)
        noun = get_noun(quantity)
        verb = get_verb(quantity, tense_choice)
        prep_phrase_1, prep_phrase_2, prep_phrase_3 = get_preposition_phrase(quantity)

        print(f"{determiner} {noun} {verb} {prep_phrase_1} {prep_phrase_2} {prep_phrase_3}")
        #get_preposition_phrase(quantity)
        z = z - 1
    #

def get_determiner(quantity):
    #
    if quantity == 1:
        words = ["the", "one"]
    else:
        words = ["some", "many"]

    word = r.choice(words)
    return word
    #

def get_noun(quantity):
    #
    if quantity == 1:
        nouns = ["adult", "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]
    else:
        nouns = ["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]

    noun = r.choice(nouns)
    return noun
    #

def get_verb(quantity, tense):
    #
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    verb = r.choice(verbs)
    return verb
    #

def get_prepositional():
    #
    prep_phrases = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    prep_phrase = r.choice(prep_phrases)
    return prep_phrase
    #

def get_preposition_phrase(quantity):
    #
    prepositional = get_prepositional()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)

    return prepositional, determiner, noun
    #return print(f"{prepositional} {determiner} {noun}")
    #

main()


#########
## END ##
#########
print()