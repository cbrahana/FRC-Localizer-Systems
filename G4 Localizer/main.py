#Mostly Notes for now

#Start of main program loop
    #Run every 0.25 seconds

#Get ORP (Odometry Robot Position) as (float,float) tuple
#Get ORH (Odometry Robot Heading) as 0-360 range, float
    
#Function - Check if ORP and ORH make sense
    #This is probably quite complicated , so do be mindful

#Function - Take photo with both cameras
    #Likely activate GPIO pin, and prep for inputs over HDMI or USB
    #Input into file 
    #Figure out how to do this!
    
#Function - Load each photo by accessing previous file into image_left and image_right
    #Need to make sure generated file and requested file have same name, but if
    #...it is possible to generate new filenames live, than this should be simple
    
#Function - Use ROI to select only the 180 degrees that the target could be in according to the ORH
    #Somewhat annoying mathematics, but relatively easy

#Denoise image_left & image_right
    #Learn how to do this effectively

#Contourize image, but only contours that are similar in size to the contours in the list

#Find corners in image

#Match each corner with the closest virtual corner on the sent-over list, as long as it is within certain distance

#Compare each corner in each image, and apply localization algorithms
    
#Output Localization Results
    
#Test results for feasibility against Odometry
    
#Give results to other services

#End main program loop



#On a second core?
#Loop
#Check ORP and ORH for feasibility
#Plug ORP and ORH into game engine, teleport camera to that position
#Contourize image
#Find length of relevant target contours
#Find pixel locations of corners
#Place length and ID and pixel locations into a list 
#Send that list over to Core One
#End Loop
