# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 12:59:49 2025

@author: ygiduturi
"""

import pandas as pd
import random             #is to create random data
from faker import Faker              #to generate fake names, dates, descritpions etc.
import uuid               #to create random id's
from datetime import datetime, timedelta



# creating Fake Values
fake = Faker()

# Predefined values
cities = ['DL001', 'MH002', 'KA003', 'TN004', 'GJ005', 'RJ006']
crime_domains = ['Theft', 'Assault', 'Cybercrime', 'Murder', 'Fraud', 'Kidnapping']
crime_domains_with_typos = crime_domains + ['Murdr', 'Frad', '', None]
weapons = ['Knife', 'Gun', 'None', 'Blunt Object', 'Poison', 'Acid', '', 'Unknown', None]
genders = ['Male', 'Female', 'Other', 'Mle', 'Fmale', '', None]



def generate_case():
    # Introduce anomalies in dates
    date_reported = fake.date_between(start_date='-2y', end_date='today')
    date_occur = date_reported - timedelta(days=random.randint(0, 30))
    date_closed = (date_reported + timedelta(days=random.randint(1, 180))) if random.random() < 0.85 else None

    # Occasionally mess up the order
    if random.random() < 0.05:
        date_occur, date_reported = date_reported, date_occur  # invalid swap

    return {
        "case_id": str(uuid.uuid4()) if random.random() > 0.01 else '',  # 1% blank IDs
        "age": random.choice([random.randint(18, 70), '', None, 'Thirty-five']),
        "case_closed": random.choice(["Yes", "No", "", None]),
        "city_crime_code": random.choice(cities + ['', None]),
        "crime_description": fake.sentence(nb_words=6) if random.random() > 0.1 else '',
        "crime_domain": random.choice(crime_domains_with_typos),
        "date_case_closed": date_closed.strftime("%Y-%m-%d") if date_closed and random.random() > 0.05 else None,
        "date_of_occurence": date_occur.strftime("%Y-%m-%d") if random.random() > 0.02 else '',
        "date_reported": date_reported.strftime("%Y-%m-%d") if random.random() > 0.02 else None,
        "police_deployed": random.choice([random.randint(1, 20), '', None, -5]),
        "report_number": fake.bothify(text="REP####") if random.random() > 0.02 else None,
        "time_of_occurence": fake.time() if random.random() > 0.05 else '99:99',  # invalid time
        "victim_age": random.choice([random.randint(5, 80), '', None, 'Eighty']),
        "victim_gender": random.choice(genders),
        "weapon_used": random.choice(weapons)
    }

# Generate 5000 records
records = [generate_case() for _ in range(5000)]

# Create DataFrame and export
df = pd.DataFrame(records)
df.to_csv(r"C:\Users\ygiduturi\Documents\Python\dirty_crime_data_india.csv", index=False)

print("✅ File generated: dirty_crime_data.csv with 5,000 messy records")

