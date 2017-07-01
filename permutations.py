#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Tripp Green

Takes in a string of letters and outputs a list of all permuations
using recursion.
"""

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    '''
    tempwordlist = []

    if len(sequence) == 1:
        return [sequence]
    else:
        for letter in sequence:
            tempwordlist = tempwordlist+[letter + word for word in get_permutations(sequence.replace(letter, "", 1))]
    return tempwordlist

if __name__ == '__main__':
    '''
    Ask the user for input and outputs all permutations
    to terminal
    
    Return: void
    '''

    original = input("Enter any number of letters: ")

    print(get_permutations(original))

    pass

