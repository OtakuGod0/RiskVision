import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import json
import sys; sys.path.append('..')  # Appending root directory of project for module import 
import os
from config.config import features_config_loc

def load_features(): 
    # list of available diseases
    try: 
        with open(os.path.join('..', features_config_loc), 'r') as fp:  # Corrected the path
            features = json.load(fp)
    except FileNotFoundError: 
        st.write("Error opening features config file")
        return {}
    except json.JSONDecodeError:
        st.write("Error decoding features config json file")
        return {}
        
    return features

def model_selection():
    # Hash map for models
    models_hashmap = {
        "Logistic Regression": LogisticRegression(),
        "Random Forest": RandomForestClassifier(),
        "Support Vector Machine": SVC(probability=True)
    }

    # Getting models from user
    models = st.sidebar.multiselect('Select Model:', models_hashmap.keys())
    
    return [models_hashmap[model] for model in models]  # Return actual model instances

def disease_selection():
    # List of available diseases
    features = load_features()
     
    # Selecting only diseases
    diseases_available = features.keys()
    
    # Getting diseases from user
    diseases = st.sidebar.multiselect("Diseases: ", diseases_available)
    
    return diseases 

def feature_selection(diseases):
    # Loading features of each disease
    features = load_features()
    
    # Empty dict for storing user-chosen features for diseases
    user_chosen_features = {}
    
    # Getting user input for features for each disease
    for disease in diseases: 
        # Feature header
        st.sidebar.subheader(disease)
        
        # Loading available features from features config file
        available_features = features[disease].keys()
        
        # Getting user-wanted features for each disease
        user_chosen_features[disease] = st.sidebar.multiselect("Select features to include: ", available_features)
        
    return user_chosen_features
        
def encode(X, encoder = OneHotEncoder(sparse_output=False), scaler = StandardScaler()): 
    # Encoding categorical data  
    # Columns to encode
    categorical_columns = X.select_dtypes(include='object').columns
    # Encoding
    encoded_columns = pd.DataFrame(encoder.fit_transform(X[categorical_columns]))  # Corrected typo
    # Naming columns
    encoded_columns.columns = encoder.get_feature_names_out(categorical_columns)
    # Concatenating with original dataframe
    X = pd.concat([X.drop(categorical_columns, axis=1), encoded_columns], axis=1)
    
    # Normalizing numerical features 
    # Features to scale
    numerical_features = X.select_dtypes(include=['int', 'float']).columns
    # Training scaler
    scaler.fit(X[numerical_features])
    # Scaling
    X[numerical_features] = scaler.transform(X[numerical_features])
    
    return X, encoder, scaler