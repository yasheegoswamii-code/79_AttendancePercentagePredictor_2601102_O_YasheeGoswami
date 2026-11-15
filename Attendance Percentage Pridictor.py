import numpy as np
import pandas as pd

# 1. Ask how you want to give the data
choice = input("Type 'manual' or 'csv': ")

if choice == "csv":
  # Load from CSV file
  filename = input("Enter your CSV file name (e.g. attendance.csv): ")
  data = pd.read_csv(filename)

  # Get the names of the columns in the CSV
  cols = data.columns

  if len(cols) >= 2:
    weeks = data[cols[0]].values  # 1st column
    attendance = data[cols[1]].values  # 2nd column
  else:
    attendance = data[cols[0]].values  # Only column
    weeks = list(range(1, len(attendance) + 1))
else:
  # Type numbers directly
  raw = input("Enter attendance separated by commas (e.g. 90, 88, 86): ")
  attendance = [float(x) for x in raw.split(",")]
  weeks = list(range(1, len(attendance) + 1))

# 2. Check if data is valid
if len(attendance) < 2:
  print("(a) At least 2 weeks of data are required.")
elif min(attendance) < 0 or max(attendance) > 100:
  print("(b) Attendance must be between 0 and 100.")
else:
  # 3. Calculate slope and intercept using numpy
  slope, intercept = np.polyfit(weeks, attendance, 1)
  print(f"Slope: {slope:.2f} | Intercept: {intercept:.2f}")

  # 4. Predict future week
  future_week = float(input("Enter week to predict for: "))
  prediction = slope * future_week + intercept

  # 5. Cap prediction between 0 and 100
  if prediction > 100:
    print(
        f"Predicted attendance for week {int(future_week)}: 100.00% (capped at"
        " 100)"
    )
    prediction = 100.0
  elif prediction < 0:
    print(f"Predicted attendance for week {int(future_week)}: 0.00%")
    prediction = 0.0
  else:
    print(
        f"Predicted attendance for week {int(future_week)}:"
        f" {prediction:.2f}%"
    )

  # 6. Safe or Warning message
  if prediction >= 75:
    print("Safe")
  else:
    print("Warning: below 75%")