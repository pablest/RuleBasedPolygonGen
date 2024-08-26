import cv2
import numpy as np
import keyboard
from PIL import Image
import os

#constants to control the quality of the drawing
LINE_QUALITY = cv2.LINE_4
LINE_SIZE = 2
MARGIN = 1/6

class FigureShower:

    def __init__(self,fig_name = "N_sides",rules_name = "Turn_Multiplication_(N_N)"):
        self.fig_name = fig_name
        self.rules_name = rules_name


    def show_and_destroy_image(self,img,turn = None):
        #then we show the new figure
        cv2.imshow('Figure', img)
        self.operate_image(img,turn)
        cv2.destroyAllWindows()

    def operate_image(self,img,turn = None):
        #Controls: 
        #any key to get next drawing
        #q quit
        #s save fig 
        while True:
            key = cv2.waitKey(0)
            if key == 115: #if key ==  s
                if turn is None:
                    generated_path = f"images/{self.fig_name}"
                    os.makedirs(generated_path, exist_ok=True)
                    generated_path += f"/{self.rules_name}.png"

                else:
                    generated_path = f"images/{self.fig_name}/{self.rules_name}/"
                    os.makedirs(generated_path, exist_ok=True)
                    generated_path += f"_{turn}.png"

                cv2.imwrite(generated_path, img)
            elif key == 113: #if key == q
                    exit(0)        
            else:
                return

    def show_figure(self,pts):

        #first we center the points to the corner
        pts -= pts.min(axis = 0)
        pts += np.int32(MARGIN*pts.max(axis = 0))

        #then the image that have to cover all points
        img = np.zeros((np.int32(pts[:,1].max()*(1+MARGIN)),np.int32(pts[:,0].max()*(1+MARGIN)),3), np.uint8)

        #construct the polygon
        cv2.circle(img, pts[0], radius=3, color=(255, 255, 255), thickness=-1)
        cv2.polylines(img,np.array([pts]),False,(0,255,255),LINE_SIZE,LINE_QUALITY)

        #show the image
        print("Figure will be generated in another window\nPress q to quit, s to save the figure, and any other key to draw the next side")
        self.show_and_destroy_image(img)
        
    def show_figure_construction(self,pts,change_colors):

        #first we center the points to the corner
        pts -= pts.min(axis = 0)
        pts += np.int32(MARGIN*pts.max(axis = 0))

        #then the image that have to cover all points
        img = np.zeros((np.int32(pts[:,1].max()*(1+MARGIN)),np.int32(pts[:,0].max()*(1+MARGIN)),3), np.uint8)

        #show construction
        cv2.circle(img, pts[0], radius=3, color=(255, 255, 255), thickness=-1)
        last_pt = pts[0]
        print("Figure will be generated in another window\nPress q to quit, s to save the figure, and any other key to draw the next side")

        for turn in range(1,pts.shape[0]):
            #draw the next side
            if(change_colors):
                cv2.polylines(img,np.array([[last_pt,pts[turn]]]),False,(turn*10%255,255,255),LINE_SIZE,LINE_QUALITY)
            else:
                cv2.polylines(img,np.array([[last_pt,pts[turn]]]),False,(0,255,255),LINE_SIZE,LINE_QUALITY)

            #Let the user do whateverer it wants
            cv2.putText(img,f"Turn {turn}", (25,25),cv2.FONT_HERSHEY_SIMPLEX,1, (255,255,255), 1, cv2.LINE_AA)
            cv2.imshow('Figure', img)
            self.operate_image(img,f"Turn_{turn}")
            last_pt = pts[turn]

            #after showing, we delete the TURN text
            cv2.putText(img,f"Turn {turn}", (25,25),cv2.FONT_HERSHEY_SIMPLEX,1, (0,0,0), 1, cv2.LINE_AA)

        self.show_and_destroy_image(img,"Final_turn")