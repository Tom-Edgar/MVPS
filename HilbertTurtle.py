from manimlib import *
from numpy import random
from scipy import *

def HL(n):
    T=[["A"]]
    for i in range(n):
        T.append([])
        for x in T[i]:
            if x=="A":
                for z in ["+","B","F","-","A","F","A","-","F","B","+"]:
                    T[i+1].append(z)
            elif x=="B":
                for z in ["-","A","F","+","B","F","B","+","F","A","-"]:
                    T[i+1].append(z)
            else:
                T[i+1].append(x)
    return T[-1]

class HilbertCurveLSystem(Scene):
    def construct(self):
        l=5
        Seq=HL(l)
        Initial=Line((0,0,0),(1,0,0)).set_stroke(width=12)
        HilbertCurve = [Initial]
        angle=0
        for i in range(len(Seq)):
            if Seq[i]=="F":
                coord = HilbertCurve[-1].get_end()
                templine=Line(coord, coord+[1,0,0]).set_stroke(width=12)
                templine.rotate(angle, about_point = coord)
                HilbertCurve.append(templine)
            elif Seq[i]=="+":
                angle+=PI/2
            elif Seq[i]=="-":
                angle+=-PI/2

        HCurve = VGroup(*HilbertCurve)

        self.camera.frame.set_height(HCurve.get_height()*1.3)
        self.camera.frame.move_to(HCurve)
        self.play(ShowCreation(HCurve[1:]), run_time=15)
        self.wait()

