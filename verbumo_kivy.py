"""
To do list:
   *Add reset button (Decrease user score if used).
   *Add some final styiling to the app. 
"""

#Basic imports
from kivymd.app import MDApp
from kivy.lang.builder import Builder   
from kivy.uix.screenmanager  import Screen,ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
import functions as func
    

class SManager(ScreenManager):
    pass

class GameScreen(Screen):
    pass

class Content(BoxLayout):
    pass

class ResetContent(BoxLayout):
    pass

#Main App
class Verbumo (MDApp):
    def build(self):
        #Pick first correct answer
        self.current_word = func.pick_random_word('correct_answers')
        #Set starting line
        self.current_line = 1
        #Set starting position in the grid's line
        self.line_position = 1
        #Load appropriate dictionary
        self.dictionary = func.words_dictionary('user_answers')
        #Variable holding user input
        self.current_user_word = ''
        #Variable holding user score
        self.score = 0
        #Color variables
        self.correct_letter_color = (0.25,0.61,0.21,1)
        self.misplaced_letter_color = (1,0.8,0,1)
        self.wrong_letter_color = (0,0,0,1)                
        print(self.current_word)
        #Load kv file
        app_uix = Builder.load_file('verbumo_kivy.kv')
        return app_uix

    #Method for reading user input from the screen keyboard    
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

            #Add the letter to user input variable
            self.current_user_word = self.current_user_word + letter
            #Move letter position in current line
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


    #Method checking if user provided word is the same as current word
    def check_user_word(self):
        #If the word has correct length
        print(f'letter position {self.line_position},line position {self.current_line}, user word {self.current_user_word}')
        if self.line_position == 6:
            #If user provided correct word
            if self.current_user_word == self.current_word:
                #Display congratulations dialog window
                correct_word = MDDialog(text='Hasło odgadnięte!')
                correct_word.open()
                #Scoring principles
                if self.current_line == 1:
                    self.score +=100
                if self.current_line == 2:
                    self.score +=50
                if self.current_line == 3:
                    self.score +=25
                if self.current_line == 4:
                    self.score +=12
                if self.current_line == 5:
                    self.score +=6
                if self.current_line == 6:
                    self.score +=3

                #Reset position variables
                self.line_position = 1
                self.current_line = 1
                self.current_user_word=''
                #Change score label
                self.root.get_screen('GameScreen').ids.score.text = str(self.score)
                #Get new correct word
                self.current_word = func.pick_random_word('correct_answers')
                #Clear all user input
                self.clear_table()
                print(self.current_word)
                print(self.current_line)
                #Activate all keyboard keys anew
                self.activate_keyboard()
            else:
                #The word is in the dictionary but not correct
                if self.current_user_word in self.dictionary:
                    
                    #Check letters with correct answer and assign appropriate background color to it.
                    for letter_index in range (self.line_position-1):
                        if self.current_user_word[letter_index] in self.current_word:
                            #If currently checked letter is in the answer in the same position
                            if self.current_user_word[letter_index] == self.current_word[letter_index]:
                                if self.current_line == 1:
                                    if letter_index+1 == 1:
                                        self.root.get_screen('GameScreen').ids.letter1line1.md_bg_color = self.correct_letter_color
                                    if letter_index+1 == 2:
                                        self.root.get_screen('GameScreen').ids.letter2line1.md_bg_color = self.correct_letter_color
                                    if letter_index+1 == 3:
                                        self.root.get_screen('GameScreen').ids.letter3line1.md_bg_color = self.correct_letter_color
                                    if letter_index+1 == 4:
                                        self.root.get_screen('GameScreen').ids.letter4line1.md_bg_color = self.correct_letter_color
                                    if letter_index+1 == 5:
                                        self.root.get_screen('GameScreen').ids.letter5line1.md_bg_color = self.correct_letter_color

                                if self.current_line == 2:
                                    if letter_index+1 == 1:
                                        self.root.get_screen('GameScreen').ids.letter1line2.md_bg_color = self.correct_letter_color
                                    if letter_index+1 == 2:
                                        self.root.get_screen('GameScreen').ids.letter2line2.md_bg_color = self.correct_letter_color
                                    if letter_index+1 == 3:
                                        self.root.get_screen('GameScreen').ids.letter3line2.md_bg_color = self.correct_letter_color
                                    if letter_index+1 == 4:
                                        self.root.get_screen('GameScreen').ids.letter4line2.md_bg_color = self.correct_letter_color
                                    if letter_index+1 == 5:
                                        self.root.get_screen('GameScreen').ids.letter5line2.md_bg_color = self.correct_letter_color

                                if self.current_line == 3:
                                    if letter_index+1 == 1:
                                        self.root.get_screen('GameScreen').ids.letter1line3.md_bg_color = self.correct_letter_color
                                    if letter_index+1 == 2:
                                        self.root.get_screen('GameScreen').ids.letter2line3.md_bg_color = self.correct_letter_color
                                    if letter_index+1 == 3:
                                        self.root.get_screen('GameScreen').ids.letter3line3.md_bg_color = self.correct_letter_color
                                    if letter_index+1 == 4:
                                        self.root.get_screen('GameScreen').ids.letter4line3.md_bg_color = self.correct_letter_color
                                    if letter_index+1 == 5:
                                        self.root.get_screen('GameScreen').ids.letter5line3.md_bg_color = self.correct_letter_color

                                if self.current_line == 4:
                                    if letter_index+1 == 1:
                                        self.root.get_screen('GameScreen').ids.letter1line4.md_bg_color = self.correct_letter_color
                                    if letter_index+1 == 2:
                                        self.root.get_screen('GameScreen').ids.letter2line4.md_bg_color = self.correct_letter_color
                                    if letter_index+1 == 3:
                                        self.root.get_screen('GameScreen').ids.letter3line4.md_bg_color = self.correct_letter_color
                                    if letter_index+1 == 4:
                                        self.root.get_screen('GameScreen').ids.letter4line4.md_bg_color = self.correct_letter_color
                                    if letter_index+1 == 5:
                                        self.root.get_screen('GameScreen').ids.letter5line4.md_bg_color = self.correct_letter_color
                                
                                if self.current_line == 5:
                                    if letter_index+1 == 1:
                                        self.root.get_screen('GameScreen').ids.letter1line5.md_bg_color = self.correct_letter_color
                                    if letter_index+1 == 2:
                                        self.root.get_screen('GameScreen').ids.letter2line5.md_bg_color = self.correct_letter_color
                                    if letter_index+1 == 3:
                                        self.root.get_screen('GameScreen').ids.letter3line5.md_bg_color = self.correct_letter_color
                                    if letter_index+1 == 4:
                                        self.root.get_screen('GameScreen').ids.letter4line5.md_bg_color = self.correct_letter_color
                                    if letter_index+1 == 5:
                                        self.root.get_screen('GameScreen').ids.letter5line5.md_bg_color = self.correct_letter_color

                                if self.current_line == 6:
                                    if letter_index+1 == 1:
                                        self.root.get_screen('GameScreen').ids.letter1line6.md_bg_color = self.correct_letter_color
                                    if letter_index+1 == 2:
                                        self.root.get_screen('GameScreen').ids.letter2line6.md_bg_color = self.correct_letter_color
                                    if letter_index+1 == 3:
                                        self.root.get_screen('GameScreen').ids.letter3line6.md_bg_color = self.correct_letter_color
                                    if letter_index+1 == 4:
                                        self.root.get_screen('GameScreen').ids.letter4line6.md_bg_color = self.correct_letter_color
                                    if letter_index+1 == 5:
                                        self.root.get_screen('GameScreen').ids.letter5line6.md_bg_color = self.correct_letter_color
                            #If the currently checked letter is in the answer but in different position
                            else:
                                if self.current_line == 1:
                                    if letter_index+1 == 1:
                                        self.root.get_screen('GameScreen').ids.letter1line1.md_bg_color = self.misplaced_letter_color
                                    if letter_index+1 == 2:
                                        self.root.get_screen('GameScreen').ids.letter2line1.md_bg_color = self.misplaced_letter_color
                                    if letter_index+1 == 3:
                                        self.root.get_screen('GameScreen').ids.letter3line1.md_bg_color = self.misplaced_letter_color
                                    if letter_index+1 == 4:
                                        self.root.get_screen('GameScreen').ids.letter4line1.md_bg_color = self.misplaced_letter_color
                                    if letter_index+1 == 5:
                                        self.root.get_screen('GameScreen').ids.letter5line1.md_bg_color = self.misplaced_letter_color

                                if self.current_line == 2:
                                    if letter_index+1 == 1:
                                        self.root.get_screen('GameScreen').ids.letter1line2.md_bg_color = self.misplaced_letter_color
                                    if letter_index+1 == 2:
                                        self.root.get_screen('GameScreen').ids.letter2line2.md_bg_color = self.misplaced_letter_color
                                    if letter_index+1 == 3:
                                        self.root.get_screen('GameScreen').ids.letter3line2.md_bg_color = self.misplaced_letter_color
                                    if letter_index+1 == 4:
                                        self.root.get_screen('GameScreen').ids.letter4line2.md_bg_color = self.misplaced_letter_color
                                    if letter_index+1 == 5:
                                        self.root.get_screen('GameScreen').ids.letter5line2.md_bg_color = self.misplaced_letter_color

                                if self.current_line == 3:
                                    if letter_index+1 == 1:
                                        self.root.get_screen('GameScreen').ids.letter1line3.md_bg_color = self.misplaced_letter_color
                                    if letter_index+1 == 2:
                                        self.root.get_screen('GameScreen').ids.letter2line3.md_bg_color = self.misplaced_letter_color
                                    if letter_index+1 == 3:
                                        self.root.get_screen('GameScreen').ids.letter3line3.md_bg_color = self.misplaced_letter_color
                                    if letter_index+1 == 4:
                                        self.root.get_screen('GameScreen').ids.letter4line3.md_bg_color = self.misplaced_letter_color
                                    if letter_index+1 == 5:
                                        self.root.get_screen('GameScreen').ids.letter5line3.md_bg_color = self.misplaced_letter_color

                                if self.current_line == 4:
                                    if letter_index+1 == 1:
                                        self.root.get_screen('GameScreen').ids.letter1line4.md_bg_color = self.misplaced_letter_color
                                    if letter_index+1 == 2:
                                        self.root.get_screen('GameScreen').ids.letter2line4.md_bg_color = self.misplaced_letter_color
                                    if letter_index+1 == 3:
                                        self.root.get_screen('GameScreen').ids.letter3line4.md_bg_color = self.misplaced_letter_color
                                    if letter_index+1 == 4:
                                        self.root.get_screen('GameScreen').ids.letter4line4.md_bg_color = self.misplaced_letter_color
                                    if letter_index+1 == 5:
                                        self.root.get_screen('GameScreen').ids.letter5line4.md_bg_color = self.misplaced_letter_color        
                                
                                if self.current_line == 5:
                                    if letter_index+1 == 1:
                                        self.root.get_screen('GameScreen').ids.letter1line5.md_bg_color = self.misplaced_letter_color
                                    if letter_index+1 == 2:
                                        self.root.get_screen('GameScreen').ids.letter2line5.md_bg_color = self.misplaced_letter_color
                                    if letter_index+1 == 3:
                                        self.root.get_screen('GameScreen').ids.letter3line5.md_bg_color = self.misplaced_letter_color
                                    if letter_index+1 == 4:
                                        self.root.get_screen('GameScreen').ids.letter4line5.md_bg_color = self.misplaced_letter_color
                                    if letter_index+1 == 5:
                                        self.root.get_screen('GameScreen').ids.letter5line5.md_bg_color = self.misplaced_letter_color        

                                if self.current_line == 6:
                                    if letter_index+1 == 1:
                                        self.root.get_screen('GameScreen').ids.letter1line6.md_bg_color = self.misplaced_letter_color
                                    if letter_index+1 == 2:
                                        self.root.get_screen('GameScreen').ids.letter2line6.md_bg_color = self.misplaced_letter_color
                                    if letter_index+1 == 3:
                                        self.root.get_screen('GameScreen').ids.letter3line6.md_bg_color = self.misplaced_letter_color
                                    if letter_index+1 == 4:
                                        self.root.get_screen('GameScreen').ids.letter4line6.md_bg_color = self.misplaced_letter_color
                                    if letter_index+1 == 5:
                                        self.root.get_screen('GameScreen').ids.letter5line6.md_bg_color = self.misplaced_letter_color        
                        #If the currently checked letter is not in the answer
                        else:
                            #Disable keyboard button 
                            #First keyboard line
                            if self.current_user_word[letter_index] == 'Ą':
                                self.root.get_screen('GameScreen').ids.letter_ą.disabled = True             
                            if self.current_user_word[letter_index] == 'Ć':
                                self.root.get_screen('GameScreen').ids.letter_ć.disabled = True
                            if self.current_user_word[letter_index] == 'Ę':
                                self.root.get_screen('GameScreen').ids.letter_ę.disabled = True
                            if self.current_user_word[letter_index] == 'Ł':
                                self.root.get_screen('GameScreen').ids.letter_ł.disabled = True                                
                            if self.current_user_word[letter_index] == 'Ó':
                                self.root.get_screen('GameScreen').ids.letter_ó.disabled = True
                            if self.current_user_word[letter_index] == 'Ś':
                                self.root.get_screen('GameScreen').ids.letter_ś.disabled = True
                            if self.current_user_word[letter_index] == 'Ń':
                                self.root.get_screen('GameScreen').ids.letter_ń.disabled = True
                            if self.current_user_word[letter_index] == 'Ż':
                                self.root.get_screen('GameScreen').ids.letter_ż.disabled = True
                            if self.current_user_word[letter_index] == 'Ź':
                                self.root.get_screen('GameScreen').ids.letter_ź.disabled = True
                            #Second keyboard line
                            if self.current_user_word[letter_index] == 'Q':
                                self.root.get_screen('GameScreen').ids.letter_q.disabled = True
                            if self.current_user_word[letter_index] == 'W':
                                self.root.get_screen('GameScreen').ids.letter_w.disabled = True
                            if self.current_user_word[letter_index] == 'E':
                                self.root.get_screen('GameScreen').ids.letter_e.disabled = True
                            if self.current_user_word[letter_index] == 'R':
                                self.root.get_screen('GameScreen').ids.letter_r.disabled = True
                            if self.current_user_word[letter_index] == 'T':
                                self.root.get_screen('GameScreen').ids.letter_t.disabled = True
                            if self.current_user_word[letter_index] == 'Y':
                                self.root.get_screen('GameScreen').ids.letter_y.disabled = True
                            if self.current_user_word[letter_index] == 'U':
                                self.root.get_screen('GameScreen').ids.letter_u.disabled = True
                            if self.current_user_word[letter_index] == 'I':
                                self.root.get_screen('GameScreen').ids.letter_i.disabled = True
                            if self.current_user_word[letter_index] == 'O':
                                self.root.get_screen('GameScreen').ids.letter_o.disabled = True
                            if self.current_user_word[letter_index] == 'P':
                                self.root.get_screen('GameScreen').ids.letter_p.disabled = True
                            #Third keyboard line
                            if self.current_user_word[letter_index] == 'A':
                                self.root.get_screen('GameScreen').ids.letter_a.disabled = True
                            if self.current_user_word[letter_index] == 'S':
                                self.root.get_screen('GameScreen').ids.letter_s.disabled = True               
                            if self.current_user_word[letter_index] == 'D':
                                self.root.get_screen('GameScreen').ids.letter_d.disabled = True
                            if self.current_user_word[letter_index] == 'F':
                                self.root.get_screen('GameScreen').ids.letter_f.disabled = True
                            if self.current_user_word[letter_index] == 'G':
                                self.root.get_screen('GameScreen').ids.letter_g.disabled = True
                            if self.current_user_word[letter_index] == 'H':
                                self.root.get_screen('GameScreen').ids.letter_h.disabled = True
                            if self.current_user_word[letter_index] == 'J':
                                self.root.get_screen('GameScreen').ids.letter_j.disabled = True
                            if self.current_user_word[letter_index] == 'K':
                                self.root.get_screen('GameScreen').ids.letter_k.disabled = True
                            if self.current_user_word[letter_index] == 'L':
                                self.root.get_screen('GameScreen').ids.letter_l.disabled = True
                            #Fourth keyboard line
                            if self.current_user_word[letter_index] == 'Z':
                                self.root.get_screen('GameScreen').ids.letter_z.disabled = True
                            if self.current_user_word[letter_index] == 'X':
                                self.root.get_screen('GameScreen').ids.letter_x.disabled = True
                            if self.current_user_word[letter_index] == 'C':
                                self.root.get_screen('GameScreen').ids.letter_c.disabled = True
                            if self.current_user_word[letter_index] == 'V':
                                self.root.get_screen('GameScreen').ids.letter_v.disabled = True
                            if self.current_user_word[letter_index] == 'B':
                                self.root.get_screen('GameScreen').ids.letter_b.disabled = True
                            if self.current_user_word[letter_index] == 'N':
                                self.root.get_screen('GameScreen').ids.letter_n.disabled = True
                            if self.current_user_word[letter_index] == 'M':
                                self.root.get_screen('GameScreen').ids.letter_m.disabled = True

                            if self.current_line == 1:
                                if letter_index+1 == 1:
                                        self.root.get_screen('GameScreen').ids.letter1line1.md_bg_color = self.wrong_letter_color               
                                if letter_index+1 == 2:
                                        self.root.get_screen('GameScreen').ids.letter2line1.md_bg_color = self.wrong_letter_color
                                if letter_index+1 == 3:
                                        self.root.get_screen('GameScreen').ids.letter3line1.md_bg_color = self.wrong_letter_color
                                if letter_index+1 == 4:
                                        self.root.get_screen('GameScreen').ids.letter4line1.md_bg_color = self.wrong_letter_color
                                if letter_index+1 == 5:
                                        self.root.get_screen('GameScreen').ids.letter5line1.md_bg_color = self.wrong_letter_color

                            if self.current_line == 2:
                                if letter_index+1 == 1:
                                        self.root.get_screen('GameScreen').ids.letter1line2.md_bg_color = self.wrong_letter_color                
                                if letter_index+1 == 2:
                                        self.root.get_screen('GameScreen').ids.letter2line2.md_bg_color = self.wrong_letter_color
                                if letter_index+1 == 3:
                                        self.root.get_screen('GameScreen').ids.letter3line2.md_bg_color = self.wrong_letter_color
                                if letter_index+1 == 4:
                                        self.root.get_screen('GameScreen').ids.letter4line2.md_bg_color = self.wrong_letter_color
                                if letter_index+1 == 5:
                                        self.root.get_screen('GameScreen').ids.letter5line2.md_bg_color = self.wrong_letter_color
                            
                            if self.current_line == 3:
                                if letter_index+1 == 1:
                                        self.root.get_screen('GameScreen').ids.letter1line3.md_bg_color = self.wrong_letter_color                
                                if letter_index+1 == 2:
                                        self.root.get_screen('GameScreen').ids.letter2line3.md_bg_color = self.wrong_letter_color
                                if letter_index+1 == 3:
                                        self.root.get_screen('GameScreen').ids.letter3line3.md_bg_color = self.wrong_letter_color
                                if letter_index+1 == 4:
                                        self.root.get_screen('GameScreen').ids.letter4line3.md_bg_color = self.wrong_letter_color
                                if letter_index+1 == 5:
                                        self.root.get_screen('GameScreen').ids.letter5line3.md_bg_color = self.wrong_letter_color
                            
                            if self.current_line == 4:
                                if letter_index+1 == 1:
                                        self.root.get_screen('GameScreen').ids.letter1line4.md_bg_color = self.wrong_letter_color                
                                if letter_index+1 == 2:
                                        self.root.get_screen('GameScreen').ids.letter2line4.md_bg_color = self.wrong_letter_color
                                if letter_index+1 == 3:
                                        self.root.get_screen('GameScreen').ids.letter3line4.md_bg_color = self.wrong_letter_color
                                if letter_index+1 == 4:
                                        self.root.get_screen('GameScreen').ids.letter4line4.md_bg_color = self.wrong_letter_color
                                if letter_index+1 == 5:
                                        self.root.get_screen('GameScreen').ids.letter5line4.md_bg_color = self.wrong_letter_color
                            
                            if self.current_line == 5:
                                if letter_index+1 == 1:
                                        self.root.get_screen('GameScreen').ids.letter1line5.md_bg_color = self.wrong_letter_color                
                                if letter_index+1 == 2:
                                        self.root.get_screen('GameScreen').ids.letter2line5.md_bg_color = self.wrong_letter_color
                                if letter_index+1 == 3:
                                        self.root.get_screen('GameScreen').ids.letter3line5.md_bg_color = self.wrong_letter_color
                                if letter_index+1 == 4:
                                        self.root.get_screen('GameScreen').ids.letter4line5.md_bg_color = self.wrong_letter_color
                                if letter_index+1 == 5:
                                        self.root.get_screen('GameScreen').ids.letter5line5.md_bg_color = self.wrong_letter_color
                            
                            if self.current_line == 6:
                                if letter_index+1 == 1:
                                        self.root.get_screen('GameScreen').ids.letter1line6.md_bg_color = self.wrong_letter_color                
                                if letter_index+1 == 2:
                                        self.root.get_screen('GameScreen').ids.letter2line6.md_bg_color = self.wrong_letter_color
                                if letter_index+1 == 3:
                                        self.root.get_screen('GameScreen').ids.letter3line6.md_bg_color = self.wrong_letter_color
                                if letter_index+1 == 4:
                                        self.root.get_screen('GameScreen').ids.letter4line6.md_bg_color = self.wrong_letter_color
                                if letter_index+1 == 5:
                                        self.root.get_screen('GameScreen').ids.letter5line6.md_bg_color = self.wrong_letter_color

                    #If the answer in the last line was wrong
                    if self.current_line == 6:
                        word_meanings = func.get_dictionary_entry(self.current_word)
                        lost_dialog = f'[color=#D91616]Porażka[/color], prawidłową odpowiedzią było słowo: [color=#409C36]{self.current_word}[/color]\n\n{word_meanings}'
                        #Display dialog window stating the answer was wrong
                        word_lost = MDDialog(text=lost_dialog)
                        word_lost.open()
                        #Reset position variables
                        self.line_position = 1
                        self.current_line = 0
                        self.current_user_word=''
                        #Get a new random correct word
                        self.current_word = func.pick_random_word('correct_answers')
                        self.clear_table()
                        print(self.current_word)
                        self.activate_keyboard()

                    #Reset variables for a new line
                    if self.current_line != 6:
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

    def activate_keyboard(self):
        #First keyboard line
        self.root.get_screen('GameScreen').ids.letter_ą.disabled = False             
        self.root.get_screen('GameScreen').ids.letter_ć.disabled = False             
        self.root.get_screen('GameScreen').ids.letter_ę.disabled = False             
        self.root.get_screen('GameScreen').ids.letter_ł.disabled = False             
        self.root.get_screen('GameScreen').ids.letter_ó.disabled = False             
        self.root.get_screen('GameScreen').ids.letter_ś.disabled = False             
        self.root.get_screen('GameScreen').ids.letter_ń.disabled = False             
        self.root.get_screen('GameScreen').ids.letter_ż.disabled = False             
        self.root.get_screen('GameScreen').ids.letter_ź.disabled = False
        #Second keyboard line
        self.root.get_screen('GameScreen').ids.letter_q.disabled = False                          
        self.root.get_screen('GameScreen').ids.letter_w.disabled = False
        self.root.get_screen('GameScreen').ids.letter_e.disabled = False
        self.root.get_screen('GameScreen').ids.letter_r.disabled = False
        self.root.get_screen('GameScreen').ids.letter_t.disabled = False
        self.root.get_screen('GameScreen').ids.letter_y.disabled = False
        self.root.get_screen('GameScreen').ids.letter_u.disabled = False
        self.root.get_screen('GameScreen').ids.letter_i.disabled = False
        self.root.get_screen('GameScreen').ids.letter_o.disabled = False
        self.root.get_screen('GameScreen').ids.letter_p.disabled = False
        #Third keyboard line
        self.root.get_screen('GameScreen').ids.letter_a.disabled = False
        self.root.get_screen('GameScreen').ids.letter_s.disabled = False
        self.root.get_screen('GameScreen').ids.letter_d.disabled = False
        self.root.get_screen('GameScreen').ids.letter_f.disabled = False
        self.root.get_screen('GameScreen').ids.letter_g.disabled = False
        self.root.get_screen('GameScreen').ids.letter_h.disabled = False
        self.root.get_screen('GameScreen').ids.letter_j.disabled = False
        self.root.get_screen('GameScreen').ids.letter_k.disabled = False
        self.root.get_screen('GameScreen').ids.letter_l.disabled = False
        #Fourth keyboard line
        self.root.get_screen('GameScreen').ids.letter_z.disabled = False
        self.root.get_screen('GameScreen').ids.letter_x.disabled = False
        self.root.get_screen('GameScreen').ids.letter_c.disabled = False
        self.root.get_screen('GameScreen').ids.letter_v.disabled = False
        self.root.get_screen('GameScreen').ids.letter_b.disabled = False
        self.root.get_screen('GameScreen').ids.letter_n.disabled = False
        self.root.get_screen('GameScreen').ids.letter_m.disabled = False

    def display_info(self):
        how_to_play = MDDialog(text="""
Twoim celem jest odgadnięcie hasła. Masz na to 6 prób.

Jeśli nie uda Ci się odgadnąć hasła, to podane litery zostaną podświetlone.

Na [color=#409C36]zielono[/color] jeśli znajdują się w haśle w tym samym miejscu, na [color=#FFCD00]żółto[/color] jeśli znajdują się w haśle, ale na innym miejscu, lub na [color=#000000]czarno[/color] jeśli nie znajdują się w haśle.

Po odgadnięciu hasła dostaniesz ilość punktów zależną od tego jak szybko zostało to dokonane.
        """)
        how_to_play.open()

    def word_reset_dialog(self):
        self.wr_dialog = MDDialog(
            title="[color=#000000]Czy na pewno chcesz wylosować nowe hasło? Stracisz 25 punktów.[/color]",
            type ="custom",
            content_cls=ResetContent(),)
        self.wr_dialog.open()

    def word_reset(self):
        #Reset position variables
        self.line_position = 1
        self.current_line = 1
        self.current_user_word=''
        #Change score label
        self.score = self.score - 25
        self.root.get_screen('GameScreen').ids.score.text = str(self.score)
        #Get new correct word
        self.current_word = func.pick_random_word('correct_answers')
        #Clear all user input
        self.clear_table()
        print(self.current_word)
        print(self.current_line)
        #Activate all keyboard keys anew
        self.activate_keyboard()
        self.wr_dialog.dismiss(force=True)

    def bug_report_window(self):
        self.sb_report = MDDialog(
          title = '[color=#000000]Wyślij raport o błędzie[/color]',
          type ="custom",
          content_cls=Content(),
        )
        self.sb_report.open()

    def send_bug_report(self,text):
        func.send_bug_report(text)
        self.sb_report.dismiss(force=True)


Verbumo().run()