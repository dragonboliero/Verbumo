from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class Verbumo (MDApp):
    def build(self):
        return(MDLabel(text='Verbumo app'))

Verbumo().run()