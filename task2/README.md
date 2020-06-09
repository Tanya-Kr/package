#Task description
Write a program which provides the statistic about given file. It has to print the following statistic about an
arbitrary file:
```
Sample file (./storage/run2019.txt):
zzzzzzzzz
zzz
zzzzzzzzzzzzzzzzzz

andromeda

and

z and a and z
```
1. [x] a number of lines
2. [x] a number of empty lines
3. [x] a number of lines with letter "z"
4. [x] a number of "z" letters in the file
5. [x] a number of lines with "and" group (for instance, "andromeda" has "and" as well as "you and me").

```
Sample statistic:
File: ./storage/run2019.txt
  total lines:      10
  empty lines:      4
  lines with "z":   4
  "z" count":       34
  lines with "and": 3
```

Please take into account, that the program

1. [x] has to ask a user about a path to a file
2. [x] has to ask a user if one more file needs to be analyzed
3. [x] has to stop only if a user wants to stop