from manimlib import *

import random

def f1(L,r,t):
    return [r*math.cos(t)*L[0]-r*math.sin(t)*L[1],r*math.sin(t)*L[0]+r*math.cos(t)*L[1]+1, 0]

def f2(L,r,t):
    return [r*math.cos(t)*L[0]+r*math.sin(t)*L[1],-r*math.sin(t)*L[0]+r*math.cos(t)*L[1]+1, 0]

class Trees618(Scene):
    def construct(self):
        self.wait()
        colors = [WHITE]
        num = 10
        theTrees=[]
        L=[[.618,2-.01*i] for i in range(175)]
        for M in L:
            Starter = Line((0, 0, 0), (0, 1, 0)).set_stroke(color=colors[0], width=2)
            rr = M[0]
            tt = M[1]
            theanis = []
            Levels = [[Starter]]
            for i in range(1, num):
                Levels.append([])
                theanis.append([])
                for j in range(len(Levels[i - 1])):
                    top = Levels[i - 1][j].get_end()
                    bottom = Levels[i - 1][j].get_start()
                    V1 = [bottom, top]
                    V2 = [bottom, top]
                    temp1 = Line(*[f1(v, rr, tt) for v in V1]).set_stroke(color=colors[0], width=2)
                    temp2 = Line(*[f2(v, rr, tt) for v in V2]).set_stroke(color=colors[0], width=2)
                    Levels[i].append(temp1)
                    Levels[i].append(temp2)
            tree=VGroup(*[x for sublist in Levels for x in sublist])
            tree.scale(3)
            tree.move_to((0,0,0))
            theTrees.append(tree.copy())

        self.play(self.camera.frame.set_height, theTrees[-1].get_height() * 1.25,run_time =.25)

        for k in range(175):
            if k==0:
                self.play(FadeIn(theTrees[k]))
            if k!=0:
                self.play(ReplacementTransform(theTrees[k-1],theTrees[k]), run_time=.33, rate_func=linear)
        self.wait(3)