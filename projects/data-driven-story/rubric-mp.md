# Midterm Project Rubric

Grading criteria for the proposal and check-in are on Canvas.

## Repository (20 Points)

### Organization and Content

Grading is based on the following criteria:

- The repository has an appropriate title.
- The instructors have access to the repository.
- All code files are present.
- All data files are present.
- All other files, including the essay and a `requirements.txt` file, are
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

### Repository Summary

**Points: XX/20**

## Implementation (65 Points)

### Scope

Grading is based on the following criteria:

- The code uses a library or feature not covered in class, such as NumPy, SciPy,
  Pandas (beyond what is covered in class), an API, `requests`, etc.
- The code accesses and/or generates a significant set of data (i.e., does not
  consist of directly downloading one or two files from a static URL with no
  post-processing).
- The code generates visuals in an effective way for the overall narrative
  (i.e., does not plot the data with default settings when a more effective
  visualization is feasible).
- The code demonstrates a significant amount of effort (roughly 2 assignments'
  worth), made clear by factors such as (but not only) the level of new features
  used and the amount of data cleaning and/or processing.

10: The code meets all of the above criteria.

8: The code has minor issues (e.g., one ineffective visual, slightly underscoped
work) in meeting one of the above criteria.

6: The code has minor issues in meeting two of the above criteria, or major
issues (e.g., only directly downloading a few text files) in meeting one of the
above criteria.

4: The code has major issues in two of the above criteria.

0: The code fails to meet any of the above criteria.

**Points: XX/10**

Grader comments: None.

### Correctness

Grading is based on the following criteria:

- The code passes all unit tests.
- When run according to the instructions, the code (1) accesses data on the Web
  or generates a set of data, and (2) downloads and/or processes this data into
  a file.
- When run according to the instructions, the code produces at least three
  substantially different visualizations of the obtained or generated data.

9: The code meets all of the above criteria.

6: The code has major issues with one of the above criteria.

3: The code has major issues with two of the above criteria.

0: The code has major issues with all of the above criteria.

**Points: XX/9**

Grader comments: None.

### Unit Tests

Where possible, a function should have unit tests that can be run to ensure that
the function implementation is correct. Each unit test should be justified with
a comment explaining why that test is there, and for each function, the set of
unit tests should reasonably cover the set of inputs to, and behaviors of, that
function.

Certain functions (e.g., those that access Web data) may not be able to be unit
tested. Where possible and appropriate, parts of a function that can be unit
tested and that stand on their own should be separated into their own functions,
and unit tests for these functions should be included.

9: Each function has unit tests meeting the above criteria, where possible.

7: One or two functions have unit tests with a minor omission in the above
criteria (e.g., unclear comment, forgot to test a small edge case), or a single
function has a docstring with a major omission (e.g., missing comment or forgot
to test a key part of the function behavior).

5: Multiple functions have sets of unit tests with major omissions.

3: A majority of the functions have sets of unit tests with major omissions.

0: No unit tests are present.

**Points: XX/9**

Grader comments: None.

### README

Grading is based on the following criteria:

- The README provides a short summary of the project.
- Where applicable, the README provides instructions for obtaining the necessary
  packages or libraries needed to run the code.
- Where applicable, the README mentions any changes necessary to the code
  required to successfully run it.
- The README provides instructions for obtaining similar or identical data to
  that used in the project.
- The README provides instructions for how to generate plots similar or
  identical to those shown in the project computational essay.

9: The README meets all of the above criteria.

7: The README is unclear or incomplete in one of these areas.

5: The README is unclear or incomplete in multiple areas, or missing one area
entirely.

3: The README is missing multiple areas.

0: The README is missing entirely.

**Points: XX/9**

Grader comments: None.

### Docstrings

Every function should have a well-written docstring that describes what the
function does, any assumptions made, the type and description of each parameter,
and the type and description of the return value.

9: Each function has a docstring matching the above description.

7: One or two functions have docstrings with a minor omission in the above
criteria (e.g., forgot to list a type), or a single function has a docstring
with a major omission (e.g., missing section).

5: Multiple functions have docstrings with major omissions.

3: A majority of the functions have docstrings with major omissions.

0: No docstrings are present.

**Points: XX/9**

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
- Variable names follow the course guidelines for formatting and
  descriptiveness.
- The code consistently uses single or double quotes, except where it would be
  convoluted to write.
- Where needed, there are comments in the code to describe what a block of code
  does (at a high level) or why that code is there.
- The code makes use of features taught in the course, particularly in making
  code more readable (e.g., using f-strings rather than calling `print` on
  multiple arguments).
- The code is well-organized into files as appropriate (e.g., separate files for
  obtaining and visualizing data).
- The code is generally readable and easy to understand.

9: The code meets all of the above criteria.

7: The code has some minor issues with one of the above criteria.

5: The code has minor issues with more than one of the above criteria, or major
issues with one criterion.

3: The code has major issues with more than one the above criteria.

0: None of the criteria above are met.

**Points: XX/9**

Grader comments: None.

### Code Summary

**Points: XX/65**

## Essay

### Research Question

Grading is based on the following criteria:

- The question is clearly stated in the essay.
- The question is well-motivated.
- The question needs quantitative data to be answered.
- The question considers a reasonably realistic scenario (e.g., no comparing
  things that might show up on Spurious Correlations).

Two points are given per criteria met, with one point given in the case of a
partially met criterion.

**Points: XX/8**

Grader comments: None.

### Methodology

Grading is based on the following criteria:

- The essay clearly states what data was collected.
- The essay states where the data is from (including a URL unless the source is
  clear, such as Wikipedia).
- The essay describes how the collected data answers the research question
  posed.
- The essay describes the approach taken to obtain and/or generate the data, and
  write it into a file.
- The essay describes the approach taken to process and visualize the data.

Two points are given per criteria met, with one point given in the case of a
partially met criterion.

**Points: XX/10**

Grader comments: None.

### Results

Grading is based on the following criteria:

- At least three substantially different visualizations are shown.
- Where applicable, each visualization has a title, axis labels, units, and a
  legend.
- Each visualization supports a point made in the text of this section.
- Each visualization is formatted to effectively and appropriately convey
  information (e.g., using a suitable plot type and not using misleading axis
  limits or scales).

Two points are given for the first criterion above, and for the remaining three
criteria, two points are given for each of the three visualizations that would
result in the highest score for this section. For any of these criteria, one
point is given for a partially met criterion.

**Points: XX/20**

Grader comments: None.

### Interpretation

Grading is based on the following criteria:

- The essay draws scientifically sound conclusions from the results.
- The essay describes important insights and lessons from this project.
- The essay addresses any contextual or ethical implications of the project.
- The essay reflects on the project work, addressing difficulties and potential
  future work.

Two points are given per criteria met, with one point given in the case of a
partially met criterion.

**Points: XX/8**

Grader comments: None.

### Style

Grading is based on the following criteria:

- The essay includes a suitable title and the authors' names.
- The essay is well-structured into sections.
- The essay is generally free of spelling and grammatical errors, well-written,
  and easy to follow and understand.
- The essay effectively mixes text, code, and visualizations in its overall
  narrative/flow.

9: The essay meets all of the above criteria.

7: The essay has minor issues (e.g., slightly unclear) in one of the above
criteria.

5: The essay has minor issues in multiple criteria, or major issues (e.g.,
entire question/section was not addressed) in one of the above criteria.

3: The essay has major issues in multiple criteria.

0: The essay does not meet any of the above criteria.

**Points: XX/9**

Grader comments: None.

### Essay Summary

**Points: XX/55**

## Presentation (20 Points)

### Clarity

5: The story told in the project comes across clearly in an easy to understand
way while covering the four components (question, methodology: data colleciton &
processing, results, and interpretation).

4: The four components are all present, but the story is told in a slightly
unclear way (e.g. one subquestion or graph being unconnected to the overall
story).

3: The story is told in a slightly unclear way and one of the four components is
lacking in depth (e.g. the methodology just lists where data was collected from
& not how/through what APIs).

2: The story is either slightly unclear (e.g. answering multiple unconnected
subquestions) or one of the four components is missing entirely.

1: The story is unclear and multiple components are either missing entirely or
lacking in depth.

0: It is not possible to tell the story from the presentation or the four
components are either not covered or are barely included.

**Points: XX/5**

Grader comments: None.

### Content Curation

5: The presentation only includes the most important points of the approach,
results, and interpretation.

4: The presentation includes the important details of the approach, results, or
interpretation, but there are minor details that could be more refined.

3: The presentation includes important details of the approach, results, or
interpretation, but adds additional details that distract from the overall story
or is missing some minor aspects of the story.

2: The presentation lacks some important details of the approach, results, or
interpretation, or adds significant unnecessary details.

1: The presentation lacks major details of the approach, results, or
interpretation, or adds too many distractions.

0: The presentation lacks many of the important details of the approach,
results, or interpretation.

**Points: XX/5**

Grader comments: None.

### Preparation

5: The slides complement the words spoken during the presentation & all students
appear to have equal understanding of the material in the presentation as
demonstrated in Q&A.

4: The slides align with the words spoken during the presentation, but are
either too heavy on text or have unnecessary information/graphics.

3: The general idea of the slides matches the presentation, but there are
missing aspects or parts of the slides that are not spoken through or some of
the students appear unfamiliar with a few of the slides during the presentation
itself or Q&A.

2: The slides have a decent amount of information matching with the
presentation, but there are major parts missing or that are not used. Some of
the students appear unfamiliar with multiple slides.

1: The slides have some content that is remniscent of the project, but the
students do not seem familiar with the presentation material.

0: The presentation does not match the slides at all and most of the team does
not appear to understand what their project was/cannot answer questions
coherently.

**Points: XX/5**

Grader comments: None.

### Performance

5: The presentation is well delivered & finishes within 5 minutes (-1 per 10s
over time; max @ 18).

4: The presentation has some small issues in delivery (e.g., lost train of
thought).

3: The presentation has a few noticable issues in delivery, but is still well
thought out & prepared.

2: The presentation has moderate issues in delivery (e.g., clearly unpracticed
slides).

1: The presentation has significant issues in delivery (e.g., clearly not
familiar with slides in the presentation).

0: The presenters look like they have never seen the presentation slides before.

**Points: XX/5**

Grader comments: None.

### Presentation Summary

**Points: XX/20**

Copy the point totals from each of the four major section summaries above.

**Git: XX/20**

**Implementation: XX/65**

**Essay: XX/55**

**Presentation: XX/20**

### Total

**TOTAL POINTS: XX/160**

### General Grader Comments

_None._

### Grader Information

_Grader_:
