from openni import *
import cv2
from random import sample,randint
import numpy as np
ctx = Context()
ctx.init()
depth = DepthGenerator()
depth.create(ctx)
depth.set_resolution_preset(RES_VGA)
depth.fps = 30

video = cv2.VideoCapture(0)

def GetVideo():
    global video
    ret,Frame = video.read()
    return Frame


def GetProccesedVideo():
    ctx.start_generating_all()
    ctx.wait_any_update_all()
    FrameProccessed=np.fromstring(depth.get_raw_depth_map_8(),"uint8").reshape(480,640)
    FrameProccessed.astype('|S10')
    status = "OK"
    tempValue = randint(0,20)
    return FrameProccessed,status,tempValue

def GetTableData():
    TableData = []
    for i in range(0,3):
        TableData.append(sample(range(30),5))
    return TableData

def GetGraphData():
    GraphData  = []
    for i in range(10):
        GraphData.append(sample(range(30),2))
    #GraphData = [[1,5],[2,10],[3,15],[4,20],[5,25],[6,30],[7,35],[8,40],[9,45],[10,50]]
    return GraphData
