import cv2
import common

class Arrow:
    def __init__(self, point_set):
        self.point_x=[0,0,0,0,0,0,0]
        self.point_y=[0,0,0,0,0,0,0]
        self.distaces=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.distaces_points=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.base_mid=0.0
        self.tip=0
        for i in range (7):
            self.point_x[i]=point_set[i][0][0]
            self.point_y[i]=point_set[i][0][1]

    def get_tip(self,frame):
        '''for i in range(7):
            cv2.putText(frame,str(i)+" "+str(self.point_x[i])+" , "+str(self.point_y[i]),(self.point_x[i],self.point_y[i]),cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8,
                    (255, 255, 255))'''

        #cv2.putText(frame,"0,0",(0,0),cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8,(255, 255, 255))
        #cv2.putText(frame,"100,100",(100,100),cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8,(255, 255, 255))
        #cv2.putText(frame,"200,200",(200,200),cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8,(255, 255, 255))

        distance_index=0

        for i in range(7):
            for j in range(i+1,7):
                self.distaces[distance_index]=common.get_distance(self.point_x[i],self.point_y[i],self.point_x[j],self.point_y[j])
                self.distaces_points[distance_index]=(self.point_x[i],self.point_y[i],self.point_x[j],self.point_y[j])
                distance_index+=1
        max_dis_points1=self.distaces_points.pop(self.distaces.index(max(self.distaces)))
        self.distaces.pop(self.distaces.index(max(self.distaces)))
        max_dis_points2=self.distaces_points.pop(self.distaces.index(max(self.distaces)))

        #print(max_dis_points1)
        #print(max_dis_points2)

        if max_dis_points1[0:2]==max_dis_points2[0:2] :
            self.tip=max_dis_points1[0:2]
            self.base_mid=(int((max_dis_points1[2])+int(max_dis_points2[2]))/2 ,(max_dis_points1[3]+max_dis_points2[3])/2)
            cv2.circle(frame,self.tip, 10, (0,0,255), -1)
            cv2.circle(frame,self.base_mid, 10, (0,255,0), -1)
            #cv2.circle(frame,max_dis_points2[2:4], 10, (255,0,0), -1)

        if max_dis_points1[0:2]==max_dis_points2[2:4]:
            self.tip=max_dis_points1[0:2]
            self.base_mid=(int((max_dis_points1[2])+int(max_dis_points2[0]))/2 ,(max_dis_points1[3]+max_dis_points2[1])/2)
            cv2.circle(frame,self.tip, 10, (0,0,255), -1)
            cv2.circle(frame,self.base_mid, 10, (0,255,0), -1)
            #cv2.circle(frame,max_dis_points2[0:2], 10, (255,0,0), -1)

        if max_dis_points1[2:4]==max_dis_points2[0:2] :
            self.tip=max_dis_points1[2:4]
            self.base_mid=(int((max_dis_points1[0])+int(max_dis_points2[2]))/2 ,(max_dis_points1[1]+max_dis_points2[3])/2)
            cv2.circle(frame,self.tip, 10, (0,0,255), -1)
            cv2.circle(frame,self.base_mid, 10, (0,255,0), -1)
            #cv2.circle(frame,max_dis_points2[2:4], 10, (255,0,0), -1)

        if max_dis_points1[2:4]==max_dis_points2[2:4]:
            self.tip=max_dis_points1[2:4]
            self.base_mid=(int((max_dis_points1[0])+int(max_dis_points2[0]))/2 ,(max_dis_points1[1]+max_dis_points2[1])/2)
            cv2.circle(frame,self.tip, 10, (0,0,255), -1)
            cv2.circle(frame,self.base_mid, 10, (0,255,0), -1)
            #cv2.circle(frame,max_dis_points2[0:2], 10, (255,0,0), -1)