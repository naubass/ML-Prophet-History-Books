from prophet import Prophet
import pandas as pd
import matplotlib.pyplot as plt

# load historical prediction data
data = pd.read_csv('library_borrowing_data.csv')
data['borrow_date'] = pd.to_datetime(data['borrow_date'])

# daily borrow counts
daily_data = data.groupby('borrow_date').size().reset_index(name='y')
daily_data.rename(columns={'borrow_date': 'ds'}, inplace=True)

# train the model
model = Prophet(daily_seasonality=False, yearly_seasonality=True, weekly_seasonality=True)
model.fit(daily_data)

# make future dataframe for 90 days
future = model.make_future_dataframe(periods=90)
forecast = model.predict(future)

# print hasil forecast
print("=== Forecast Results ===")
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(10))

# plot the results
fig = model.plot(forecast)
plt.title('Peminjaman Buku Perpustakaan - Prediksi 90 Hari ke Depan')
plt.xlabel('Tanggal')
plt.ylabel('Nomer Peminjaman')
plt.show()

# plot components
fig2 = model.plot_components(forecast)
plt.show()

# save forecast to CSV
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv('prediksi_peminjaman_buku.csv', index=False) 