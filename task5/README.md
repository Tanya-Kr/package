#Task description
Please write a "questionnaire" application which transforms text files into interactive
command-line questionnaire and reports answers and statistic.

Logical data structure:

-[x] a quiz consists at least from one section
-[x] each section consists at least from one question

Physical data structure:

-[x] a quiz is a directory
-[x] a section is a file in the directory
-[x] a question is a line in the file

The application runs quiz based on given directory and stores all answers in a separate file using
<question> : <answer> format. Also, it stores timing (how long it takes) for each individual
section and for the whole quiz in a separate file.

The order of section or questions in not important.