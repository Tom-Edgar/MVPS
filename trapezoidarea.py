from manimlib import *

class Playground(Scene):
    def construct(self):
        color1="#3137fd"
        color2="#e60000"
        Points=[(0,0,0),(3,0,0),(2,2,0),(.5,2,0)]
        downpoint=(2,0,0)
        midpoint=(.25,1,0)
        theTrap=Polygon(*Points)

        hLine=Line(theTrap.get_vertices()[2],downpoint)
        hlabel=Tex("h")
        tLine=Line(Points[2],Points[3])

        bLine=Line(Points[0],Points[1])

        theDot=Dot()
        theDot.set_fill(color2, opacity=1)
        theDot.move_to(midpoint)
        Triangle1=Polygon(midpoint, Points[3],Points[2]).set_fill(color1, opacity=1)
        Trap2=Polygon(midpoint, Points[0],Points[1],Points[2]).set_fill(color1, opacity=1)
        line1=Line(Points[0],midpoint)
        line1.set_stroke(color2, width=6)
        line2=Line(midpoint, Points[2])

        Diagram=VGroup(theTrap,hLine,theDot,tLine,bLine,Triangle1,line1,line2,Trap2)
        Diagram.move_to((0,.75,0))
        Diagram.scale(1.5)

        topbrace=Brace(tLine,UP)
        b2label=Tex("b_2").scale(1)
        b2label.next_to(topbrace,UP)
        botbrace=Brace(bLine,DOWN)
        b1label=Tex("b_1").scale(1)
        b1label.next_to(botbrace,DOWN)
        hlabel.next_to(hLine,.5*LEFT)

        self.play(ShowCreation(theTrap), run_time=3)
        self.play(theTrap.animate.set_fill(color1, opacity=1))
        trapish=theTrap.copy()

        AreaFormula=VGroup(Tex(r"\mbox{Area}("),trapish.scale(.2),Tex(r")"),Tex("="))

        AreaFormula.arrange(RIGHT)
        AreaFormula.to_edge(DOWN, buff=.5)
        AreaFormula.to_edge(LEFT, buff=2)

        self.play(GrowFromCenter(botbrace),Write(b1label), run_time=2)

        self.play(GrowFromCenter(topbrace),Write(b2label), run_time=2)

        self.play(ShowCreation(hLine),Write(hlabel), run_time=2)
        hlabel.add_updater(lambda mob: self.bring_to_front(mob))
        hLine.add_updater(lambda mob: self.bring_to_front(mob))

        self.play(Write(AreaFormula[0]))
        self.play(ReplacementTransform(theTrap.copy(),AreaFormula[1]), run_time=3)
        self.play(Write(AreaFormula[2]))
        self.play(Write(AreaFormula[3]))

        self.wait(2)

        self.play(FadeIn(theDot,scale=.2))
        self.play(ShowCreation(line1), run_time=2)
        self.play(Rotate(line1,PI, about_point=theDot.get_center()), run_time=2)
        self.play(Uncreate(line1), run_time=2)
        self.wait(2)
        self.play(ShowCreation(line2), run_time=3)
        self.play(FadeOut(theDot))
        self.add(Triangle1,Trap2)
        self.remove(theTrap)
        self.play(Rotate(Triangle1,PI, about_point=theDot.get_center()), FadeOut(topbrace), run_time=3)
        finalTri=Polygon(Triangle1.get_vertices()[2],theTrap.get_vertices()[1], theTrap.get_vertices()[2]).set_fill(color1, opacity=1)
        fbrace=Brace(finalTri,DOWN)
        finlabel=Tex("b_1","+","b_2")
        finlabel.next_to(fbrace,DOWN)
        AreaFormula2=VGroup(Tex(r"\mbox{Area}("),finalTri.copy().scale(.2),Tex(r")"),Tex("="),Tex(r"\frac{1}{2}","h","(b_1+b_2)"))
        AreaFormula2.arrange(RIGHT)
        AreaFormula2.next_to(AreaFormula,.5*RIGHT)
        self.play(ReplacementTransform(botbrace,fbrace),TransformMatchingShapes(VGroup(b1label,b2label),finlabel), FadeIn(finalTri), run_time=2)
        self.wait(3)
        self.play(Write(AreaFormula2[0]))
        self.play(ReplacementTransform(finalTri.copy(),AreaFormula2[1]), run_time=3)
        self.play(Write(AreaFormula2[2]))

        self.wait(2)

        self.play(Write(AreaFormula2[3]))
        self.play(TransformMatchingShapes(VGroup(hlabel,finlabel).copy(),AreaFormula2[4]), run_time=3)
        self.wait(3)

        self.remove(Trap2,Triangle1)
        botbracen=Brace(bLine,DOWN)

        self.play(FadeOut(finalTri), FadeIn(theTrap),FadeOut(finlabel), FadeOut(fbrace), FadeIn(topbrace), FadeIn(b1label),FadeIn(botbracen), FadeIn(b2label))

        self.wait(5)




