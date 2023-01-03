from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.boxlayout import MDBoxLayout


KV = '''
MDBoxLayout:
    orientation: "vertical"

    MDTopAppBar:
        title: "Расчет прочности зубчатых колес"

    MDTabs:
        Tab:
            title:"Ввод данных"
            MDGridLayout:
                cols:2
                rows:5
                spacing:30
                padding:20
                
                MDTextField:
                    id: tf_m
                    size_hint_x:None 
                    width:100
                    hint_text: "Модуль"
                    helper_text: "This will disappear when you click off"
                    helper_text_mode: "on_focus"
                    
                
                MDTextField:
                    id: tf_z1
                    size_hint_x:None 
                    width:100
                    hint_text: "Z1"
                    helper_text: "Число зубьев"
                    helper_text_mode: "on_focus"
                    
                MDTextField:
                    id: tf_z2
                    size_hint_x:None 
                    width:100
                    hint_text: "Z2"
                    helper_text: "Число зубьев"
                    helper_text_mode: "on_focus"
                    
                MDTextField:
                    id: tf_m
                    size_hint_x:None 
                    width:100
                    hint_text: "X1"
                    helper_text: "This will disappear when you click off"
                    helper_text_mode: "on_focus"
                
                MDTextField:
                    id: tf_z1
                    size_hint_x:None 
                    width:100
                    hint_text: "X2"
                    helper_text: "Число зубьев"
                    helper_text_mode: "on_focus"
                    
                MDTextField:
                    id: tf_z2
                    size_hint_x:None 
                    width:100
                    hint_text: "h1ka"
                    helper_text: "Число зубьев"
                    helper_text_mode: "on_focus"
                    
                MDTextField:
                    id: tf_m
                    size_hint_x:None 
                    width:100
                    hint_text: "h2ka"
                    helper_text: "This will disappear when you click off"
                    helper_text_mode: "on_focus"
                
                
        Tab:
            title:"Результат"
            MDBoxLayout:
                orientation: "vertical"
                MDTextField:
                    id: tf_m
                    size_hint_x:None 
                    width:100
                    hint_text: "Число"
                    helper_text: "Чисто проверка"
                    helper_text_mode: "on_focus"
'''


class Tab(MDFloatLayout, MDTabsBase):
    pass


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)



Example().run()