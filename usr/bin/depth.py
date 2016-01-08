#!/usr/bin/python
## The equivalent of:
##  "Working with Depth, Color and Audio Maps"
## in the OpenNI user guide.

"""
This creates a depth generator, checks if it can generate VGA maps in 30 FPS,
configures it to that mode, and then reads frames from it, printing out the
middle pixel value.
"""


from openni import *
import cv2
import numpy as np
ctx = Context()
ctx.init()

# Create a depth generator
depth = DepthGenerator()
depth.create(ctx)

# Set it to VGA maps at 30 FPS
depth.set_resolution_preset(RES_VGA)
depth.fps = 30

# Start generating
ctx.start_generating_all()

	
if __name__ == "__main__":
    while 1:
        #get a frame from RGB camera
        ctx.wait_any_update_all()
        #get a frame from depth sensor
        frame=np.fromstring(depth.get_raw_depth_map_8(),"uint8").reshape(480,640)
        cv2.imshow('RGB image',frame)
        
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()
