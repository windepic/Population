# -*- coding: utf-8 -*-
"""
Created on Thu May  5 16:21:24 2022

@author: Shiyu Song
"""

        for peo in range(self.num):
            
       #set the moving radius for people and prevent the value goes out of range
            
            self.people_array[peo,0] += random.uniform(-T,T)
      
        
            self.people_array[peo,1] += random.uniform(-T,T)
            if self.people_array[peo,0]<0:
                self.people_array[peo,0]=400
            if self.people_array[peo,1]<0:
                self.people_array[peo,1]=400
            if self.people_array[peo,0]>400:
                self.people_array[peo,0]=0
            if self.people_array[peo,1]>400:
                self.people_array[peo,1]=0
        
        
        