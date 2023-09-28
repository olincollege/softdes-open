# Final Project Rubric

The architecture review and code review are graded separately on Canvas and have
their own rubrics visible there.

## Repository (20 Points)

### Organization and Content

Grading is based on the following criteria:

- The repository has an appropriate title, not containing the names of the
- authors, the project advisor, the course, or the semester.
- The instructors have access to the repository.
- All code files are present.
- All static resources (e.g., images, sounds) are present.
- All other files (e.g., website files and a `requirements.txt` file) are
  present.
- No sensitive information, such as API keys or credentials, appears in the
  repository.

Each of the first five criteria receive 2 points if fully met or 1 point if
partially met.

If sensitive information appears in the repository, up to 10 points may be
deducted from this section's score.

**Points: XX/10**

Grader comments: None.

### Git

Two points for meeting each of the following criteria (checked over all commits
relevant to the submission):

- The header line of commit message succinctly summarizes what was changed.
- The commit message provides context for the changes made.
- The final version of the repo does not contain files not necessary for
  submission, including `.vscode` folders, `__pycache__` folders, `.pyc` files,
  etc.
- The final version of the repo does not contain Git conflict indicators (e.g.,
  `<<<<<<< HEAD`) that need to be removed during grading.
- The commit message does not contain lines that exceed 72 characters in length.

One point may be given for each criterion that is partially satisfied (e.g., one
commit message out of five fails to summarize changes).

**Points: XX/10**

Grader comments: None.

### Repository Summary

**Points: XX/20**

## Implementation (80 Points)

### Scope and Design

Grading is based on the following criteria:

- The code demonstrates independent learning through the use of a library or
  feature not covered in class, such as Pygame, `argparse`, or other modules.
- The code demonstrates comfort with classes in Python, such as the use of
  private attributes, inheritance, or composition as necessary.
- The code demonstrates comfort with small software architecture design, as
  evidenced through data attributes stored in classes and the interface through
  which class instances can be used.
- The code demonstrates a significant amount of effort (roughly 2 assignments'
  worth), made clear by factors such as (but not only) the level of features
  used and the complexity of the functions.

15: The code meets all of the above criteria.

12: The code has minor issues (e.g., improper access of private attributes,
slightly underscoped work) in meeting one of the above criteria.

9: The code has minor issues in meeting two of the above criteria, or major
issues (e.g., using inheritance instead of composition) in meeting one of the
above criteria.

6: The code has major issues in two of the above criteria.

0: The code fails to meet any of the above criteria.

**Points: XX/15**

Grader comments: None.

### Correctness

Grading is based on the following criteria:

- The code passes all unit tests.
- The code consists of at least three separate classes.
- The code is divided among at least three separate files.
- The code follows the MVC architecture, with a clear model, view, and
  controller component, or the instructor has approved an alternative
  architecture.
- The code is interactive, obtaining input from the user during execution or as
  a command-line argument.

Two points are given for each criterion met, with one point given if a criterion
is partially met.

**Points: XX/10**

Grader comments: None.

### Unit Tests

Where possible, a function should have unit tests that can be run to ensure that
the function implementation is correct. Each unit test should be justified with
a comment explaining why that test is there, and for each function, the set of
unit tests should reasonably cover the set of inputs to, and behaviors of, that
function.

Certain functions may not be able to be unit tested. Where possible and
appropriate, parts of a function that can be unit tested and that stand on their
own should be separated into their own functions, and unit tests for these
functions should be included.

15: Each function has unit tests meeting the above criteria, where possible.

12: One or two functions have unit tests with a minor omission in the above
criteria (e.g., unclear comment, forgot to test a small edge case), or a single
function has a docstring with a major omission (e.g., missing comment or forgot
to test a key part of the function behavior).

9: Multiple functions have sets of unit tests with major omissions.

6: A majority of the functions have sets of unit tests with major omissions.

0: No unit tests are present.

**Points: XX/15**

Grader comments: None.

### README

Grading is based on the following criteria:

- The README provides a short summary of the project.
- Where applicable, the README provides instructions for obtaining the necessary
  packages or libraries needed to run the code.
- Where applicable, the README mentions any changes necessary to the code
  required to successfully run it.
- The README provides instructions for successfully running the code.

10: The README meets all of the above criteria.

8: The README is unclear or incomplete in one of these areas.

6: The README is unclear or incomplete in multiple areas, or missing one area
entirely.

4: The README is missing multiple areas.

0: The README is missing entirely.

**Points: XX/10**

Grader comments: None.

### Docstrings

Every function should have a well-written docstring that describes what the
function does, any assumptions made, the type and description of each parameter,
and the type and description of the return value.

10: Each function has a docstring matching the above description.

8: One or two functions have docstrings with a minor omission in the above
criteria (e.g., forgot to list a type), or a single function has a docstring
with a major omission (e.g., missing section).

6: Multiple functions have docstrings with major omissions.

4: A majority of the functions have docstrings with major omissions.

0: No docstrings are present.

**Points: XX/10**

Grader comments: None.

### Pylint

Pylint, when run, returns a "style score" out of 10. After running this on all
Python files, take the style score and round it _down_, with minimum of 0
points.

**Points: XX/10**

Grader comments: None.

### Miscellaneous Style

Outside of where they are already covered by other parts of this rubric,
consider the following criteria:

- Black, when run on all `.py` files, does not report any changes it would make
  to the files.

* Variable names follow the course guidelines for formatting and
  descriptiveness.
* The code consistently uses single or double quotes, except where it would be
  convoluted to write.
* Where needed, there are comments in the code to describe what a block of code
  does (at a high level) or why that code is there.
* The code makes use of features taught in the course, particularly in making
  code more readable (e.g., using f-strings rather than calling `print` on
  multiple arguments).
* The code is well-organized into files as appropriate (e.g., separate files for
  each class).
* The code is generally readable and easy to understand.

10: The code meets all of the above criteria.

8: The code has some minor issues with one of the above criteria.

6: The code has minor issues with more than one of the above criteria, or major
issues with one criterion.

4: The code has major issues with more than one the above criteria.

0: None of the criteria above are met.

**Points: XX/10**

Grader comments: None.

### Code Summary

**Points: XX/80**

## Website (20 Points)

### Content

Grading is based on the following criteria:

- The big idea and highlights of the project are clearly described.
- The website provides instructions for obtaining and using the project
  software, or links to a page that provides this information.
- The website includes some text or visuals that show the software being used
  (e.g., a screenshot or example).
- If any external resources were used, the website provides attribution for
  these resources.
- The website provides some attribution to the authors of the project (even if
  pseudonymous, such as a link to a GitHub profile).

Two points are given per criteria met, with one point given in the case of a
partially met criterion.

**Points: XX/10**

Grader comments: None.

### Style

Grading is based on the following criteria:

- The website includes a suitable title.
- The website is reasonably well-styled, with appropriate choices of colors,
  font sizes, etc.
- The website is well-structured into sections.
- The website is generally free of spelling and grammatical errors,
  well-written, and easy to follow and understand.
- The website effectively mixes text and other content in its overall
  narrative/flow.

Two points are given per criteria met, with one point given in the case of a
partially met criterion.

**Points: XX/10**

Grader comments: None.

### Website Summary

**Points: XX/20**

## Video (20 Points)

The video presentation is expected to cover the following four items:

1. A description of the project at a level the audience can understand.
2. A description of the project architecture and design at an appropriate level
   of detail.
3. A demonstration (e.g., video, example run) of the software being used.
4. A summary of insights from the project and/or planned future work.

### Story

3: The overall narrative of the project comes across clearly, in an easy to
understand way.

2: The narrative is told in a slightly unclear way (for example, a
feature/detail unconnected to the overall story).

1: The narrative is unclear (for example, a project trying to do multiple
unrelated things).

0: It is not possible to tell what the narrative is from the presentation.

**Points: XX/3**

Grader comments: None.

### Content Curation

3: The presentation includes only the most important points of the project's
goals, design, features, and lessons.

2: The presentation includes the important points listed above, but adds
additional details that distract from the overall story or is missing some minor
aspects of the story.

1: The presentation lacks some important details of the above points, or adds
significant unnecessary details.

0: The presentation lacks many of the important details of the above points.

**Points: XX/3**

Grader comments: None.

### Organization

2: The presentation is well-organized, covering the four points above in order.

1: The presentation is generally well-organized, but has some issues with the
ordering.

0: The presentation is not well-organized.

**Points: XX/2**

Grader comments: None.

### Delivery

3: The presentation is well-delivered and well-practiced.

2: The presentation has some small issues in delivery (e.g., lost train of
thought).

1: The presentation has moderate issues in delivery (e.g., clearly unpracticed
slides).

0: The presentation has significant issues in delivery (e.g., clearly not
familiar with slides in the presentation).

**Points: XX/3**

Grader comments: None.

### Slides

3: The slides complement the words spoken during the presentation.

2: There are some minor issues between the words spoken and the slides (e.g.,
unexplained point or graphic on slides).

1: There are a few significant differences between the words spoken and the
slides shown.

0: The slides have little relation to what is being spoken in the presentation.

**Points: XX/3**

Grader comments: None.

### Timing

3: The presentation finishes within the allotted time of 5 minutes.

In this category, 1 point is subtracted for every 10 seconds over time, up to a
maximum of 18 points lost.

**Points: XX/3**

Grader comments: None.

### Miscellaneous Style

3: Slides contain proper spelling, readable font size/colors, and audio
levels/speed is good.

2: Slides/audio have a minor issue with one of the above.

1: Slides/audio have a major issue with one of the above, or minor issues with
multiple points.

0: Slides/audio have multiple major issues.

**Points: XX/3**

Grader comments: None.

### Presentation Summary

**Points: XX/20**

## Summary

Copy the point totals from each of the four major section summaries above.

**Git: XX/20**

**Implementation: XX/80**

**Website: XX/20**

**Presentation: XX/20**

### Total

**TOTAL POINTS: XX/140**

### Grader Information

_Grader_:
