# riffleShuffle1
21 Feb 2018

write a method to tell us if a full deck of cards shuffledDeck is single riffle of two halves
half1 and half2.

single deck of cards will be represented by array of integers in range 1...52

** the reasoning for this is that a single riffle is not a completely random shuffle **
what is a riffle alogorithm


you are going to need to sort then search this is best done with a binary search and a merge sort not in that order.
this is a recursion process.

if element x is in deck1 or deck2, but not in both then this will helpus determine if the riffle happened. if x is not in 1 or 2 then a riffle

return -1 if false
