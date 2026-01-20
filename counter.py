import cv2
import numpy as np
from ultralytics import solutions

videoCars = cv2.VideoCapture('Data/people.mp4')
model = "yolov8x.pt"

w, h, fps = (int(videoCars.get(x)) for x in (
    cv2.CAP_PROP_FRAME_WIDTH,
    cv2.CAP_PROP_FRAME_HEIGHT,
    cv2.CAP_PROP_FPS
))

y1, y2 = 300, 1079
x1, x2 = 700, 1780

regionPoints = [(100, 300), (825, 300)]

videoWriter = cv2.VideoWriter("people_control.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))

counter = solutions.ObjectCounter(
    show=False,
    region=regionPoints,
    model='yolov8x.pt',
    classes=[0],
    show_in=False,
    show_out=False
)

while videoCars.isOpened():
    success, im0 = videoCars.read()

    if not success:
        print("Video frame is empty or processing is complete.")
        break

    cv2.putText(im0, "ROI", (x1, y1-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.rectangle(im0, (x2, y2), (x1, y1), (0, 0, 255), 2)
    roi = np.ascontiguousarray(im0[y1:y2, x1:x2])

    results = counter(roi)

    processRoi = results.plot_im

    im0[y1:y2, x1:x2] = processRoi

    cv2.rectangle(im0, (40, 25), (410, 55), (255, 255, 255), -1)
    cv2.putText(im0, f"In: {counter.in_count} Out: {counter.out_count} Total: {counter.in_count + counter.out_count}",
                (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    videoWriter.write(im0)


videoCars.release()
videoWriter.release()
cv2.destroyAllWindows()
