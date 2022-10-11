from manimlib import *

class circleArea(Scene):
    def construct(self):
        purple = "#332288"
        green = "#117733"
        lgreen ="#44AA99"
        r=3
        circ = ParametricCurve(
            lambda u: (r*math.cos(u), r*math.sin(u), 0), t_min=0, t_max=2*PI)
        circ.set_stroke(WHITE, width=2)
        initialrad=Line((0,0,0),(3,0,0)).set_stroke(width=2)
        self.play(ShowCreation(initialrad), run_time=2)
        self.wait()
        line1=Line((.5*PI*r,1.5,0),(-.5*PI*r,1.5,0))
        line2=Line((-.5*PI*r,-1.5,0),(.5*PI*r,-1.5,0))
        line3=Line((-.5*PI*r,-1.5,0),(-.5*PI*r,1.5,0))
        line4=Line((.5*PI*r,-1.5,0),(.5*PI*r,1.5,0))
        topcirc = ParametricCurve(
            lambda u: (r * math.cos(u), r * math.sin(u), 0), t_min=0, t_max=PI)
        topcirc.set_stroke(WHITE, width=2)
        botcirc = ParametricCurve(
            lambda u: (r * math.cos(u), r * math.sin(u), 0), t_min=PI, t_max=2*PI)
        botcirc.set_stroke(WHITE, width=2)
        theradius=Line((0,0,0),(0,3,0)).set_stroke(WHITE, width=2)
        topbrace = Brace(line1, UP)
        halfcircum = Tex(r"\pi r")
        halfcircum.next_to(topbrace, UP)
        leftbrace = Brace(line3, LEFT)
        radlabel = Tex(r"r")
        radlabel.next_to(leftbrace, LEFT)
        def rotcirc(mob):
            mob.become(Line((0,0,0),circ.get_end()).set_stroke(width=2))
        initialrad.add_updater(rotcirc)
        self.play(ShowCreation(circ), run_time=2)
        initialrad.remove_updater(rotcirc)
        self.play(FadeOut(initialrad))
        self.wait(2)
        for n in [4,8,20,50,100,200]:
            if n>4:
                circ.set_fill(purple, opacity=1)
                self.play(FadeIn(circ))
            if n==4:
                self.play(circ.animate.set_fill(purple, opacity=1))
                self.wait()
                circ2 = circ.copy()
                circ2.set_fill(purple)
                Final = VGroup(TexText("Area(", font_size=40), circ2.scale(.075), TexText(")"), TexText("="),
                               halfcircum.copy(),
                               Tex("\cdot "), radlabel.copy(), Tex("\pi", " r", "^2"))
                Final.arrange(RIGHT)
                Final.to_edge(DOWN, buff=.25)
                self.play(Write(Final[0]), Write(Final[2]))
                self.play(ReplacementTransform(circ.copy(),Final[1]), run_time=2)
                self.play(Write(Final[3]), run_time=.5)
                quest=Tex("?")
                quest.next_to(Final[3],RIGHT)
                self.play(Write(quest))
                self.wait()
            self.wait(.5)
            Sects=[AnnularSector(inner_radius=0, outer_radius=3, angle=2*PI/n, start_angle=2*PI*i/n, fill_opacity=1,
                      stroke_width=0, color=purple) for i in range(n)]
            if n<100:
                VGroup(*Sects).set_stroke(WHITE, width=.75)
            else:
                VGroup(*Sects).set_stroke(WHITE, width=.01)
            self.play(FadeIn(VGroup(*Sects)))
            topp=[]
            bot=[]
            anis=[]
            for i in range(n):
                temp=Sects[i].copy()
                if i<math.floor(n/2):
                    temp.rotate(-2*PI*i/n, about_point=[0,0,0])
                    temp.rotate(PI/2-PI/n, about_point=[0,0,0])
                    temp.set_fill(lgreen, opacity=1)
                    topp.append(temp)
                    anis.append(Sects[i].animate.set_fill(lgreen, opacity=1))
                else:
                    temp.rotate(-2 * PI * i / n, about_point=[0, 0, 0])
                    temp.rotate(3*PI / 2 - PI / n, about_point=[0, 0, 0])
                    bot.append(temp)
            self.remove(circ)
            self.wait(.5)
            self.play(*anis)
            topSects=VGroup(*topp)
            topSects.arrange(LEFT, buff=0)
            topSects.shift(.5*r*UP)
            botSects=VGroup(*bot)
            botSects.arrange(RIGHT, buff=0)
            botSects.shift(.5*r*DOWN)
            self.play(ReplacementTransform(VGroup(*Sects[:math.floor(n/2)]),topSects),ReplacementTransform(VGroup(*Sects[math.floor(n/2):]),botSects), run_time=2)
            self.wait(.5)
            self.play(topSects.animate.shift(.5*math.cos(PI/n)*r*DOWN+.5*Sects[0].get_width()*RIGHT), botSects.animate.shift(.5*math.cos(PI/n)*r*UP), run_time=2)
            self.wait(.5)
            self.play(topSects.animate.set_stroke(purple, width=0).set_fill(purple, opacity=1),botSects.animate.set_stroke(purple, width=0))
            self.wait(3)
            if n!=200:
                self.play(FadeOut(VGroup(topSects,botSects)))
        self.play(FadeOut(quest))
        self.play(FadeIn(VGroup(topcirc,botcirc,theradius)))
        self.wait()
        self.play(topcirc.animate.shift(.75*UP),botcirc.animate.shift(.75*DOWN),theradius.animate.shift(1.5*DOWN), run_time=2)
        self.play(ReplacementTransform(topcirc,line1), ReplacementTransform(botcirc,line2),ReplacementTransform(theradius.copy(),line3), ReplacementTransform(theradius,line4), run_time=2)
        self.wait()
        self.play(GrowFromCenter(topbrace), Write(halfcircum), run_time=2)
        self.wait(.5)
        self.play(GrowFromCenter(leftbrace), Write(radlabel), run_time=2)
        self.wait()
        self.play(TransformMatchingShapes(halfcircum.copy(),Final[4]), run_time=2)
        self.play(Write(Final[5]),run_time=.25)
        self.play(TransformMatchingShapes(radlabel.copy(),Final[6]), run_time=2)
        self.wait()
        Final[-1].move_to(Final[4].get_center())
        Final[-1].shift(.1*UP+.1*RIGHT)
        self.play(TransformMatchingShapes(Final[-4:-1],Final[-1]), run_time=1.5)
        self.wait(1)
        self.play(VGroup(Final[0:-4],Final[-1]).animate.next_to(line2,2*DOWN))
        self.wait()
        finalrect=SurroundingRectangle(VGroup(Final[0],Final[-1]), color=WHITE)
        self.play(ShowCreation(finalrect))
        self.wait(5)