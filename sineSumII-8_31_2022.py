from manimlib import *
import scipy.special
import numpy as np


class SineZhou(Scene):
    def construct(self):
        color1 = "#009E73"
        color2 = "#7DF9FF"
        color3 = "#FF10F0"
        color4 = "#FFF01F"
        color5 = "#79CBB8"
        color6 = "#39ff14"
        ###
        a=.8*3
        x=.8*2
        b=.8*math.sqrt(7)
        y=.8*math.sqrt(6)

        lb=(0,0,0)
        lm=(0,b,0)
        lt=(0,b+x,0)
        tm=(a,b+x,0)
        rt=(a+y,b+x,0)
        rm=(a+y,b,0)
        rb=(a+y,0,0)
        bm=(a,0,0)
        mm=(a,b,0)

        bm1=(y,0,0)
        rm1=(a+y,x,0)

        ###
        OuterSquare=Polygon(*[lb,lt,rt,rb])


        LeftUpRect=Polygon(*[lm,lt,tm,mm])

        LeftTri1=Polygon(*[lm,tm,lt])
        LeftTri2=Polygon(*[tm,lm,mm])
        LeftTri1.set_fill(color6, opacity=1)
        LeftTri2.set_fill(color6, opacity=1)


        aa=math.atan(x/a)
        anglea=Arc(arc_center=tm,start_angle=PI,angle=aa, radius=.5, color=BLACK)
        anglealab=Tex(r"\alpha", color=BLACK).scale(.75)

        bb=math.atan(b/y)
        angleb=Arc(arc_center=bm1,start_angle=PI-bb,angle=bb, radius=.5, color=BLACK)
        angleblab=Tex(r"\beta", color=BLACK).scale(.75)

        anglealab.next_to(anglea,.5*LEFT)
        anglealab.shift(.05*DOWN)
        angleblab.next_to(angleb,.7*LEFT)


        aa2=math.atan(a/b)
        anglea2=Arc(arc_center=lm,start_angle=PI/2-aa2,angle=aa2, radius=.3, color=BLACK)
        anglea2lab=Tex(r"\alpha", color=BLACK).scale(.75)

        bb2=math.atan(a/b)
        angleb2=Arc(arc_center=lm,start_angle=3*PI/2,angle=bb2, radius=.5, color=BLACK)
        angleb2lab=Tex(r"\beta", color=BLACK).scale(.75)

        anglea2lab.next_to(anglea2,.2*UP)
        anglea2lab.shift(.05*RIGHT)

        angleb2lab.next_to(angleb2,.2*DOWN)

        LeftDownRect=Polygon(*[lb,lm,mm,bm])
        LeftUpRect.set_fill(color6, opacity=1)
        LeftDownRect.set_fill(WHITE, opacity=1)
        LeftDownRect.set_stroke(width=0)
        RightUpRect=Polygon(*[mm,rm,rt,tm])
        RightDownRect=Polygon(*[mm,rm,rb,bm])
        RightDownRect.set_fill(color3, opacity=1)
        RightUpRect.set_fill(WHITE, opacity=1)
        RightUpRect.set_stroke(width=0)

        RightTri1=Polygon(*[mm,rm,rb])
        RightTri2=Polygon(*[rb,bm,mm])
        RightTri1.set_fill(color3, opacity=1)
        RightTri2.set_fill(color3, opacity=1)


        Parallelogram=Polygon(*[lm,bm,rm,tm])
        Parallelogram=Polygon(*[lm,bm1,rm1,tm])

        Parallelogram.set_fill(WHITE, opacity=1)
        Parallelogram.set_stroke(width=0)

        anglearc=ParametricCurve(
            lambda u: (.3*math.cos(u),b+.3*math.sin(u),0), t_min=-PI/5.3, t_max=PI/5, color=BLACK)
        anglearc = ParametricCurve(
            lambda u: (.3 * math.cos(u), b + .3 * math.sin(u), 0), t_min=-PI/3.8, t_max=PI/5, color=BLACK)
        cosa=Tex(r"\cos(\alpha)")
        cosb=Tex(r"\cos(\beta)")
        cosb2=Tex(r"\cos(\beta)")

        sina=Tex(r"\sin(\alpha)")
        sinb=Tex(r"\sin(\beta)")
        tlabel2=Tex(r"\alpha+\beta", color=BLACK)
        t2label2=Tex(r"\dfrac{\pi}{2}-\alpha+\beta", color=BLACK).scale(.6)

        sacb=Tex(r"\sin(\alpha)",r"\cos(\beta)", color=BLACK).scale(.75)
        sbca=Tex(r"\sin(\beta)",r"\cos(\alpha)", color=BLACK).scale(.75)

        sbca.move_to(LeftDownRect.get_center())
        sacb.move_to(RightUpRect.get_center())

        dlabel1=Tex("1", color=BLACK).scale(.75)
        dlabel2=Tex("1", color=BLACK).scale(.75)


        dlabel1.rotate(PI/5.5)
        dlabel2.rotate(-PI/4)

        dlabel1.move_to((.4*a,b+.4*b,0))

        dlabel2.move_to((.5*a-.5,b-.5*b,0))

        cosa.next_to(LeftUpRect,UP)
        cosb.next_to(RightUpRect,UP)

        sina.next_to(LeftUpRect,LEFT)
        sinb.next_to(LeftDownRect,LEFT)
        cosb2.next_to(LeftDownRect,DOWN)
        cosb2.shift((-.3,0,0))
        tlabel2.move_to((1,b,0))
        t2label2.move_to((1.1,b,0))

        Pic=VGroup(Parallelogram,OuterSquare,RightTri2,RightTri1,LeftTri2,LeftTri1,sina,sinb,cosa,cosb,tlabel2,anglearc,RightUpRect,RightDownRect,LeftDownRect,LeftUpRect,sacb,sbca,dlabel1,dlabel2, anglea,anglealab,cosb2,angleb, angleblab, anglea2, anglea2lab, angleb2,angleb2lab, t2label2)
        Pic.move_to((0,-.5,0))

        RightTri2.shift(a * LEFT)
        RightTri1.shift(x * UP)
        LeftTri2.shift(y * RIGHT + b * DOWN)

        self.wait()

        self.play(FadeIn(LeftTri1), run_time=1)
        self.play(ShowCreation(anglea))
        self.play(Write(anglealab))
        self.play(Write(dlabel1))
        self.wait()
        self.play(Write(VGroup(sina,cosa)), run_time=2)

        self.play(FadeIn(RightTri2), run_time=1)
        self.play(ShowCreation(angleb))
        self.play(Write(angleblab))
        self.play(Write(dlabel2))
        self.wait()
        self.play(Write(VGroup(sinb,cosb2)), run_time=2)
        self.wait(2)

        temp=RightTri2.copy()
        self.play(Rotate(temp,PI), run_time=2)
        self.play(ReplacementTransform(temp,RightTri1), run_time=2)
        self.play(TransformMatchingShapes(cosb2,cosb), run_time=2)
        temp2=LeftTri1.copy()
        self.play(Rotate(temp2,PI), run_time=2)
        self.play(ReplacementTransform(temp2,LeftTri2), run_time=2)
        self.play(FadeIn(OuterSquare), run_time=1)


        self.wait()

        self.play(GrowFromCenter(Parallelogram), run_time=2)
        self.wait(1)
        self.play(ShowCreation(anglearc))
        self.play(Write(tlabel2), run_time=2)
        self.wait(2)

        Formula=Tex(r"1\cdot 1",r"\cdot ","\sin","(",r"\alpha+\beta",")","=","\\text{ unshaded area }","=",r"\sin(\alpha)\cos(\beta)","+",r"\sin(\beta)\cos(\alpha)").scale(.9)

        Formula.to_edge(UP, buff=.5)

        self.play(Write(Formula[7]))

        self.play(Write(Formula[6]))
        self.play(TransformMatchingShapes(VGroup(dlabel1,dlabel2),Formula[0]), run_time=1.5)
        self.play(Write(VGroup(Formula[1],Formula[2],Formula[3],Formula[5])))
        self.play(TransformMatchingShapes(tlabel2,Formula[4]), run_time=1.5)
        self.wait(.5)
        self.play(FadeOut(Formula[0:2]))

        self.wait(2)

        self.play(FadeOut(Parallelogram),FadeOut(anglea),FadeOut(angleb),FadeOut(anglealab),FadeOut(angleblab),FadeOut(anglearc), run_time=1)

        self.wait()

        self.play(LeftTri2.animate.shift(y*LEFT+b*UP), run_time=3)
        self.wait(.5)
        self.play(RightTri2.animate.shift(a*RIGHT), RightTri1.animate.shift(x*DOWN), run_time=3)

        self.wait()

        self.play(FadeIn(LeftUpRect),FadeIn(RightDownRect), run_time=1)

        self.play(GrowFromCenter(LeftDownRect), run_time=2)
        self.play(GrowFromCenter(RightUpRect), run_time=2)
        self.wait()
        self.play(TransformMatchingShapes(sinb.copy(),sbca[0]),TransformMatchingShapes(cosa.copy(),sbca[1]), run_time=2)
        self.wait(.5)
        self.play(TransformMatchingShapes(sina.copy(),sacb[0]),TransformMatchingShapes(cosb.copy(),sacb[1]), run_time=2)
        self.wait(2)

        self.play(Write(Formula[8]))
        self.play(TransformMatchingShapes(sacb,Formula[9]), run_time=2)
        self.play(Write(Formula[10]))
        self.play(TransformMatchingShapes(sbca,Formula[11]), run_time=2)
        self.wait(2)

        self.play(Formula[2:6].animate.next_to(Formula[8],LEFT), FadeOut(Formula[6:8]), run_time=2)
        form=VGroup(Formula[2:6],Formula[8:])
        self.play(form.animate.move_to((0,form.get_y(),0)), run_time=2)
        rect=SurroundingRectangle(form, color=WHITE)
        self.play(ShowCreation(rect))
        self.wait()
        FinalText=TexText(r"Visual proof that \(\cos(\alpha-\beta) = \cos(\alpha)\cos(\beta)+\sin(\alpha)\sin(\beta)\)?", font_size=35)

        FinalText.to_edge(DOWN, buff=.5)
        self.play(Write(FinalText), run_time=2)
        self.wait()

        self.play(FadeIn(VGroup(RightTri2,RightTri1,LeftTri1,LeftTri2)))

        self.remove(LeftUpRect,RightDownRect)


        self.play(FadeOut(VGroup(LeftDownRect,RightUpRect,cosa,cosb,sina,sinb)))

        self.play(RightTri2.animate.shift(a*LEFT), RightTri1.animate.shift(x*UP), run_time=3)
        self.wait(.5)
        self.play(LeftTri2.animate.shift(y*RIGHT+b*DOWN), run_time=3)

        self.play(ShowCreation(anglea2))
        self.play(Write(anglea2lab))
        self.play(Write(dlabel1))


        self.play(ShowCreation(angleb))
        self.play(Write(angleblab))
        self.play(Write(dlabel2))

        cosa.next_to(LeftUpRect,LEFT)
        cosb.next_to(RightUpRect,UP)

        sina.next_to(LeftUpRect,UP)
        sinb.next_to(LeftDownRect,LEFT)
        self.play(FadeIn(VGroup(cosa,cosb,sina,sinb)))

        self.play(GrowFromCenter(Parallelogram), run_time=1.5)
        self.wait(.5)
        self.play(ShowCreation(anglearc),Write(t2label2))
        self.wait(4)
