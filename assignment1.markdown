---
layout: default
---
# Assignment 1

In this assignment, you\'ll investigate gender
*[homophily](https://en.wikipedia.org/wiki/homophily)*
on Twitter. In the process you\'ll learn about APIs, streaming
computation, data manipulation, and plotting. While it is possible to
complete this assignment entirely on a local machine (e.g., your
personal laptop), we *highly* recommend setting up a remote server. If
you don\'t already have a remote server setup, you can always use
[Stanford
Farmshare](https://web.stanford.edu/group/farmshare/cgi-bin/wiki/index.php/User_Guide) (additional information [here](https://uit.stanford.edu/service/sharedcomputing)). 
There are a number of things that can go wrong in this assignment, so
please start early!

**Step 1.** The Twitter Streaming API provides access to a small
[random](https://developer.twitter.com/en/docs/tweets/sample-realtime/overview/GET_statuse_sample)
sample of public tweets as they are generated, and also lets one query
for tweets that
[match](https://developer.twitter.com/en/docs/tweets/filter-realtime/overview)
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
[tweet\_stream.py](http://www.github.com/mse231/mse231_f22/assignment1/tweet_stream.py). The script requires that you
create a file with your API credentials in [this
format](https://github.com/mse231/mse231_f22/blob/main/assignment1/creds.txt), where you replace the parameters with your
own credentials. (For example, replace \<YOUR\_API\_KEY\> with your
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
[zless](https://web.archive.org/web/20210413060501/http://linux.die.net/man/1/zless),
[zcat](https://web.archive.org/web/20210413060501/http://linux.die.net/man/1/zcat),
or similar utilities (e.g., gzcat on OS X).

In addition to simply returning a random sample of tweets, the Twitter
API lets you fetch all tweets that contain a specific word. For example,
via tweet\_stream.py, you can obtain the stream of all tweets that
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
[tmux](https://web.archive.org/web/20210413060501/http://en.wikipedia.org/wiki/Tmux)
or
[nohup](https://web.archive.org/web/20210413060501/http://en.wikipedia.org/wiki/Nohup).
For example, with nohup, you can run the command in the background with:

`nohup python3 tweet_stream.py --keyfile creds.txt --gzip tweets.gz &`

Note that you are only allowed to connect to at most one streaming API
endpoint at a time, and attempting to connect to more than one
simultaneously may result in some of the streams being terminated.
However, your teammates can each use their own credentials to poll the
API in parallel.

To terminate a script that\'s running in the background, first find its
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
a more suitable format. Write a Python script (named parse\_tweets.py)
that takes a stream of tweets as input ([via
stdin](https://web.archive.org/web/20210413060501/http://en.wikibooks.org/wiki/Python_Programming/Input_and_Output#Standard_File_Objects)),
and writes tab-separated output (to stdout) where each row corresponds
to a tweet and the four columns of the output are: (1) date; (2) time
rounded to the nearest 15-minute interval (e.g., 18:30); (3) the name of
the user; and (4) the name of the original poster, if the tweet is a
retweet (otherwise \'NA\'). The
[json](https://docs.python.org/2/library/json.html)
module is useful for parsing the input. **Ensure that your script is not
memory intensive (i.e., convert the data in a streaming fashion).**

Your script should run with the following command, writing the results
to stdout:

`zcat tweets.gz | python3 parse_tweets.py`

Using your parse\_tweets.py script, parse the random sample of tweets
and also the filtered set of tweets, and save them to two separate
files.

Hint: Some entries collected from Twitter might not be \"valid\" (e.g.,
deleted tweets, empty lines), so make sure your parse\_tweets.py script
deals with theses situations gracefully.

**Step 5.** Import your tweet data into R. You may need to set
`quote = ''`{style="display: inline; padding: 2px; background-color:gainsboro"}
in
[read\_tsv](https://www.rdocumentation.org/packages/readr/versions/1.3.1/topics/read_delim)
to ignore quotes that may appear in user names. Devise and apply a
(simple) statistical strategy to infer the gender of users based on
their first names. To do so, you may use baby name popularity data
provided by the [Social Security
Administration](https://web.archive.org/web/20210413060501/http://www.ssa.gov/oact/babynames/limits.html)
(SSA): the
[female](/web/20210413060501/https://5harad.com/mse125/assets/hw1/female_names.tsv.gz)
and
[male](/web/20210413060501/https://5harad.com/mse125/assets/hw1/male_names.tsv.gz)
datasets give the number of times each name was registered in the United
States, annually, from 1880 to 2013. What are the limitations of your
strategy? P

Use
[ggplot2](https://ggplot2.tidyverse.org/)
to plot the volume of tweets over time, with separate lines indicating
the volume by gender (i.e., gender of the user who posted the tweet, not
the gender of the original user). To generate the plot, first use
[dplyr](https://dplyr.tidyverse.org/)
to compute the volume of tweets in each 15-minute interval in your data
(separately by gender). You can use both ggplot2 and dplyr via the
single
[tidyverse](https://www.tidyverse.org/)
package in R. Make two plots: One for the random sample of tweets, and
one for the filtered set of tweets.

Do you see evidence of gender *homophily*, in which women retweet women
and men retweet men disproportionately often? Devise a (simple)
statistical strategy to gauge the extent to which this phenomenon may
(or may not) occur in your data.

Save your gender inference, plot generation, and homophily code in a
single script called tweet\_analysis.R. Your script should be completely
self-contained (e.g., load all necessary libraries), and not contain any
extraneous calculations. In particular, if you run the script in a
directory that contains the tweet data and the baby name files, it
should read in the data and output the plots in that same directory
without any additional setup or user intervention. That is, the
following command (which we will run) must reproduce your results:

`Rscript tweet_analysis.R`

Alternatively, you can write your report in
[Rmarkdown](https://web.archive.org/web/20210413060501/http://rmarkdown.rstudio.com/),
in which case you must make sure the markdown file compiles, i.e., the
following command must generate the final output:

`Rscript -e "rmarkdown::render('tweet_analysis.Rmd')"`

Here are a few suggestions for making plots in R. First, use a white
background (the default is gray), which you can produce by setting the
appropriate ggplot2 theme at the top of your script:

`theme_set(theme_bw())`

Second, use the
[scales](https://cran.r-project.org/web/packages/scales/scales.pdf)
package (also installed with tidyverse, but loaded separately) to format
plot labels (e.g., to format numbers). Third, for reports, save plots in
PDF (a [vector
format](https://en.wikipedia.org/wiki/Vector_graphics))
rather than PNG or JPEG
([raster](https://en.wikipedia.org/wiki/Raster_graphics)
formats). Finally, explicitly set the height and width of plots to get
the appropriate aspect ratio (this also has the added benefit of helping
to ensure the axis labels are appropriately sized). For example, for a
square plot you might use something like this:

`ggsave(plot=my_plot, file="my_plot.pdf", width=5, height=5)`

**Step 6.** Prepare a short report (2-page maximum) detailing your
results. The report should include a description of your approach to
inferring gender, your strategy for measuring gender homophily, and the
two plots you generated. Brief describe your conclusions and discuss
limitations of the methodology. The report is an important component of
the assignment; we will be grading both the substantive content as well
as the writing and presentation style.

Submit the following: (1) parse\_tweets.py; (2) tweet\_analysis.R(md);
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
appropriate axis names, coloring, etc. that emphasize findings, with
lessons from the visualization lecture kept in mind
-   Quality of the report, which should focus on clearly communicating
findings, insights, and limitations

Please submit your work on Canvas (only one submission per group), and
ensure that all team members are listed on your report.

