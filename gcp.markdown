---
layout: default
title: "Setting up a free-tier GCP instance"
---

Stanford Farmshare provides free computing resources to anyone with a Stanford ID card. Unfortunately the version of Python (3.5) that Farmshare machines are running has been deprecated, and in particular is incompatible with the latest version of Tweepy. There is a way to install a newer version of Python locally on Farmshare -- for help with this, contact Greg.

If you'd prefer a service that works out of the box, consider using [Google Compute Engine Free Tier](https://cloud.google.com/free/docs/free-cloud-features#compute). If you stay within the prescribed free tier limits when setting up and operating your instance, there will be no cost to you. Note, however, that you are limited to 1 GB of free network egress (e.g. downloading from your GCP instance to your local machine) before you start accumulating charges.

Note that GCP offers a trial to first-time customers that provides $300 of free GCP credit for 90 days. $300 is much, much more than you will need for this course, but you will likely be ineligible for this free trial once you start using the GCP free tier mentioned above. In case you think you'll want to take advantage of the $300 credit 90-day trial in the future, Farmshare is always an option.

To get started with GCP, create a Google Cloud billing account, create a project, and link the project to your billing account. From your project page, click `Create a VM` and configure the parameters as you'd like. **IMPORTANT:** Unless you want to pay out-of-pocket or are using the 90-day free trial, the parameters you select must remain within the bounds specified by the [GCP free tier page](https://cloud.google.com/free/docs/free-cloud-features#compute). It appears that the "Monthly estimate" column to the right does not take the free tier into account when quoting a price. However the actual billing console does, and the cost of your free-tier machine will be met with an equivalent credit to your billing account.

Once your VM has been created, navigate to `Compute Engine` in the left-hand big hamburger menu. In `VM instances`, you should see the instance you configured. Under the `Connect` header, click on the dropdown next to `SSH`. If you `Open in browser window`, your browser will open a pop-up with a SSH connection to your instance. 

If you stuck with the free-tier configuration, by typing `python3` you'll see that Python 3.9.2 is installed and working on your machine. To get `pip`, exit the `python` console (type `exit()`) and type:

``sudo apt install python3-pip``

After this you'll be ready to `pip install tweepy` and get started on Assignment 1!

