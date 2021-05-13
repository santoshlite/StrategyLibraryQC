from System import *
from QuantConnect import *
from QuantConnect.Algorithm import *
from QuantConnect.Data.Custom.Tiingo import *

class TiingoNewsAlgorithm(QCAlgorithm):

    def Initialize(self):
        # Predefine a dictionary of words with scores to scan for in the description
        # of the Tiingo news article
        self.words = {
            "bad": -0.5, "good": 0.5,
            "negative": -0.5, "great": 0.5,
            "growth": 0.5, "fail": -0.5,
            "failed": -0.5, "success": 0.5, "nailed": 0.5,
            "beat": 0.5, "missed": -0.5,
        }

        self.SetStartDate(2019, 6, 10)
        self.SetEndDate(2019, 10, 3)
        self.SetCash(100000)

        aapl = self.AddEquity("AAPL", Resolution.Hour).Symbol
        self.aaplCustom = self.AddData(TiingoNews, aapl).Symbol

        # Request underlying equity data.
        ibm = self.AddEquity("IBM", Resolution.Minute).Symbol
        # Add news data for the underlying IBM asset
        news = self.AddData(TiingoNews, ibm).Symbol
        # Request 60 days of history with the TiingoNews IBM Custom Data Symbol
        history = self.History(TiingoNews, news, 60, Resolution.Daily)

        # Count the number of items we get from our history request
        self.Debug(f"We got {len(history)} items from our history request")

    def OnData(self, data):
        # Confirm that the data is in the collection
        if not data.ContainsKey(self.aaplCustom):
            return

        # Gets the data from the slice
        article = data[self.aaplCustom]

        # Article descriptions come in all caps. Lower and split by word
        descriptionWords = article.Description.lower().split(" ")

        # Take the intersection of predefined words and the words in the
        # description to get a list of matching words
        intersection = set(self.words.keys()).intersection(descriptionWords)

        # Get the sum of the article's sentiment, and go long or short
        # depending if it's a positive or negative description
        sentiment = sum([self.words[i] for i in intersection])

        self.SetHoldings(article.Symbol.Underlying, sentiment)
