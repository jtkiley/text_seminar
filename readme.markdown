# BADM 6100: Text Analysis: Planning to Publication

## Overview

This course is designed to help students learn modern text analysis techniques, from planning a study to publication.
The topics will include a streamlined set of data science prerequisites, understanding how text becomes data, familiarization with some advanced techniques, and in-depth coverage of papers that utilize various techniques.

Text analysis continues to grow in use in macro research (e.g., firm impression management, media narratives), and has interesting emerging work in micro settings (e.g., unobtrusive measures of the big 5, emotional content of transcripts). As data access expands both at the macro (e.g., earnings call transcripts) and micro (e.g., group work tools like Slack and Microsoft Teams) levels, researchers with this skillset can ask and answer new and interesting theoretical questions.


## Course details

Because I am making these resources publicly available, the information about the course for enrolled students is in the `course` directory.


## Prerequisites

The skill requirements assume essentially no prior training, though reasonable spreadsheet skills and some familiarity with one of the commonly--used commercial statistical systems (in either micro or macro work) is helpful.


## Schedule

The course is divided into fifteen weeks, each with two 75 minute segments, with breaks between segments.
In the first half of the course, we will use a hands-on design to learn foundational skills, working with data, and practical text analysis techniques.
In the second half, we will analyze recent papers as part of learning how to design and conduct projects to maximize validity, rigor, and publication prospects.


### Applied methods

week | topic
---|--------
0a | Introduction
0b | Setup, Anaconda, and Jupyter
1a | Python basics I
1b | Python basics II
2a | Data handling
2b | Review and self-study tracks
3a | Data retrieval I
3b | Data retrieval II
4a | Student data I
4b | Student data II
5a | Text analysis I
5b | Text analysis II
6a | Supervised learning
6b | Unsupervised learning
7a | Regression with panel data (an aside)
7b | Exam I Review


### Planning to publication

week | topic
---|--------
8  | Text analysis project design
9 | Qualitative
10 | Metadata and human coding
11 | Dictionary methods I
12 | Dictionary methods II
13 | Supervised learning
14 | Unsupervised learning


## Materials

There is a notebook and slide deck for each week of the applied methods unit.
The slides are available in zip archives containing Keynote and Powerpoint versions in the releases section.
Please note that the Keynote slides are the ones actually presented.

Also, there is an `environment.yml` file for setting up your Anaconda environment, using the instructions below.


## Preparing for the course

Before the first meeting, please complete the following.
If you encounter issues, get as far as you can, and we will work through them in class.

**Please note:** It is best to install (and work with) this software on a physical computer (i.e. not virtualized) that is not locked down with IT permissions.


### Install software

1. Install [Anaconda, Python 3.7 version](https://www.anaconda.com/distribution/).
1. (optional, but encouraged) Install Microsoft Visual Studio Code. The Anaconda installer asks if you would like to install it.
1. (experts-only alternative) Install miniconda instead of the GUI version. While there are direct download versions, you would typically use a package manager (e.g., brew on macOS, apt on Ubuntu). Similarly, you could install VS Code with your package manager as well.


### Importing the Anaconda environment.

1. Open the Anaconda Navigator app.
1. On the left, click Environment.
1. At the bottom of the resulting main window, click Import.
1. In the resulting popup, click the folder icon, navigate to the `environment.yml` file, and click Open.
1. Back in the import popup, the environment name should be filled in automatically from the file, `tapp` in this case. Click Import.
1. Wait for the packages for the environment to be downloaded and installed. This could take a few minutes.

**Note:** there is also a file named `environment_full.yml`.
This file is much more specific about particular software versions, and it is largely specific to both macOS and particular hardware.
I include it for documentation reasons, but you should generally use the more general (i.e. compatible) `environment.yml`.


### Install the Jupyter Lab Extension for Plot.ly

1. Open a terminal (on Windows, use the prompt labeled either "Anaconda Prompt" or "Anaconda (64-bit)" in the start menu).
1. Activate the `tapp` environment using the command `conda activate tapp`.
1. Install the extensions using these commands:

```
jupyter labextension install @jupyter-widgets/jupyterlab-manager@1.1 --no-build
jupyter labextension install jupyterlab-plotly@1.4.0 --no-build
jupyter labextension install plotlywidget@1.4.0 --no-build
jupyter lab build

```

**Note:** On my desktop, the last command takes about six minutes to complete, so give it time. If you see any errors relating to memory, you may need to use some additional commands, shown in the [plot.ly getting started](https://plot.ly/python/getting-started/) document. I did not need anything other than the commands above, though.


### Install TextBlob text corpora and spacy word models.

1. Open a terminal (on Windows, use the prompt labeled either "Anaconda Prompt" or "Anaconda (64-bit)" in the start menu).
1. Activate the `tapp` environment using the command `conda activate tapp`.
1. Install the corpora using the command `python -m textblob.download_corpora`. There may be warnings or errors that are not relevant for our purposes, but you should see a series of successful downloads.
1. Install the spacy English models using the command `python -m spacy download en_core_web_lg`.


## About Jason

Jason T. Kiley is an Assistant Professor and Spears Fellow at Oklahoma State University.
His research examines the interplay of audience perceptions of firms, impression management, and their associations with outcomes, including recent publications in the Academy of Management Journal and Strategic Management Journal.
As part of his work, he works to advance the use of software to increase the range, efficiency, and rigor of conducting empirical research.
He is a co-organizer of the annual AOM Content Analysis PDW, and his published and in-progress work often uses state-of-the-art content analysis techniques, including recent work with semantic text analysis and machine learning.
