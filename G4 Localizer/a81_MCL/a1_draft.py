# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 10:13:40 2019

@author: Collin Brahana
"""

"""
Uses a Monte Carlo Localizer to find a robot given the relative headings of various lights, not identified.
Currently experimental.
"""

'''


'''

import math
import numpy as np
import random

#Location of the lights
light_location = np.array([[12.5,-25,0],
                          [0,-25,0],
                          [-12.5,-25,0],
                          [12.5,25,1],
                          [0,25,1],
                          [-12.5,25,1]]) #light_location[n] gives a tripple, light_location[n][m] gives specic

#Defines the borders of field so points can be checked
map_borders_x = 25
map_borders_y = 50

#Defines the dimensions for a half-field. When a random number -1<=x<=1 is multiplied, will create a point in the field
map_size_x = 25
map_size_y = 12.5

#Randomness Control
random.seed() #Creates a RNG seed with system-clock

#Error Values
move_error = 0.05
rotate_error = 0.05
sensor_error = 0.05

#Number of particles
n = 1000 


#Describes each particle,
class Particle():
    
    def __init__(self,rx=0,ry=0,rt=0,p=0):
        self.rx = rx
        self.ry = ry
        self.rt = rt
        
        self.p = p
    
        return None

    def randomizeParticle(self,x_max,y_max): 
        self.rx = random.uniform(0,1) * x_max - (x_max/2)
        self.ry = random.uniform(0,1) * y_max - (y_max/2)
        self.rt = random.uniform(0,1) * math.pi *2
        #TODO: This needs randomness testing!
        return None
    
    #moves the particle, with gaussian error
    def moveParticle(self,dx,dy,dt):
        self.rx += dx + getGaussRandom(move_error)
        self.ry += dy + getGaussRandom(move_error)
        self.rt += dt + getGaussRandom(rotate_error)
        #TODO: Edge cases not handled.
        return None
    
    #Calculates probability of x for 1-dim Gaussian with mean mu and var. sigma
    def calculateProbability(self,mu,sigma,x):
        return math.exp(-(math.pow((mu-x),2)) / (math.pow(sigma,2)) / 2.0) / math.sqrt(2.0 * math.pi * (math.pow(sigma,2)))

    #Generates list of angles that the robot should see from each particle location
    def generateAngles(self):
        self.a = []
        for i in range(len(light_location)):
            self.a.append(((math.atan2((light_location[i][1] - self.ry),(light_location[i][0] - self.rx))*-1)+math.pi/2)%(math.pi * 2))
        return None
    
    def getSensorAngles(self,ang = []):
        self.a_s = ang
        return None
    
    def compareAngles(self,sensor_error):
        prob_sum = [self.calculateProbability(self.a[x],sensor_error,self.a_s[y]) for x in self.a for y in self.a_s]
        self.p = self.multiply(prob_sum)
        return None  
    
    def multiply(l):
        total = 1.0
        for x in range(len(l)):
            total *= l[x]
        return total
    
    def giveProbability(self):
        return self.p
    
    def normalizeProbability(self,sums):
        return self.p/sums

def getGaussRandom(var): #Creates a random number on a bell curve with mu = 0, sigma = 1
    return random.gauss(0.0,var)

def sensor(centroids = []):
    #Talks to the camera program, gets the angles and colors of each light the camera can see
    a_s = [((math.atan2(centroids[c][1],centroids[c][0])*-1)+math.pi/2)%(math.pi * 2) for c in centroids]
    return a_s

def RandomPicker(p_list,w_list,n):
    random.choices(p_list,w_list)
    
    
    
#Start of actual implementation
p = [] #List of particles
w = [] #List of weights
normalizer = []

for q in range(1000):
    p.append(Particle())
    p[q].randomizeParticle(map_borders_x,map_borders_y)

for n in range(50):
    sen = sensor()
    for q in range(n):
        p[q].moveParticle(1.0,0,math.pi/2)
        p[q].generateAngles()
        p[q].compareAngles(sensor_error)
        normalizer.append(p[q].giveProbability)

    n_sum = sum(normalizer)
    for r in range(n):
        p[r].normalizeProbability(n_sum)
        w.append(p[r].giveProbability)
        
        








#PROTOTYPES
p = Particle(5)
q = Particle(9)

z = []
z.append(Particle())
z.append(Particle())
z.append(Particle())

z[2].randomizeParticle(25,50)

print(z[2].generateAngles())
