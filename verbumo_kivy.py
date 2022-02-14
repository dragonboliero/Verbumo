from kivymd.app import MDApp
from kivy.lang.builder import Builder   
from kivy.uix.screenmanager  import Screen,ScreenManager
from kivymd.uix.label import MDLabel
import functions as func

class GridSquare(MDLabel):
    pass

class SManager(ScreenManager):
    pass

class GameScreen(Screen):
    pass

class Verbumo (MDApp):
    def build(self):
        self.starting_word = func.pick_random_word('5')
        print(self.starting_word)
        app_uix = Builder.load_file('verbumo_kivy.kv')
        return app_uix

Verbumo().run()