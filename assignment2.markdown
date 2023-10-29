---
layout: default
---
# Assignment 2

**Due Date: Thursday, November 2, 11:59pm PT **

**Assignment description:**

In this assignment, you\'ll investigate gender
*[homophily](https://en.wikipedia.org/wiki/homophily)*
on Twitter. In the process you\'ll learn about streaming
computation, data manipulation, and plotting. 

**Step 1.**

The Twitter Streaming API provides access to a small
[random](https://developer.twitter.com/en/docs/twitter-api/tweets/volume-streams/introduction)
sample of public tweets as they are generated, and also lets one query
for tweets that
[match](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/introduction)
a user-provided list of keywords (eg. fetch all tweets that contain a specific word. 
you can obtain the stream of all tweets that
contain \"stanford\"). Using these endpoints, we have streamlined the process for you by already streaming the tweets. We've compiled two distinct datasets of tweets which are essential for this assignment. You can access these datasets through the the drive link [here](https://drive.google.com/drive/folders/1MqLfhO-XsWx5v1eHd8NyaYbejcYGyrSY?usp=sharing). Once you've accessed the drive link, download the files to your local system. Ensure that you save them in a location that's easily accessible, as you'll be working with these files for the next steps of the assignment.

`tweets_random.gz` contains ~5.2 million randomly sampled tweets gathered over a span of 24 hours.
`tweets_filtered.gz` contains ~283,000 filtered tweets scraped over 24 hours with the keyword 'queen'.

We selected **"queen"** as the keyword due to its intrinsic association with gender, its prevalent usage in contemporary slang, and the fact that these tweets were collected around the period of Queen Elizabeth II's passing in Sept 2022. Hence, we believe it will show an interesting time trend and gender pattern. 


**Step 2.** Each line of the above files is in JSON,
and before you can analyze the results, you need to convert the data to
a more suitable format. Write a Python script (named `parse_tweets.py`)
that takes a stream of tweets as input ([via
stdin](http://en.wikibooks.org/wiki/Python_Programming/Input_and_Output#Standard_File_Objects)),
and writes tab-separated output (to stdout) where each row corresponds
to a tweet and the four columns of the output are: (1) date; (2) time
rounded to the nearest 15-minute interval (e.g., 18:30); (3) the name of
the user; and (4) the name of the original poster, if the tweet is a
retweet (otherwise \'NA\'). The
[json](https://docs.python.org/3/library/json.html)
module is useful for parsing the input. **Ensure that your script is not
memory intensive (i.e., convert the data in a streaming fashion).**

Your script should run with the following command, writing the results
to stdout:

`zcat tweets.gz | python3 parse_tweets.py`

If `zcat` command fails, try: 
`gzcat tweets.gz | python3 parse_tweets.py`

Using your `parse_tweets.py` script, parse the random sample of tweets
and also the filtered set of tweets, and save them to two separate
files.

Hint: Some entries collected from Twitter might not be \"valid\" (e.g.,
deleted tweets, empty lines), so make sure your `parse_tweets.py` script
deals with theses situations gracefully.

**Step 3.** Import your tweet data into Python. Devise and apply a
(simple) statistical strategy to infer the gender of users based on
their first names. To do so, you may use baby name popularity data
provided by the [Social Security
Administration](http://www.ssa.gov/oact/babynames/limits.html)
(SSA): the
[female](https://github.com/msande231/msande231.github.io/blob/main/assets/hw1/female_names.tsv.gz)
and
[male](https://github.com/msande231/msande231.github.io/blob/main/assets/hw1/male_names.tsv.gz)
datasets give the number of times each name was registered in the United
States, annually, from 1880 to 2013. What are the limitations of your
strategy?

Use [`matplotlib`](https://matplotlib.org/) (again, install with pip)
to plot the volume of tweets over time, with separate lines indicating
the volume by gender (i.e., gender of the user who posted the tweet, not
the gender of the original user). To generate the plot, first compute 
the volume of tweets in each 15-minute interval in your data
(separately by gender).  Make two plots: One for the random sample 
of tweets, and one for the filtered set of tweets.

Do you see evidence of gender *homophily*, in which women retweet women
and men retweet men disproportionately often? Devise a (simple)
statistical strategy to gauge the extent to which this phenomenon may
(or may not) occur in your data.

Save your gender inference, plot generation, and homophily code in a
single script called `tweet_analysis.py`. Your script should be completely
self-contained (e.g., load all necessary libraries), and not contain any
extraneous calculations. In particular, if you run the script in a
directory that contains the tweet data and the baby name files, it
should read in the data and output the plots in that same directory
without any additional setup or user intervention. That is, the
following command (which we will run) must reproduce your results:

`python3 tweet_analysis.py`

Here are a few suggestions for making plots in matplotlib. First, use a white
background. Second, format plot labels (e.g., numbers). Third, for reports, 
save plots in PDF (a [vector format](https://en.wikipedia.org/wiki/Vector_graphics))
rather than PNG or JPEG ([raster](https://en.wikipedia.org/wiki/Raster_graphics)
formats). Finally, explicitly set the height and width of plots to get
the appropriate aspect ratio (this also has the added benefit of helping
to ensure the axis labels are appropriately sized). For example, for a
square plot you might use something like this to set an x inch by y inch size:
```
import matplotlib.pyplot as plt
...
plt.figure(figsize=(x,y))
```
See also the [`matplotlib` documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html) for `plt.figure`.

**Step 4.** Prepare a short report (2-page maximum) detailing your
results. The report should include a description of your approach to
inferring gender, your strategy for measuring gender homophily, and the
two plots you generated. Brief describe your conclusions and discuss
limitations of the methodology. The report is an important component of
the assignment; we will be grading both the substantive content as well
as the writing and presentation style.

Submit the following: (1) `parse_tweets.py`; (2) `tweet_analysis.py`;
(3) the two files generated in Step 4 (i.e., the cleaned tweet data);
and (4) your report, as a single PDF file.

We will run diagnostic tests on your code. You can assume that we will
run your code in a directory that contains *female\_names.tsv.gz* and
*male\_names.tsv.gz*, so please ensure your scripts load those files
from the local directory.

**Grading rubric.** This assignment will be graded on the following
criteria:

-   Correct stream parsing of the raw tweet data; the data *must not* be
loaded into memory in its entirety
-   Suitability of your strategies for inferring gender and gender
homophily
-   Effectiveness of your plots: they must be clean and legible, with
appropriate axis names, coloring, etc. 
-   Quality of the report, which should focus on clearly communicating
findings, insights, and limitations

**Submission instructions:**

We ask that all project files (code and data) be uploaded to Canvas, and that a PDF of the report be uploaded to Gradescope.

To help make sure your team gets the deliverables submitted correctly, here's a project submission checklist:   

1. Write the names of all your group members into the report PDF and at least one of the source code files you submit. 
2. Write the names of each group member and which parts of the project they worked on at the top of your project PDF. You can all work on each part or split it up in any way you'd like. For example, you can write: "Person A (report); Person B (`tweet_analysis.py`); Person C: (report)''.
3. Go to the People page on Canvas, hit the Groups tab, and ensure that you're in the right group with the right people. If there's anyone else in your group who you are not working with, please email the TA team or make a private post on Ed so that they can be moved to the right group. We'll be using these groups to assign grades, so it's very important that they're correct.
4. Now, submit all files you made to create your report to the assignment on Canvas. This includes Python scripts, Jupyter notebooks, the submission PDF, etc. Only one person has to submit the files. Your group and its members will automatically be recorded on the submission.
5. Finally, please submit just the report PDF on Gradescope. On Gradescope, the group is not automatically recorded, so you'll have to select your group members when you submit. Only one person has to submit the PDF.

Good luck!

