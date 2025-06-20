import pandas as pd

def label_priority(row):
    if row["population_density"] > 5000:
        return "High"
    elif row["population_density"] > 2000:
        return "Medium"
    else:
        return "Low"

def apply_labels(pop_df):
    pop_df["priority"] = pop_df.apply(label_priority, axis=1)
    return pop_df