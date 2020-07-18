"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
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


if __name__ == '__main__':
    main(*sys.argv)

    resp = nsfg.ReadFemResp()

    print(resp.pregnum.value_counts().sort_index())
