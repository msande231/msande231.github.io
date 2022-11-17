---
layout: default
---
# Assignment 3

**Due Date: Thursday November 17th at 11:59pm**

This assignment is divided into two independent parts, as described below.

## Part I.

In this first part of the assignment you'll augment an existing survey dataset and statistically correct for potential sample biases using US Census data.

**Step 1: Data Exploration.** The survey dataset we'll be working with can be found [here](https://raw.githubusercontent.com/fivethirtyeight/data/master/comma-survey/comma-survey.csv). Spend some time exploring the dataset --- which demographic groups are respesented in the data? Is there missingness in the collected data?  Write a Python script (called `survey_analysis.py`) to analyze the responses. Compute and plot the demographic distributions, and analyze the (unadjusted) answers for the substantive questions.

**Step 2: Data Augmentation.** Using Google Forms or Qualtrics, replicate the survey represented in the baseline dataset. Administer this survey to at least 10 additional people -- including the demographic data! Note: poll for Sex instead of Gender to ensure your results line up with the available US Census data as well as the assignment survey dataset. Process the downloaded file into a separate `.csv` formatted identically to the original survey dataset named `new_comma_survey.csv` in whatever way you deem best (dataframe manipulation with `pandas`, processing answers line-by-line, etc.).

**Step 3: Post-stratification I** Now generate statistically adjusted estimates for the survey questions by post-stratifying the data on sex, age, income, education, and location. You'll do this in two steps. First, create a script `survey_poststrat.py` that fits multinomial logistic regression models that predict survey responses as a function of the respondent's demographics (use separate models for each substantive question). You can do this with `sklearn` using `sklearn.linear_model.LogisticRegression` with `multi_class='multinomial'`. Train a separate model for each response variable, e.g.

```
from sklearn.linear_model import LogisticRegression
...
lr = LogisticRegression(multi_class='multinomial', ...)
q1_model = lr.fit(X_demographics, y_q1)
```

Ensure that you preprocess the data properly before training; you'll find the classes of `sklearn.preprocessing` quite useful in this regard. Be sure to combine your `new_comma_survey.csv` data with `comma_survey.csv` when fitting the logistic regressions as well.

**Step 4: Census Data Gathering.** Your survey population does not necessarily match the population demographics of the United States. In order to post-stratify the data on age, sex, income, education, and location, you'll need to gather this information from [US Census MDAT](https://data.census.gov/mdat). Using the 2021 vintage, construct a table consisting of the relevant categories for your dataset (age, sex, etc.). The MDAT web interface allows you to bin variables, so you can construct the categories which are relevant for the survey data. Make sure to gather "counts" instead of Having done so, navigate to the Download tab and click the `COPY API TABULATE QUERY` button. (Note: it might also be convenient to bookmark the `COPY BOOKMARK` so that you don't have to redo all of your earlier work to fix a mistake.) Include this URL in your report.

Open the `API TABULATE QUERY` url and save the resulting `.json` file. You will need to construct the mapping between the data labels in the `.json` file and the original categories you selected from the MDAT interface. This can be done manually (if you find an automated way to retrieve this mapping, let us know and we'll update this assignment). Load the census counts

**Step 5: Post-stratification II** Finally, use your fitted models to estimate attitudes for each combination of sex, age, education, and location, and then weight the cell-level estimates by the number of U.S. adults in each cell you collected in Step 4 to generate population-level estimates. (Note: you can use the `sklearn.linear_model.LogisticRegression.predict_proba` function to generate cell-level estimates from your model.) Include your code for this in `survey-poststrat.py`. Hint: you might consider using [itertools](https://docs.python.org/3/library/itertools.html) to generate the possible cells as part of this task.

Please include your final population-level estimates in the report, along with a brief description of how your post-stratified estimates differ from what you would have estimated directly from the data using sample means.

## Part II. 

Let us consider two papers not discussed in the course. [Michel et al. (2011)](https://www.science.org/doi/epdf/10.1126/science.1199644) analyzed a corpus of five million books to quantitatively study cultural trends. [White et al. (2012)](https://academic.oup.com/jamia/article-pdf/20/3/404/17374497/20-3-404.pdf) mined web search queries to detect drug-drug interactions. If you had access to the full digitized text of every book ever written and/or the full log of search queries, what scientific questions would you ask? Write a short, 1 page (single-spaced) proposal defining your question and how you think one of these datasets would help answer it. Be sure to discuss the benefits and downsides of such data sources over traditional data sources or experiments for answering the scientific question(s) you propose.

**Submission.** Submit the following files: (1) your report (as a PDF file) from Part I of the assignment, which shoul detail the results from your survey and your analysis decisions; (2) your processed survey data `new_comma_survey.csv`; (3) your `survey_analysis.py` script; and (4) your proposal (as a PDF) from Part II.

**Grading rubric.** This assignment will be graded on the following criteria:

Part I.
* You explored the unadjusted base survey data.
* You augmented the survey data and used this data in the rest of the assignment.
* You correctly gathered census data using appropriate cells.
* Correct computation for step 3 and step 5.
* CSV of post-stratified attitudes and summary for the report.
* Your code is readable and well formatted.
* Report should be well written and formated. It should be no longer than 3 pages.

Part II.
* The questions you pose regarding books or search queries are thoughtful and attainable.
* Your analysis of the benefits / downsides of the posited sources is plausible.

**Submission instructions:**

We ask that all project files (code and data) be uploaded to Canvas, and that a PDF of the report be uploaded to Gradescope.

To help make sure your team gets the deliverables submitted correctly, here's a project submission checklist:   

1. Write the names of all your group members, and your group number, into the report PDF and at least one of the source code files you submit. This is important to complete, as we may assign individual grades if we see major discrepancies between different parts of the project, so that everyone is treated fairly.
2. Write the names of each group member and which parts of the project they worked on at the top of your project PDF. You can all work on each part or split it up in any way you'd like. For example, you can write: "Person A (report); Person B (`survey_analysis.py`); Person C: (report)''.
3. Go to the People page on Canvas, hit the Groups tab, and ensure that you're in the right group with the right people. If there's anyone else in your group who you are not working with, please email the TA team or make a private post on Ed so that they can be moved to the right group. We'll be using these groups to assign grades, so it's very important that they're correct.
4. Now, submit all files you made to create your report to the assignment on Canvas. This includes Python scripts, Jupyter notebooks, the submission PDF, etc. Only one person has to submit the files. Your group and its members will automatically be recorded on the submission.
5. Finally, please submit just the report PDF on Gradescope. On Gradescope, the group is not automatically recorded, so you'll have to select your group members when you submit. Only one person has to submit the PDF.

Good luck!

