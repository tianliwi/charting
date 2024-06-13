from lightweight_charts import Chart
import pandas as pd
from time import sleep
import tkinter

root = tkinter.Tk()
root.withdraw()
WIDTH, HEIGHT = root.winfo_screenwidth(), root.winfo_screenheight()

file_name = 'CME_1min_sample.csv'

df = pd.read_csv(file_name)
df['volume'] = 0
df_future = df.tail(50)
df_past = df.iloc[:-50]
df_delta = pd.DataFrame()

click_count = 0

def on_timeframe_selection(chart: Chart):
    print(chart.topbar['timeframe'].value)

def on_replay(target_chart: Chart):
    for chart in charts:
        if not chart.unplayed_quotes.empty:
            quote = chart.unplayed_quotes.iloc[0]
            chart.update(quote)
            chart.unplayed_quotes = chart.unplayed_quotes.drop(chart.unplayed_quotes.index[0])

def on_buy(chart: Chart):
    quote = chart.unplayed_quotes.iloc[0]
    print('buy', quote.open)

if __name__ == '__main__':
   
    chart = Chart(position='right', toolbox=True, width=1920, height=1080, inner_width=0.6)
    chart.unplayed_quotes = df_future
    # chart.candle_style(up_color='#000000', border_up_color='#42bda8', wick_up_color='#42bda8', down_color='#f23645', border_down_color='#f23645', wick_down_color='#f23645')
    chart.topbar.textbox('symbol', 'NQ')
    chart.topbar.switcher('timeframe', ('5 mins', '15 mins', '1 hour'), default='5 mins', func=on_timeframe_selection)
    chart.topbar.button('replay', 'Play', func=on_replay)
    chart.topbar.button('buy', 'Buy', func=on_buy)
    chart.grid(vert_enabled=False, horz_enabled=False)

    chart2 = chart.create_subchart(toolbox=False, position='left', width=0.4, height=1, sync=True)
    # chart2.candle_style(up_color='#000000', border_up_color='#42bda8', wick_up_color='#42bda8', down_color='#f23645', border_down_color='#f23645', wick_down_color='#f23645')
    chart2.topbar.textbox('symbol', 'ES')
    chart2.unplayed_quotes = df_future
    chart2.grid(vert_enabled=False, horz_enabled=False)

    charts = [chart, chart2]

    chart.set(df_past)  
    chart2.set(df_past)

    # Imports the drawings saved in the JSON file.
    # chart.toolbox.import_drawings('drawings.json')
    
    # Loads the drawings under the default symbol.
    # chart.toolbox.load_drawings(chart.topbar['symbol'].value)  
    
    # Saves drawings based on the symbol.
    # chart.toolbox.save_drawings_under(chart.topbar['symbol'])  
    
    chart.show(block=True)
    # Exports the drawings to the JSON file upon close.
    # chart.toolbox.export_drawings('drawings.json')  