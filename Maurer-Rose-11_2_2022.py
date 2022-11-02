from manimlib import *

class MRose(Scene):
    def construct(self):
        colors = ["#39ff14", "#7DF9FF", "#FF10F0", "#FFF01F","#FFF01F","#FF10F0","#7DF9FF","#39ff14"]
        TheRoses=VGroup()
        j=0
        for P in [[3,29,2],[3,41,3],[3,23,4],[3,67,5],[3,53,6],[3,23,7],[3,83,8],[3,31,9]]:
            ARose = ParametricCurve(
                lambda u: (P[0] * math.sin(P[2]*u)*math.cos(u), P[0] * math.sin(P[2]*u)*math.sin(u), 0), t_min=0, t_max=(1+(P[2]+1)%2) * PI)
            ARose.set_stroke(WHITE, width=4)
            points=[[P[0] * math.sin(P[2]*k*PI*P[1]/180)*math.cos(P[1]*k*PI/180), P[0] * math.sin(P[2]*PI*k*P[1]/180)*math.sin(P[1]*PI*k/180), 0] for k in range(361)]
            FullCurve=VGroup()
            for i in range(360):
                FullCurve.add(Line(points[i],points[i+1]).set_stroke(width=1, color=colors[j]))
            tempRose=VGroup(ARose,FullCurve)
            TheRoses.add(tempRose)
            j+=1
        for h in range(4):
            TheRoses[h].move_to((7*h,0,0))
            TheRoses[4+h].move_to((7*h,-7,0))
        self.camera.frame.set_width(TheRoses.get_width()*1.05)
        self.camera.frame.move_to((TheRoses.get_center()[0],-2.5,0))
        Title=TexText("Maurer Roses: Connect 360 Points on a Rose Curve", font_size=100)
        Title.next_to(TheRoses,UP, buff=1)
        self.play(Write(Title))
        self.wait(.5)
        anis1=[]
        for x in TheRoses:
            anis1.append(ShowCreation(x[0]))
        self.play(*anis1, run_time=8)
        self.wait(2)
        for x in TheRoses:
            self.play(ShowCreation(x[1]), run_time=21)
            self.wait(.5)
        self.wait(1.5)
        anis2=[]
        for x in TheRoses:
            anis2.append(FadeOut(x[0]))
        self.play(*anis2, run_time=2)
        self.wait(3)
        anis3=[]
        for x in TheRoses:
            anis3.append(FadeIn(x[0]))
        self.play(*anis3, run_time=2)
        self.wait(3)
        self.play(*anis2, run_time=2)
        self.wait(3)