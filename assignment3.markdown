---
layout: default
---
# Assignment 3

**Due Date: Thursday, November 17**

This assignment is divided into two independent parts, as described below.

## Part I.

In this first part of the assignment you'll augment an existing survey dataset and statistically correct for potential sample biases using US Census data.

**Step 1: Data Exploration.** The survey dataset we'll be working with can be found [here](https://raw.githubusercontent.com/fivethirtyeight/data/master/comma-survey/comma-survey.csv). Spend some time exploring the dataset --- which demographic groups are respesented in the data? Is there missingness in the collected data?  Write an Python script (called `survey_analysis.py`) to analyze the responses. Compute and plot the demographic distributions, and analyze the (unadjusted) answers for the substantive questions.

**Step 2: Data Augmentation.** Using Google Forms or Qualtrics, replicate the survey represented in the baseline dataset. Administer this survey to at least 10 additional people -- including the demographic data! Download the responses, and write a Python script `parse_survey.py` to process the downloaded file into a separate `.csv` formatted identically to the original survey dataset. Your script must accept the input file format as command-line argument and write the `.csv` line-by-line to standard out, so that we can replicate your data processing with the command:
```
python3 parse_survey.py YOUR_COLLECTED_DATA_FILE > new_comma_survey.csv
```

**Step 3: Census Data Gathering.** Your survey population does not necessarily match the population demographics of the United States. In order to post-stratify the data on age, sex, income, education, and location, you'll need to gather this information from [US Census MDAT](data.census.gov/mdat). Using the 2021 vintage, construct a table consisting of the relevant categories for your dataset (age, sex, etc.). The MDAT web interface allows you to bin variables, so you can construct the categories which are relevant for the survey data. Having done so, navigate to the Download tab and click the `COPY API TABULATE QUERY` button. (Note: it might also be convenient to bookmark the `COPY BOOKMARK` so that you don't have to redo all of your earlier work to fix a mistake.)

Open the `API TABULATE QUERY` url and save the resulting `.json` file. You will need to construct the mapping between the data labels in the `.json` file and the original categories you selected from the MDAT interface. This can be done manually (if you find an automated way to retrieve this mapping, let us know and we'll update this assignment). 

**Step 4.** Now generate statistically adjusted estimates for your substantive questions by post-stratifying the data on sex, age, race, and education. You'll do this is two steps. First fit multinomial logistic regression models that predict survey responses as a function of the respondent's demographics (use separate models for each substantive question). **REPLACE THIS WITH PYTHON**You can do this with the multinom function in the nnet package. For example, if the question answer is recorded in a column named q1 in a DataFrame named `response_data`, you can do the following:

```
q1_model <- multinom(q1 ~ sex + age + race + education, data=response_data)
```

**Step 5.** Finally, use your fitted models to estimate attitudes for each combination of sex, age, race, and education, and then weight the cell-level estimates by the number of U.S. adults in each cell to generate population-level estimates. To help you do this, we computed the number of people in each cell, based on the 2015 PUMS data from the U.S. Census Bureau. (Note: you can use the predict function to generate cell-level estimates from your model.)


## Part II. 
Identify a plausible natural experiment that could be used to answer a social scientific question of your choice. You do not need to carry out any data analysis, but the natural experiment you describe should be based on a specific instance of as-if randomization that does in fact exist in the real-world. That is, it should be possible in theory to carry out your proposal. What are the assumptions your approach relies on? What are the advantages and limitations of your proposal? Write 1-2 single-spaced pages describing your question and approach.

Submission. Submit the following files: (1) your report (as a PDF file) from Part I of the assignment, which should briefly describe the HITs you completed in Step 1, and detail the results from your survey and your analysis decisions; (2) your survey data (i.e., the CSV file you downloaded from Mechanical Turk); (3) your `survey_analysis.py` script; and (4) your proposal (as a PDF file) from Part II.

Grading rubric. This assignment will be graded on the following criteria:

Part I.
* Survey contains the required demographics.
* Your code is readable and well formatted.
* Correct computation for step 7 and step 8.
* Report should be well written and formated. It should be no longer than 3 pages.
Part II.
* The natural experiment should not be a pre-post (interrupted time-series) analysis, but rather leverage as-if randomization.
* The question should be related to social science.

**Submission instructions:**

We ask that all project files (code and data) be uploaded to Canvas, and that a PDF of the report be uploaded to Gradescope.

To help make sure your team gets the deliverables submitted correctly, here's a project submission checklist:   

1. Write the names of all your group members, and your group number, into the report PDF and at least one of the source code files you submit. This is important to complete, as we may assign individual grades if we see major discrepancies between different parts of the project, so that everyone is treated fairly.
2. Write the names of each group member and which parts of the project they worked on at the top of your project PDF. You can all work on each part or split it up in any way you'd like. For example, you can write: "Person A (report); Person B (`tweet_analysis.py`); Person C: (report)''.
3. Go to the People page on Canvas, hit the Groups tab, and ensure that you're in the right group with the right people. If there's anyone else in your group who you are not working with, please email the TA team or make a private post on Ed so that they can be moved to the right group. We'll be using these groups to assign grades, so it's very important that they're correct.
4. Now, submit all files you made to create your report to the assignment on Canvas. This includes Python scripts, Jupyter notebooks, the submission PDF, etc. Only one person has to submit the files. Your group and its members will automatically be recorded on the submission.
5. Finally, please submit just the report PDF on Gradescope. On Gradescope, the group is not automatically recorded, so you'll have to select your group members when you submit. Only one person has to submit the PDF.

Good luck!

