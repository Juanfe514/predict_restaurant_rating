#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 17:55:23 2017

@author: juanfelipegonzalez
"""
import os
import json
import re
import random

restaurants = json.loads(open('/Users/juanfelipegonzalez/Desktop/St Gobain/data/restaurants.json').read())

#f=open('/Users/juanfelipegonzalez/Desktop/St Gobain/data/restaurants.json','r')
#restaurants = f.read()

x=re.compile(r'(.*)Reviews-')
y=re.compile(r'Reviews-(.*)')


i=0
l=[]


for b in range(100):
    c=random.randint(0,len(restaurants))
    while c in l:
        c = random.randint(0,len(restaurants))
    l.append(c)
    
    for k in range(21):
        if k==0:
            os.system('scrapy runspider getComments-2.py -a start_url="https://www.tripadvisor.com'+restaurants[c][‘restaurant’]+’” -o data/Comments-restaurant-‘+str(i)+'-'+str(k)+'.json')
            comments = json.loads(open('data/Comments-restaurant-‘+str(i)+'-'+str(k)+'.json').read())
            j=0
            print(comments)
            if comments==None:
                k+=1
            else:
                for comment in comments :
                    os.system('scrapy runspider getAllComments-4.py -a start_url="https://www.tripadvisor.com'+comment['comment']+'" -o data/AllComments-restaurant-‘+str(i)+'-'+str(k)+'-'+str(j)+'.json')
                    j+=1
        else:
            p=restaurants[c][‘restaurant’]
            x1=x.search(p)
            y1=y.search(p)
            ajout = x1.group(1)+'Reviews-or'+str(k)+str(0)+'-'+y1.group(1)
            os.system('scrapy runspider getComments-2.py -a start_url="https://www.tripadvisor.com'+ajout+'" -o data/Comments-restaurant-‘+str(i)+'-'+str(k)+'.json')
            comments = json.loads(open('data/Comments-restaurant-‘+str(i)+'-'+str(k)+'.json').read())
            if comments==None:
                k+=1
            else:
                j=0
                for comment in comments :
                    os.system('scrapy runspider getAllComments-4.py -a start_url="https://www.tripadvisor.com'+comment['comment']+'" -o data/AllComments-restaurant-‘+str(i)+'-'+str(k)+'-'+str(j)+'.json')
                    j+=1
            print(k)                         
    i += 1