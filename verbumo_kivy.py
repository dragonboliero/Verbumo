"""
To do list:
    *Make keyboard keys change color when a letter is not resent in the 
    current word.
    *Score modifiers depending on user answers. The more correct 
    letters in earlier tries te more points.
"""

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
        self.current_line = 1
        self.dictionary = func.words_dictionary('5')
        self.current_user_word = ''
        self.score = 0
        self.line_position = 1
        print(self.current_word)
        app_uix = Builder.load_file('verbumo_kivy.kv')
        return app_uix
    def provide_input(self,letter):
        #If not all letters have been filled
        if self.line_position < 6:
            #If the user is in the first line
            if self.current_line == 1:
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
            #If the user is in the second line
            if self.current_line == 2:
                if self.line_position == 1:
                    self.root.get_screen('GameScreen').ids.letter1line2.text = letter
                if self.line_position == 2:
                    self.root.get_screen('GameScreen').ids.letter2line2.text = letter
                if self.line_position == 3:
                    self.root.get_screen('GameScreen').ids.letter3line2.text = letter
                if self.line_position == 4:
                    self.root.get_screen('GameScreen').ids.letter4line2.text = letter
                if self.line_position == 5:
                    self.root.get_screen('GameScreen').ids.letter5line2.text = letter
            #If the user is in the third line
            if self.current_line == 3:
                if self.line_position == 1:
                    self.root.get_screen('GameScreen').ids.letter1line3.text = letter
                if self.line_position == 2:
                    self.root.get_screen('GameScreen').ids.letter2line3.text = letter
                if self.line_position == 3:
                    self.root.get_screen('GameScreen').ids.letter3line3.text = letter
                if self.line_position == 4:
                    self.root.get_screen('GameScreen').ids.letter4line3.text = letter
                if self.line_position == 5:
                    self.root.get_screen('GameScreen').ids.letter5line3.text = letter
            #If user is in the fourth line
            if self.current_line == 4:
                if self.line_position == 1:
                    self.root.get_screen('GameScreen').ids.letter1line4.text = letter
                if self.line_position == 2:
                    self.root.get_screen('GameScreen').ids.letter2line4.text = letter
                if self.line_position == 3:
                    self.root.get_screen('GameScreen').ids.letter3line4.text = letter
                if self.line_position == 4:
                    self.root.get_screen('GameScreen').ids.letter4line4.text = letter
                if self.line_position == 5:
                    self.root.get_screen('GameScreen').ids.letter5line4.text = letter
            #If user is in the fifth line
            if self.current_line == 5:
                if self.line_position == 1:
                    self.root.get_screen('GameScreen').ids.letter1line5.text = letter
                if self.line_position == 2:
                    self.root.get_screen('GameScreen').ids.letter2line5.text = letter
                if self.line_position == 3:
                    self.root.get_screen('GameScreen').ids.letter3line5.text = letter
                if self.line_position == 4:
                    self.root.get_screen('GameScreen').ids.letter4line5.text = letter
                if self.line_position == 5:
                    self.root.get_screen('GameScreen').ids.letter5line5.text = letter
            #If the user is in the sixth line
            if self.current_line == 6:
                if self.line_position == 1:
                    self.root.get_screen('GameScreen').ids.letter1line6.text = letter
                if self.line_position == 2:
                    self.root.get_screen('GameScreen').ids.letter2line6.text = letter
                if self.line_position == 3:
                    self.root.get_screen('GameScreen').ids.letter3line6.text = letter
                if self.line_position == 4:
                    self.root.get_screen('GameScreen').ids.letter4line6.text = letter
                if self.line_position == 5:
                    self.root.get_screen('GameScreen').ids.letter5line6.text = letter

            self.current_user_word = self.current_user_word + letter
            self.line_position += 1

    #Clears all lines from all user input
    def clear_table(self):
        #First line
        self.root.get_screen('GameScreen').ids.letter1line1.md_bg_color = (1,1,1,0)
        self.root.get_screen('GameScreen').ids.letter1line1.text = ''
        self.root.get_screen('GameScreen').ids.letter2line1.md_bg_color = (1,1,1,0)
        self.root.get_screen('GameScreen').ids.letter2line1.text = ''
        self.root.get_screen('GameScreen').ids.letter3line1.md_bg_color = (1,1,1,0)
        self.root.get_screen('GameScreen').ids.letter3line1.text = ''
        self.root.get_screen('GameScreen').ids.letter4line1.md_bg_color = (1,1,1,0)
        self.root.get_screen('GameScreen').ids.letter4line1.text = ''
        self.root.get_screen('GameScreen').ids.letter5line1.md_bg_color = (1,1,1,0)
        self.root.get_screen('GameScreen').ids.letter5line1.text = ''
        #Second line
        self.root.get_screen('GameScreen').ids.letter1line2.md_bg_color = (1,1,1,0)
        self.root.get_screen('GameScreen').ids.letter1line2.text = ''
        self.root.get_screen('GameScreen').ids.letter2line2.md_bg_color = (1,1,1,0)
        self.root.get_screen('GameScreen').ids.letter2line2.text = ''
        self.root.get_screen('GameScreen').ids.letter3line2.md_bg_color = (1,1,1,0)
        self.root.get_screen('GameScreen').ids.letter3line2.text = ''
        self.root.get_screen('GameScreen').ids.letter4line2.md_bg_color = (1,1,1,0)
        self.root.get_screen('GameScreen').ids.letter4line2.text = ''
        self.root.get_screen('GameScreen').ids.letter5line2.md_bg_color = (1,1,1,0)
        self.root.get_screen('GameScreen').ids.letter5line2.text = ''
        #Third line
        self.root.get_screen('GameScreen').ids.letter1line3.md_bg_color = (1,1,1,0)
        self.root.get_screen('GameScreen').ids.letter1line3.text = ''
        self.root.get_screen('GameScreen').ids.letter2line3.md_bg_color = (1,1,1,0)
        self.root.get_screen('GameScreen').ids.letter2line3.text = ''
        self.root.get_screen('GameScreen').ids.letter3line3.md_bg_color = (1,1,1,0)
        self.root.get_screen('GameScreen').ids.letter3line3.text = ''
        self.root.get_screen('GameScreen').ids.letter4line3.md_bg_color = (1,1,1,0)
        self.root.get_screen('GameScreen').ids.letter4line3.text = ''
        self.root.get_screen('GameScreen').ids.letter5line3.md_bg_color = (1,1,1,0)
        self.root.get_screen('GameScreen').ids.letter5line3.text = ''
        #Fourth line
        self.root.get_screen('GameScreen').ids.letter1line4.md_bg_color = (1,1,1,0)
        self.root.get_screen('GameScreen').ids.letter1line4.text = ''
        self.root.get_screen('GameScreen').ids.letter2line4.md_bg_color = (1,1,1,0)
        self.root.get_screen('GameScreen').ids.letter2line4.text = ''
        self.root.get_screen('GameScreen').ids.letter3line4.md_bg_color = (1,1,1,0)
        self.root.get_screen('GameScreen').ids.letter3line4.text = ''
        self.root.get_screen('GameScreen').ids.letter4line4.md_bg_color = (1,1,1,0)
        self.root.get_screen('GameScreen').ids.letter4line4.text = ''
        self.root.get_screen('GameScreen').ids.letter5line4.md_bg_color = (1,1,1,0)
        self.root.get_screen('GameScreen').ids.letter5line4.text = ''
        #Fifth line
        self.root.get_screen('GameScreen').ids.letter1line5.md_bg_color = (1,1,1,0)
        self.root.get_screen('GameScreen').ids.letter1line5.text = ''
        self.root.get_screen('GameScreen').ids.letter2line5.md_bg_color = (1,1,1,0)
        self.root.get_screen('GameScreen').ids.letter2line5.text = ''
        self.root.get_screen('GameScreen').ids.letter3line5.md_bg_color = (1,1,1,0)
        self.root.get_screen('GameScreen').ids.letter3line5.text = ''
        self.root.get_screen('GameScreen').ids.letter4line5.md_bg_color = (1,1,1,0)
        self.root.get_screen('GameScreen').ids.letter4line5.text = ''
        self.root.get_screen('GameScreen').ids.letter5line5.md_bg_color = (1,1,1,0)
        self.root.get_screen('GameScreen').ids.letter5line5.text = ''
        #Sixth line
        self.root.get_screen('GameScreen').ids.letter1line6.md_bg_color = (1,1,1,0)
        self.root.get_screen('GameScreen').ids.letter1line6.text = ''
        self.root.get_screen('GameScreen').ids.letter2line6.md_bg_color = (1,1,1,0)
        self.root.get_screen('GameScreen').ids.letter2line6.text = ''
        self.root.get_screen('GameScreen').ids.letter3line6.md_bg_color = (1,1,1,0)
        self.root.get_screen('GameScreen').ids.letter3line6.text = ''
        self.root.get_screen('GameScreen').ids.letter4line6.md_bg_color = (1,1,1,0)
        self.root.get_screen('GameScreen').ids.letter4line6.text = ''
        self.root.get_screen('GameScreen').ids.letter5line6.md_bg_color = (1,1,1,0)
        self.root.get_screen('GameScreen').ids.letter5line6.text = ''


    def check_user_word(self):
        #If the word has correct length
        print(f'letter position {self.line_position},line position {self.current_line}, user word {self.current_user_word}')
        if self.line_position == 6:
            if self.current_user_word == self.current_word:
                correct_word = MDDialog(text='Hasło odgadnięte!')
                correct_word.open()
                self.score +=100
                self.root.get_screen('GameScreen').ids.score.text = str(self.score)
                self.current_word = func.pick_random_word('5')
                self.clear_table()
                print(self.current_word)
            else:
                #And it's in the dictionary
                if self.current_user_word in self.dictionary:
                    #If the answer in the last line was wrong
                    if self.current_line == 6:
                        lost_dialog = f'Porażka, prawidłową odpowiedzią było słowo: {self.current_word}'
                        word_lost = MDDialog(text=lost_dialog)
                        word_lost.open()
                        self.current_word = func.pick_random_word('5')
                        self.clear_table()
                        print(self.current_word)
                    #Check letters with correct answer and assign appropriate background color to it.
                    for letter_index in range (self.line_position-1):
                        if self.current_user_word[letter_index] in self.current_word:
                            #If currently checked letter is in the answer in the same position
                            if self.current_user_word[letter_index] == self.current_word[letter_index]:
                                if self.current_line == 1:
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

                                if self.current_line == 2:
                                    if letter_index+1 == 1:
                                        self.root.get_screen('GameScreen').ids.letter1line2.md_bg_color = (0,1,0,1)
                                    if letter_index+1 == 2:
                                        self.root.get_screen('GameScreen').ids.letter2line2.md_bg_color = (0,1,0,1)
                                    if letter_index+1 == 3:
                                        self.root.get_screen('GameScreen').ids.letter3line2.md_bg_color = (0,1,0,1)
                                    if letter_index+1 == 4:
                                        self.root.get_screen('GameScreen').ids.letter4line2.md_bg_color = (0,1,0,1)
                                    if letter_index+1 == 5:
                                        self.root.get_screen('GameScreen').ids.letter5line2.md_bg_color = (0,1,0,1)

                                if self.current_line == 3:
                                    if letter_index+1 == 1:
                                        self.root.get_screen('GameScreen').ids.letter1line3.md_bg_color = (0,1,0,1)
                                    if letter_index+1 == 2:
                                        self.root.get_screen('GameScreen').ids.letter2line3.md_bg_color = (0,1,0,1)
                                    if letter_index+1 == 3:
                                        self.root.get_screen('GameScreen').ids.letter3line3.md_bg_color = (0,1,0,1)
                                    if letter_index+1 == 4:
                                        self.root.get_screen('GameScreen').ids.letter4line3.md_bg_color = (0,1,0,1)
                                    if letter_index+1 == 5:
                                        self.root.get_screen('GameScreen').ids.letter5line3.md_bg_color = (0,1,0,1)

                                if self.current_line == 4:
                                    if letter_index+1 == 1:
                                        self.root.get_screen('GameScreen').ids.letter1line4.md_bg_color = (0,1,0,1)
                                    if letter_index+1 == 2:
                                        self.root.get_screen('GameScreen').ids.letter2line4.md_bg_color = (0,1,0,1)
                                    if letter_index+1 == 3:
                                        self.root.get_screen('GameScreen').ids.letter3line4.md_bg_color = (0,1,0,1)
                                    if letter_index+1 == 4:
                                        self.root.get_screen('GameScreen').ids.letter4line4.md_bg_color = (0,1,0,1)
                                    if letter_index+1 == 5:
                                        self.root.get_screen('GameScreen').ids.letter5line4.md_bg_color = (0,1,0,1)
                                
                                if self.current_line == 5:
                                    if letter_index+1 == 1:
                                        self.root.get_screen('GameScreen').ids.letter1line5.md_bg_color = (0,1,0,1)
                                    if letter_index+1 == 2:
                                        self.root.get_screen('GameScreen').ids.letter2line5.md_bg_color = (0,1,0,1)
                                    if letter_index+1 == 3:
                                        self.root.get_screen('GameScreen').ids.letter3line5.md_bg_color = (0,1,0,1)
                                    if letter_index+1 == 4:
                                        self.root.get_screen('GameScreen').ids.letter4line5.md_bg_color = (0,1,0,1)
                                    if letter_index+1 == 5:
                                        self.root.get_screen('GameScreen').ids.letter5line5.md_bg_color = (0,1,0,1)

                                if self.current_line == 6:
                                    if letter_index+1 == 1:
                                        self.root.get_screen('GameScreen').ids.letter1line6.md_bg_color = (0,1,0,1)
                                    if letter_index+1 == 2:
                                        self.root.get_screen('GameScreen').ids.letter2line6.md_bg_color = (0,1,0,1)
                                    if letter_index+1 == 3:
                                        self.root.get_screen('GameScreen').ids.letter3line6.md_bg_color = (0,1,0,1)
                                    if letter_index+1 == 4:
                                        self.root.get_screen('GameScreen').ids.letter4line6.md_bg_color = (0,1,0,1)
                                    if letter_index+1 == 5:
                                        self.root.get_screen('GameScreen').ids.letter5line6.md_bg_color = (0,1,0,1)
                            #If the currently checked letter is in the answer but in different position
                            else:
                                if self.current_line == 1:
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

                                if self.current_line == 2:
                                    if letter_index+1 == 1:
                                        self.root.get_screen('GameScreen').ids.letter1line2.md_bg_color = (1,0.8,0,1)
                                    if letter_index+1 == 2:
                                        self.root.get_screen('GameScreen').ids.letter2line2.md_bg_color = (1,0.8,0,1)
                                    if letter_index+1 == 3:
                                        self.root.get_screen('GameScreen').ids.letter3line2.md_bg_color = (1,0.8,0,1)
                                    if letter_index+1 == 4:
                                        self.root.get_screen('GameScreen').ids.letter4line2.md_bg_color = (1,0.8,0,1)
                                    if letter_index+1 == 5:
                                        self.root.get_screen('GameScreen').ids.letter5line2.md_bg_color = (1,0.8,0,1)

                                if self.current_line == 3:
                                    if letter_index+1 == 1:
                                        self.root.get_screen('GameScreen').ids.letter1line3.md_bg_color = (1,0.8,0,1)
                                    if letter_index+1 == 2:
                                        self.root.get_screen('GameScreen').ids.letter2line3.md_bg_color = (1,0.8,0,1)
                                    if letter_index+1 == 3:
                                        self.root.get_screen('GameScreen').ids.letter3line3.md_bg_color = (1,0.8,0,1)
                                    if letter_index+1 == 4:
                                        self.root.get_screen('GameScreen').ids.letter4line3.md_bg_color = (1,0.8,0,1)
                                    if letter_index+1 == 5:
                                        self.root.get_screen('GameScreen').ids.letter5line3.md_bg_color = (1,0.8,0,1)

                                if self.current_line == 4:
                                    if letter_index+1 == 1:
                                        self.root.get_screen('GameScreen').ids.letter1line4.md_bg_color = (1,0.8,0,1)
                                    if letter_index+1 == 2:
                                        self.root.get_screen('GameScreen').ids.letter2line4.md_bg_color = (1,0.8,0,1)
                                    if letter_index+1 == 3:
                                        self.root.get_screen('GameScreen').ids.letter3line4.md_bg_color = (1,0.8,0,1)
                                    if letter_index+1 == 4:
                                        self.root.get_screen('GameScreen').ids.letter4line4.md_bg_color = (1,0.8,0,1)
                                    if letter_index+1 == 5:
                                        self.root.get_screen('GameScreen').ids.letter5line4.md_bg_color = (1,0.8,0,1)        
                                
                                if self.current_line == 5:
                                    if letter_index+1 == 1:
                                        self.root.get_screen('GameScreen').ids.letter1line5.md_bg_color = (1,0.8,0,1)
                                    if letter_index+1 == 2:
                                        self.root.get_screen('GameScreen').ids.letter2line5.md_bg_color = (1,0.8,0,1)
                                    if letter_index+1 == 3:
                                        self.root.get_screen('GameScreen').ids.letter3line5.md_bg_color = (1,0.8,0,1)
                                    if letter_index+1 == 4:
                                        self.root.get_screen('GameScreen').ids.letter4line5.md_bg_color = (1,0.8,0,1)
                                    if letter_index+1 == 5:
                                        self.root.get_screen('GameScreen').ids.letter5line5.md_bg_color = (1,0.8,0,1)        

                                if self.current_line == 6:
                                    if letter_index+1 == 1:
                                        self.root.get_screen('GameScreen').ids.letter1line6.md_bg_color = (1,0.8,0,1)
                                    if letter_index+1 == 2:
                                        self.root.get_screen('GameScreen').ids.letter2line6.md_bg_color = (1,0.8,0,1)
                                    if letter_index+1 == 3:
                                        self.root.get_screen('GameScreen').ids.letter3line6.md_bg_color = (1,0.8,0,1)
                                    if letter_index+1 == 4:
                                        self.root.get_screen('GameScreen').ids.letter4line6.md_bg_color = (1,0.8,0,1)
                                    if letter_index+1 == 5:
                                        self.root.get_screen('GameScreen').ids.letter5line6.md_bg_color = (1,0.8,0,1)        
                        #If the currently checked letter is not in the answer
                        else:
                            if self.current_line == 1:
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

                            if self.current_line == 2:
                                if letter_index+1 == 1:
                                        self.root.get_screen('GameScreen').ids.letter1line2.md_bg_color = (0,0,0,1)                
                                if letter_index+1 == 2:
                                        self.root.get_screen('GameScreen').ids.letter2line2.md_bg_color = (0,0,0,1)
                                if letter_index+1 == 3:
                                        self.root.get_screen('GameScreen').ids.letter3line2.md_bg_color = (0,0,0,1)
                                if letter_index+1 == 4:
                                        self.root.get_screen('GameScreen').ids.letter4line2.md_bg_color = (0,0,0,1)
                                if letter_index+1 == 5:
                                        self.root.get_screen('GameScreen').ids.letter5line2.md_bg_color = (0,0,0,1)
                            
                            if self.current_line == 3:
                                if letter_index+1 == 1:
                                        self.root.get_screen('GameScreen').ids.letter1line3.md_bg_color = (0,0,0,1)                
                                if letter_index+1 == 2:
                                        self.root.get_screen('GameScreen').ids.letter2line3.md_bg_color = (0,0,0,1)
                                if letter_index+1 == 3:
                                        self.root.get_screen('GameScreen').ids.letter3line3.md_bg_color = (0,0,0,1)
                                if letter_index+1 == 4:
                                        self.root.get_screen('GameScreen').ids.letter4line3.md_bg_color = (0,0,0,1)
                                if letter_index+1 == 5:
                                        self.root.get_screen('GameScreen').ids.letter5line3.md_bg_color = (0,0,0,1)
                            
                            if self.current_line == 4:
                                if letter_index+1 == 1:
                                        self.root.get_screen('GameScreen').ids.letter1line4.md_bg_color = (0,0,0,1)                
                                if letter_index+1 == 2:
                                        self.root.get_screen('GameScreen').ids.letter2line4.md_bg_color = (0,0,0,1)
                                if letter_index+1 == 3:
                                        self.root.get_screen('GameScreen').ids.letter3line4.md_bg_color = (0,0,0,1)
                                if letter_index+1 == 4:
                                        self.root.get_screen('GameScreen').ids.letter4line4.md_bg_color = (0,0,0,1)
                                if letter_index+1 == 5:
                                        self.root.get_screen('GameScreen').ids.letter5line4.md_bg_color = (0,0,0,1)
                            
                            if self.current_line == 5:
                                if letter_index+1 == 1:
                                        self.root.get_screen('GameScreen').ids.letter1line5.md_bg_color = (0,0,0,1)                
                                if letter_index+1 == 2:
                                        self.root.get_screen('GameScreen').ids.letter2line5.md_bg_color = (0,0,0,1)
                                if letter_index+1 == 3:
                                        self.root.get_screen('GameScreen').ids.letter3line5.md_bg_color = (0,0,0,1)
                                if letter_index+1 == 4:
                                        self.root.get_screen('GameScreen').ids.letter4line5.md_bg_color = (0,0,0,1)
                                if letter_index+1 == 5:
                                        self.root.get_screen('GameScreen').ids.letter5line5.md_bg_color = (0,0,0,1)
                            
                            if self.current_line == 6:
                                if letter_index+1 == 1:
                                        self.root.get_screen('GameScreen').ids.letter1line6.md_bg_color = (0,0,0,1)                
                                if letter_index+1 == 2:
                                        self.root.get_screen('GameScreen').ids.letter2line6.md_bg_color = (0,0,0,1)
                                if letter_index+1 == 3:
                                        self.root.get_screen('GameScreen').ids.letter3line6.md_bg_color = (0,0,0,1)
                                if letter_index+1 == 4:
                                        self.root.get_screen('GameScreen').ids.letter4line6.md_bg_color = (0,0,0,1)
                                if letter_index+1 == 5:
                                        self.root.get_screen('GameScreen').ids.letter5line6.md_bg_color = (0,0,0,1)
                
                    #Reset variables for a new line
                    self.line_position = 1
                    if self.current_line < 6:
                        self.current_line +=1
                    self.current_user_word = ''

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
                if self.current_line == 1:
                    self.root.get_screen('GameScreen').ids.letter2line1.text = ''
                    self.root.get_screen('GameScreen').ids.letter2line1.md_bg_color = (0,0,0,0)
                if self.current_line == 2:
                    self.root.get_screen('GameScreen').ids.letter2line2.text = ''
                    self.root.get_screen('GameScreen').ids.letter2line2.md_bg_color = (0,0,0,0)
                if self.current_line == 3:
                    self.root.get_screen('GameScreen').ids.letter2line3.text = ''
                    self.root.get_screen('GameScreen').ids.letter2line3.md_bg_color = (0,0,0,0)
                if self.current_line == 4:
                    self.root.get_screen('GameScreen').ids.letter2line4.text = ''
                    self.root.get_screen('GameScreen').ids.letter2line4.md_bg_color = (0,0,0,0)
                if self.current_line == 5:
                    self.root.get_screen('GameScreen').ids.letter2line5.text = ''
                    self.root.get_screen('GameScreen').ids.letter2line5.md_bg_color = (0,0,0,0)
                if self.current_line == 6:
                    self.root.get_screen('GameScreen').ids.letter2line6.text = ''
                    self.root.get_screen('GameScreen').ids.letter2line6.md_bg_color = (0,0,0,0)

            if self.line_position == 3:
                if self.current_line == 1:
                    self.root.get_screen('GameScreen').ids.letter3line1.text = ''
                    self.root.get_screen('GameScreen').ids.letter3line1.md_bg_color = (0,0,0,0)
                if self.current_line == 2:
                    self.root.get_screen('GameScreen').ids.letter3line2.text = ''
                    self.root.get_screen('GameScreen').ids.letter3line2.md_bg_color = (0,0,0,0)
                if self.current_line == 3:
                    self.root.get_screen('GameScreen').ids.letter3line3.text = ''
                    self.root.get_screen('GameScreen').ids.letter3line3.md_bg_color = (0,0,0,0)
                if self.current_line == 4:
                    self.root.get_screen('GameScreen').ids.letter3line4.text = ''
                    self.root.get_screen('GameScreen').ids.letter3line4.md_bg_color = (0,0,0,0)
                if self.current_line == 5:
                    self.root.get_screen('GameScreen').ids.letter3line5.text = ''
                    self.root.get_screen('GameScreen').ids.letter3line5.md_bg_color = (0,0,0,0)
                if self.current_line == 6:
                    self.root.get_screen('GameScreen').ids.letter3line6.text = ''
                    self.root.get_screen('GameScreen').ids.letter3line6.md_bg_color = (0,0,0,0)

            if self.line_position == 4:
                if self.current_line == 1:
                    self.root.get_screen('GameScreen').ids.letter4line1.text = ''
                    self.root.get_screen('GameScreen').ids.letter4line1.md_bg_color = (0,0,0,0)
                if self.current_line == 2:
                    self.root.get_screen('GameScreen').ids.letter4line2.text = ''
                    self.root.get_screen('GameScreen').ids.letter4line2.md_bg_color = (0,0,0,0)
                if self.current_line == 3:
                    self.root.get_screen('GameScreen').ids.letter4line3.text = ''
                    self.root.get_screen('GameScreen').ids.letter4line3.md_bg_color = (0,0,0,0)
                if self.current_line == 4:
                    self.root.get_screen('GameScreen').ids.letter4line4.text = ''
                    self.root.get_screen('GameScreen').ids.letter4line4.md_bg_color = (0,0,0,0)
                if self.current_line == 5:
                    self.root.get_screen('GameScreen').ids.letter4line5.text = ''
                    self.root.get_screen('GameScreen').ids.letter4line5.md_bg_color = (0,0,0,0)
                if self.current_line == 6:
                    self.root.get_screen('GameScreen').ids.letter4line6.text = ''
                    self.root.get_screen('GameScreen').ids.letter4line6.md_bg_color = (0,0,0,0)

            if self.line_position == 5:
                if self.current_line == 1:
                    self.root.get_screen('GameScreen').ids.letter5line1.text = ''
                    self.root.get_screen('GameScreen').ids.letter5line1.md_bg_color = (0,0,0,0)
                if self.current_line == 2:
                    self.root.get_screen('GameScreen').ids.letter5line2.text = ''
                    self.root.get_screen('GameScreen').ids.letter5line2.md_bg_color = (0,0,0,0)
                if self.current_line == 3:
                    self.root.get_screen('GameScreen').ids.letter5line3.text = ''
                    self.root.get_screen('GameScreen').ids.letter5line3.md_bg_color = (0,0,0,0)
                if self.current_line == 4:
                    self.root.get_screen('GameScreen').ids.letter5line4.text = ''
                    self.root.get_screen('GameScreen').ids.letter5line4.md_bg_color = (0,0,0,0)
                if self.current_line == 5:
                    self.root.get_screen('GameScreen').ids.letter5line5.text = ''
                    self.root.get_screen('GameScreen').ids.letter5line5.md_bg_color = (0,0,0,0)
                if self.current_line == 6:
                    self.root.get_screen('GameScreen').ids.letter5line6.text = ''
                    self.root.get_screen('GameScreen').ids.letter5line6.md_bg_color = (0,0,0,0)

        if self.line_position == 1:
            if self.current_line == 1:
                self.root.get_screen('GameScreen').ids.letter1line1.text = ''
                self.root.get_screen('GameScreen').ids.letter1line1.md_bg_color = (0,0,0,0)
            if self.current_line == 2:
                self.root.get_screen('GameScreen').ids.letter1line2.text = ''
                self.root.get_screen('GameScreen').ids.letter1line2.md_bg_color = (0,0,0,0)
            if self.current_line == 3:
                self.root.get_screen('GameScreen').ids.letter1line3.text = ''
                self.root.get_screen('GameScreen').ids.letter1line3.md_bg_color = (0,0,0,0)
            if self.current_line == 4:
                self.root.get_screen('GameScreen').ids.letter1line4.text = ''
                self.root.get_screen('GameScreen').ids.letter1line4.md_bg_color = (0,0,0,0)
            if self.current_line == 5:
                self.root.get_screen('GameScreen').ids.letter1line5.text = ''
                self.root.get_screen('GameScreen').ids.letter1line5.md_bg_color = (0,0,0,0)
            if self.current_line == 6:
                self.root.get_screen('GameScreen').ids.letter1line6.text = ''
                self.root.get_screen('GameScreen').ids.letter1line6.md_bg_color = (0,0,0,0)

Verbumo().run()