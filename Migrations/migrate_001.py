#! DO NOT RUN THIS

# UNLESS YOU KNOW WHAT YOU'RE DOING (Ask Ash).

import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd
import os

# Initialize Firebase Admin SDK
cred = credentials.Certificate("../serviceAccountKey.json")  # Replace with your service account key path
firebase_admin.initialize_app(cred)

# Initialize Firestore client
db = firestore.client()

# def migrate_readings():
#     # Reference to the readings collection
#     readings_ref = db.collection('readings')
#     # Reference to the Experiment document
#     experiment_ref = db.collection('Experiment').document('Rice1')
    
#     # File path for the CSV
#     csv_file_path = 'reading_data.csv'

#     # Check if CSV exists
#     if os.path.exists(csv_file_path):
#         print("Loading data from existing CSV file...")
#         # Load data from CSV into a DataFrame
#         df = pd.read_csv(csv_file_path)
#         # Convert DataFrame to list of dictionaries
#         readings_data = df.to_dict(orient='records')
#     else:
#         print("CSV file not found. Fetching data from Firestore...")
#         # Get all documents from the readings collection
#         readings_docs = readings_ref.stream()
        
#         # Create an array to hold the readings data
#         readings_data = []

#         # Loop through each document and append data to the readings_data list
#         for doc in readings_docs:
#             data = doc.to_dict()
#             readings_data.append(data)

#         # Save the readings_data to CSV
#         df = pd.DataFrame(readings_data)
#         df.to_csv(csv_file_path, index=False)
#         print(f"Data saved to {csv_file_path}.")

#     # Update the Rice1 document with the readings data
#     experiment_ref.update({
#         'readings': firestore.ArrayUnion(readings_data)
#     })

#     print("Data migration completed.")

# # Run the migration function
# migrate_readings()
