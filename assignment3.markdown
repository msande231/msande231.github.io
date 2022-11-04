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

## Setting up FarmShare:

To use the following instructions in the assignment description below, you will have to set up your FarmShare machine with a newer version of Python than is currently supported on FarmShare out of the box.

**Option 1: Use `pyenv` (RECOMMENDED)**

This is the most elegant solution. SSH into FarmShare and from your home directory, install `pyenv` with:
```
curl https://pyenv.run | bash
```
Once this finishes, add the lines your `.bashrc` that the `pyenv` install script suggests to make your life easier in the future. Then install Python 3.7.14 (it is important that you install a 3.7.x version, or else you might run into issues with the old version of openssl running on FarmShare). 
```
pyenv install -v 3.7.14
```
Navigate to your project directory. Assuming you cloned it to your home directory from the course repo without changing the name: `cd mse231_f22`. From this directory, run
```
pyenv local 3.7.14
```
to configure `pyenv` to use Python 3.7.14 for the course repository. To test that it is working, you should run `python --version` and observe `Python 3.7.14`. Install `tweepy` with
```
pip install tweepy
```
and you'll be ready to start the assignment! Many thanks to Daniel Jenson for [suggesting this on Ed](https://edstem.org/us/courses/30212/discussion/1869524).

**Option 2: Use the setup script from the course repo**

_If you skip this step, the following steps of Option 2 will not work._ In the [course repo](https://github.com/mse231/mse231_f22) there is a script called `farmshare-setup.sh`. Please clone the course repo onto your FarmShare home directory (which is the default directory you enter when you SSH into FarmShare, e.g. `/home/your_user_name`). Copy `farmshare-setup.sh` into this FarmShare home directory from the cloned repo directory. Then enter the following commands:
1. `cd ~`
2. `chmod +x farmshare-setup.sh`
3. `tmux` (a new pane in the terminal will open when you execute this command; that's normal)
4. `./farmshare-setup.sh`
5. `exit`

Step #4 above will take roughly 20 minutes as a large volume of output is written to the screen. If you get disconnected from the server during this time, please reconnect via SSH and enter the command `tmux a -t 0` to be brought back to the executing setup process. When you see "DONE" printed to the terminal and are returned to the command prompt, you can safely exit tmux and continue with the below instructions.

**Assignment description:**

In this assignment, you\'ll investigate gender
*[homophily](https://en.wikipedia.org/wiki/homophily)*
on Twitter. In the process you\'ll learn about APIs, streaming
computation, data manipulation, and plotting. While it is possible to
complete this assignment entirely on a local machine (e.g., your
personal laptop), we *highly* recommend setting up a remote server. If
you don\'t already have a remote server setup, you can always use
[Stanford
Farmshare](https://web.stanford.edu/group/farmshare/cgi-bin/wiki/index.php/User_Guide) (additional information [here](https://uit.stanford.edu/service/sharedcomputing)). If you
are using your own setup, make sure you that you can use a recent (3.5+) 
version of Python with [pip](https://pip.pypa.io/en/stable/installation/) installed.
There are a number of things that can go wrong in this assignment, so please start early!

**Step 1.** The Twitter Streaming API provides access to a small
[random](https://developer.twitter.com/en/docs/twitter-api/tweets/volume-streams/introduction)
sample of public tweets as they are generated, and also lets one query
for tweets that
[match](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/introduction)
a user-provided list of keywords. We will use both of these features.

To get started,
[create](https://developer.twitter.com/en/apps)
a Twitter application that you\'ll use to access the API. (In order to
create the application, you may need to first
[apply](https://developer.twitter.com/en/apply-for-access)
for a developer account; your account only needs permission to analyze
tweets, not send tweets.) The application will only be used by you, so
what you enter for the name, description and website are not terribly
important.

After creating your application, select the \"keys and tokens\" tab, and
then create an access token. You\'ll need to save five pieces of
information from this page: the API key, API secret key, access token,
access token secret, and the bearer token. If you need to access or update your
application information at a later data, you can return to it via the
[management
console](https://developer.twitter.com/en/apps).

**Step 2.** Install
[Tweepy](https://github.com/tweepy/tweepy),
a Python wrapper for the Twitter API. The easiest way to install it is
with pip, using the \"\--user\" option to install to your home
directory:

`pip3 install --user tweepy`

**Step 3.** To help you get started with Tweepy and the Twitter
Streaming API, we wrote a short Python script,
[tweet\_stream.py](https://github.com/mse231/mse231_f22/blob/main/assignment1/tweet_stream.py). The script requires that you
create a file with your API credentials in [this
format](https://github.com/mse231/mse231_f22/blob/main/assignment1/creds.txt), where you replace the parameters with your
own credentials. (For example, replace `<YOUR_API_KEY>` with your
actual API key.) Assuming you save the file as creds.txt in your working
directory, you can run the script with the command:

`python3 tweet_stream.py --keyfile creds.txt`

Enter
[Control-C](https://en.wikipedia.org/wiki/Control-C)
to terminate the script. The output of the above call is a near
real-time
[JSON](https://en.wikipedia.org/wiki/JSON)
stream of randomly selected tweets. To save the results, you can
redirect the output to a file like this:

`python3 tweet_stream.py --keyfile creds.txt > tweets`

However, as the API returns a fair amount of data, it\'s more efficient
to store a compressed version of the data. The script lets you store a
[gzipped](https://en.wikipedia.org/wiki/Gzip)
version of the results as follows:

`python3 tweet_stream.py --keyfile creds.txt --gzip tweets.gz`

You can view the compressed data with
[zless](http://linux.die.net/man/1/zless),
[zcat](http://linux.die.net/man/1/zcat),
or similar utilities (e.g., gzcat on OS X).

In addition to simply returning a random sample of tweets, the Twitter
API lets you fetch all tweets that contain a specific word. For example,
via `tweet_stream.py`, you can obtain the stream of all tweets that
contain \"stanford\" (where the matching is case-insensitive) with the
command:

`python3 tweet_stream.py --keyfile creds.txt --filter stanford`

(The API limits the number of results it will return, so if your filter
term is too common, you\'ll only get a subset of the tweets.)

After playing with the API, start collecting a random sample of tweets,
and also collect a filtered set of tweets matching a term of your
choosing. Select a term that you believe will show an interesting time
trend and gender pattern. Collect at least 24 hours worth of tweets. To
prevent your command from terminating when you disconnect from the
session, you can use a utility such as
[tmux](http://en.wikipedia.org/wiki/Tmux)
or
[nohup](http://en.wikipedia.org/wiki/Nohup).
For example, with nohup, you can run the command in the background with:

`nohup python3 tweet_stream.py --keyfile creds.txt --gzip tweets.gz &`

Generally, we recommend using tmux, as it offers greater flexibility
and is consistently useful for running processes on remote servers. You
can visit [this tmux commands cheat sheet](https://tmuxguide.readthedocs.io/en/latest/tmux/tmux.html)
for basic usage information, or find several tutorial videos on YouTube.

Note that you are only allowed to connect to at most one streaming API
endpoint at a time, and attempting to connect to more than one
simultaneously may result in some of the streams being terminated.
However, your teammates can each use their own credentials to poll the
API in parallel.

To terminate a script that's running in the background, first find its
[process
ID](https://en.wikipedia.org/wiki/Process_identifier)
with:

`ps -u<user-id>`

where you replace \<user-id\> with your actual user ID. Then kill it
with:

`kill <pid>`

where \<pid\> is the process ID you found with ps.

When using [Stanford Farmshare
machines](https://web.stanford.edu/group/farmshare/cgi-bin/wiki/index.php/Main_Page),
there are a couple things to be aware of: (1) Farmshare machines have
regular maintenance, and may shut down for a scheduled period of time;
regularly check the [system
status](https://web.stanford.edu/group/farmshare/cgi-bin/wiki/index.php/Main_Page#System_Status)
for scheduled maintenance/service outages. (2) ssh\'ing into
rice.stanford.edu will redirect you to a specific machine (e.g.,
rice*11*.stanford.edu) depending on load. When you start your process,
it will be running on that *specific* machine, so to return to it later
you\'ll need to keep track of the machine and then directly ssh into it.

**Step 4.** Each line of the output from the above commands is in JSON,
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

Using your `parse_tweets.py` script, parse the random sample of tweets
and also the filtered set of tweets, and save them to two separate
files.

Hint: Some entries collected from Twitter might not be \"valid\" (e.g.,
deleted tweets, empty lines), so make sure your `parse_tweets.py` script
deals with theses situations gracefully.

**Step 5.** Import your tweet data into Python. Devise and apply a
(simple) statistical strategy to infer the gender of users based on
their first names. To do so, you may use baby name popularity data
provided by the [Social Security
Administration](http://www.ssa.gov/oact/babynames/limits.html)
(SSA): the
[female](/assets/hw1/female_names.tsv.gz)
and
[male](/assets/hw1/male_names.tsv.gz)
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

**Step 6.** Prepare a short report (2-page maximum) detailing your
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

-   Coverage of tweets collected (at least 24 hours)
-   Correct stream parsing of the raw tweet data; the data *must not* be
loaded into memory in its entirety
-   Appropriateness of your strategies for inferring gender and gender
homophily
-   Effectiveness of your plots: they must be clean and legible, with
appropriate axis names, coloring, etc. 
-   Quality of the report, which should focus on clearly communicating
findings, insights, and limitations

Please submit your work on Canvas (only one submission per group), and
ensure that all team members are listed on your report.

