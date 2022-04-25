from manimlib import *
import random

class MultMod100(Scene):
    def construct(self):
        color5 = "#7DF9FF"
        color6 = "#FF10F0"
        color7 = "#FFF01F"
        color8 = "#39ff14"

        colors = [color8, color5, color6, color7]
        DiffDiagrams=VGroup()
        n=100
        m=0
        for k in range(2,52):
            if math.gcd(k,100)!=1 and m<50:
                tempenv=VGroup()
                Points=[(3*math.cos(2*PI*i/n), 3*math.sin(2*i*PI/n), 0) for i in range(n)]
                Circ=ParametricCurve(
                    lambda u: (3*math.cos(u),3*math.sin(u),0), t_min=0, t_max=2*PI)
                Circ.set_stroke(WHITE, width=4)
                tempenv.add(Circ)
                theLines=VGroup()
                for i in range(n):
                    theLines.add(Line(Points[i],Points[(k*i)%n]).set_stroke(width=1))
                tempenv.add(theLines)
                DiffDiagrams.add(tempenv)
                m+=1

        DiffDiagrams.scale(.25)
        Rows=[VGroup(*DiffDiagrams[:8])]
        Rows[0].arrange(RIGHT)
        Rows[0].to_edge(UP, buff=.65)
        for i in range(1,5):
            temp=VGroup(*DiffDiagrams[i*8:i*8+8])
            temp.arrange(RIGHT)
            temp.next_to(Rows[i-1],DOWN)
            Rows.append(temp)

        anis1=[]
        for x in DiffDiagrams:
            anis1.append(ShowCreation(x[0]))
        self.play(*anis1, run_time=4)

        anis2 = []
        for x in DiffDiagrams:
            anis2.append(ShowCreation(x[1]))
        self.play(*anis2, run_time=10)
        self.wait(2)

        i=0
        thelist=[i for i in range(len(DiffDiagrams))]
        random.shuffle(thelist)
        for j in thelist:
            self.play(FadeOut(DiffDiagrams[j][1]))
            DiffDiagrams[j][1].set_stroke(color=colors[thelist[i]%4])
            self.play(ShowCreation(DiffDiagrams[j][1]), run_time=3)
            i+=1
        self.wait(5)
        




