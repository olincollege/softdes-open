# Rubric for Assignment 1

## Submission

### Effort

This item concerns the five files/directories that should be modified for
submission:

- `baby_ai.py`
- `billion.py`
- `floating_point.py`
- `password.py`
- `pricy_fall.py`
- `0-intro-to-assignments/`

For each file/directory:

3: Changes to the file seem to show a good-faith attempt on all problem parts
relating to this file.

2: Changes to the file seem to show a good-faith attempt on at least 50% (but
strictly less than 100%) of problem parts relating to this file.

1: Changes to the file seem to show a good-faith attempt on less than 50% (but
strictly more than 0%) of problem parts relating to this file.

0: The file was unchanged from its initial state.

**Points: XX/18**

#### Grader Comments

None.

### Scope of Changes

3: No files are added, changed, or deleted other than those listed above.

2: One file was added, changed, or deleted other than those listed above.

1: Two files were added, changed, or deleted other than those listed above.

0: Three or more files were added, changed, or deleted other than those listed
above.

**Points: XX/3**

#### Grader Comments

None.

### Submission Summary

Add the point totals from the two parts above.

**Points: XX/21**

#### Grader Comments

None.

## Correctness

### 1. (Describe Function Here)

For each function, one point is given for each of the following criteria:

- The docstring includes a one-sentence description of what the function does.
- The docstring indicates what type each parameter is (each parameter is worth
  one point).
- The docstring indicates what each parameter represents (each parameter is
  worth one point).
- If there is a return value, the docstring indicates the return type. (If there
  is no return value, one point for omitting the Returns section or for
  indicating that nothing is returned.)
- If there is a return value, the docstring indicates what the return value
  represents. (If there is no return value, one point for omitting the Returns
  section or for indicating that nothing is returned.)

**Extra credit**: for each function, one bonus point is given for adding extra
detail to the docstring, which may include assumptions the function makes about
the input, caveats about the return value or behavior, or a more precise
description about what the function does.

#### 1.1. One Billion Seconds

This part concerns the file `billion.py`.

**Points: XX/5**

##### Grader Comments

None.

#### 1.2. Artificial...Intelligence?

This part concerns the file `baby_ai.py`.

**Points: XX/9**

##### Grader Comments

None.

#### (Describe Function Here) Summary

Add the points from the previous sections.

**Points: XX/14**

##### Grader Comments

None.

### 2. Password Checker (9 points)

This part concerns the file `password.py`.

For each of the four checkers:

3: The given solution passes all tests.

2: The given solution fails one or more tests due to a minor error.

1: The given solution fails one or more tests due to a major error.

0: The given solution was not implemented.

#### 2.1. Blocklisted Passwords

This part concerns the function `not_common_password`.

**Points: XX/3**

##### Grader Comments

None.

#### 2.2. Password Length

This part concerns the function `meets_length_restriction`.

**Points: XX/3**

##### Grader Comments

None.

#### 2.3. Character Classes

This part concerns the function `uses_all_character_classes`.

**Points: XX/3**

##### Grader Comments

None.

#### 2.4. Multiple Sets of Password Rules

This part concerns the function `long_enough_or_all_rules`.

**Points: XX/3**

##### Grader Comments

None.

#### Password Checker Summary

Add the points from the previous sections.

**Points: XX/12**

##### Grader Comments

None.

### 3. Let me `float` an idea by you...

This part concerns the file `floating_point.py`.

For each of the four steps:

3: The given solution passes all tests.

2: The given solution fails one or more tests due to a minor error.

1: The given solution fails one or more tests due to a major error.

0: The given solution was not implemented.

#### 3.1. Split the Bitstring

This part concerns the function `split_bits`.

**Points: XX/3**

##### Grader Comments

None.

#### 3.2. Convert Exponent

This part concerns the function `convert_to_power`.

**Points: XX/3**

##### Grader Comments

None.

#### 3.3. Convert Fraction

This part concerns the function `convert_to_significand`.

**Points: XX/3**

##### Grader Comments

None.

#### 3.4. Assemble the Float

This part concerns the function `interpret_as_float`.

**Points: XX/3**

##### Grader Comments

None.

#### Let me `float` an idea by you... Summary

Add the points from the previous sections.

**Points: XX/12**

##### Grader Comments

None.

### 4. Code Repair

#### Variable Names

For each of the 10 variables that should be renamed:

1: The variable is reasonably named according to the course's style guidelines.

0: The variable is not named according to the style guidelines, including being
the name of a mathematical symbol or using excessive abbreviation.

For every **two** variables that are "on the fence" (i.e., potentially
reasonable), add back one point.

**Points: XX/10**

##### Grader Comments

None.

#### Code Errors

2: The function passes all unit tests.

1: The function passes some, but not all, unit tests.

0: Errors remain in the function that prevent it from passing any unit tests.

**Points: XX/2**

##### Grader Comments

None.

#### Code Repair Summary

Add the points from the previous sections.

**Points: XX/12**

##### Grader Comments

None.

### 5. Resubmission Practice

#### Code Fixes

2: All errors reported by pytest, pylint, or black in the original sample
submission have been fixed.

1: There are fewer errors reported by pytest, pylint, or black than in the
original submission, but some errors remain. Minor new errors may be introduced.

0: All errors remain, or major new errors were introduced.

**Points: XX/2**

##### Grader Comments

None.

#### Commit Message

2: The commit message is detailed in describing all changes made in the
resubmission, with each change justified (e.g., due to a failing test).

1: The commit message does not describe all changes, or does not justify each
change made.

0: The commit message is very vague or does not contain any detail (e.g.,
"Resubmit A0").

**Points: XX/2**

##### Grader Comments

None.

#### Commit Scope

1: The commit only affects files in the sample submission folder
`0-intro-to-assignments`.

0: The commit affects files anywhere outside the sample submission folder (e.g.,
in `1-python-basics`).

**Points: XX/1**

##### Grader Comments

None.

#### Commit Cleanliness

2: The commit does not add, change, or delete any unnecessary files.

1: The commit adds, changes, or deletes one or two unnecessary files.

0: The commit adds, changes, or deletes three or more unnecessary files.

**Points: XX/2**

##### Grader Comments

None.

#### Resubmission Practice Summary

Add the points from the previous sections.

**Points: XX/7**

##### Grader Comments

None.

### Correctness Summary

Add the points from the summary sections of each problem.

**Points: XX/57**

#### Grader Comments

None.

## Style

### General

2: The submission contains at most one spelling/grammar mistake.

1: The submission contains a few spelling/grammar mistakes.

0: The submission contains a substantial number of spelling/grammar mistakes.

**Points: XX/2**

#### Grader Comments

None.

### Git

The Git style score takes some or all of the following into account:

- The header line of commit messages succinctly summarizes what was changed.
- The commit messages provides context for the changes made.
- The changes in each commit correspond to the contents of the commit messages.
- The commit message does not contains lines that exceed 72 characters in
  length.

**Points: XX/4**

#### Grader Comments

None.

### Python

#### Black

3: Black reports no changes it would make in formatting to any of the files.

2: Black reports minor changes it would make to the formatting of one or two
files.

1: Black reports minor changes it would make to the formatting of three or more
files, or major changes it would make to the formatting of one or two files.

0: Black reports major chnages it would make to the formatting of three or more
files.

**Points: XX/3**

##### Grader Comments

None.

#### Pylint

Pylint, when run, returns a "style score" out of 10. After running this on all
Python files, take the style score and round it _down_, with minimum of 0
points.

**Points: XX/10**

##### Grader Comments

None.

#### Miscellaneous Code Style

Outside of where they are already covered by other parts of this rubric,
consider the following criteria:

- Variable names follow the course guidelines for formatting and
  descriptiveness.
- The code consistently uses single or double quotes except where it would be
  convoluted to write.
- Where needed, there are comments in the code to describe what a block of code
  does (at a high level) or why that code is there.
- The code is generally readable and easy to understand.

3: The code meets all of the above criteria.

2: The code has some minor issues with one of the above criteria.

1: The code has minor issues with more than one of the above criteria, or major
issues with one criterion.

0: The code has major issues with more than one the above criteria.

**Points: XX/3**

##### Grader Comments

None.

#### Python Summary

**Points: XX/16**

##### Grader Comments

None.

### Style Summary

Add up the points from all style subsection summaries.

**Points: XX/22**

### Grader Comments

None.

## Summary

Copy the point totals from each of the four major section summaries above.

**Submission: XX/21**

**Correctness: XX/57**

**Style: XX/22**

### Total

**TOTAL POINTS: XX/100**

### General Grader Comments

None.

### Grader Information

Grader:

Reviewer:
