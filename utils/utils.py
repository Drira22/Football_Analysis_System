import cv2 

def read_video(video_path):
    cap=cv2.VideoCapture(video_path)
    frames=[]

    while 1:
        ret,frame=cap.read()
        if not ret:
            break
        frames.append(frame)
    return frames

def save_video(output_video_frame,output_video_path):
    fourcc=cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path,fourcc,24,(output_video_frame[0].shape[1],output_video_frame[0].shape[0]))
    for frame in output_video_frame:
        out.write(frame)
    out.release() 

def measure_xy_distance(p1,p2):
    return p1[0]-p2[0],p1[1]-p2[1]