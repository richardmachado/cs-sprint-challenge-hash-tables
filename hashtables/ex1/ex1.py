"""
# Merging Two Packages

Given a package with a weight limit `limit` and a list `weights` of item
weights, implement a function `get_indices_of_item_weights` that finds
two items whose sum of weights equals the weight limit `limit`. Your
function will return a tuple of integers that has the following form:

```
(zero, one)
```

where each element represents the item weights of the two packages.
_**The higher valued index should be placed in the `zeroth` index and
the smaller index should be placed in the `first` index.**_ If such a
pair doesn’t exist for the given inputs, your function should return
`None`.

Your solution should run in linear time.

Example:
```
input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21
```
"""

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    the_list_of_weights = {}

    for w in range(length):
        result = limit - weights[w]
        if result in the_list_of_weights.keys():
            second_index = weights.index(result)
            if w != second_index:
                print(the_list_of_weights)
                return [w, second_index]
        the_list_of_weights.update({weights[w]:w})


l = [4,6,10,15,16]

print(get_indices_of_item_weights(l,5,21))

