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
        self.line_position = 1
        print(self.starting_word)
        app_uix = Builder.load_file('verbumo_kivy.kv')
        return app_uix
    def provide_input(self,letter):
        if self.line_position == 1:
            self.root.get_screen('GameScreen').ids.letter1line1.text = letter
        if self.line_position == 2:
            self.root.get_screen('GameScreen').ids.letter2line1.text = letter
        if self.line_position == 3:
            self.root.get_screen('GameScreen').ids.letter3line1.text = letter
        if self.line_position == 4:
            self.root.get_screen('GameScreen').ids.letter4line1.text = letter
        if self.line_position == 5:
            self.root.get_screen('GameScreen').ids.letter5line1.text = letter

        if self.line_position < 6:
            self.current_user_word = self.current_user_word + letter
            self.line_position += 1

    def check_user_word(self):
        for letter_index in range (self.line_position-1):
            if self.current_user_word[letter_index] in self.starting_word:

                if self.current_user_word[letter_index] == self.starting_word[letter_index]:
                    if letter_index+1 == 1:
                        self.root.get_screen('GameScreen').ids.letter1line1.md_bg_color = (0,1,0,1)
                    if letter_index+1 == 2:
                        self.root.get_screen('GameScreen').ids.letter2line1.md_bg_color = (0,1,0,1)
                    if letter_index+1 == 3:
                        self.root.get_screen('GameScreen').ids.letter3line1.md_bg_color = (0,1,0,1)
                    if letter_index+1 == 4:
                        self.root.get_screen('GameScreen').ids.letter4line1.md_bg_color = (0,1,0,1)
                    if letter_index+1 == 5:
                        self.root.get_screen('GameScreen').ids.letter5line1.md_bg_color = (0,1,0,1)
                else:
                    if letter_index+1 == 1:
                        self.root.get_screen('GameScreen').ids.letter1line1.md_bg_color = (1,0.8,0,1)
                    if letter_index+1 == 2:
                        self.root.get_screen('GameScreen').ids.letter2line1.md_bg_color = (1,0.8,0,1)
                    if letter_index+1 == 3:
                        self.root.get_screen('GameScreen').ids.letter3line1.md_bg_color = (1,0.8,0,1)
                    if letter_index+1 == 4:
                        self.root.get_screen('GameScreen').ids.letter4line1.md_bg_color = (1,0.8,0,1)
                    if letter_index+1 == 5:
                        self.root.get_screen('GameScreen').ids.letter5line1.md_bg_color = (1,0.8,0,1)
            else:
                if letter_index+1 == 1:
                        self.root.get_screen('GameScreen').ids.letter1line1.md_bg_color = (0,0,0,1)                
                if letter_index+1 == 2:
                        self.root.get_screen('GameScreen').ids.letter2line1.md_bg_color = (0,0,0,1)
                if letter_index+1 == 3:
                        self.root.get_screen('GameScreen').ids.letter3line1.md_bg_color = (0,0,0,1)
                if letter_index+1 == 4:
                        self.root.get_screen('GameScreen').ids.letter4line1.md_bg_color = (0,0,0,1)
                if letter_index+1 == 5:
                        self.root.get_screen('GameScreen').ids.letter5line1.md_bg_color = (0,0,0,1)
            
    
    def delete_last_user_letter(self):
        if self.current_user_word != '':
            self.current_user_word = self.current_user_word[:-1]
            if self.line_position > 1:
                self.line_position -=1
            print(self.current_user_word)

Verbumo().run()