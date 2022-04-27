# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 17:36:29 2022

@author: srinivasan.c
"""
import json
from pandas import json_normalize

import pprint
#print("Hello after long time")
# input json
json_str1 = '[{"NAME":"RAJ","SEM":"1","SUBJECT":"ENG","MARKS":10},{"NAME":"RAJ","SEM":"1","SUBJECT":"TAM","MARKS":20},{"NAME":"RAJ","SEM":"1","SUBJECT":"MAT","MARKS":30},{"NAME":"RAJ","SEM":"2","SUBJECT":"ENG","MARKS":102},{"NAME":"RAJ","SEM":"2","SUBJECT":"TAM","MARKS":202},{"NAME":"RAJ","SEM":"2","SUBJECT":"MAT","MARKS":302},{"NAME":"SAM","SEM":"1","SUBJECT":"ENG","MARKS":60},{"NAME":"SAM","SEM":"1","SUBJECT":"TAM","MARKS":70},{"NAME":"SAM","SEM":"1","SUBJECT":"MAT","MARKS":80},{"NAME":"SAM","SEM":"2","SUBJECT":"ENG","MARKS":602},{"NAME":"SAM","SEM":"2","SUBJECT":"TAM","MARKS":702},{"NAME":"SAM","SEM":"2","SUBJECT":"MAT","MARKS":802}]'

# load json object
data_list1 = json.loads(json_str1)

# create dataframe
df1 = json_normalize(data_list1, None, None)

def recur_dictify(frame):
    if len(frame.columns) == 1:
        if frame.values.size == 1: return frame.values[0][0]
        return frame.values.squeeze()
    grouped = frame.groupby(frame.columns[0])
    d = {k: recur_dictify(g.iloc[:,1:]) for k,g in grouped}
    return d
recur_dictify(df1)

ff = recur_dictify(df1)
#print(ff)

# Prints the nicely formatted dictionary
#pprint.pprint(ff)

# Sets 'pretty_dict_str' to the formatted string value
pretty_dict_str = pprint.pformat(ff)
print(pretty_dict_str)
# {'RAJ': {'1': {'ENG': 10, 'MAT': 30, 'TAM': 20},
         # '2': {'ENG': 102, 'MAT': 302, 'TAM': 202}},
 # 'SAM': {'1': {'ENG': 60, 'MAT': 80, 'TAM': 70},
         # '2': {'ENG': 602, 'MAT': 802, 'TAM': 702}}}
