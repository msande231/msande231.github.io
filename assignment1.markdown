---
layout: default
---
# Assignment 1

**Due Date: Tuesday October 17, 11:59p PT**

This assignment is divided into two independent parts, as described below.

## Part I.

In this first part of the assignment you'll augment an existing survey dataset and statistically correct for potential sample biases using US Census data. You'll also probe the extent to which LLMs have sensible notions of a "population". 

**Step 1: Data Exploration.** The survey dataset `comma_survey.csv` we'll be working with can be found [here](https://raw.githubusercontent.com/fivethirtyeight/data/master/comma-survey/comma-survey.csv). Spend some time exploring the dataset --- which demographic groups are respesented in the data? Is there missingness in the collected data?  Write a Python script (called `survey_analysis.py`) to analyze the responses. Compute and plot the demographic distributions, and analyze the (unadjusted) answers for the substantive questions.

**Step 2: LLM Survey responses.** Using the OpenAI GPT API, administer the above survey to an "in silico" population that corresponds to the above baseline dataset. Select demographic attributes for the survey participants from the provided file, and collect survey responses from the OpenAI GPT API. Note: poll for Sex instead of Gender to ensure your results line up with the available US Census data as well as the assignment survey dataset.

Create an OpenAI account and API key [here](https://platform.openai.com/account/api-keys). Be sure to check the billing and rate limits [here](https://openai.com/pricing) and [here](https://platform.openai.com/account/rate-limits). Please be sure to set a conservative ``usage limit' on the OpenAI [billing page](https://platform.openai.com/account/billing/overview). This assignment should not cost more than $15 to complete. Setting a limit of $10 is a good starting point, to make sure that you don't accidentally run a loop of queries for much longer than intended. 

We have provided a starter code [here](https://github.com/msande231/msande231.github.io/blob/main/assets/hw1/gpt_prompt_starter.py) to query openAI's API. Before running your survey for the full in silico population, explore a few variations in the prompt construction (you can also explore with chatGPT) to see how changes in the prompt changes the distribution responses. If you prefer to work with another LLM (either an OpenAI model other than text-davinci-002, or some other model entirely) that is fine, just document it in your submission.

Process the LLM responses into a separate `.csv` formatted identically to the original survey dataset named `gpt_comma_survey.csv` in whatever way you deem best (dataframe manipulation with [pandas](https://pandas.pydata.org), processing answers line-by-line, etc.).

**Step 3: Post-stratification I on Baseline Data** Now generate statistically adjusted estimates for the survey questions by post-stratifying the data on sex, age, income, education, and location. You'll do this in two steps. First, create a script `survey_poststrat.py` that fits multinomial logistic regression models that predict survey responses as a function of the respondent demographics in `comma_survey.csv` (use separate models for each substantive question).

You can do this with `sklearn` using `sklearn.linear_model.LogisticRegression` with `multi_class='multinomial'`. Train a separate model for each response variable, e.g.

```
from sklearn.linear_model import LogisticRegression
...
lr = LogisticRegression(multi_class='multinomial', ...)
q1_model = lr.fit(X_demographics, y_q1)
```

Ensure that you preprocess the data properly before training; you'll find the classes of `sklearn.preprocessing` quite useful in this regard.

**Step 4: Post-stratification I on LLM Data** Repeat the above step (Step 3), but this time using the LLM data `gpt_comma_survey.csv`. obtained in Step 2. 

**Step 5: Census Data Gathering.** Your survey population does not necessarily match the population demographics of the United States. In order to post-stratify the data on age, sex, income, education, and location, you'll need to gather this information from [US Census MDAT](https://data.census.gov/mdat). Using the 2021 vintage, construct a table consisting of the relevant categories for your dataset (age, sex, etc.). The MDAT web interface allows you to bin variables, so you can construct the categories which are relevant for the survey data. Make sure to gather "counts". Having done so, navigate to the Download tab and click the `COPY API TABULATE QUERY` button. (Note: it might also be convenient to bookmark the `COPY BOOKMARK` so that you don't have to redo all of your earlier work to fix a mistake.) Include this URL in your report.

Open the `API TABULATE QUERY` url and save the resulting `.json` file. You will need to construct the mapping between the data labels in the `.json` file and the original categories you selected from the MDAT interface. This can be done manually (if you find an automated way to retrieve this mapping, let us know and we'll update this assignment). Load the census counts.

**Step 6: Post-stratification II - Baseline and GPT Data** The objective is to perform post-stratification for each population (baseline dataset and GPT dataset), aligning it with the demographics of the US census population. For this, for each population, use your fitted models to estimate attitudes for each combination of sex, age, education, and location, and then weight the cell-level estimates by the number of U.S. adults in each cell you collected in Step 5 to generate population-level estimates. (Note: you can use the `sklearn.linear_model.LogisticRegression.predict_proba` function to generate cell-level estimates from your model.) Include your code for this in `survey-poststrat.py`. Hint: you might consider using [itertools](https://docs.python.org/3/library/itertools.html) to generate the possible cells as part of this task.

Please include your final population-level estimates in the report, along with a brief description of how your post-stratified estimates differ from what you would have estimated directly from the data using sample means.

**Step 7: Validation Survey for Census Population** Administer the survey to an "in silico" sample of the U.S. census population, matching the size of the earlier data sample, but now with the demographics representing the U.S. census. Obtain responses using OpenAI API with the same prompt structure (but different demographics) and process them similarly to earlier repsonses. 

**Step 8: Discussion** Discuss how responses differ between (i) the raw human survey responses, (ii) the GPT in silico responses for the initial population demographics, (iii) the post-stratified estimates for the human population, (iv) the post-stratified estimates for the in silico population, and (v) the GPT in silico responses for the census population. Comparing (i) and (iii) are the traditional comparison of pre vs. post-stratification. Comparing (ii), (iv), and (v) is an interesting inspection of the internals of modern LLMs.

Incase you're curious and want to read more about the  538 story that the survey data comes from, here's the [link](https://fivethirtyeight.com/features/elitist-superfluous-or-popular-we-polled-americans-on-the-oxford-comma/).


## Part II. 

Let us consider two papers not discussed in the course. [Michel et al. (2011)](https://www.science.org/doi/epdf/10.1126/science.1199644) analyzed a corpus of five million books to quantitatively study cultural trends. [White et al. (2012)](https://academic.oup.com/jamia/article-pdf/20/3/404/17374497/20-3-404.pdf) mined web search queries to detect drug-drug interactions. If you had access to the full digitized text of every book ever written and/or the full log of search queries, what scientific questions would you ask? Write a short, 1 page (single-spaced) proposal defining your question and how you think one of these datasets would help answer it. Be sure to discuss the benefits and downsides of such data sources over traditional data sources or experiments for answering the scientific question(s) you propose.

**Submission.** Submit the following files: (1) your report (as a PDF file) from Part I of the assignment, which should detail the results from your survey and your analysis decisions; (2) your processed survey data `gpt_comma_survey.csv`; (3) your `survey_analysis.py` and `survey_poststrat.py` scripts; and (4) your proposal (as a PDF) from Part II.

**Grading rubric.** This assignment will be graded on the following criteria:

Part I.
* You explored the unadjusted base survey data.
* You succesfully collected LLM responses and used this data in the rest of the assignment.
* You correctly gathered census data using appropriate cells.
* Correct computation for step 3, step 4 and step 6.
* CSV of post-stratified attitudes and summary for the report.
* Your code is readable and well formatted.
* Report should be well written and formated. It should ideally be no longer than 4 pages.

Part II.
* The questions you pose regarding books or search queries are thoughtful and attainable.
* Your analysis of the benefits / downsides of the posited sources is plausible.

**Submission instructions:**

We ask that all project files (code and data) be uploaded to Canvas, and that a PDF of the report be uploaded to Gradescope.

To help make sure your team gets the deliverables submitted correctly, here's a project submission checklist:   

1. Write the names of all your group members, and your group number, into the report PDF and at least one of the source code files you submit. This is important to complete.

2. Go to the People page on Canvas, hit the Groups tab, and ensure that you're in the right group with the right people. If there's anyone else in your group who you are not working with, please email the TA team or make a private post on Ed so that they can be moved to the right group. We'll be using these groups to assign grades, so it's very important that they're correct.

3. Now, submit all files you made to create your report to the assignment on Canvas. This includes Python scripts, Jupyter notebooks, the submission PDF, etc. Only one person has to submit the files. Your group and its members will automatically be recorded on the submission.

4. Finally, please submit just the report PDF on Gradescope. On Gradescope, the group is not automatically recorded, so you'll have to select your group members when you submit. Only one person has to submit the PDF.

Good luck!