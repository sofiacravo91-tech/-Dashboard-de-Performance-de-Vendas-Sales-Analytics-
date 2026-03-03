import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

reps = []

for i in range(12):
    reps.append({
        "rep_id": i+1,
        "rep_name": fake.name(),
        "region": random.choice(["North America","Europe","LATAM"])
    })

reps_df = pd.DataFrame(reps)

accounts = []

for i in range(600):
    accounts.append({
        "account_id": i+1,
        "company": fake.company(),
        "segment": random.choice(["Enterprise","Mid-Market","SMB"])
    })

accounts_df = pd.DataFrame(accounts)

deals = []

for i in range(1200):

    deals.append({
        "deal_id": i+1,
        "account_id": random.randint(1,600),
        "rep_id": random.randint(1,12),
        "stage": random.choice(["Prospecting","Demo","Proposal","Closed Won","Closed Lost"]),
        "value": random.randint(3000,200000)
    })

deals_df = pd.DataFrame(deals)

reps_df.to_csv("reps.csv",index=False)
accounts_df.to_csv("accounts.csv",index=False)
deals_df.to_csv("deals.csv",index=False)

print("Data generated")
