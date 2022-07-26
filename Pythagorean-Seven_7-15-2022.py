from manimlib import *
import scipy.special
import numpy as np


class PTSeven(Scene):
    def construct(self):
        color1 = "#009E73"
        color2 = "#7DF9FF"
        color3 = "#FF10F0"
        color4 = "#FFF01F"
        color5 = "#79CBB8"
        color6 = "#39ff14"
        Formula=Tex("(","c","+","h",")","^2","=","(","a","+","b",")","^2","+","h","^2")
        Formula2=Tex("c^2","+","2ch","+","h^2","=","a^2","+","2ab","+","b^2","+","h","^2")
        Formula3=Tex("c^2","=","a^2","+","b^2")
        Formula.to_edge(UP, buff=.5)
        Formula2.to_edge(UP, buff=1.5)
        Formula3.to_edge(UP, buff=1.5)

        RTri=Polygon((0,0,0),(math.sqrt(3),0,0),(math.sqrt(3),1,0))
        RTri.set_fill(color2, opacity=1)
        RTri2=RTri.copy()
        RTri2.set_fill(color1, opacity=1)
        RTri2.shift(RIGHT+DOWN)
        RTri2.rotate(2*PI/6)
        RTri.rotate(5*PI/6)

        RTVerts=RTri.get_vertices()
        RectTop=Polygon(RTVerts[0],RTVerts[2],(RTVerts[2][0],RTVerts[1][1],0),(RTVerts[0][0],RTVerts[1][1],0))
        RectRight=RectTop.copy()
        RectRight.rotate(PI/2,about_point=RTVerts[0])
        RectRight.shift(.5*math.sqrt(3)*RIGHT)
        cSquare=Polygon(RTVerts[0],(RTVerts[0][0],RTVerts[0][1]-2,0),(RTVerts[2][0],RTVerts[2][1]-2,0),RTVerts[2])

        OuterSquare=Polygon((RTVerts[2][0],RTVerts[2][1]-2,0),(RTVerts[2][0],RTVerts[2][1]+.5*math.sqrt(3),0),(RTVerts[2][0]+2+.5*math.sqrt(3),RTVerts[2][1]+.5*math.sqrt(3),0),(RTVerts[2][0]+2+.5*math.sqrt(3),RTVerts[2][1]-2,0)).set_fill(YELLOW, opacity=1)

        hSquare=Polygon(RTVerts[0],(RTVerts[0][0],RTVerts[0][1]+.5*math.sqrt(3),0),(RTVerts[0][0]+.5*math.sqrt(3),RTVerts[0][1]+.5*math.sqrt(3),0),(RTVerts[0][0]+.5*math.sqrt(3),RTVerts[0][1],0))
        hSquare.set_fill(color4, opacity=1)
        smallTriTop=Polygon(RTVerts[2],(RTVerts[2][0],RTVerts[1][1],0),RTVerts[1])
        smallTriTop.set_fill(color2,opacity=1)
        bigTriTop=Polygon(RTVerts[0],(RTVerts[0][0],RTVerts[1][1],0),RTVerts[1])
        bigTriTop.set_fill(color2,opacity=1)

        hline=DashedLine(RTVerts[1],(RTVerts[1][0],RTVerts[1][1]-.5*math.sqrt(3),0), color=PURPLE)

        smallTriRight=smallTriTop.copy()
        smallTriRight.shift(2*RIGHT)
        smallTriRight.rotate(-PI/2, about_point=RTVerts[0])
        bigTriRight=bigTriTop.copy()
        bigTriRight.rotate(-PI/2, about_point=RTVerts[0])
        bigTriRight.shift(2*DOWN)

        smalltriTop2=smallTriTop.copy()
        smallTriRight2=smallTriRight.copy()
        bigTriTop2=bigTriTop.copy()
        bigTriRight2=bigTriRight.copy()
        smalldist=RTVerts[1][0]-RTVerts[0][0]
        smalldist2=RTVerts[2][0]-RTVerts[1][0]
        smalltriTop2.shift((2+.5*math.sqrt(3))*DOWN-(smalldist)*RIGHT)
        bigTriTop2.shift((2+.5*math.sqrt(3))*DOWN+(smalldist2)*RIGHT)
        smallTriRight2.shift((2+.5*math.sqrt(3))*LEFT-(smalldist)*DOWN)
        bigTriRight2.shift((2+.5*math.sqrt(3))*LEFT+(smalldist2)*DOWN)
        hline2=hline.copy()
        hline2.shift(smalldist2*RIGHT)

        hline3=hline.copy()
        hline3.shift(smalldist*LEFT)

        hline5=hline3.copy()
        hline5.shift(.5*math.sqrt(3)*RIGHT)

        thePic=VGroup(OuterSquare,RTri,RTri2,RectTop,RectRight,cSquare,hSquare,smallTriTop,smalltriTop2, smallTriRight,smallTriRight2,bigTriTop, bigTriTop2, bigTriRight, bigTriRight2, hline,hline2,hline3,hline5)

        thePic.move_to((0,-.5,0))
        thePic.scale(1.25)

        alab=Tex("a", color=BLACK).scale(.75)
        blab=Tex("b", color=BLACK).scale(.75)
        clab=Tex("c", color=BLACK).scale(.75)
        for x in [alab,blab,clab]:
            x.move_to(RTri.get_center())
        alab.shift(.85*LEFT+.1*DOWN)
        clab.shift(.4*DOWN+.4*LEFT)

        alab2=Tex("a", color=BLACK).scale(.75)
        blab2=Tex("b", color=BLACK).scale(.75)
        alab2.move_to(RTri2.get_center())
        alab2.shift(.85*UP+.1*LEFT)
        blab2.move_to(bigTriRight2.get_center())
        blab2.shift(.2*RIGHT)


        self.play(GrowFromCenter(RTri), run_time=2)
        self.wait()
        for x in [alab,blab,clab]:
            self.play(Write(x))
            self.wait(.5)

        T2=RTri.copy()
        self.play(Rotate(T2,-PI/2))
        hline4=hline3.copy()
        hline4.rotate(PI/2, about_point=hline4.get_start())
        hline4.shift(math.sqrt(3)*DOWN)
        hline3.shift(.5*math.sqrt(3)*RIGHT)

        self.play(ReplacementTransform(T2,RTri2), run_time=2)
        self.wait()
        self.play(ShowCreation(cSquare), run_time=2)
        self.wait()
        self.play(cSquare.animate.set_fill(color4, opacity=1), run_time=2)
        self.wait(2)
        self.play(FadeIn(smallTriTop),FadeIn(bigTriTop))
        self.wait()
        bigTriRight.set_fill(color1, opacity=1)
        bigTriRight2.set_fill(color1, opacity=1)
        smallTriRight.set_fill(color1, opacity=1)
        smallTriRight2.set_fill(color1, opacity=1)
        self.play(FadeIn(bigTriRight),FadeIn(smallTriRight))
        self.play(FadeIn(RectTop),FadeIn(RectRight))
        self.wait(2)
        cBracel=Brace(cSquare,LEFT)
        clab2=Tex("c")
        clab2.next_to(cBracel,LEFT)
        cBracet=Brace(RectTop,UP)
        clab1=Tex("c")
        clab1.next_to(cBracet,UP)
        self.play(GrowFromCenter(cBracel), Write(clab2), run_time=1.5)
        self.play(GrowFromCenter(cBracet), Write(clab1), run_time=1.5)
        self.wait(2)
        hlab1=Tex("h").scale(.75)
        hlab1.next_to(hline,RIGHT)
        hlab2=Tex("h").scale(.75)
        hlab2.next_to(hline4,UP)
        self.play(ShowCreation(hline),ShowCreation(hline4), fun_time=2)
        self.play(Write(hlab1),ShowCreation(hlab2))
        self.wait(3)

        topbr=Brace(OuterSquare,UP)
        toplabel=Tex("c","+","h")
        toplabel.next_to(topbr,UP)
        leftbr=Brace(OuterSquare,LEFT)
        leftlabel=Tex("c","+","h")
        leftlabel.next_to(leftbr,LEFT)

        self.play(ReplacementTransform(hline,hline5),hline4.animate.shift(math.sqrt(3)*UP),hlab2.animate.shift(math.sqrt(3)*UP),hlab1.animate.next_to(hline5,RIGHT),run_time=2)

        self.wait(2)

        self.play(GrowFromCenter(hSquare),run_time=2)
        self.remove(hline4,hline5)
        self.wait(2)

        self.play(ReplacementTransform(cBracet,topbr), TransformMatchingShapes(VGroup(clab1,hlab2),toplabel), run_time=2)
        self.play(ReplacementTransform(cBracel,leftbr), TransformMatchingShapes(VGroup(clab2,hlab1),leftlabel), run_time=2)

        self.wait(2)
        self.play(TransformMatchingShapes(VGroup(toplabel,leftlabel),Formula[0:6]), FadeOut(VGroup(leftbr,topbr)), run_time=1.5)
        self.wait(3)

        self.play(ReplacementTransform(smallTriTop,smalltriTop2), run_time=2)
        self.play(ReplacementTransform(bigTriTop,bigTriTop2), run_time=2)
        self.play(ReplacementTransform(smallTriRight,smallTriRight2), run_time=2)
        self.play(ReplacementTransform(bigTriRight,bigTriRight2), run_time=2)
        self.wait(2)
        self.play(FadeOut(RectTop),FadeOut(RectRight))

        hlab1=Tex("h")
        hlab1.next_to(hline,RIGHT)
        hlab2=Tex("h")
        hlab2.next_to(hline4,UP)

        self.wait(2)
        self.play(FadeIn(hlab1), FadeIn(hlab2), FadeOut(clab))
        self.wait(2)

        self.play(ReplacementTransform(alab.copy(), alab2), run_time=2)
        self.play(ReplacementTransform(blab.copy(), blab2), run_time=2)
        self.wait(2)

        self.play(Write(Formula[6]))
        self.wait()
        self.play(TransformMatchingShapes(VGroup(alab,alab2,blab,blab2),Formula[7:13]), run_time=2)
        self.play(Write(Formula[13]))
        self.play(TransformMatchingShapes(VGroup(hlab1,hlab2),Formula[14:]), run_time=2)

        self.wait(5)

        self.play(FadeOut(VGroup(cSquare,hSquare,RTri2, smalltriTop2,smallTriRight2,bigTriRight2,bigTriTop2)))

        self.play(RTri.animate.shift(DOWN))
        self.play(RTri.animate.scale(1.5))

        NRTVerts=RTri.get_vertices()

        hline=DashedLine(NRTVerts[1],(NRTVerts[1][0],NRTVerts[1][1]-1.866*.5*math.sqrt(3),0), color=WHITE)
        self.play(ShowCreation(hline), run_time=2)
        alab=Tex("a", color=WHITE).scale(.75)
        blab=Tex("b", color=WHITE).scale(.75)
        clab=Tex("c", color=WHITE).scale(.75)
        for x in [alab,blab,clab]:
            x.move_to(RTri.get_center())
        alab.shift(1.7*LEFT+.025*DOWN)
        blab.shift(.5*RIGHT+.25*UP)
        clab.shift(1*DOWN+.1*LEFT)
        hlab1=Tex("h").scale(.75)
        hlab1.next_to(hline,.75*RIGHT)

        for x in [alab,blab,clab,hlab1]:
            self.play(Write(x))

        areaequal=Tex("\\frac{1}{2}","ab","=","\\frac{1}{2}","ch")
        areaequal.next_to(RTri,3*DOWN)

        self.wait(2)
        self.play(TransformMatchingShapes(Formula.copy(),Formula2), run_time=2)
        self.wait(3)

        self.play(Write(areaequal))
        self.wait()
        self.play(FadeOut(areaequal[0]), FadeOut(areaequal[3]), areaequal[-1].animate.shift(.35 * LEFT))
        self.wait(3)

        self.play(TransformMatchingShapes(Formula2,Formula3), run_time=2)
        self.wait(2)

        self.play(FadeOut(areaequal[1:3]),FadeOut(areaequal[-1]))

        Rectangle1=SurroundingRectangle(Formula, color=WHITE)
        Rectangle2=SurroundingRectangle(Formula3, color=WHITE)

        self.play(ShowCreation(Rectangle1))
        self.wait()
        self.play(ShowCreation(Rectangle2))
        self.wait()
        self.play(VGroup(Formula,Rectangle1).animate.next_to(RTri,2*UP),VGroup(Formula3,Rectangle2).animate.next_to(RTri,4*DOWN), run_time=2)

        self.wait(5)