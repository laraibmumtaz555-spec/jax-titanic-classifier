import pandas as pd
import numpy as np

def load_data():
    df = pd.read_csv("titanic.csv")
    
    # Fill missing values
    df['Age'].fillna(df['Age'].mean(), inplace=True)
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
    
    # Convert categorical to numeric
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
    df['Embarked'] = df['Embarked'].map({'S':0, 'C':1, 'Q':2})
    
    # Select features
    X = df[['Pclass', 'Sex', 'Age', 'Fare', 'Embarked']].values
    y = df['Survived'].values
    
    return X, y