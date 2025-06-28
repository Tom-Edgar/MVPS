from manimlib import *

class PursuitCurves(Scene):
    def construct(self):
        n=4
        scalefactor=.95
        PolyPoints=[[2*math.cos(2*PI*i/n), 2*math.sin(2*PI*i/n),0] for i in range(n)]
        OuterPoly=Polygon(*PolyPoints).set_stroke(width=2)
        self.camera.frame.set_height(OuterPoly.get_height()*1.1)
        thePolys=[OuterPoly]
        for i in range(200):
            temp=thePolys[-1].copy()
            temp.scale(scalefactor)
            temp.rotate(PI/60)
            thePolys.append(temp)
        self.play(ShowCreation(OuterPoly), run_time=2)
        self.play(ShowCreation(VGroup(*thePolys[1:])), run_time=10)

        colors=[BLUE, RED, GREEN, YELLOW, ORANGE]
        thepaths=[]
        for j in range(n):
            temppoints=[x.get_vertices()[j] for x in thePolys]
            temppath = VMobject()
            temppath.set_points_smoothly(temppoints)
            temppath.set_stroke(color=colors[j%n])
            thepaths.append(temppath)

        self.wait()
        anis=[ShowCreation(y) for y in thepaths]

        self.play(*anis, run_time=10)
        self.wait(2)
        self.play(*[FadeOut(y) for y in thepaths])
        self.play(Uncreate(VGroup(*thePolys[1:])), run_time=10)

        self.wait(2)

        self.play(*anis, run_time=10)
