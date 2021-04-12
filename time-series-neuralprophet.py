import pandas as pd
from neuralprophet import NeuralProphet

data = pd.read_csv('datasets/seattleWeather_1948-2017.csv')
# print(data.head(10))

# rearrange the original dataset
prcp_data = data.rename(columns={'DATE': 'ds', 'PRCP': 'y'})[['ds', 'y']]

model = NeuralProphet()
"""fit function

    params:: validate_each_epoch: a flag indicating whether or not to validate the model’s performance on the validation data in each epoch.
    parmas:: valid_p: a float between 0 and 1 indicating the proportion of the data that should be used for validation.
    params:: plot_live_loss: a flag indicating whether or not to generate a live plot of the model’s training and validation loss.
    params:: epochs: the number of epochs that the model should be trained for.
    n_changepoints — specifies the number of points where the broader trend (rate of increase/decrease) in the data changes.
    trend_reg — a regularization parameter that controls the flexibility of changepoint selection. Larger values (~1–100) will limit the variability of changepoints. Smaller values (~0.001–1.0) will allow for more variability in changepoints.
"""
metrics = model.fit(
    prcp_data, validate_each_epoch=True,
    valid_p=0.2,
    freq='D',
    plot_live_loss=True,
    epochs=10
)

future = model.make_future_dataframe(prcp_data, periods=365*5)
forecast = model.predict(future)
forecasts_plot = model.plot(forecast)

