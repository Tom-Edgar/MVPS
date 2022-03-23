from manimlib import *
import scipy.special
import numpy as np


class parallel(Scene):
    def construct(self):
        color1="#009E73"
        color2="#0072B2"
        color3="#CC79A7"
        color4="#F0E442"

        Points=[(0,0,0),(3,0,0),(4,2,0),(1,2,0)]
        Parallelogram=Polygon(*Points)
        StartText=TexText("Consider a parallelogram with sides of length \(a\) and \(b\) and an angle of \(\\theta\)", font_size=30)
        StartText2=TexText("between the sides.", font_size=30)
        StartText.to_edge(UP, buff=.5)
        StartText.to_edge(LEFT, buff=1)
        StartText2.next_to(StartText,.5*RIGHT)
        StartText2.to_edge(UP, buff=.5)

        self.play(Write(VGroup(StartText,StartText2)), run_time=3)

        TLine=Line((3,0,0),(3,2,0))
        TPoints=[(3,0,0),(4,2,0),(3,2,0)]
        TrapPoints=[(0,0,0),(3,0,0),(3,2,0),(1,2,0)]
        Triangle=Polygon(*TPoints)
        Triangle.set_stroke(width=4)
        Trapezoid=Polygon(*TrapPoints)
        Triangle.set_fill(color2, opacity=1)
        Trapezoid.set_fill(color3, opacity=1)
        anglearc=ParametricCurve(
            lambda u: (.25*math.cos(u),.25*math.sin(u),0), t_min=0, t_max=PI/3)
        topanglearc=ParametricCurve(
            lambda u: (4+.25*math.cos(u),2+.25*math.sin(u),0), t_min=PI, t_max=4*PI/3)
        anglearc2=anglearc.copy()
        topanglearc2=topanglearc.copy()
        Tri2=Triangle.copy()
        Tri2.shift(3*LEFT)
        Tri3=Tri2.copy()
        Tri3.set_fill(color3, opacity=1)
        Parallelogram.rotate(PI/5)

        ThePic=VGroup(Parallelogram,TLine,Triangle,Trapezoid,Tri2,Tri3,anglearc, topanglearc,anglearc2, topanglearc2)
        ThePic.move_to((0,0,0))
        ThePic.scale(1.5)

        self.play(ShowCreation(Parallelogram), run_time=3)
        self.play(Parallelogram.animate.set_fill(color1, opacity=1))
        self.wait(2)

        self.play(Rotate(Parallelogram,-PI/5), run_time=2)

        alabel=Tex("a")
        alabel.next_to(Parallelogram,DOWN)
        blabel=Tex("b")
        blabel.next_to(Parallelogram,RIGHT)
        VGroup(alabel,blabel).shift(.75*LEFT)
        diaglength=Tex("b\\sin(\\theta)")
        diaglength.rotate(PI/2)
        diaglength.next_to(TLine,.55*LEFT)
        thetalabel=Tex("\\theta")
        thetalabel2=Tex("\\theta")
        thetalabel.next_to(anglearc,.65*RIGHT)
        thetalabel.shift(.2*UP)
        thetalabel2.next_to(topanglearc,.65*LEFT)
        thetalabel2.shift(.2*DOWN)
        thetalabelcop=thetalabel.copy()
        thetalabelcop2=thetalabel2.copy()

        self.play(Write(alabel))
        self.play(Write(blabel))

        AreaFormula=[TexText("Area(", font_size=35),Parallelogram.copy().scale(.13),TexText(")", font_size=35),TexText("=", font_size=35),TexText("Area(", font_size=35),VGroup(Trapezoid,Tri3).copy().scale(.13),TexText(")", font_size=35),TexText("\(=\)", font_size=35),TexText("\(a\)","\(b\\sin(\\theta)\)", font_size=35)]
        Form=VGroup(*AreaFormula)
        Form.arrange(RIGHT)
        Form.shift(3*DOWN)

        self.play(ShowCreation(anglearc), Write(thetalabel))
        self.play(ShowCreation(topanglearc), Write(thetalabel2))
        self.wait(2)

        self.play(Write(Form[0]))
        self.play(ReplacementTransform(Parallelogram.copy(), Form[1]), run_time=3)
        self.play(Write(Form[2]))
        self.play(Write(Form[3]))
        self.wait(3)

        self.play(ShowCreation(TLine), run_time=2)
        self.wait()
        self.play(FadeIn(Trapezoid), FadeIn(Triangle), FadeIn(anglearc2), FadeIn(topanglearc2),FadeIn(thetalabelcop), FadeIn(thetalabelcop2))
        self.remove(anglearc, topanglearc,thetalabel, thetalabel2)
        self.wait(3)
        self.play(Write(diaglength),run_time=1.5)
        self.wait(2)
        self.play(FadeOut(blabel), FadeOut(thetalabelcop2), FadeOut(topanglearc2))

        self.remove(Parallelogram)
        self.play(ReplacementTransform(Triangle,Tri2), diaglength.animate.shift(4.5*LEFT), run_time=3)

        self.wait(2)
        self.play(Tri2.animate.set_fill(color3, opacity=1), run_time=1.5)

        self.play(Write(Form[4]))
        self.play(ReplacementTransform(VGroup(Trapezoid,Tri3).copy(), Form[5]),run_time=3)
        self.play(Write(Form[6]))
        self.wait(2)
        self.play(Write(Form[7]))
        self.play(TransformMatchingShapes(alabel.copy(), Form[8][0]),run_time=3)
        diag2=diaglength.copy()
        self.play(Rotate(diag2,-PI/2))
        self.play(TransformMatchingShapes(diag2, Form[8][1]),run_time=3)
        self.wait(4)
        self.play(FadeIn(Parallelogram), FadeIn(blabel), FadeIn(anglearc), FadeIn(thetalabel), FadeIn(topanglearc), FadeIn(thetalabel2), FadeOut(diaglength),FadeOut(Tri2),FadeOut(Form[4:8]), Form[8].animate.next_to(Form[3], RIGHT), run_time=2)
        finalRect=SurroundingRectangle(VGroup(Form[0],Form[8]), color=WHITE)
        self.wait(3)
        self.play(ShowCreation(finalRect))
        self.wait(5)