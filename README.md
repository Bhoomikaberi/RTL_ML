# RTL Timing Prediction using Machine Learning

## Overview

RTL Timing Prediction is a machine learning-based framework that estimates the timing delay of RTL (Register Transfer Level) Verilog designs before synthesis. The goal is to reduce design iteration time by predicting timing characteristics directly from RTL features without requiring a complete synthesis flow.

This project extracts structural and behavioral features from Verilog RTL designs, generates a dataset using synthesis statistics, and trains machine learning models to predict timing delay.

---

## Project Structure

RTL_ML/ │ ├── rtl_dataset/              # Verilog RTL designs ├── feature_extraction/       # RTL feature extraction scripts ├── synthesis/                # Yosys automation scripts ├── dataset/                  # Generated datasets ├── models/                   # ML model training scripts ├── saved_models/             # Trained models ├── visualization/            # Feature importance & correlation plots ├── generated/                # Sample generated RTL designs ├── report/                   # Project report and documentation └── README.md

---

## Features

- Automated RTL feature extraction
- Yosys-based synthesis statistics generation
- Dataset creation and preprocessing
- Random Forest Regression model
- XGBoost Regression model
- Timing delay estimation
- Feature importance analysis
- Correlation visualization

---

## Extracted RTL Features

The framework extracts several RTL-level metrics including:

- Data width
- Number of adders
- Number of subtractors
- Number of multipliers
- Number of logical operations
- Number of conditional statements
- Estimated logic depth
- Complexity-related statistics

These features are used as inputs to machine learning models.

---

## Machine Learning Models

### Random Forest Regressor
- Ensemble-based regression model
- Robust against overfitting
- Good interpretability through feature importance

### XGBoost Regressor
- Gradient boosting framework
- High prediction accuracy
- Efficient handling of nonlinear relationships

---

## Workflow

1. Collect RTL Verilog designs.
2. Extract RTL features.
3. Synthesize designs using Yosys.
4. Generate timing dataset.
5. Train ML models.
6. Evaluate prediction accuracy.
7. Predict timing for unseen RTL designs.

---

## Installation

Clone the repository:

bash git clone https://github.com/your-username/RTL_ML.git cd RTL_ML 

Install dependencies:

bash pip install pandas numpy scikit-learn xgboost matplotlib seaborn 

---

## Running the Project

### Feature Extraction

bash python feature_extraction/extract_feature.py 

### Train Random Forest Model

bash python models/train_rf.py 

### Train XGBoost Model

bash python models/train_xgb.py 

### Evaluate Model

bash python models/evaluate.py 

---

## Results

The trained models are evaluated using:

- Mean Absolute Error (MAE)
- R² Score

The objective is to achieve accurate delay prediction while significantly reducing synthesis runtime.

---

## Applications

- Early timing estimation
- Design-space exploration
- RTL optimization guidance
- EDA acceleration
- VLSI design automation research

---

## Technologies Used

- Python
- Verilog HDL
- Yosys
- Pandas
- Scikit-Learn
- XGBoost
- Matplotlib

---

## Future Improvements

- Support for larger industrial RTL designs
- Deep Learning-based prediction models
- FPGA-specific timing estimation
- Multi-output timing and area prediction
- Integration with complete EDA flows

---

## Author

Bhoomika

RTL Timing Prediction using Machine Learning for VLSI Design Automation.