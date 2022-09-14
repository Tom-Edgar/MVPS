from manimlib import *
from numpy import random
from scipy import *

class SierpinskiZoom(Scene):
    def construct(self):
        bblue="#0072B2"

        Points=[(100*math.cos(2*PI*i/3-PI/6), 100*math.sin(2*i*PI/3-PI/6), 0) for i in range(3)]
        TheTri=Polygon(*Points)
        TheTri.set_fill(bblue, opacity=1)
        TheTri.set_stroke(width=1, color=bblue)
        TheTri.move_to((0,0,0))
        self.camera.frame.set_height(TheTri.get_height())
        self.camera.frame.move_to(TheTri.get_center())

        num=9
        levels=[]
        for j in range(num):
            levels.append(VGroup())
            for i in range(3):
                if j==0:
                    temp=TheTri.copy()
                    temp.scale(.5)
                    levels[j].add(temp)
                else:
                    temp = levels[j-1].copy()
                    temp.scale(.5)
                    levels[j].add(temp)
            levels[j][0:2].arrange(.01*RIGHT)
            levels[j][0:2].next_to(levels[j][2],.01*DOWN)
            if j==0:
                levels[j].move_to(TheTri.get_center())
            else:
                levels[j].move_to(levels[j-1].get_center())

        self.add(levels[num-1])

        self.play(self.camera.frame.set_height, levels[2][2].get_height(),
                      self.camera.frame.move_to, levels[2][2], run_time=10, rate_func=linear)