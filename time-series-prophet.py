# forecasting predicting future values based on previously observed values
# Facebook's Prophet != autoregressive
# pip install fbprophet
# y(t) = g(t) + s(t) + h(t) + e(t)
# g(t): representing the trend
# s(t): represents preiodic changes (weekly, monthly, yearly)
# h(t): effects of holiday
# e(t): error term
# fiting procedure is very fast

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from fbprophet import Prophet

data = pd.read_csv('datasets/GOOG.csv')
print(data.head(5))

# Build the predictive model
data = data[["Date", "Close"]]
# Rename the feature: these name are NEEDED for the model fitting
data = data.rename(columns={"Date": "ds", "Close": "y"})
print(data.head(5))

m = Prophet(daily_seasonality=True)
m.fit(data)

# Plot the prediction
## specify the number of days in future
future = m.make_future_dataframe(periods=365)
prediction = m.predict(future)
m.plot(prediction)

# predict from June 2020 to June 2021
plt.title("Prediction of the Stock using Prophet")
plt.xlabel("Date")
plt.ylabel("Close")
plt.show()

m.plot_components(prediction)
plt.show()