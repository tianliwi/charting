import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

# Load CSV data
csv_file_path = 'ohlcv.csv'
df = pd.read_csv(csv_file_path)

# Ensure the 'time' column is in datetime format
df['date'] = pd.to_datetime(df['date'])

# Set the 'time' column as the index
df.set_index('date', inplace=True)

# Plot candlestick chart
fig, ax = plt.subplots(figsize=(10, 6))  # You can adjust the figure size as needed
mpf.plot(df, type='candle', ax=ax)

# Save the chart as a JPEG image
output_image_path = 'candlestick_chart.jpg'
plt.savefig(output_image_path, format='jpg')