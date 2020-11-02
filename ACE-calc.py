#!/bin/python

# This calculator is a port of the PowerShell calculator for the ACE-III by E-Sid to Python 2.7.8. (May not work on Python 3 without modifications). 
# Original version can be found here: https://github.com/E-Sid/scripts

# Data for ACE-III English Version A (2012)
# Available from:https://neurovascularmedicine.com/ace.pdf

# Attention
A1 = [0,5,"orientation to time"]
A2 = [0,5,"orientation to place"]
A3 = [0,3,"registration"]
A4 = [0,5,"serial 7 subtraction"]
# Memory
M1 = [0,3,"recall of 3 items"]
# Fluency
F1 = [0,7,"letter fluency"]
F2 = [0,7,"category fluency"]
# Memory
M2 = [0,7,"anterograde memory"]
M3 = [0,4,"retrograde memory"]
# Language
L1 = [0,3,"comprehension"]
L2 = [0,2,"writing"]
L3 = [0,2,"single word repetition"]
L4 = [0,2,"proverb repetition"] #should it be split in two?
L5 = [0,12,"object naming"]
L6 = [0,4,"comprehension?"]
L7 = [0,1,"reading"]
# Visuospatial abilities
V1 = [0,1,"intersecting infinity loops"]
V2 = [0,2,"3D wire cube"]
V3 = [0,5,"clock-drawing test"]
V4 = [0,4,"counting dots"]
V5 = [0,4,"identifying letters"]
# Memory
M4 = [0,7,"recall of name & address"]
M5 = [0,5,"recognition"]

subscores = (A1, A2, A3, A4, M1, F1, F2, M2, M3, L1, L2, L3, L4, L5, L6, L7, V1, V2, V3, V4, V5, M4, M5) 

# Main modules

def get_user_input(list):
    i = 0
    while i < len(list):
        item = list[i]
        try:
           user_input = raw_input("Please enter the value for " + item[2] + "[0-" + str(item[1]) + "]" )
           item[0] = int(user_input) # convert value to an integer
           check_range(item)
           i = i + 1
        except ValueError:
            print "The value you entered is out of range."
    return list
    
def check_range(item):
    if item[0] > item[1]:
        raise ValueError, "value is out of range"
    return True
    
# Script starts executing from here
    
print "Python Calculator for ACE-III"
print "============================="

get_user_input(subscores)

# Calculate subscores and total score
attention_score = A1[0] + A2[0] + A3[0] + A4[0]
memory_score = M1[0] + M2[0] + M3[0] + M4[0] + M5[0]
fluency_score = F1[0] + F2[0]
language_score = L1[0] + L2[0] + L3[0] + L4[0] + L5[0] + L6[0] + L7[0]
visuospatial_score = V1[0] + V2[0] + V3[0] + V4[0] + V5[0]
total_score = attention_score + memory_score + fluency_score + language_score + visuospatial_score

print "\n" #print new line
print "Attention Score: %s/18" % attention_score
print "Memory Score: %s/26" % memory_score
print "Fluency Score: %s/14" % fluency_score
print "Language Score: %s/26" % language_score
print "Visuospatial Score: %s/16" % visuospatial_score
print "----------------------"
print "Total ACE-III Score: %s/100" % total_score
