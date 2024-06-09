from lightweight_charts import Chart
import pandas as pd

def on_timeframe_selection(chart: Chart):
    print(chart.topbar['timeframe'].value)

if __name__ == '__main__':
    chart = Chart(inner_width=0.3, toolbox=True)
    chart2 = chart.create_subchart(position='top', width=0.7, height=1, sync=True, toolbox=True)
    
    chart.topbar.textbox('symbol', 'NQ')
    chart.topbar.switcher('timeframe', ('5 mins', '15 mins', '1 hour'), default='5 mins', func=on_timeframe_selection)

    chart.watermark('1')
    chart2.watermark('2')

    df = pd.read_csv('ohlcv.csv')
    chart.set(df)
    chart2.set(df)


    # Imports the drawings saved in the JSON file.
    chart.toolbox.import_drawings('drawings.json')
    
    # Loads the drawings under the default symbol.
    chart.toolbox.load_drawings(chart.topbar['symbol'].value)  
    
    # Saves drawings based on the symbol.
    chart.toolbox.save_drawings_under(chart.topbar['symbol'])  

    chart2.set_visible_range(start_time='2015-10-08', end_time='2019-10-08')
    chart2.grid(vert_enabled=False, horz_enabled=False)
    chart2.candle_style(down_color='#000000', wick_down_color='#ffffff', border_down_color='#ffffff')

    chart.show(block=True)
    
    # Exports the drawings to the JSON file upon close.
    chart.toolbox.export_drawings('drawings.json')  