import cv2
import numpy as np
import keyboard
from PIL import Image
import os

#constants to control the quality of the drawing and resolution
LINE_QUALITY = cv2.LINE_8
LINE_SIZE = 2
MARGIN_PERCENTAGE = 1/8
WANTED_RESOLUTION = (1200,700) #the wanted width and heigth, to mantain proportion, the resulting figure will have one of the width or heigth and the other meassurment will be less than the wanted

class FigureShower:

    def __init__(self,fig_name = "N_sides",rules_name = "Turn_Multiplication_(N_N)"):
        self.fig_name = fig_name
        self.rules_name = rules_name

    def resize_image(self,img):
        #function to resize the image to the wanted width and heigth, 
        #to mantain proportion, the resulting figure will have one of the width or heigth and the other meassurment will be less than the wanted

        img_height, img_width = img.shape[:2]
        if(img_width/img_height > WANTED_RESOLUTION[0]/WANTED_RESOLUTION[1]):
             img = cv2.resize(img, (WANTED_RESOLUTION[0],int(img_height*WANTED_RESOLUTION[0]/img_width)), interpolation=cv2.INTER_CUBIC)
        else:
            img = cv2.resize(img, (int(img_width*WANTED_RESOLUTION[1]/img_height),WANTED_RESOLUTION[1]), interpolation=cv2.INTER_CUBIC)
        return img
    
    def show_and_destroy_image(self,img,turn = None):
        #first resize the image to the wanted resolution
        img = self.resize_image(img)

        #then we show the new figure
        cv2.imshow('Figure', img)
        self.operate_image(img,turn)
        cv2.destroyAllWindows()

    def operate_image(self,img,turn = None):
        #Controls: 
        #any key to get next drawing
        #q quit
        #s save fig 

        #show the image and make the controls functional
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
        pts += np.int32(MARGIN_PERCENTAGE*pts.max(axis = 0))

        #then the image that have to cover all points
        img = np.zeros((np.int32(pts[:,1].max()*(1+MARGIN_PERCENTAGE)),np.int32(pts[:,0].max()*(1+MARGIN_PERCENTAGE)),3), np.uint8)

        #construct the polygon
        cv2.polylines(img,np.array([pts]),False,(0,255,255),LINE_SIZE,LINE_QUALITY)

        #show the image
        print("Figure will be generated in another window\nPress q to quit, s to save the figure, and any other key to draw the next side")
        self.show_and_destroy_image(img)
        
    def show_figure_construction(self,pts,change_colors):

        #first we center the points to the corner
        pts -= pts.min(axis = 0)
        pts += np.int32(MARGIN_PERCENTAGE*pts.max(axis = 0))

        #then the image that have to cover all points
        img = np.zeros((np.int32(pts[:,1].max()*(1+MARGIN_PERCENTAGE)),np.int32(pts[:,0].max()*(1+MARGIN_PERCENTAGE)),3), np.uint8)
        
        #show construction
        last_pt = pts[0]
        print("Figure will be generated in another window\nPress q to quit, s to save the figure, and any other key to draw the next side")

        for turn in range(1,pts.shape[0]):
            #draw the next side
            if(change_colors):
                cv2.polylines(img,np.array([[last_pt,pts[turn]]]),False,(turn*10%255,255,255),LINE_SIZE,LINE_QUALITY)
            else:
                cv2.polylines(img,np.array([[last_pt,pts[turn]]]),False,(0,255,255),LINE_SIZE,LINE_QUALITY)

            #resize the image
            resized_img = self.resize_image(img)

            #Put the TURN text
            texted_img = resized_img.copy()
            cv2.putText(texted_img,f"Turn {turn}", (25,25),cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255), 1, cv2.LINE_AA)

            #show and let the user operate the image
            cv2.imshow('Figure', texted_img)
            self.operate_image(texted_img,f"Turn_{turn}")
            last_pt = pts[turn]

        self.show_and_destroy_image(texted_img,"Final_turn")