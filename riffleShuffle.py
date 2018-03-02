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


def merge(firstDeck, secondDeck, cardArray)
    # the following are the next elements to be considered in the split lists.
    first = 0
    second = 0
    j = 0

    while first < len(firstDeck) and second < len(secondDeck) : 
        # the following code will determine which deck list an ith element belongs to, then amends the element to the list.
        if firstDeck[first] < secondDeck[second] :
            values[j] = firstDeck[first]
        else :
            cardArray[j] = secondDeck[second]
            second = second + 1
       
    j = j + 1
    # copy remaining entries in the firstDeck list.
    while first < len(firstDeck) :
        cardArray[j] = firstDeck[first]
        first = first + 1
        j = j + 1
   
    while second < len(secondDeck) :
        cardArray[j] = secondDeck[second]
        second = second + 1
        j = j + 1
    
# create a binary search because this was previously sorted to determine whether card target is either in the first or second deck 
    # if so, then the card shuffle is a riffle shuffle
def binary(values, low, high, target) :
    if low <= high 
