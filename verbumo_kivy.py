from kivymd.app import MDApp
from kivy.lang.builder import Builder   
from kivy.uix.screenmanager  import Screen,ScreenManager
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
import functions as func

class GridSquare(MDLabel):
    pass

class SManager(ScreenManager):
    pass

class GameScreen(Screen):
    pass

class Verbumo (MDApp):
    def build(self):
        self.current_word = func.pick_random_word('5')
        self.dictionary = func.words_dictionary('5')
        self.current_user_word = ''
        self.score = 0
        self.line_position = 1
        print(self.current_word)
        app_uix = Builder.load_file('verbumo_kivy.kv')
        return app_uix
    def provide_input(self,letter):
        if self.line_position < 6:
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

            
            self.current_user_word = self.current_user_word + letter
            self.line_position += 1

    def check_user_word(self):
        #If the word has correct length
        print(self.line_position)
        if self.line_position == 6:
            if self.current_user_word == self.current_word:
                correct_word = MDDialog(text='Hasło odgadnięte!')
                correct_word.open()
                self.score +=100
                self.root.get_screen('GameScreen').ids.score.text = str(self.score)
                self.current_word = func.pick_random_word('5')
                print(self.current_word)
            else:
                #And it's in the dictionary
                if self.current_user_word in self.dictionary:
                    #Check letters with correct answer and assign appropriate background color to it.
                    for letter_index in range (self.line_position-1):
                        if self.current_user_word[letter_index] in self.current_word:

                            if self.current_user_word[letter_index] == self.current_word[letter_index]:
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
                    #If the word is not in the dictionary.
                else:
                    word_not_in_dictionary = MDDialog(text='Słowo nie znajduje się w słowniku! Podaj poprawne słowo.')
                    word_not_in_dictionary.open()
        #If the word is shorter than 5 letters.
        else:
            word_not_complete = MDDialog(text='Słowo musi składać się z 5 liter!')
            word_not_complete.open()
            
    
    def delete_last_user_letter(self):
        if self.line_position > 1:
            self.line_position -= 1
            print(self.line_position)
            self.current_user_word = self.current_user_word[:-1]
            if self.line_position == 2:
                self.root.get_screen('GameScreen').ids.letter2line1.text = ''
                self.root.get_screen('GameScreen').ids.letter2line1.md_bg_color = (0,0,0,0)
            if self.line_position == 3:
                self.root.get_screen('GameScreen').ids.letter3line1.text = ''
                self.root.get_screen('GameScreen').ids.letter3line1.md_bg_color = (0,0,0,0)
            if self.line_position == 4:
                self.root.get_screen('GameScreen').ids.letter4line1.text = ''
                self.root.get_screen('GameScreen').ids.letter4line1.md_bg_color = (0,0,0,0)
            if self.line_position == 5:
                self.root.get_screen('GameScreen').ids.letter5line1.text = ''
                self.root.get_screen('GameScreen').ids.letter5line1.md_bg_color = (0,0,0,0)

        if self.line_position == 1:
            self.root.get_screen('GameScreen').ids.letter1line1.text = ''
            self.root.get_screen('GameScreen').ids.letter1line1.md_bg_color = (0,0,0,0)

Verbumo().run()