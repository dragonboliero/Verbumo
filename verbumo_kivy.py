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
        self.current_user_word = ''
        print(self.starting_word)
        app_uix = Builder.load_file('verbumo_kivy.kv')
        return app_uix
    def provide_input(self,letter):
        self.root.get_screen('GameScreen').ids.oneone.text = letter
        self.current_user_word = self.current_user_word + letter
        print(self.current_user_word)

    def check_user_word(self):
        if self.current_user_word[0] in self.starting_word:

            if self.current_user_word[0] == self.starting_word[0]:
                self.root.get_screen('GameScreen').ids.oneone.md_bg_color = (0,1,0,1)
            else:
                self.root.get_screen('GameScreen').ids.oneone.md_bg_color = (1,0.8,0,1)
        else:
            self.root.get_screen('GameScreen').ids.oneone.md_bg_color = (0,0,0,1)
    
    def delete_last_user_letter(self):
        if self.current_user_word != '':
            self.current_user_word = self.current_user_word[:-1]
            print(self.current_user_word)

Verbumo().run()