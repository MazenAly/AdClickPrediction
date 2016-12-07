import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
from datetime import datetime
from sklearn.linear_model import SGDClassifier
import sklearn.cross_validation
from sklearn.preprocessing import MinMaxScaler
import sklearn.metrics
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import xgboost
from vowpalwabbit.sklearn_vw import VWClassifier
import langdetect as ld
#from difflib import SequenceMatcher
from fuzzywuzzy import fuzz

SELECTED = ['ID', 'Title', 'SearchDate', 'SearchParams', 'SearchQuery', 'Position', 'HistCTR', 'IsUserLoggedOn', 'Price',
 'SearchCategoryLevel', 'reg_ads', 'highlighted_ads', 'context_ads', 'user_clicks_no',
 'user_non_clicks_no', 'user_click_prob']
# 'IsClick', 

print("START: Reading data")
SOURCE = "data/testt3.csv"
df = pd.read_csv(SOURCE, sep=',', usecols=SELECTED)
# df = pd.read_csv(SOURCE, sep=',', index_col=0)
print("END: Reading data")

print("START: Fill NA")
df.SearchQuery.fillna("", inplace=True)
df.Title.fillna("", inplace=True)
df.SearchParams.fillna("", inplace=True)
print("END: Fill NA")

print("START: Dates")
df["SearchDate"] = pd.to_datetime(df["SearchDate"])

df["day_of_week"] = df["SearchDate"].dt.dayofweek
df["hour"] = df["SearchDate"].dt.hour
print("END: Dates")

# print("START: lang")
# def detectLanguage(x):
    
#     query = ""
    
#     if (str(x["SearchQuery"]) != "" or (any(c.isalpha() for c in query) == False)):
#         query = "No text found here."
#     else:
#         query = str(x["SearchQuery"])
            
#     detectedLang = ld.detect(query.decode('utf-8'))
#     if detectedLang == "ru":
#         x['SearchRussian'] = 1
#     else:
#         x['SearchRussian'] = 0
        
#     return x

# df.apply(detectLanguage, axis=1)
# print("END: lang")

print("START: 3 features")
df["AdTitleSZ"] = df["Title"].str.len()
df["SearchParamsSZ"] = df["SearchParams"].str.len()
df["SearchQuerySZ"] = df["SearchQuery"].str.len()
print("END: 3 features")

# print("START: Ratios")
# def calculateAdQueryRatios(x):
#     searchAdSimpleRatio = fuzz.ratio(str(x["Title"]), str(x["SearchQuery"]))
#     searchAdPartialRatio = fuzz.partial_ratio(str(x["Title"]), str(x["SearchQuery"]))
#     return searchAdSimpleRatio, searchAdPartialRatio

# df["SearchAdSimpleRatio"], df["SearchAdPartialRatio"] = zip(*df.apply(calculateAdQueryRatios, axis=1))
# print("END: Ratios")

# print("START: SearchParamNum")
# def getSearchParamsNum(x):
#     x['SearchParamsNum'] = len(str(x["SearchParams"]).split(":")) - 1
#     return x

# df.apply(getSearchParamsNum, axis=1)
# print("END: SearchParamNum")

TO_KEEP = ['ID', 'Position', 'HistCTR', 'IsUserLoggedOn', 'Price',
 'SearchCategoryLevel', 'reg_ads', 'highlighted_ads', 'context_ads', 'user_clicks_no',
 'user_non_clicks_no', 'user_click_prob', 'day_of_week', 'hour', 'AdTitleSZ', 'SearchParamsSZ', 'SearchQuerySZ']

print("START: writing to file")
df.to_csv("data/valid_set_updated_ltd.csv", index_label = False, columns=TO_KEEP)
print("END: writing to file")

# print("START: writing to file")
# df.to_csv("data/valid_set_updated_all.csv", index_label = False)
# print("END: writing to file")