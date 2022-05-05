# -*- coding: utf-8 -*-
"""
Created on Tue May  3 17:12:35 2022

@author: Shiyu Song
"""

            while True:
                
                IR1=input("please enter infection rate(between 0.3-0.8)")
                if 0.3<=float(IR1)<=0.8:
                    IR=float(IR1)
                    break
                else:
                    print("please enter decimal in the range")
                    continue
                
            while True:
                
                RC1=input("please enter recover rate(between 0.1-0.3)")
                if 0.1<=float(RC1)<=0.3:
                    RC=float(RC1)
                    break
                else:
                    print("please enter decimal in the range")
                    continue
                
            while True:
                
                DR1=input("please enter death rate(between 0.01-0.05)")
                if 0.01<=float(DR1)<=0.05:
                    DR=float(DR1)
                    break
                else:
                    print("please enter decimal in the range")
                    continue