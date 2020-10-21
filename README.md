### Clustering Project
**Kwame Taylor, Codeup Darden Cohort, Oct 2020**

<img src="https://www.underconsideration.com/brandnew/archives/zillow_logo.png">

# Kwame's Zillow Zestimates Error Control

Welcome to my data science clustering project: **Kwame's Zillow Zestimates Error Control**! This project will use clustering to find the drivers of error in the Zestimate of single-unit properties that were listed on Zillow in 2017. I will demonstrate how this data can be used for quality control and preventing more Zestimate errors in the future.

I plan to create an MVP and then iterate through the data science pipeline multiple times.

## Project Plan

|    Date    |                                Goal                               |     Finished?     |
|:----------:|:-----------------------------------------------------------------:|:-----------------:|
| 10/15/2020 | Project planning, start on outline/bones of project.              |<ul><li>- [x] </li>
| 10/17/2020 | Finish MVP of wrangle.py and preprocessing.py.                    |<ul><li>- [x] </li>
| 10/18/2020 | Finish MVP of explore.py and start model.py MVP.                  |<ul><li>- [x] </li>
| 10/19/2020 | Finish model.py MVP and iterate through data science pipeline 1x. |<ul><li>- [x] </li>
| 10/20/2020 | Practice presentation, 1x iteration, sleep.                       |<ul><li>- [x] </li>
| 10/21/2020 | Presentation day! (turn in project)                               |<ul><li>- [ ] </li>

The project deliverables are the following: **Jupyter Notebook** data science pipeline walkthrough with **conclusions**, data **visualizations**, **README**, and **modules with functions** (```wrangle.py```, ```preprocessing.py```, ```explore.py```, and ```model.py```).

---

## Iterations through the Data Science pipeline

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
- [x] make README more thorough
- [x] add the data dictionary the hypotheses to README
- [x] review my notes and the project specs
- [x] turn cluster_area into dummy variables (i.e. is_cluster_area_1, is_cluster_area_2, etc.)
- [x] change statistical test to be better regarding the distribution of years
- [x] takeaways on how where to focus efforts to reduce log error
- [x] put remaining notebook code into functions
- [x] add two more models and test the best model on test data
- [x] copy comments from prepare code into presentation notebook
- [x] conclusions
- [x] practice presentation and make script/notes

**Things I'll save for future iterations for the sake of time:**
* title and label visualizations better
* plot centroids
* GeoPy implementation
* plot elevation's relation to latitude/longitude to see if log error has anything to do with topographical data
* make my module functions more generic and useful
* another hypothesis test

---

## Data Dictionary

| Term                         | Definition                                                                              |
|------------------------------|-----------------------------------------------------------------------------------------|
| parcelid (index)             | Unique identifier for parcels (lots)                                                    |
| bathcnt                      | Number of bathrooms in home including fractional bathrooms                              |
| sqft                         | Calculated total finished living area of the home                                       |
| latitude                     | Latitude of the middle of the parcel multiplied by 10e6                                 |
| longitude                    | Longitude of the middle of the parcel multiplied by 10e6                                |
| yearbuilt                    | The Year the principal residence was built                                              |
| value                        | The total tax assessed value of the parcel                                              |
| county (engineered)          | County in which the parcel is located                                                   |
| bathbedcnt (engineered)      | Number of bedrooms plus bathrooms in home                                               |
| decade (engineered)          | The Decade the principal residence was built                                            |
| century (engineered)         | The Century the principal residence was built                                           |
| cluster_area (engineered)    | Clusters based on latitude, longitude, and county                                       |
| logerror (prediction target) | The difference between log of Zestimate (prediction) and log of actual sales price of a property   |

| County encoded | County             |
|----------------|--------------------|
| 0              | Los Angeles County |
| 1              | Orange County      |
| 2              | Ventura County     |

---

## Hypotheses

𝐻0: There is no difference in Zestimate log error in properties built in the 1800s and the overall log error.<br>
𝐻𝑎: There is a difference in Zestimate log error in properties built in the 1800s and the overall log error.

𝐻0: There is no difference in Zestimate log error in properties built in the 1960s and the overall log error.<br>
𝐻𝑎: There is a difference in Zestimate log error in properties built in the 1960s and the overall log error.

---

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

---

### Big thanks to the following resources for education and inspiration:
* <a href="https://ds.codeup.com/">Codeup curriculum</a>
* <a href="https://towardsdatascience.com/simple-and-multiple-linear-regression-in-python-c928425168f9">Simple and Multiple Linear Regression in Python</a>
* <a href="https://geopy.readthedocs.io/en/stable/">GeoPy</a>
* <a href="https://machinelearningmastery.com/model-based-outlier-detection-and-removal-in-python/">4 Automatic Outlier Detection Algorithms in Python</a>
* <a href="https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html">Isolation Forest documentation</a>
* <a href="https://towardsdatascience.com/outlier-detection-with-isolation-forest-3d190448d45e">Outlier Detection with Isolation Forest</a>
* <a href="https://www.tablesgenerator.com/markdown_tables#">Markdown Table generator</a>
* <a href="https://jakevdp.github.io/PythonDataScienceHandbook/04.13-geographic-data-with-basemap.html">Geographic Data with Basemap</a>
* <a href="https://dardenreviews.github.io/">Faith's Darden reviews, of course!</a>
* And extra big thanks to my Codeup Darden cohort colleagues for being a constant source of knowledge, help, and motivation!
