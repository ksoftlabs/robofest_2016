import cv2
import arr

def release_cam():
    cap.release()
    cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)
cv2.namedWindow("Frame")

while(1):


    __,img = cap.read()
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,127,255,0)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        if cv2.contourArea(cnt)>1000 and cv2.contourArea(cnt)<30000:
            #print(cv2.contourArea(cnt))
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.01 * peri,True)
            if len(approx)==7:
                cv2.drawContours(img, [approx], -1, (255, 0, 0), 2)
                #print(str(approx))
                arrow=arr.Arrow(approx)
                arrow.get_tip(img)
                #cv2.putText(img, str(approx), (5,50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8,(255, 255, 255)
                #cv2.circle(img,arr.get_tip(approx), 10, (0,0,255), -1)

    cv2.imshow('Frame',img)

    k = cv2.waitKey(50) & 0xFF
    if k == 27:
        break
release_cam()