---
layout: default
---
# Assignment 2

## Twitter Conversation Analysis

**Due Date: November 3, 2022, 11:59pm**

A reminder: you must complete this assignment in a group of 2--3. Submission instructions are included below.

In this assignment, you will build on your experience collecting Twitter data in PS1 to investigate the structural differences between Twitter conversations prompted by Democrat vs. Republican members of the United States Congress. 

Every time a Twitter user posts a tweet, other users can reply to it, then others can reply to the reply, and so on, leaving behind a structural signature of how the conversation proceeded. 

We will consider two ways of representing the structure of Twitter conversations: reply trees and reply graphs.

- The *reply trees* encode the relationship between individual tweets. The root node is the tweet that started the conversation, the descendant nodes are the replies, and one tweet is connected to another if it is posted in reply to it. Each tweet is a reply to only one other tweet, but a tweet may have multiple replies, forming a reply tree as the one described above. 

- The *reply graphs* are user-centric views of the conversations, where each node represents a user who participated in the conversation, and one node is connected to another if they replied to one of their tweets. (This definition describes an unweighted directed graph, but you are free to consider other definitions of the graph that may be useful in computing informative aggregate statistics describing the conversation, e.g., adding weights or ignoring the direction of the edges.)

**Step 1: Identify Twitter accounts whose conversation you are going to analyze.**
Use the [congress-legislators](https://github.com/unitedstates/congress-legislators) Github repository to compile the Twitter accounts and biographical information of the current members of Congress. The legislators’ bio information (including their political party) can be found in the file called `legislators-current`, and their official social media accounts can be found in `legislators-social-media`. You will find more information about the files in the repository’s read me file. Use pandas to read the two files, select the relevant fields, and join them into a single table. To simplify the analysis, you can ignore the Independents. Save both the legislators’ Twitter user names and user IDs, but rely on the user IDs to fetch their tweets as their user names may change. These two files change frequently and to ensure that your analysis can be replicated, timestamp the copy that you will download and use in the rest of the analysis. 

The assignment is framed around conversations prompted by Republican vs. Democrat legislators, but there are several allowable study populations. We expect ~90% of students to (a) choose to use those two populations as their populations of interest for this assignment. But you are welcome to (b) choose to study these legislators under another division of the legislator population (e.g., members of the House vs. the Senate, male vs. female, young vs. old) or (c) you can also consider a completely different set of accounts that interests you, e.g., left-leaning vs. right-leaning news outlets. 

To answer this step of the assignment, define your two populations and describe hypotheses about how the Twitter conversations around posts by these groups may differ.

If going a non-traditional route (b) or (c) above, make sure that the accounts post often enough (you can fetch tweets only from the last 7 days) and that their tweets get enough replies (single tweet conversations have a pretty boring structure). 

**Step 2: Download tweets posted by the selected Twitter accounts.**

Use the [`get-users-id-tweets` API](https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/api-reference/get-users-id-tweets) end-point ([tweepy API](https://docs.tweepy.org/en/stable/client.html#tweepy.Client.get_users_tweets)) to download the tweets posted by the accounts identified in Step 1. Ignore tweets that are replies (i.e., not root tweets) and retweets. Use the `expansions` and `tweet.fields` query parameters to request additional information that will help you construct the reply trees and reply graphs in the following steps. Save only tweets posted in the last 7 days since you will be able to search and download tweets/replies to those tweets posted in during that time frame. 

**Step 3. Download the conversations started by the tweets collected in Step 2.**

Use the [`get-tweets-search-recent` API](https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent) end-point to search for tweets posted as part of the conversations prompted by the tweets collected in Step 2. Use `conversation_id` as a filter operator in your queries (more information [here](https://developer.twitter.com/en/docs/twitter-api/conversation-id)). Use the `expansions` and `tweet.fields` query parameters to request the information you will need in the later analysis.

Test your code on a single conversation and make sure that you have all the data you need to complete the following steps before you download all conversations. You might be missing a field and would have to fetch the data again. (If that happens, use the tweet ids and fetch more information about them using the [`get tweets` API](https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/api-reference/get-tweets) which does not contribute to your accounts tweet cap.) Spot check a few conversations by comparing the downloaded tweets on the web (you can open any tweet by going to `https://twitter.com/anything/status/<tweet_id>`). 

**Step 4. Construct the reply trees and reply graphs.**

Group the tweets by conversation ID and construct the reply tree and reply graphs for each conversation. You can use the [`treelib` Python package](https://treelib.readthedocs.io/en/latest/) to construct and process the reply trees, and [`networkx`](https://networkx.org/documentation/stable/install.html) or [`igraph-python`](https://igraph.org/python/versions/latest/) to construct and analyze the reply graphs. You can also save some tweet or user information as node attributes (e.g., users follower count) that might be useful in Step 5. 

Visualize some reply trees and reply graphs and include at least one visualization of each kind in your report that clearly visualize the structure of a conversation. 

**Step 5. Characterize the reply trees and the reply graphs.**
Compute various characteristics of the reply trees (e.g., size, depth, breadth) and the reply graphs (e.g., size, density, number of connected components, reciprocity). Use the web interface to browse conversations from each category and think of interesting features that may be a good summary of the conversation structure. If you are looking for inspiration, read carefully the papers on information diffusion we discussed in Week 4 and consider which diffusion tree features may be relevant in describing the reply trees. Note that the features may use certain user or tweet characteristics, e.g., follower count [assortativity](https://networkx.org/nx-guides/content/algorithms/assortativity/correlation.html).

While the main focus of this problem set are the structural features, you can also include other features which you believe are important descriptors of the conversations and may help you build better classifiers in Step 6.

**Step 6. Build a conversation classifier.**
Using the conversation characteristics computed in the previous step, train a model that classifies the conversations by whether they were started by a Democrat or a Republican (or whichever groups you defined). You can use the [`scikit-learn` package](https://scikit-learn.org/stable/) to train and evaluate your models. You are free to use any model. Run k-fold cross-validation and report the model performance. Next, rank the features (i.e., conversation characteristics) by an appropriate measure of predictive power (e.g., single-feature model performance, but you may opt for other measures). Examine and visualize the distributions of the most predictive features across the conversation categories.

**Step 7. Write a report.**
Prepare a short report (8 page maximum) detailing your findings. 

**Pointers**
* To avoid exceeding your account’s monthly tweet cap, use the [tweet count](https://developer.twitter.com/en/docs/twitter-api/tweets/counts/api-reference) API end-points before starting a loop of requests.
* Respect the Twitter rate limit and add some wait time (`time.sleep(x)`) between your requests.
* You can use the [tweepy documentation](https://docs.tweepy.org/en/stable/client.html) to identify the appropriate methods to call in your Python code.
* For multipage results use the [`Paginator`](https://docs.tweepy.org/en/stable/v2_pagination.html)
* If the model you are using in Step 6 does not allow you to easily rank the features by predictive power, use [permutation feature importance](https://scikit-learn.org/stable/modules/permutation_importance.html) to rank the features.

**Grading rubric.** 

The following are requirements for a "good grade":
* Gather conversation data using the Twitter v2 API. Include your data gathering script in your submission.
* Correctly assemble reply trees and reply graphs from conversations and visualize an example of each in the report.
* Extract features from trees and graphs. The baseline is what Martin discussed in lecture on October 18 --- but we encourage and reward groups that design different features. Explain your choices in the report.
* Include sensible visualizations of the distribution of these features in your dataset, including (when relevant) CCDF plots, in your report.
* Train a conversation classifier, assess its performance using k-fold cross-validation, rank and visualize features by an appropriate measure of predictive power, and visualize the distributions of the most predictive features across conversation categories. Include this information in your report.

Please submit your work on Canvas (only one submission per group), and
ensure that all team members are listed on your report.


**Submission instructions:**

We ask that all project files (code and data) be uploaded to Canvas, and that a PDF of the report be uploaded to Gradescope.

To help make sure your team gets the deliverables submitted correctly, here's a project submission checklist:   

1. Write the names of all your group members, and your group number, into the report PDF and at least one of the source code files you submit. This is important to complete, as we may assign individual grades if we see major discrepancies between different parts of the project, so that everyone is treated fairly.
2. Write the names of each group member and which parts of the project they worked on at the top of your project PDF. You can all work on each part or split it up in any way you'd like. For example, you can write: "Person A (report); Person B (`tweet_analysis.py`); Person C: (report)''.
3. Go to the People page on Canvas, hit the Groups tab, and ensure that you're in the right group with the right people. If there's anyone else in your group who you are not working with, please email the TA team or make a private post on Ed so that they can be moved to the right group. We'll be using these groups to assign grades, so it's very important that they're correct.
4. Now, submit all files you made to create your report to the assignment on Canvas. This includes Python scripts, Jupyter notebooks, the submission PDF, etc. Only one person has to submit the files. Your group and its members will automatically be recorded on the submission.
5. Finally, please submit just the report PDF on Gradescope. On Gradescope, the group is not automatically recorded, so you'll have to select your group members when you submit. Only one person has to submit the PDF.

Good luck!
