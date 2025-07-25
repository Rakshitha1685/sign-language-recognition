cam = cv2.VideoCapture(0)
num_frames = 0
element = 10
num_imgs_taken = 0
while True:
                         ret, frame = cam.read()
# flipping the frame to prevent inverted image of captured frame...
frame = cv2.flip(frame, 1)
frame_copy = frame.copy()
roi = frame[ROI_top:ROI_bottom, ROI_right:ROI_left]
gray_frame = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
gray_frame = cv2.GaussianBlur(gray_frame, (9, 9), 0)
if num_frames < 60:
cal_accum_avg(gray_frame, accumulated_weight)
if num_frames <= 59:
             cv2.putText(frame_copy, "FETCHING BACKGROUND...PLEASE WAIT",
(80, 400), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,255), 2)
#Time to configure the hand specifically into the ROI...
elif num_frames <= 300:
hand = segment_hand(gray_frame)
cv2.putText(frame_copy, "Adjust hand...Gesture for" +
str(element), (200, 400), cv2.FONT_HERSHEY_SIMPLEX, 1,
0,0,255),2)
# Checking if the hand is actually detected by counting the number
of contours detected...
if hand is not None:
thresholded, hand_segment = hand
# Draw contours around hand segment
cv2.drawContours(frame_copy, [hand_segment + (ROI_right,
ROI_top)], -1, (255, 0, 0),1)
cv2.putText(frame_copy, str(num_frames)+"For" + str(element),
(70, 45), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
   # Also display the thresholded image
cv2.imshow("Thresholded Hand Image", thresholded)
else:
# Segmenting the hand region...
hand = segment_hand(gray_frame)
# Checking if we are able to detect the hand...
if hand is not None:
# unpack the thresholded img and the max_contour...
thresholded, hand_segment = hand
# Drawing contours around hand segment
cv2.drawContours(frame_copy, [hand_segment + (ROI_right,
ROI_top)], -1, (255, 0, 0),1)
cv2.putText(frame_copy, str(num_frames), (70, 45),
cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
cv2.putText(frame_copy, str(num_imgs_taken) + 'images' +"For"
+ str(element), (200, 400), cv2.FONT_HERSHEY_SIMPLEX, 1,
(0,0,255), 2)
# Displaying the thresholded image
cv2.imshow("Thresholded Hand Image", thresholded)
if num_imgs_taken <= 300:
cv2.imwrite(r"D:\\gesture\\train\\"+str(element)+"\\" +
str(num_imgs_taken+300) + '.jpg', thresholded)
else:
break
num_imgs_taken +=1
else:
cv2.putText(frame_copy, 'No hand detected...', (200, 400),
cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
# Drawing ROI on frame copy
cv2.rectangle(frame_copy, (ROI_left, ROI_top), (ROI_right,ROI_bottom), (255,128,0), 3)
cv2.putText(frame_copy, "DataFlair hand sign recognition_ _ _", (10, 20),                          cv2.FONT_ITALIC, 0.5, (51,255,51), 1)
# increment the number of frames for tracking
num_frames += 1
# Display the frame with segmented hand
cv2.imshow("Sign Detection", frame_copy)
# Closing windows with Esc key...(any other key with ord can be used too.)
k = cv2.waitKey(1) & 0xFF
if k == 27:
break
# Releasing the camera & destroying all the windows...
cv2.destroyAllWindows()
cam.release()