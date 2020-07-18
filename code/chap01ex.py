"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import pandas as pd
import sys

import nsfg
import thinkstats2

"""
#1 write a function that reads the respondent file, 2002FemResp.dat.gz.

The variable pregnum is a recode that indicates how many times each respondent has been pregnant

#2 Print the value counts and comepare them to the codebook
#3 Cross-validate the respondent and pregnancy files by 
comparing pregnum with the number of records in the pregnancy file

use nsfg.MakePegMap to make a dictionary that maps from each caseid
to a list of indices in the dataframe"""


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    print('%s: All tests passed.' % script)

def CrossValidatePregnum(resp, preg):
    """Print a cross validation output 

    resp: dataframe with nsfg respondents
    preg: dataframe with nsfg pregnancies
    """

    cv_preg = preg['caseid'].value_counts().reset_index()
    cv_preg.columns = ['caseid','count_preg']

    cv_resp = resp[['caseid','pregnum']]

    #left join pregs to resp to check ids
    cv_merge = pd.merge(left=cv_resp, right=cv_preg,
     how='left', left_on='caseid', right_on='caseid')

    #if a respondent had no pregnancies, they won't have a caseid in preg
    cv_merge.count_preg.replace(np.nan, 0, inplace=True)

    cv_merge['preg_diff'] = cv_merge.count_preg - cv_merge.pregnum

    print(cv_merge.preg_diff.value_counts()) 


def CrossValPythonically(resp, preg):
    """Use the dict returned by MakePregMap to validate

    resp: dataframe with nsfg respondents
    preg: dataframe with nsfg pregnancies
    """
    dict_preg = nsfg.MakePregMap(preg)
    validatecases = []
    for key, value in dict_preg.items():
        preg_val = resp.loc[resp.caseid==key,'pregnum'].values[0] - len(value)
        if preg_val != 0:
            validatecases.append(key)
    
    print(len(validatecases))


if __name__ == '__main__':
    main(*sys.argv)

    resp = nsfg.ReadFemResp()
    preg = nsfg.ReadFemPreg()

    #part one
    #print(resp.pregnum.value_counts().sort_index())

    #part two first attempt
    #CrossValidatePregnum(resp, preg)

    #part three with dict
    CrossValPythonically(resp, preg)
