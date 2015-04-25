# your code goes here
import glob
import os
photosArray = glob.glob("*.png")#gets the photos in the imgs fold..
print photosArray
if len(photosArray)>=9:#10 photos were created?
   print "YAY lets start the bubble sorting!"
   #sort
   alist = photosArray
   # bubble sorting
   for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if os.path.getmtime(alist[i])>os.path.getmtime(alist[i+1]):
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

   print photosArray
   a = 1
   # remove the oldest 5 files (pics)
   while(a<5):
    	os.remove(photosArray[a])
    	photosArray.remove(photosArray[a])
    	a=a+1
   print photosArray


