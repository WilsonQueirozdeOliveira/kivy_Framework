from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button

class BoxLayoutExample(BoxLayout):
    pass
    '''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="a")
        b2 = Button(text="b")
        self.add_widget(b1)
        self.add_widget(b2)
    '''

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()