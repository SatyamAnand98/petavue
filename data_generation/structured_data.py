import json
import os
import random

import numpy as np
import pandas as pd

from faker import Faker
from openai import OpenAI

# Fetch the OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key is fetched correctly
if not openai_api_key:
    raise ValueError("OpenAI API key not found. Please set OPENAI_API_KEY in the .env file.")

# Initialize OpenAI client
client = OpenAI(api_key=openai_api_key)


# Initialize Faker
fake = Faker()

# Function to generate structured data
def generate_structured_data(num_rows, num_columns):
    data = {
        "ID": range(1, num_rows + 1),
        "Name": [fake.name() for _ in range(num_rows)],
        "Age": [random.randint(18, 65) for _ in range(num_rows)],
        "Gender": [random.choice(["Male", "Female"]) for _ in range(num_rows)],
        "Department": [random.choice(["IT", "Marketing", "Finance", "HR", "Sales", "Operations", "Development"]) for _ in range(num_rows)],
        "Salary": [random.randint(50000, 100000) for _ in range(num_rows)],
        "Start Date": [fake.date_between(start_date='-10y', end_date='today') for _ in range(num_rows)],
        "Performance Score": [random.randint(50, 100) for _ in range(num_rows)]
    }
    
    # Adding additional columns with random numerical data
    for i in range(num_columns - len(data)):
        data[f"Column_{i+1}"] = np.random.randn(num_rows) * 10000

    # Writing data to xlsx file:
    df = pd.DataFrame(data)
    df.to_excel("./files/petavue_structured_data.xlsx", sheet_name="structured", index=False)

    # Returning the json format of dataframe for first 10 values and showing ... for remaining
    json_data = df.head(10).to_dict(orient='records')
    return {
        "data": json_data + [f'... {num_rows - 10} more data']
    }

# Function to generate unstructured data
def generate_unstructured_data(num_rows):
    data = {
        "Review ID": range(1, num_rows + 1),
        "Customer Name": [fake.name() for _ in range(num_rows)],
        "Review Date": [fake.date_between(start_date='-1y', end_date='today') for _ in range(num_rows)],
        "Product": [random.choice(["Wireless Mouse", "Office Chair", "Laptop Stand", "Noise Cancelling Headphones", "Coffee Maker", "Desk Lamp", "Smartwatch"]) for _ in range(num_rows)],
        "Review Text": [fake.paragraph(nb_sentences=3) for _ in range(num_rows)],
        "Sentiment": [random.choice(["Positive", "Neutral", "Negative"]) for _ in range(num_rows)]
    }

    # Writing data to xlsx file:
    df = pd.DataFrame(data)
    df.to_excel("./files/petavue_unstructured_data.xlsx", sheet_name="unstructured", index=False)

    # Returning the json format of dataframe for first 10 values and showing ... for remaining
    json_data = df.head(10).to_dict(orient='records')
    return {
        "data": json_data + [f'... {num_rows - 10} more data']
    }