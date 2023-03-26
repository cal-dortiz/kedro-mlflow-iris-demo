# kedro-mlflow-iris-demo
Exploration with Kedro workflow to develop reproducable pipelines, mlflow to track experiments, and pycaret for automl on the iris data set. The focus of this repo is the process flow.

## Setting up the environment
After cloning the repo, build a conda environment with the following code

`<code here>`

## Data Processing Pipeline Workflow
---

### Load data into "Raw" folder and register data
Regester raw data set in `conf/base/catalog.yml`

### Data Preprocessing Pipeline
This portion of the workflow is the initial data cleaning of each indipendent datasset. 

    - run run `kedro pipeline create data_processing` to build new pipeline
    - Initial data preprocessing exploration in Jupyter Notebook
    - Preprocessing code is created in the data cleaning pipeline
    - Preprocessing code is mapped to the pipeline
    - Register preprocessed data to 02_intermediate data folder


### Building Primary Dataset
This portion of the work flow would merge multiple datasets into the primart modeling data set. Since Iris is a single dataset, the function just passes it through.

    - Explore data joining in jupyter
    - Pull code into node and pipeline files in data_processing pipeline
    - Register primary data to 03_primary folder.

## Modeling Pipeline Workflow
---

### Model Exploration