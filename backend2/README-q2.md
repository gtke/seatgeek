# Data Center Recovery

Uh oh! We made an Ops oops(â„¢)

Some of our data centers had a loss of data. The
administrators have managed to restore backups, but some data sets are
still missing from some data centers. Fortunately, every data set can be
found at least once in one or more of the data centers. However, before
SeatGeek can resume normal operations, it needs to ensure that each data
center has a copy of every data set.

Your goal is to help us resume normal operations as quickly as
possible by writing a program to synchronize data sets between data
centers using as few copies as possible.

Input:
------

Your program will read standard input.

The first line of input will contain an integer between 0 and 999999
inclusive, representing the number of data centers.

Following that will be one line of input for each data center with a
space-separated list of data set ids currently present at that data
center. Data set ids are each an integer between 1 and 999999, inclusive.
Each line will be at most 1000 characters long.

A data center with no data sets is represented with a blank line. Data
set ids are not necessarily consecutive. The list of data sets will not
be in any particular order.

There will be exactly one line for each data center, meaning the total
number of lines in the file will be `N+1`, where `N` is the number of data
centers.


Output:
-------

The program must output an optimal data set copy strategy to ensure that
every data center has a copy of every data set. Output one line for every
copy instruction.

"optimal" means no data set is copied to a data center that already contains
said data set, and at the end of operation every data center has a single
copy of every data set.

A copy instruction is of the form

`ds_id` `from_dc` `to_dc`

where `ds_id` is the data set id, `from_dc` is the index of the data center
the data set will be copied to (1 = the first data center) and `to_dc` is the
index of the data center to copy the data set to.

The last line of your output must be the word `done` on a line by itself. No
instructions after the word `done` will be honored.

There is often more than one correct output for a given input, and any
output that satisfies the requirements.


Constraints:
------------

The code you submit must take input from stdin and produce output to
stdout as specified above. No other output is permitted. You can
assume the input will be valid.

You may use any language you want, so long as you only use standard libraries
within that language.

Your code will be graded with an automatic grader. Your code should be
in the form of an executable called "datasync" that can be executed as follows

```
$ ./datasync < input.txt
1 1 1
1 2 1
done
```

NB: The person running this will be an engineer, and will use some reasonable effort
to get your code to run on the grading machine. Examples of reasonable things include
modifying the location of a local `python` interpreter, or understanding how to build
`java` files. Please try to conform to typical standards and behaviors as much as possible.

Example 1:
----------
Input:

```
4  - number of data centers
1 3 4 - data set ids for dataset 1
1 2 3 - data set ids for dataset 2
1 3
1 4 2
```

One Possible Correct Output:
`ds_id` `from_dc` `to_dc`
```
2 2 1 ---> 1 2 3 4
4 1 2 ---> 1 2 3 4
2 2 3 ---> 1 2 3
4 4 3 ---> 1 2 3 4
3 1 4 ---> 
done
```


Example 2:
----------
Input:

```
2
1 2
2 1
```

Output:

```
done
```

Example 3:
----------
Input:

```
3
1 3 4 5 7
1 3
2
```

One Possible Correct Output:

```
2 3 2
2 3 1
1 1 3
4 1 2
5 1 3
5 3 2
4 2 3
3 1 3
7 1 2
7 1 3
done
```
