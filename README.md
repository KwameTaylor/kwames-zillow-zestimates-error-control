### Clustering Project
**Kwame Taylor, Codeup Darden Cohort, Oct 2020**

<img src="https://www.underconsideration.com/brandnew/archives/zillow_logo.png">

# Kwame's Zillow Zestimates Error Control

Welcome to my data science clustering project: **Kwame's Zillow Zestimates Error Control**! This project will use clustering to find the drivers of error in the Zestimate of single-unit properties that were listed on Zillow in 2017. I will demonstrate how this data can be used for quality control and preventing more Zestimate errors in the future.

I plan to create an MVP and then iterate through the data science pipeline multiple times.

**Project Plan:**
|    Date    |                                Goal                               |     Finished?     |
|:----------:|:-----------------------------------------------------------------:|:-----------------:|
| 10/15/2020 | Project planning, start on outline/bones of project.              |<ul><li>- [x] </li>
| 10/17/2020 | Finish MVP of wrangle.py and preprocessing.py.                    |<ul><li>- [x] </li>
| 10/18/2020 | Finish MVP of explore.py and start model.py MVP.                  |<ul><li>- [x] </li>
| 10/19/2020 | Finish model.py MVP and iterate through data science pipeline 1x. |<ul><li>- [x] </li>
| 10/20/2020 | Practice presentation, 1x iteration, sleep. (turn in project)     |<ul><li>- [ ] </li>
| 10/21/2020 | Presentation day!                                                 |<ul><li>- [ ] </li>

The project deliverables are the following: **Jupyter Notebook** data science pipeline walkthrough with **conclusions**, data **visualizations**, **README**, and **modules with functions** (```wrangle.py```, ```preprocessing.py```, ```explore.py```, and ```model.py```).

**Pipeline iteration 1:**
* Project plan and timeline
* README outline
* Structure project bones
* Reach the minimum/MVP for each stage to be able to move on to the next stage.

**Pipeline iteration 2:**
* Recalibrate project plan timeline
* Tidy the data a little further
* Put functions into modules
* Flesh out README
* Run one statistical test
* Explore and feature engineering with clustering

**Pipeline iteration 3 (to-do list):**
- [x] remove outliers with isolation forest
- [ ] make cluster_area into dummy variables
- [ ] change statistical test to be better regarding the distribution of years
- [ ] turn cluster_area into dummy variables (i.e. is_cluster_area_1, is_cluster_area_2, etc.)
- [ ] takeaways and conclusions on how where to focus efforts to reduce log error
- [ ] read my notes
- [ ] read the project specs
- [ ] put remaining notebook code into functions
- [ ] add two more models
- [ ] test the best model on test data
- [ ] copy comments from acquire and prepare code into presentation notebook
- [ ] make README more thorough
- [x] add the data dictionary the hypotheses to README
- [ ] practice presentation and make script/notes
- [ ] title and label visualizations better
- [ ] geo.py implementation if extra time

Data Dictionary:
[Table here]

Hypotheses:
* x
* x
* x

Instructions for use and reproduction:
## Main notebook
To see and read through the main notebook, you can navigate to ```kwames-zillow-zestimates-error-control.ipynb``` in this GitHub repository.

You can explore the functions from the notebook more indepth in the ```wrangle.py```, ```preprocessing.py```, ```explore.py```, and ```model.py``` files.

## Setup

In order to run the code in this repository, you'll need:

1. An installation of python through anaconda
2. An ```env.py``` file that defines the following variables:
  - 'user'
  - 'host'
  - 'password'

The code in here was developed on MacOS, but should run fine anywhere you can install python + anaconda.
