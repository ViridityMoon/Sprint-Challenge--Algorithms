# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```
n = 3
n**3 = 27
n*2 = 9
a = 9
a = 18
a = 27

n = 4
n**3 = 64
n*2 = 16
a = 16
a = 32
a = 48
a = 64

n = 5
n**3 = 125
n*2 = 25
a = 25
a = 50
a = 75
a = 100
a = 125 # ends

n = 5000
n**3 = 125000000000
n*2 = 25000000
a = 25000000 # add n*2 to your value until it exceeds n**3
a = 50000000
a = 75000000
a = 100000000
(and so on)


```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```
n = 3
j = 1
j = 2
sum = 1
j = 4
sum = 2
ops: 2

n = 10
j = 1
j = 2
j = 4
j = 8
j = 16
ops: 4

n = 100
j = 1
j = 2
j = 4
j = 8
j = 16
j = 32
j = 64
j = 128
ops: 6

```
c)  def bunnyEars(bunnies):
      <!-- is bunnies equal to 0 -->
      if bunnies == 0:
        <!-- return 0 -->
        return 0

      <!-- recursively invoke bunnyEars with decremented bunnies -->
      return 2 + bunnyEars(bunnies-1)
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.


I would say this is definitely a binary search. I'd do it recursively as well, just making the floor f be the target. I'd also add in a counter to count the 'broken_eggs'.