# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

def detect_language(text, languages):
    """
        Returns the detected language of given text.

        Starting point:
        words_in_dict - Keeping track of max amount of words found in a language
        lang_match - Name of the most close language match
    """
    words_in_dict = 0
    lang_match = ''
    # Iterate through the languages collection
    for language in languages:
        # Pass the length of an array (collection) that contains the common_words
        # found in the text found in argument 0
        words = len([word for word in language['common_words'] if word in text])
        # If words (the collection of words found in the current language) is
        # greater than words_in_dict (largest amount of words found in a language)
        # then keep track of the amount of words found and the language name in
        # lang_match as a String.
        if words > words_in_dict:
            words_in_dict = words
            lang_match = language['name']
    # Self explanatory
    return lang_match

# TODO
# Stats (What word is most common, percentage of languages etc etc)
"""
    Most common word: You could iterate the text using every word found in text,
    check which word has more lets say 'iterations' and keep 
    track of it in a dispossable collection whose values would be
    
"""