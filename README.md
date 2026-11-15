->Name: Yashee Goswami
->ERP: RU-2601102
->Section: O

---> How the Predictor Works
1.Takes weekly attendance percentages (from user input or a CSV file) and verifies that at least **2 weeks** of valid data (values between **0 and 100**) are provided.
2. Fits a best-fit straight line ($y = mx + c$) across the recorded weeks using NumPy's `np.polyfit(weeks, attendance, 1)` to determine the **slope** (rate of weekly attendance change) and **intercept**.
3. Uses the computed slope and intercept to predict the attendance percentage for a target future week, capping the result strictly within the **0% to 100%** range.
4. Evaluates the predicted percentage against the **75%** attendance requirement:
    75% or higher:Outputs `Safe`
   Below 75%:Outputs `Warning: below 75%`

--->Concepts Used
Language: Python 3
Libraries:NumPy (`np.polyfit`), Pandas
Core Concept: Simple Linear Regression & Trend Forecasting
