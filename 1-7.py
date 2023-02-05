import pyautogui
import cv2 as cv
import numpy as np
import time
import os

#适用于1920*1080分辨率

def back_home():
    
    time.sleep(5)
    pyautogui.screenshot().save("./screenshot.png")
    temp_img=cv.imread("./screenshot.png")
    home_img=cv.imread("./temp/home.png")
    h,w,c=home_img.shape
    result=cv.matchTemplate(temp_img,home_img,cv.TM_SQDIFF_NORMED)
    min_val,max_val,min_loc,max_loc=cv.minMaxLoc(result)
    if(min_val<0.02):
        print("未在主界面",format(min_val))
        upper_left=cv.minMaxLoc(result)[2]
        lower_right=(upper_left[0]+w,upper_left[1]+h)
        avg=(int((upper_left[0]+lower_right[0])/2),int((upper_left[1]+lower_right[1])/2))
        pyautogui.click(avg)
        time.sleep(1)
        pyautogui.screenshot().save("./screenshot.png")
        temp_img=cv.imread("./screenshot.png")
        home_img=cv.imread("./temp/home2.png")
        h,w,c=home_img.shape
        result=cv.matchTemplate(temp_img,home_img,cv.TM_SQDIFF_NORMED)
        min_val,max_val,min_loc,max_loc=cv.minMaxLoc(result)
        upper_left=cv.minMaxLoc(result)[2]
        lower_right=(upper_left[0]+w,upper_left[1]+h)
        avg=(int((upper_left[0]+lower_right[0])/2),int((upper_left[1]+lower_right[1])/2))
        pyautogui.click(avg)
        os.remove("./screenshot.png")

    else:
        time.sleep(1)
        print("已在主界面，开始执行")

def star():
    time.sleep(2)
    min_val=100
    while(min_val>0.02):
        pyautogui.screenshot().save("./screenshot.png")
        temp_img=cv.imread("./screenshot.png")
        star_img=cv.imread("./temp/star.png")
        h,w,c=star_img.shape
        result=cv.matchTemplate(temp_img,star_img,cv.TM_SQDIFF_NORMED)
        min_val,max_val,min_loc,max_loc=cv.minMaxLoc(result)
        print("检测中",format(min_val))
        os.remove("./screenshot.png")
        time.sleep(1)
    upper_left=cv.minMaxLoc(result)[2]
    lower_right=(upper_left[0]+w,upper_left[1]+h)
    avg=(int((upper_left[0]+lower_right[0])/2),int((upper_left[1]+lower_right[1])/2))
    pyautogui.click(avg)


    time.sleep(1)

    min_val=100
    while(min_val>0.02):
        pyautogui.screenshot().save("./screenshot.png")
        temp_img=cv.imread("./screenshot.png")
        star2_img=cv.imread("./temp/star2.png")
        h,w,c=star2_img.shape
        result=cv.matchTemplate(temp_img,star2_img,cv.TM_SQDIFF_NORMED)
        min_val,max_val,min_loc,max_loc=cv.minMaxLoc(result)
        print("检测中",format(min_val))
        os.remove("./screenshot.png")
        time.sleep(1)
    upper_left=cv.minMaxLoc(result)[2]
    lower_right=(upper_left[0]+w,upper_left[1]+h)
    avg=(int((upper_left[0]+lower_right[0])/2),int((upper_left[1]+lower_right[1])/2))
    pyautogui.click(avg)


    time.sleep(1)

    min_val=100
    while(min_val>0.02):
        pyautogui.screenshot().save("./screenshot.png")
        temp_img=cv.imread("./screenshot.png")
        star3_img=cv.imread("./temp/star3.png")
        h,w,c=star3_img.shape
        result=cv.matchTemplate(temp_img,star3_img,cv.TM_SQDIFF_NORMED)
        min_val,max_val,min_loc,max_loc=cv.minMaxLoc(result)
        print("检测中",format(min_val))
        os.remove("./screenshot.png")
        time.sleep(1)
    upper_left=cv.minMaxLoc(result)[2]
    lower_right=(upper_left[0]+w,upper_left[1]+h)
    avg=(int((upper_left[0]+lower_right[0])/2),int((upper_left[1]+lower_right[1])/2))
    pyautogui.click(avg)


    time.sleep(1)

    min_val=100
    while(min_val>0.02):
        pyautogui.screenshot().save("./screenshot.png")
        temp_img=cv.imread("./screenshot.png")
        star4_img=cv.imread("./temp/star4.png")
        h,w,c=star4_img.shape
        result=cv.matchTemplate(temp_img,star4_img,cv.TM_SQDIFF_NORMED)
        min_val,max_val,min_loc,max_loc=cv.minMaxLoc(result)
        print("检测中",format(min_val))
        os.remove("./screenshot.png")
        time.sleep(1)
    upper_left=cv.minMaxLoc(result)[2]
    lower_right=(upper_left[0]+w,upper_left[1]+h)
    avg=(int((upper_left[0]+lower_right[0])/2),int((upper_left[1]+lower_right[1])/2))
    pyautogui.click(avg)


    time.sleep(1)

    min_val=100
    while(min_val>0.02):
        pyautogui.screenshot().save("./screenshot.png")
        temp_img=cv.imread("./screenshot.png")
        star5_img=cv.imread("./temp/star5.png")
        h,w,c=star5_img.shape
        result=cv.matchTemplate(temp_img,star5_img,cv.TM_SQDIFF_NORMED)
        min_val,max_val,min_loc,max_loc=cv.minMaxLoc(result)
        print("检测中",format(min_val))
        os.remove("./screenshot.png")
        time.sleep(1)
    upper_left=cv.minMaxLoc(result)[2]
    lower_right=(upper_left[0]+w,upper_left[1]+h)
    avg=(int((upper_left[0]+lower_right[0])/2),int((upper_left[1]+lower_right[1])/2))
    pyautogui.click(avg)

    time.sleep(3)

    min_val=100
    while(min_val>0.02):
        pyautogui.screenshot().save("./screenshot.png")
        temp_img=cv.imread("./screenshot.png")
        star6_img=cv.imread("./temp/star6.png")
        h,w,c=star6_img.shape
        result=cv.matchTemplate(temp_img,star6_img,cv.TM_SQDIFF_NORMED)
        min_val,max_val,min_loc,max_loc=cv.minMaxLoc(result)
        print("检测中",format(min_val))
        os.remove("./screenshot.png")
        time.sleep(1)
    upper_left=cv.minMaxLoc(result)[2]
    lower_right=(upper_left[0]+w,upper_left[1]+h)
    avg=(int((upper_left[0]+lower_right[0])/2),int((upper_left[1]+lower_right[1])/2))
    pyautogui.click(avg)

def startmission():

    time.sleep(1)
    min_val=100
    while(min_val>0.02):
        pyautogui.screenshot().save("./screenshot.png")
        temp_img=cv.imread("./screenshot.png")
        star_img=cv.imread("./temp/star_mission.png")
        h,w,c=star_img.shape
        result=cv.matchTemplate(temp_img,star_img,cv.TM_SQDIFF_NORMED)
        min_val,max_val,min_loc,max_loc=cv.minMaxLoc(result)
        print("检测中",format(min_val))
        os.remove("./screenshot.png")
        time.sleep(1)
    upper_left=cv.minMaxLoc(result)[2]
    lower_right=(upper_left[0]+w,upper_left[1]+h)
    avg=(int((upper_left[0]+lower_right[0])/2),int((upper_left[1]+lower_right[1])/2))
    pyautogui.click(avg)
    time.sleep(1)


    if(check_san()==1):
        return 1                        #返回1，代表理智不足
    else:       
        time.sleep(2)
        pyautogui.screenshot().save("./screenshot.png")
        temp_img=cv.imread("./screenshot.png")
        star_img=cv.imread("./temp/OPERATION_START.png")
        h,w,c=star_img.shape
        result=cv.matchTemplate(temp_img,star_img,cv.TM_SQDIFF_NORMED)
        upper_left=cv.minMaxLoc(result)[2]
        lower_right=(upper_left[0]+w,upper_left[1]+h)
        avg=(int((upper_left[0]+lower_right[0])/2),int((upper_left[1]+lower_right[1])/2))
        pyautogui.click(avg)
        os.remove("./screenshot.png")

        #等待战斗结束
        min_val=100
        while(min_val>0.02):
            print("等待战斗结束")
            print(min_val)
            pyautogui.screenshot().save("./screenshot.png")
            temp_img=cv.imread("./screenshot.png")
            finish_img=cv.imread("./temp/mission_complete.png")
            result=cv.matchTemplate(temp_img,finish_img,cv.TM_SQDIFF_NORMED)
            min_val,max_val,min_loc,max_loc=cv.minMaxLoc(result)
            os.remove("./screenshot.png")
            time.sleep(2)
        pyautogui.click(avg)
        print("战斗结束")
        time.sleep(3)
        return 0                        #返回0，代表理智足够并且战斗结束

def check_san():
    pyautogui.screenshot().save("./screenshot.png")
    temp_img=cv.imread("./screenshot.png")
    check_img=cv.imread("./temp/medice.png")
    h,w,c=check_img.shape
    result=cv.matchTemplate(temp_img,check_img,cv.TM_SQDIFF_NORMED)
    min_val,max_val,min_loc,max_loc=cv.minMaxLoc(result)
    if(min_val>0.02):
        print("理智足够")
        return 0
    else:
        print("理智不足")
        os.remove("./screenshot.png")
        return 1



back_home()
star()
while(startmission()==0):
    if(startmission()==1):
        break
print("完成任务")


