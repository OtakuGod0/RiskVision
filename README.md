# RiskVision: Disease Risk Prediction

## Project Overview

RiskVision is a web application built using Flask that helps users assess their potential risk of contracting three common diseases: stroke, heart disease, and diabetes. It leverages machine learning models trained on data obtained from online sources (like Kaggle) to provide users with risk probabilities. Streamlit is used for model evaluation and more flexible prediction capabilities.

## Features

### Disease Prediction Interface (Flask)
- Interactive web interface for disease risk assessment
- Step-by-step questionnaire system
- Disease-specific and common feature grouping
- Real-time probability calculation using pre-trained models
- Support for multiple diseases:
  - Stroke
  - Heart Disease
  - Diabetes

### Model Evaluation Dashboard (Streamlit)
- Interactive model evaluation interface
- Support for multiple machine learning models:
  - Logistic Regression
  - Random Forest
  - Additional models
- Performance metrics visualization:
  - Accuracy
  - F1 Score
  - Recall
  - Additional metrics
- Flexible feature selection for predictions
- Live model training and evaluation

## Technology Stack

- **Backend Framework:** Flask
- **ML Libraries:** scikit-learn
- **Model Evaluation:** Streamlit
- **Model Persistence:** pickle
- **Data Sources:** Kaggle datasets

## Project Structure

```
RiskVision/
├── app.py                         # Main Flask app for disease prediction
├── requirements.txt               # Project dependencies
├── config/
│   ├── config.py                  # Configuration settings
│   ├── features.json              # Features metadata
│   └── **pycache**/
├── data/
│   ├── model_training/            # Training data organized by disease
│   │   ├── diabetes/
│   │   ├── heart_disease/
│   │   └── stroke/
│   ├── processed/                 # Processed datasets
│   └── raw/                       # Raw datasets
├── models/                        # Trained models and scalers
│   ├── diabetes/
│   ├── heart_disease/
│   └── stroke/
├── notebooks/                     # Jupyter notebooks for EDA and model training
│   ├── diabetes/
│   ├── heart_disease/
│   ├── kidney_disease/
│   └── stroke/
├── static/                        # Static files for Flask
├── streamlit/                     # Streamlit app files for evaluation
├── templates/                     # HTML templates for Flask
├── tests/                        # Unit and integration tests
└── utils/                        # Utility scripts
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/RiskVision.git
cd RiskVision
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Flask Application
1. Start the Flask server:
```bash
python app.py
```
2. Navigate to `http://localhost:5000` in your browser
3. Select a disease and follow the questionnaire
4. View your risk assessment results

### Streamlit Dashboard
1. Navigate to the streamlit directory:
```bash
cd streamlit
```
2. Run the Streamlit app:
```bash
streamlit run app.py
```
3. Access the dashboard at `http://localhost:8501`

## Model Training

- Models are trained using data from public datasets (Kaggle)
- Flask app uses pre-trained models (saved using pickle)
- Streamlit dashboard supports live model training and evaluation
- Separate notebooks are available for each disease's model development

## Acknowledgments

- Data sources from Kaggle
- Open source community for various libraries used in this project