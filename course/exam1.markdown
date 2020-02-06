# Exam 1

## Objectives

This practical exam has three primary objectives.

1. Demonstrate student mastery of the hands--on content of the course.
1. Create a bridge from the hands--in content in the abstract to the specific types of data that each student expects to work with.
1. Generate a feedback cycle that allows the instructor to share high return--on--investment paths forward for the student--specific research needs.


## Grading and timing

This is not intended to be a high--stakes assignment.
As a result, you will have opportunities to seek feedback and revise your work before the deadline.
My intent is that each student put in the work to get his or her work up to an A level.
When in doubt, consider the objectives listed above; the grading is meant to be consistent with those outcomes.

You will be equipped to begin after week 2 (indexed from zero).
When time permits, I'm happy to look at and comment on your work.
In week 4, we will spend the class time working on this.
I will go around to help individually, and I will amplify topics that are widely applicable.

In general, you can work at your own pace, though I encourage you to stay ahead of the work.
I am happy to comment on work that is in progress, though I may ask you to wait for in--class coverage of some topics if you are working ahead.
The deadline is a final version delivered to me before we move to the readings portion of the course.
By that time, I should have seen it repeatedly on an informal basis, and, if I can see that it complies with the requirements from those interactions, I may simply tell you that you're finished (and no formal submission will be needed).


## Tasks

Delivery format: A single Jupyter Notebook that contains code and discussion of each of the following tasks.

1. Identify and gather data.
    - Describe your intended sample and the level of your intended ready--for--analysis dataset.
    - There should be at least three data components (i.e. a table or dataset) to be combined, and at least one of them should require aggregation or a non--one--to--one merge.
    - At least one dataset should contain text data for use in the creation of a sentiment or categorization measure (i.e. as the output of a classification model).
    - If you use code to do the gathering, include the code and save a copy of the untransformed data (so that I do not need to independently run queries or web--scrapers).
    - If you use an interface of some sort (e.g., the WRDS web interface), provide sufficient documentation for an exact recreation of the data you retrieved.
    - Provide links to descriptions of the data to ensure that the names, sources, and units are explicitly clear.
    - If you are a micro researcher, you may not have three datasets, and that's fine. For macro/archival researchers, we tend to combine a lot of data, so three (or more) should be very easy to find.
1. Clean and transform each component dataset.
    - Ensure proper datatypes. If a data column is truly numeric, make sure it is numeric. If you have a string that is meant to encode categorical data or an identifier, make sure that they are consistent.
    - Handle missing data in a defensible way. For example, if you are measuring firm positive emotional content in press coverage, consider whether no results should be a missing value sentinel (`NaN`) or a zero. Defend the choice, and consider having a column flagging the filled observations to allow running models that exclude them.
    - Drop unneeded columns.
    - Rename variables to have an intelligible naming scheme. I often find that prefixing variables from a particular source with a prefix makes the combined dataset easier to with with. For example, if I had the `at` variable from Compustat, I might prefix is so that the new full name is `compa_at`.
1. Examine each component dataset.
    - Plot the pairwise scatter plots for the variables of interest, and look at the distribution of each variable of interest (e.g., histograms). Note that there are ways to do a single plot with subplots for each pair or variable, and this is both more concise and less work than doing each individually.
    - Note any issues that you see, and describe what you may want to look at later. These are often helpful to track down causes when you see puzzling results in analyses.
1. Compute your text analysis measure(s).
    - If you need text run in LIWC, let me know. I will need a CSV with an identifier column and a column of text to use for computing measures.
1. Combine the final ready--for--analysis dataset.
    - Use merging or querying as needed.
    - Demonstrate that you do not have unintended many--to--many merges or default value issues (i.e. observations without proper identifiers all having a single value; creating spurious matches).
    - Make sure that the combined data is cleaned or transformed as needed. This should carry over from the component data, but you will sometimes need to calculate new variables that depend on data from multiple component datasets.
1. Examine the final dataset (like the components).
1. Export a version to use in the stats software of your choice.
1. Run a very simple model (e.g., OLS regression) and reproduce the output in your notebook.
    - The main goal here is to spot any data issues that your stats software has with the data, in order to fix them as needed.
    - You are looking for things like errors, perfectly collinear variables (may be a coding error), a smaller than expected sample size, and data type issues.
