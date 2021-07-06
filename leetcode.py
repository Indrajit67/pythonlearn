#Two SUm

    # Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    #
    # You may assume that each input would have exactly one solution, and you may not use the same element twice.
    #
    # You can return the answer in any order.   hife
    #https://github.com/Indrajit67/Indrajit67.git


#!/usr/bin/env python

import re
#importing regular expression

show_tech = open("show_tech_20714-AN03-001.txt","r")

for line in show_tech:
    if re.match("000328: Jun 29 13:11:43.363 NL-DST: %CRYPTO_ENGINE-5-KEY_ADDITION", line):
        print (line)
#above only prints line starting with and not containing
# to dowload file curl -O http://www.gutenberg.org/dirs/etext97/wssnt10.txt

print ("Comming the code to git")