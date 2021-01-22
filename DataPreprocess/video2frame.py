import os
import cv2 as cv

root_dir = "E://mono2binaural_data/"
videos_dir = os.path.join(root_dir, "videos")
frames_dir = os.path.join(root_dir, "frames")
if not os.path.exists(frames_dir):
    os.mkdir(frames_dir)
for video in os.listdir(videos_dir):
    print("processing {}".format(video))
    video_path = os.path.join(videos_dir, video)
    if(not os.path.exists(video_path)):
        print(video_path)
    frame_path = os.path.join(frames_dir, video)
    if not os.path.exists(frame_path):
        os.mkdir(frame_path)
    if os.listdir(frame_path) != []:
        continue
    cap = cv.VideoCapture(video_path)
    cap.set(cv.CAP_PROP_FPS,10)
    ret = True
    while(ret):
        frame_count = int(cap.get(cv.CAP_PROP_POS_FRAMES))
        fp = str(frame_count).zfill(6)+'.png'
        fp = os.path.join(frame_path, fp)
        ret, img = cap.read()
        if ret:
            cv.imwrite(fp, img)