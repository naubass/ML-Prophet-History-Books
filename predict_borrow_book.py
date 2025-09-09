from prophet import Prophet
import pandas as pd
import matplotlib.pyplot as plt
from prophet.diagnostics import cross_validation, performance_metrics
from prophet.plot import plot_cross_validation_metric

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# load data
data = pd.read_csv('library_borrowing_book_data.csv')
data['borrow_date'] = pd.to_datetime(data['borrow_date'])

# prepare data for Prophet
borrow_counts = data.groupby('borrow_date').size().reset_index(name='y')
borrow_counts.rename(columns={'borrow_date': 'ds'}, inplace=True)

# load holidays
holidays = pd.read_csv('library_holidays_exams.csv')
holidays['date'] = pd.to_datetime(holidays['date'])
holidays = holidays.rename(columns={'date': 'ds', 'event': 'holiday'})
holidays['lower_window'] = -1
holidays['upper_window'] = 1

# initialize and fit model
model = Prophet(holidays=holidays, yearly_seasonality=False, weekly_seasonality=True, daily_seasonality=False)
model.fit(borrow_counts)

# cross-validation
df_cv = cross_validation(model, initial='365 days', period='90 days', horizon='90 days')
df_p = performance_metrics(df_cv)
print(df_p.head())

# plot cross-validation metrics
fig = plot_cross_validation_metric(df_cv, metric="rmse")
plt.show()

# create future dataframe sepanjang test
future = model.make_future_dataframe(periods=90)
forecast = model.predict(future)

# hasil forecast train & evaluate model
print("Forecasting completed successfully.")
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(10))

# plot results
fig1 = model.plot(forecast)
plt.title('Forecast of Book Borrowing')
plt.xlabel('Date')
plt.ylabel('Number of Borrows')
plt.show()

# plot components
fig2 = model.plot_components(forecast)
plt.show()

# save forecast to CSV
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv('library_borrowing_forecast.csv', index=False)
print("Forecast data saved to library_borrowing_forecast.csv")


