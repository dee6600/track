import cv2
import sys
 
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
 
if __name__ == '__main__' :
 
    # Set up tracker.
    # Instead of MIL, you can also use
 
    tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'GOTURN']
    tracker_type = tracker_types[4]
    
    
    #creating first tracker
    if int(minor_ver) < 3:
        tracker = cv2.Tracker_create(tracker_type)
    else:
        if tracker_type == 'BOOSTING':
            tracker = cv2.TrackerBoosting_create()
            tracker_1 = cv2.TrackerBoosting_create()
        if tracker_type == 'MIL':
            tracker = cv2.TrackerMIL_create()
            tracker_1 = cv2.TrackerMIL_create()
        if tracker_type == 'KCF':
            tracker = cv2.TrackerKCF_create()
            tracker_1 = cv2.TrackerKCF_create()
        if tracker_type == 'TLD':
            tracker = cv2.TrackerTLD_create()
            tracker_1 = cv2.TrackerTLD_create()
        if tracker_type == 'MEDIANFLOW':
            tracker = cv2.TrackerMedianFlow_create()
            tracker_1 = cv2.TrackerMedianFlow_create()
        if tracker_type == 'GOTURN':
            tracker = cv2.TrackerGOTURN_create()
            tracker_1 = cv2.TrackerGOTURN_create()
 
    # Read video
    video = cv2.VideoCapture("p2.mp4")
 
    # Exit if video not opened.
    if not video.isOpened():
        print ("Could not open video")
        sys.exit()
 
    # Read first frame.
    ok, frame = video.read()
    if not ok:
        print ('Cannot read video file')
        sys.exit()
     
    # Define an initial bounding box
    bbox = (287, 23, 86, 320)
    bbox_1 = (287, 23, 86, 320)
    
 
    # Uncomment the line below to select a different bounding box
    bbox = cv2.selectROI(frame, False)
    bbox_1 = cv2.selectROI(frame, False)
    
 
    # Initialize tracker with first frame and bounding box
    ok = tracker.init(frame, bbox)
    ok = tracker_1.init(frame, bbox_1)
    #while loop for first tracker
    while (video.isOpened()):
        # Read a new frame
        ok, frame = video.read()
        if not ok:
            break
         
        # Start timer
        timer = cv2.getTickCount()
 
        # Update tracker
        ok, bbox = tracker.update(frame)
        ok, bbox_1 = tracker_1.update(frame)
 
        # Calculate Frames per second (FPS)
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
 
        # Draw bounding box
        if ok:
            # Tracking success
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            #print(p1,p2)
            cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
            
            p1 = (int(bbox_1[0]), int(bbox_1[1]))
            p2 = (int(bbox_1[0] + bbox_1[2]), int(bbox_1[1] + bbox_1[3]))
            #print(p1,p2)
            cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
        else :
            # Tracking failure
            cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
 
        # Display tracker type on frame
        cv2.putText(frame, tracker_type + " Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2)
     
        # Display FPS on frame
        cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2)
 
        # Display result
        cv2.imshow("Tracking", frame)
 
        # Exit if ESC pressed
        k = cv2.waitKey(1) & 0xff
        if k == 27 : 
            cv2.destroyAllWindows()

"""
    ok = tracker_1.init(frame, bbox_1)
    #while loop for second tracker_1
    while (video.isOpened()):
        # Read a new frame
        ok, frame_1 = video.read()
        if not ok:
            break
         
        # Start timer
        timer_1 = cv2.getTickCount()
 
        # Update tracker
        ok, bbox_1 = tracker_1.update(frame)
 
        # Calculate Frames per second (FPS)
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
 
        # Draw bounding box
        if ok:
            # Tracking success
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            #print(p1,p2)
            cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
            
            p1 = (int(bbox_1[0]), int(bbox_1[1]))
            p2 = (int(bbox_1[0] + bbox_1[2]), int(bbox_1[1] + bbox_1[3]))
            #print(p1,p2)
            cv2.rectangle(frame_1, p1, p2, (255,0,0), 2, 1)
        else :
            # Tracking failure
            cv2.putText(frame_1, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
 
        # Display tracker type on frame
        cv2.putText(frame_1, tracker_type + " Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2)
     
        # Display FPS on frame
        cv2.putText(frame_1, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2)
 
        # Display result
        cv2.imshow("Tracking", frame_1)
 
        # Exit if ESC pressed
        k = cv2.waitKey(1) & 0xff
        if k == 27 : 
            cv2.destroyAllWindows()
"""            