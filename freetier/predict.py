from dsAlternative import se
from dsCryptopanic import ne
from dsTimeSeries import ts
from marketdepth import ma
from models import md
import config as cf

cm = "You are a master FX strategist and market analyst with deep knowledge of global macroeconomics, technical analysis, and risk management"
co = f"""Analyze the following OHLC market price data, 
formulate RSI, EMA, MACD, Bollinger Bands, Stochastic, ATR, Parabolic, Harmonics, Fibonacci, Gann,
and another other indicators that could be useful for prediction.
Together with the following news, market depth and market sentiment to predict the trend and price for the next 30 minutes:

*Time Series*\n{ts()}

*Latest News*\n{ne()}

*Market Depth*\n{ma()}

*Market Sentiment*\n{se()}"""

print(co)

cf.ml = 'groq'
cf.mo = 'deepseek-r1-distill-llama-70b'
print(md(cm, co))

cf.ml = 'gemini'
cf.mo = 'gemini-2.0-flash-lite'
print(md(cm, co))