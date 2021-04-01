# 2021-04-01

Firstly, please vote on the poll in the announcements channel, we want to hear your feedback on what topics we should cover!

Until we see that a majority of people have voted on the poll, we'll be doing CCC questions. We will start with J3s and J4s and move on to doing J5s as time pass. Of course, if the poll shows that y'all want to do a topic other than CCC (i.e. game development) we'll switch to that whenever we can.

In this meeting, we will be doing two questions - CCC 2016 J3 and CCC 2018 J3. You can see the problem statements at these links:

-   https://github.com/SWC-Python-Club/meetings/blob/main/meetings/2021-04-01/CCC-2016-J3.md
-   https://github.com/SWC-Python-Club/meetings/blob/main/meetings/2021-04-01/CCC-2018-J3.md

Let's start with CCC 2016 J3 - Hidden Palindrome.

# CCC 2016 J3 - Hidden Palindrome

Please read the problem statement on your own first.

[pause]

In short, this question asks us to find the longest substring contained in the input string that is a _palindrome_. We then print the length of this substring to standard output. For example, in the string `hello_mom`, we would print `3` as that is the length of `mom`, the longest palindrome.

## Determining whether a string is a palindrome

There are a few ways we can go about solving the problem but they all have one thing in common - we need to know how to determine whether a string is a palindrome. Again, there are a few ways to go about this, but we'll be using the simplest one here.

First, Recall that a palindrome is a word that reads the same backward as forward. Therefore, we can determine whether a string is a palindrome by checking whether reversing the string results in the same string.

A simple way of reversing a string in Python is:

```python
reversed_string = string[::-1]
```

> This utilizes Python's slice notation to create a reversed copy of the string. For more information on this, you can check out the following blog post: https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/.

Now, with this code, we can define a function that determines whether a string is a palindrome:

```python
def is_palindrome(string):
	reversed_string = string[::-1]
	return string == reversed_string
```

And now let's try it out:

```py
>>> is_palindrome("hello")
False
>>> is_palindrome("mom")
True
>>> is_palindrome("a")
True
```

> For the last example, note that a word with one letter is still a palindrome, per the problem statement.

Cool, looks like it works. Now, let's use this to solve the problem.

## Solution

At the start of the code, let us paste the function we wrote earlier that determines whether a string is a palindrome:

```python
def is_palindrome(string):
	reversed_string = string[::-1]
	return string == reversed_string
```

Next, let us read the next line of input and store it in a variable:

```python
text = input()
```

Next, let us create a variable that holds the length of the longest palindrome we have found so far:

```python
longest_len = 0
```

Next, let us iterate over all indices of the string:

```python
for start_index in range(0, len(text)):
	pass
```

Next, let us iterate over all possible palindromes that start at this index. To do this, we can iterate from `the index of the last character + 1` down to `start_index`, and then slice the string.

For example, given the input string `abcde` and assuming `start_index` is `0`, `substr` would be one of the following:

-   `abcde`
-   `abcd`
-   `abc`
-   `ab`
-   `a`

```python
for start_index in range(0, len(text)):
	for end_index in range(len(text), start_index, -1):
		substr = text[start_index:end_index]
```

Next, check whether the string is a palindrome. If it is, check whether it's longer in length than the current longest palindrome we have found. If so, update the longest length.

```python
if is_palindrome(substr):
	substr_len = len(substr)
	if substr_len > longest_len:
		longest_len = substr_len
```

And finally, after all the loops have finished, print out the longest length found.

```python
print(longest_len)
```

## Resulting Code

And... that's it! Here is the code in its entirety:

> You can also see the code as a Python file [here](./code/ccc_2016_j3.py).

```python
def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string


text = input()
longest_len = 0


for start_index in range(0, len(text)):
    for end_index in range(len(text), start_index, -1):
        substr = text[start_index:end_index]
        if is_palindrome(substr):
            substr_len = len(substr)
            if len(substr) > longest_len:
                longest_len = substr_len

print(longest_len)

```

## Does it work?

Let's check if it works using DMOJ:

![DMOJ submission image](https://i.imgur.com/2QGarS6.png)

Cool, looks like it's working!

## Summary

Once you understand what this question is asking, it's relatively simple - just two nested loops and some comparisons. The solution presented above is absolutely _not_ optimized - for example, doing some more clever calculation and adding some more conditions would have allowed us to perform less iterations and thus arrive at a more efficient solution. However, the code works, and is relatively simple to understand, which is what matters.

# CCC 2018 J3 - Are we there yet?

Again, please read the problem statement on your own first.

[pause]

This question is relatively straight-forward, especially after reading the example, so we'll just get straight into the code.

## Solution

First, let us read the next line of input and then parse it into a list. To do this, we use `str.split()`, which splits the given string at whitespace in addition to a [list comprehension](https://realpython.com/list-comprehension-python/) to parse the strings into integers.

For example, if the input were `1 2 3 4`, `distances` would be `[1, 2, 3, 4]`.

```python
distances = [int(x) for x in input().split()]
```

Next, let us define a function that will compute the distance between two cities `a` and `b`.
We will use the `distances` array to do this - per the question statement, the _i_-th integer represents the distance between city _i_ and city _i + 1_. Thus, the distance between city _i_ and city _i + n_ would the sum of all integers from the _i_-th integer to the _i + n_-th integer, excluding the last integer in that range.

For example, suppose we wanted to compute the distance between cities 1 and 3, given a distance array of `[3, 10, 12, 5]`. We would sum the integers between the 1st position and the 3rd position, resulting in `3 + 10` = `13`.

```python
def distance(a, b):
	# If the cities are the same, return 0.
	if a == b:
		return 0

	min_city = min(a, b)
	max_city = max(a, b)

	# Subtract one because the distances array is 0-based.
	return sum(distances[min_city - 1 : max_city - 1])
```

Next, let us iterate through all cities. Each iteration will generate a line of input.
In the body of the loop, we will create a `row` variable, to store the current row of values in the table.

```python
# Note: We use 6 for the upper bound as `range()` is exclusive on the upper bound, but we want to include 5 in the iteration.
for first_city in range(1, 6):
	row = []
```

Next, let us iterate through all cities again in the body of the first loop. Then, compute the distance between the first city and the second city, and add it to the `row` list.

```python
for first_city in range(1, 6):
	row = []
	for second_city in range(1, 6):
		dist = distance(first_city, second_city)
		row.append(str(dist))
```

Finally, let us print out this row of values, joined by a single space.

```python
for first_city in range(1, 6):
	row = []
	for second_city in range(1, 6):
		dist = distance(first_city, second_city)
		row.append(str(dist))

	print(" ".join(row))
```

## Resulting Code

And... that's it! Here is the code in its entirety:

> You can also see the code as a Python file [here](./code/ccc_2018_j3.py).

```python
distances = [int(x) for x in input().split()]


def distance(a, b):
    if a == b:
        return 0

    min_city = min(a, b)
    max_city = max(a, b)

    return sum(distances[min_city - 1 : max_city - 1])


for first_city in range(1, 6):
    row = []
    for second_city in range(1, 6):
        dist = distance(first_city, second_city)
        row.append(str(dist))

    print(" ".join(row))
```

## Does it work?

Let's check if it works using DMOJ:

![DMOJ submission image](https://i.imgur.com/ukml84M.png)

Cool, looks like it's working!

## Summary

Again, this is a relatively simple problem that uses some counting and nested loops. The solution presented above is simple but not optimized at all. This does not matter much considering the constraints put upon the number of cities (4) in the problem, but if more cities were given we might run into some time issues. A more sophisticated solution might use a precomputed [prefix sum array](https://www.geeksforgeeks.org/prefix-sum-array-implementation-applications-competitive-programming/) to compute the distance between two cities in constant time.
