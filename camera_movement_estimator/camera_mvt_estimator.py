import cv2
import numpy as np 
import pickle
import sys
import os 
sys.path.append("../")
from utils import measure_distance,measure_xy_distance

class CameraMovementEstimator():
    def __init__(self,frame):

        first_frame_grayscale= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        mask_features = np.zeros_like(first_frame_grayscale)
        mask_features[:,0:20]=1
        mask_features[:,900:1050]=1

        self.features_params = dict(
            maxCorners=30,        
            qualityLevel=0.3,
            minDistance=3,
            blockSize=7,
            mask=mask_features
        )
        

        self.lk_params=dict(
            winSize=(15, 15),        
            maxLevel=2,
            criteria=(cv2.TERM_CRITERIA_COUNT | cv2.TERM_CRITERIA_EPS, 10, 0.03)
                #indicates that the termination condition is based on the number of iterations which is in our case 10 
                #indicates that the termination condition is based on accuracy (epsilon). The algorithm will stop if the change in the flow vectors is less than this threshold which is 0.03
        )

        self.minimmum_distance=5

    def get_camera_movement(self,frames, read_from_stub=False,stub_path=None):
        #read from stub if exists
        if read_from_stub and stub_path is not None and os.path.exists(stub_path):
            with open(stub_path,'rb') as f:
                return pickle.load(f)

        #mvt list
        camera_movement=[[0,0]]*len(frames)
        #first old frame
        old_gray = cv2.cvtColor(frames[0],cv2.COLOR_BGR2GRAY)
        #extract features from the first frame 
        old_features = cv2.goodFeaturesToTrack(old_gray,**self.features_params)

        for frame_num in range(1,len(frames)):
            frame_gray=cv2.cvtColor(frames[frame_num],cv2.COLOR_BGR2GRAY)
            new_features,_,_ = cv2.calcOpticalFlowPyrLK(old_gray,frame_gray,old_features,None,**self.lk_params)

            max_distance = 0 
            camera_movement_x,camera_movement_y = 0,0 

            for i,(new,old) in enumerate(zip(new_features,old_features)):
                new_features_point = new.ravel()
                old_features_point = old.ravel()

                distance = measure_distance(new_features_point,old_features_point)
                if distance > max_distance:
                    max_distance=distance
                    camera_movement_x,camera_movement_y=measure_xy_distance(old_features_point,new_features_point)
            if max_distance > self.minimmum_distance:
                camera_movement[frame_num]=[camera_movement_x,camera_movement_y]
                old_features=cv2.goodFeaturesToTrack(frame_gray,**self.features_params)
            old_gray=frame_gray.copy()
        
        if stub_path is not None:
            with open(stub_path,'wb') as f:
                pickle.dump(camera_movement,f)


        return camera_movement
    
    def draw_camera_movement(self,frames,camera_movement_per_frame):
        output_frames=[]
        for frame_num, frame in enumerate(frames):
            frame= frame.copy()

            overlay = frame.copy()
            cv2.rectangle(overlay,(0,0),(500,100),(255,255,255),-1)
            alpha =0.6
            cv2.addWeighted(overlay,alpha,frame,1-alpha,0,frame)

            x_movement, y_movement = camera_movement_per_frame[frame_num]
            frame = cv2.putText(frame,f"Camera Movement X: {x_movement:.2f}",(10,30), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),3)
            frame = cv2.putText(frame,f"Camera Movement Y: {y_movement:.2f}",(10,60), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),3)

            output_frames.append(frame) 

        return output_frames