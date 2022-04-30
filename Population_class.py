# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 17:54:24 2022

@author: Shiyu Song
"""

class Population():
    def __init__(self,num=pop):
        
        #initiallise number of people
        self.num=num
        
        #set the first infection
        self.first=random.randint(0,self.num-1)
        
       
        #create arrays in 2 x num dimension
        self.people_array=np.arange(2*self.num).reshape(self.num,2)
        
        self.infected=[self.first]
        
        #set the color for healthy people and first infected person
        self.color=["green"]*self.num
        self.color[self.first]="red"
        self.recovered=[]
        self.dead=[]