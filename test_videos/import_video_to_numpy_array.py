
import numpy as np
import time
import cv2
def load_video(fname):
	
	#this did all the files except the movs at the end. Needs to be dealt with.

	camera = cv2.VideoCapture(fname)
	video_array=[]
	num_frame=0 #this is only used if one wishes to pull out the width, height, and channel
	
	# keep looping
	while True:
		#num_frame=num_frame+1
		# grab the current frame
		(grabbed, frame) = camera.read()
		#if num_frame==1:
		#	print "width: %d pixels" % (frame.shape[1])
		#	print "height: %d pixels" % (frame.shape[0])
		#	print "channels: %d pixels" % (frame.shape[2])
		# check to see if we have reached the end of the
		# video
		if not grabbed:
			break

		
		
		# show the frame and the binary image
		
		#cv2.imshow("Movie", frame)  displays video as array is made
		video_array.append(frame)
		
		
		# if the 'q' key is pressed, stop the loop
		if cv2.waitKey(1) & 0xFF == ord("q"):
			break

	
	camera.release()
	cv2.destroyAllWindows()
	return video_array #returns array
	
if __name__ == "__main__":
	v_array=load_video('m02.avi') #give segmentation fault if it cannot find the file
	print v_array
	
