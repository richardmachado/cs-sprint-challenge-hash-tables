
"""
# Positive and Negative

For an input list of integers, we wish to know which positive numbers
have corresponding negative numbers in the list.

Example input:

```python
[ 1, -1, 2, 3, -4, -3, 4, -5, 6, 7 ]
```

Input can be in any order.

Example return value:

```python
[ 1, 3, 4 ]
```
"""
def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    result = []
    cache = {}

    for num in a:
        cache[num] = None

    for num in a:
        if num* -1 in cache and num > 0:
            result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
