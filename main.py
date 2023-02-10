import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget
from kivy.lang import Builder
from random import choice
import random




#Defining screens
class MainWindow(Screen):
    pass

#FIRST WINDOW
class FirstWindow_1(Screen):
    pass

class FirstWindow_2(Screen):
    pass

class FirstWindow_3(Screen):
    pass

class FirstWindow_4(Screen):
    pass

class FirstWindow_5(Screen):
    pass

class FirstWindow_6(Screen):
    pass

class FirstWindow_7(Screen):
    pass

class FirstWindow_8(Screen):
    pass

class FirstWindow_9(Screen):
    pass

class FirstWindow_10(Screen):
    pass

class FirstWindow_11(Screen):
    pass

class FirstWindow_12(Screen):
    pass

class FirstWindow_13(Screen):
    pass

class FirstWindow_14(Screen):
    pass

class FirstWindow_15(Screen):
    pass

class FirstWindow_16(Screen):
    pass

class FirstWindow_17(Screen):
    pass

class FirstWindow_18(Screen):
    pass

class FirstWindow_19(Screen):
    pass

class FirstWindow_20(Screen):
    pass

class FirstWindow_21(Screen):
    pass

class FirstWindow_22(Screen):
    pass

class FirstWindow_23(Screen):
    pass

class FirstWindow_24(Screen):
    pass

class FirstWindow_25(Screen):
    pass

class FirstWindow_26(Screen):
    pass

class FirstWindow_27(Screen):
    pass

class FirstWindow_28(Screen):
    pass

class FirstWindow_29(Screen):
    pass

class FirstWindow_30(Screen):
    pass

class FirstWindow_31(Screen):
    pass

class FirstWindow_32(Screen):
    pass

class FirstWindow_33(Screen):
    pass

class FirstWindow_34(Screen):
    pass






#SECOND WINDOWS
class SecondWindow_1(Screen):
    pass

class SecondWindow_2(Screen):
    pass

class SecondWindow_3(Screen):
    pass

class SecondWindow_4(Screen):
    pass

class SecondWindow_5(Screen):
    pass

class SecondWindow_6(Screen):
    pass

class SecondWindow_7(Screen):
    pass

class SecondWindow_8(Screen):
    pass

class SecondWindow_9(Screen):
    pass

class SecondWindow_10(Screen):
    pass


    pass

#THIRD WINDOWS
class ThirdWindow_1(Screen):
    pass

class ThirdWindow_2(Screen):
    pass

class ThirdWindow_3(Screen):
    pass

class ThirdWindow_4(Screen):
    pass

class ThirdWindow_5(Screen):
    pass

class ThirdWindow_6(Screen):
    pass

class ThirdWindow_7(Screen):
    pass

class ThirdWindow_8(Screen):
    pass

class ThirdWindow_9(Screen):
    pass

class ThirdWindow_10(Screen):
    pass

class ThirdWindow_11(Screen):
    pass

class ThirdWindow_12(Screen):
    pass


    




class ScreenManager(ScreenManager):
    pass

kv = Builder.load_file('styl.kv')

class FinalApp(App):
    def build(self):
        return kv

if __name__ == '__main__':
    FinalApp().run()
