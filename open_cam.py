from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2

class CamApp(App):
    def build(self):
        self.img1=Image()
        layout = BoxLayout()
        layout.add_widget(self.img1)
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0/33.0)
        return layout
    def update(self, dt):
        ret, frame = self.capture.read()
        buf1 = cv2.flip(frame, 0)
        buf = buf1.tostring()
        texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr') 
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        self.img1.texture = texture1

    def get_image_size(self):
        width=self.capture.get(3)
        height=self.capture.get(4)
        return (width,height)
        

if __name__ == '__main__':
    CamApp().run()