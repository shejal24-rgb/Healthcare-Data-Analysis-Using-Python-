
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\ProjectDA\healthcare_data.csv")

print(df.head())
print(df.info())
print(df.describe())

print("Total Patients:", len(df))
print("Average Age:", np.mean(df["Age"]))
print("Average Treatment Cost:", np.mean(df["Treatment_Cost"]))

print("\nPatients by Gender:")
print(df["Gender"].value_counts())

print("\nMedical Conditions:")
print(df["Medical_Condition"].value_counts())

print("\nPatients by Hospital:")
print(df["Hospital"].value_counts())

print("\nAverage Treatment Cost by Hospital:")
print(df.groupby("Hospital")["Treatment_Cost"].mean())

sns.countplot(data=df, x="Gender")
plt.title("Patients by Gender")
plt.show()

sns.histplot(data=df, x="Age", bins=10)
plt.title("Patient Age Distribution")
plt.show()

sns.countplot(data=df, x="Medical_Condition")
plt.title("Medical Conditions")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

sns.barplot(data=df, x="Hospital", y="Treatment_Cost")
plt.title("Treatment Cost by Hospital")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

sns.scatterplot(data=df, x="Age", y="Treatment_Cost", hue="Gender")
plt.title("Age vs Treatment Cost")
plt.tight_layout()
plt.show()

print("Healthcare Data Analysis Completed!")
