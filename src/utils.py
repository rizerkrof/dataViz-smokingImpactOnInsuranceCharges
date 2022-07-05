#!/usr/bin/env python3

def getBodyWeightCatFromBMI(bmi):
    if bmi <18.5: return "underWeight"
    elif bmi < 25: return "healthyWeight"
    elif bmi < 30: return "overWeight"
    else: return "obese"
