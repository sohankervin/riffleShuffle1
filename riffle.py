#! /usr/bin/python
"""
write a method to tell us if a full deck of cards shuffledDeck is single riffle of two halves
half1 and half2.
"""
cardArray = np.array([1, 52, 1])

def shuffledDeck( ) :
     # what you need to is verify if it's actually part of the single riffle 

     # measure against 2 split arrays of the original 52 elements of the deck

def mergeDecks(cardArray) :
     # create a merge list of the 52 elements of the array
         # deck1 and deck2
      if len(cardArray) :
          mid = len(cardArray) // 2
          # the first half of the cardArray is split into two lists from 0th element to mid, and mid to endth element.
          firstDeck = cardArray[ : mid]
          secondDeck = cardArray[mid : ]
          mergeSort(firstDeck)
          mergeSort(secondDeck)
          mergeList(firstDeck, secondDeck, cardArray)



