"""
Author : 이상헌
2021.06.16.
고양이 사진 다운받는 프로그램
"""

import time
import pywinmacro as pw

location = (187,341)
location2 = (689,271)
location3 = (770,477)
location4 = (867,184)

def scrap():
    pw.click(location)
    pw.key_press_once("tab")
    pw.type_in("고양이")
    time.sleep(1)
    pw.key_press_once("enter")
    time.sleep(1)
    for i in range(13):
        pw.key_press_once("tab")
        time.sleep(0.1)
    pw.key_press_once("enter")
    time.sleep(3)
    for i in range(29):
        pw.key_press_once("tab")
        time.sleep(0.1)
    pw.key_press_once("enter")
    time.sleep(3)
    downloads()


def downloads():
    while True:
        pw.right_click(location2)
        time.sleep(0.5)
        pw.click(location3)
        time.sleep(1)
        pw.key_press_once("enter")
        time.sleep(3)
        pw.click(location4)
        time.sleep(3)


scrap()
