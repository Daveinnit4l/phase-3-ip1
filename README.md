# Phase-3-Wk-1 Toy_Problems 


## Title
Phase-3-Wk-1 Toy-Problems

### Author : Kyle dave November 27th 2023

### Description

## Challenge 1: Converting 12-hour time to 24-hour time

Converting a 12-hour time like "8:30 am" or "8:30 pm" to 24-hour time (like "0830" or "2030") sounds easy enough, right? Well, let's see if you can do it!

Define a function, which will be given an hour (always in the range of 1 to 12, inclusive), a minute (always in the range of 0 to 59, inclusive), and a period (either "am" or "pm") as input.

The task is to return a four-digit string that encodes that time in 24-hour time.
Notes:
By convention, noon is 12:00 pm, and midnight is 12:00 am.

On 12-hours clock, there is no 0 hour, and time just after midnight is denoted as, for example, 12:15 am. On 24-hour clock, this translates to 0015.

- {:02d} is a string formatting syntax in Python, and it's used to format integers.
- {}: This is a placeholder for the value that will be inserted into the string.
- :02d: This is a formatting option that specifies how the value should be formatted.
- 0: It indicates that leading zeros should be used for padding.
- 2: It specifies the minimum width of the field, in this case, 2 characters.
- d: It indicates that the value should be treated as an integer.


## Challenge 2: Two numbers are positive.

Task:
Your job is to write a function, which takes three integers a, b, and c as arguments, and returns True if exactly two of of the three integers are positive numbers (greater than zero), and False - otherwise.

 # Examples:
(2, 4, -3) == True

(-4, 6, 0) == False

## Challenge 3: Consonant value

Given a lowercase string that has alphabetic characters only and no spaces, return the highest value of consonant substrings. Consonants are any letters of the alphabet except "aeiou".We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.

 # Examples;
For the word "zodiacs", solve("zodiacs") = 26

For example, for the word "zodiacs", let's cross out the vowels. We get: "z d cs"

-- The consonant substrings are: "z", "d" and "cs" and the values are z = 26, d = 4 and cs = 3 + 19 = 22. The highest is 26.

For the word "strength", solve("strength") = 57.

The consonant substrings are: "str" and "ngth" with values "str" = 19 + 20 + 18 = 57 and "ngth" = 14 + 7 + 20 + 8 = 49. The highest is 57.






## How To Run It
> fork the repository, copy the SSH code, then in your terminal navigate to where you want it to be saved and type git clone "repo SSH code"


## Contact Information
* Email : mutigaim@gmail.com
*****

## [License](LICENSE)
MIT License
Copyright (c) 2023 Isaac Mutiga