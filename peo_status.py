# -*- coding: utf-8 -*-
"""
Created on Wed May  4 19:35:24 2022

@author: Shiyu Song
"""


#create empty lists to hold people in different status
        new_infected=[]
        new_recovered=[]
        new_dead=[]
        
        for peo in range(self.num):
            is_infect=0
            for inf in self.infected:
                if peo==inf:
                    is_infect=1
                    break
            if is_infect==1:
                continue
            for inf in self.infected:
                #infection machanism and infection rate
                if (self.people_array[peo,0]-self.people_array[inf,0])**2+(self.people_array[peo,1]-self.people_array[inf,1])**2<=25 and IR>random.random():
                    new_infected.append(peo) # append infected people to the list
                    print(new_infected,"1")