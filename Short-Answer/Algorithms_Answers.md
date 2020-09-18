#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Linear O(n), the amount of operations will be equal to the input


b) Logarithmic O(log n), initially the values follow a trend of taking a little under half the amount of operations
versus the input to run, but as it scales, that ratio will drop considerably


c) Linear O(n), it's looking for a specific value and recursively invokes with a decremented parameter
## Exercise II

Runtime Complexity - O(log n)

I would say this is definitely a binary search. I'd do it recursively as well, just making the floor f be the target. I'd also add in a counter to count the 'broken_eggs'.

define function taking in a list, target, bottom_floor, and top_floor

if bottom_floor is less than top_floor
    return invalid index

otherwise
    define a midpoint
    check if the midpoint is the target
        return it
    is the midpoint smaller?
        recursively invoke passing in the same list, same target, same bottom_floor, but the midpoint - 1 for the top_floor
        (we can reasonably drop the second half because we know 'f' has to be lower)
    is the midpoint greater?
        recursively invoke the same way except this time start will need to be midpoint + 1
        (this will drop the bottom half)
    