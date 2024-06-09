from lightweight_charts import Chart
import pandas as pd
from time import sleep
import asyncio

async def data_loop(chart: Chart):
    df = pd.read_csv('ohlcv.csv').tail(50)
    
    # while True:
    #     while chart.replay_count > 0:
    #         for i, quote in df.iterrows():
    #             if not chart.is_alive:
    #                 return
    #             chart.update(quote)
    #             chart.replay_count = chart.replay_count - 1
    #         sleep(0.5)
        # await asyncio.sleep(0.3)

def on_replay(chart: Chart):
    chart.replay_count = chart.replay_count+1
    print("played", chart.replay_count)

def on_timeframe_selection(chart: Chart):
    print(chart.topbar['timeframe'].value)

def on_replay(chart: Chart):
    chart.replay_count = chart.replay_count+1
    print("played", chart.replay_count)

async def main():
    chart = Chart()
    
    chart.topbar.switcher('timeframe', ('1min', '5min'), func=on_timeframe_selection)
    chart.topbar.button('replay', 'play', func=on_replay)
    df = pd.read_csv('ohlcv.csv').iloc[:-50]
    chart.unplayed_quotes = pd.read_csv('ohlcv.csv').tail(50)
    
    chart.set(df)
    await asyncio.gather(chart.show_async(), data_loop(chart))
    

if __name__ == '__main__':
    asyncio.run(main())