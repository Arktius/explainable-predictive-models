## How to use

### Dependencies
- Python version 3.6
- Tensorflow 1.12.0
- Keras 2.2.4
- Catboost 0.14.2
- Scikit learn 0.20.3
- Shap 0.28.5
- Keras-vis 0.5.0
- Innvestigate 1.0.8
- NumPy 1.16.2
- Matplotlib 3.0.3
- Seaborn 0.9.0
- Pyyaml 3.12

Or you can use the environment file provided [here](environment.yml).


### 1. Setting up the Configuration File

Edit the [config.yml](config.yml) script to customize your implementation and set folder paths. 

Implementation options are:

- features : Dictionary of feature names with keys respresenting column names in dataset and values representing names 
to be displayed in the feature importance plots.
- models to use : List of model names to be trained and evaluated (e.g GLM, Lasso etc.). Any model to be used has to be 
defined as a model class [here](code/utils/models.py) and has to be listed in the exact name of the defined class.
- test size: The proportion of the dataset to include in the test split. 
- number of splits : Number of training-test splits, i.e shuffles
- final performance measures: List of measures to calculate final performance (e.g AUC). Any measure to be used must 
be defined in the calc_perf_score function [here](code/utils/helper_functions.py). 
- subsampling to use : Type of subsampling to use on the traning set. Any type of subsampling to be used must be defined in 
the subsample fuction [here](code/utils/helper_functions.py). For no subsampling must be set to 'none'.
- fixed hyperparameters : Hyperparameters that won't be included in model tuning. All fixed hyperparameters must be set
to a single value.
- use grid search : Must be set to 'Yes' to perform model tuning through grid search with cross-validation. If set to 'No'
the models will be trained once on each training set given the 
- cross-validation folds : Number of cross-validation folds. Will be used only if 'use grid search' is set to yes.
- cross-validation score : Validation performance measure. Will be used only if 'use grid search' is set to yes.
- tuning hyperparameters : Hyperparameters that can be tuned. All tuning hyperparameters must be set to a list of values 
if 'use grid search' is set to yes. Otherwise they must be set to a single value and will be regarded as fixed 
hyperparameters for training.

Path options are:

- data path : Path to dataset file. 
- splits path : Path to training-test splits file. If file doesn't exist, this will be used as the path to save splits 
generated by the implementation.
- models folder path : Folder path to save models.
- parameters folder path : Folder path to save best tuning hyperparameters.
- importance folder path : Folder path to save feature importance values.
- scores folder path : Folder path to save performance scores.
- figures folder path : Folder path to save figures.

### 2. Train Models

Run the script train_models.py under code/. Training options such as fixed and tuning hyperparameters, cv folds, 
grid search choice etc. will be imported from the configuration file automatically. 

The trained models will be saved in the following format:

    [models folder path]/[model_name]_model_[subsampling_type]_subsampling_split_[current_split_number].pkl 
    [models folder path]/[model_name]_model_[subsampling_type]_subsampling_split_[current_split_number].h5 (MLP)

If models were tuned using gridsearch, the selected tuning hyperparameters will be saved in the following format:

    [parameters folder path]/best_[model_name]_parameters_[subsampling_type]_subsampling_split_[current_split_number].json 

### 3. Evaluate Performance

Run the script evaluate_models_performance.py under code/. Evaluation options such as choice of performance measures 
will be imported from the configuration file automatically.

Performance results will be saved in the following format:

    [scores folder path]/[model_name]_[performance_measure_name]_scores_[subsampling_type]_subsampling.csv

Custom trained models can be evaluated if the models file format is compatible (see part 2).

### 4. Evaluate Features Importance

Run the script evaluate_feature_importance.py under code/. 

Calculated importance values will be saved in the following format:
    
    [importance folder path]/[model_name]_weights_[subsampling_type]_subsampling.csv (Linear models)
    [importance folder path]/[model_name]_shap_values_[subsampling_type]_subsampling.csv (Tree boosting)
    [importance folder path]/[model_name]_dt_values_[subsampling_type]_subsampling.csv (MLP)


Custom trained models can be evaluated if the models file format is compatible (see part 2).

### 5. Visualization

