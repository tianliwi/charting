from lightweight_charts import Chart
import pandas as pd
from time import sleep
import tkinter

root = tkinter.Tk()
root.withdraw()
WIDTH, HEIGHT = root.winfo_screenwidth(), root.winfo_screenheight()

df = pd.read_csv("ohlcv.csv")
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

if __name__ == '__main__':
   
    chart = Chart(toolbox=True, width=1600, height=900, inner_width=0.7)
    chart.unplayed_quotes = df_future
    chart.topbar.textbox('symbol', 'NQ')
    chart.topbar.switcher('timeframe', ('5 mins', '15 mins', '1 hour'), default='5 mins', func=on_timeframe_selection)
    chart.topbar.button('replay', 'Play', func=on_replay)
    # chart = Chart(toolbox=True, width=1000, inner_width=0.6, inner_height=1)
    # chart.legend(True)

    chart2 = chart.create_subchart(toolbox=True, position='right', width=0.3, height=1)
    chart2.unplayed_quotes = df_future

    charts = [chart, chart2]

    chart.set(df_past)  
    chart2.set(df_past)

    # Imports the drawings saved in the JSON file.
    chart.toolbox.import_drawings('drawings.json')
    
    # Loads the drawings under the default symbol.
    chart.toolbox.load_drawings(chart.topbar['symbol'].value)  
    
    # Saves drawings based on the symbol.
    chart.toolbox.save_drawings_under(chart.topbar['symbol'])  
    
    chart.show(block=True)
    # Exports the drawings to the JSON file upon close.
    chart.toolbox.export_drawings('drawings.json')  