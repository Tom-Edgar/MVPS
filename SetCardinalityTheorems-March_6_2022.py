from manimlib import *

class SetSumPrinciple(Scene):
    def construct(self):
        self.wait(2)
        color1="#009E73"
        color2="#0072B2"
        color3="#CC79A7"
        color4="#F0E442"

        CompDef=VGroup(Text("Sum Principle.",font_size=35, font="Optima", t2c={"Sum Principle.": color3}),
                        TexText("Let \(A\) and \(B\) both be finite sets (possibly with elements in common).",font_size=35, font="Optima"))
        CompDef[0].to_edge(LEFT,buff=.5)
        CompDef[0].to_edge(UP,buff=.5)
        CompDef[1].next_to(CompDef[0],RIGHT)
        CompDef[1].to_edge(UP, buff=.5)
        self.play(Write(CompDef), run_time=3)
        circ1 = Circle(color=color2, fill_opacity=0)
        circ1.move_to([-.5, 0, 0])
        circ2 = Circle(color=color3, fill_opacity=0)
        circ2.move_to([.5,0,0])


        ABCircs=VGroup(circ1,circ2)
        ABCircs.scale(1.5)

        ABCircs.to_edge(UP, buff=2)

        ABCircs.to_edge(LEFT, buff=.75)

        alabel=Tex("A")
        alabel.next_to(circ1,DOWN)
        blabel=Tex("B")
        blabel.next_to(circ2,DOWN)
        ablabel = Tex("A","\\cup"," B")
        ablabel.next_to(ABCircs, UP)


        for x in [[circ1,alabel, color2],[circ2,blabel, color3]]:
            self.play(FadeIn(x[0]))
            self.play(Write(x[1]))

        self.wait(2)
        for x in [[circ1, alabel, color2], [circ2, blabel, color3]]:
            self.play(x[0].animate.set_fill(x[2], opacity=.5))

        self.wait()

        finalform = Tex("|","A", "\\cup", " B","|", "=", "|A|", "+", "|B|", "- ", "|A\\cap B|").scale(.95)
        finalform.to_edge(DOWN, buff=1)
        self.wait(2)

        self.play(TransformMatchingShapes(VGroup(alabel.copy(),blabel.copy()),ablabel), run_time=2)
        self.wait(2)
        self.play(TransformMatchingTex(ablabel, finalform[:5]),run_time=2)
        self.play(Write(finalform[5]))
        self.wait()
        football = Intersection(circ1, circ2, color=color1, fill_opacity=1)

        Acopy=circ1.copy()
        Acopy.shift(5.75*RIGHT)
        Bcopy = circ2.copy()
        Bcopy.shift(8.25*RIGHT)
        IntA=football.copy()
        IntB=football.copy()
        IntA.shift(5.75*RIGHT)
        IntB.shift(8.25*RIGHT)
        LeftOver=Difference(Bcopy,IntB,color=color3)
        LeftOver.set_fill(color3, opacity=.5)

        self.wait()

        aandblabel = Tex("A", "\\cap ", "B")
        aandblabel.next_to(football, DOWN)

        Equals=Tex("=")
        Equals.next_to(ABCircs,2*RIGHT)
        self.play(Write(Equals))

        self.wait(2)

        self.play(ReplacementTransform(circ1.copy(),Acopy), run_time=3)
        self.wait()

        self.play(TransformMatchingShapes(alabel,finalform[6]), run_time=2)
        self.wait()

        self.play(ReplacementTransform(circ2.copy(),Bcopy), run_time=3)
        self.wait()

        self.play(Write(finalform[7]))
        self.play(TransformMatchingShapes(blabel,finalform[8]), run_time=2)
        self.wait(3)
        self.play(FadeIn(football))
        self.play(Write(aandblabel))
        self.wait(2)
        self.play(ReplacementTransform(football,IntA),ReplacementTransform(football.copy(),IntB), run_time=3)

        self.wait(2)


        self.add(LeftOver)
        self.remove(Bcopy)
        self.play(FadeOut(IntB),Write(finalform[9]))

        self.play(TransformMatchingShapes(aandblabel,finalform[10]), run_time=2)
        self.wait(2)

        finalRect=SurroundingRectangle(finalform,color=WHITE, buff=.3)
        self.play(ShowCreation(finalRect))

        self.wait(5)


class SetProdPrinciple(Scene):
    def construct(self):
        self.wait(2)
        color1="#009E73"
        color2="#0072B2"
        color3="#CC79A7"
        color4="#F0E442"
        CompDef=VGroup(Text("Product Principle.",font_size=35, font="Optima", t2c={"Product Principle.": color3}),
                        TexText("Let \(A\) and \(B\) both be finite sets.",font_size=35, font="Optima"))
        CompDef[0].to_edge(LEFT,buff=.5)
        CompDef[0].to_edge(UP,buff=.5)
        CompDef[1].next_to(CompDef[0],RIGHT)
        CompDef[1].to_edge(UP, buff=.5)

        finalform = Tex("|", "A", "\\times", " B", "|", "=", "|A|", "\\cdot ", "|B|").scale(.95)
        #finalform.next_to(CompDef, 2*RIGHT)
        finalform.to_edge(DOWN, buff=.75)
        finalform.shift(2*LEFT)

        ADots=[Dot() for i in range(9)]
        BDots=[Dot() for i in range(7)]
        for x in ADots:
            x.set_fill(color2, opacity=1)
        for x in BDots:
            x.set_fill(color3, opacity=1)
        AD=VGroup(*ADots)
        AD.arrange(1.5*DOWN)
        AD.move_to((0,0,0))
        BD=VGroup(*BDots)
        BD.arrange(1.5*DOWN)
        BD.move_to((0,0,0))
        circA = Ellipse(width=.5, height=5.5, color=color2)
        circA.set_fill(color=color2, opacity=.35)
        circB = Ellipse(width=.5, height=4.5, color=color3)
        circB.set_fill(color=color3,opacity=.35)
        setA=VGroup(AD,circA)
        setA.to_edge(LEFT, buff=.75)
        setA.to_edge(UP, buff=2)
        setB=VGroup(BD,circB)
        setB.to_edge(LEFT, buff=1.75)
        setB.to_edge(UP, buff=2.5)
        setB=VGroup(BD,circB)
        setB.to_edge(LEFT, buff=2)
        setB.to_edge(UP, buff=2.5)
        alabel=Tex("A")
        alabel.next_to(setA,UP)
        blabel = Tex("B")
        blabel.next_to(setB, UP)
        atimes=Tex("\\times")
        atimes.move_to((.5*setA.get_x()+.5*setB.get_x(),.5*setA.get_y()+.5*setB.get_y(),0))

        equals=Tex("=")
        equals.move_to((-3,.5*setA.get_y()+.5*setB.get_y(),0))

        axblabel = Tex("A","\\times ","B")

        axblabel.move_to((0,alabel.get_y()-.2,0))
        axblabel.to_edge(RIGHT, buff=4)

        self.play(Write(CompDef), run_time=3)
        self.play(FadeIn(circA), run_time=1)
        self.play(ShowCreation(AD), run_time=3)
        self.play(Write(alabel), run_time=1)

        self.play(Write(atimes))

        self.play(FadeIn(circB), run_time=1)
        self.play(ShowCreation(BD), run_time=3)
        self.play(Write(blabel), run_time=1)
        self.wait()

        self.play(Write(equals))

        self.wait(2)

        setAcopy=setA.copy()

        setAcopy.rotate(-PI/2)
        setAcopy.to_edge(RIGHT, buff=2)
        setAcopy.to_edge(UP, buff=6.5)

        self.play(TransformMatchingShapes(VGroup(alabel,blabel).copy(),axblabel), run_time=3)

        self.wait(.5)

        self.play(ReplacementTransform(setA.copy(), setAcopy), run_time=3)
        self.wait(2)

        BCopies=VGroup(*[setB.copy() for x in ADots])
        anis=[]
        for i in range(9):
            BCopies[i].next_to(setAcopy[0][i],.2*UP)
            anis.append(ReplacementTransform(setB.copy(),BCopies[i]))
        self.play(*anis,run_time=3)
        self.wait(2)

        LBrace=Brace(BCopies[-1][0],LEFT)
        LBrace.shift(.1*LEFT)
        cardb=Tex("|","B","|")
        cardb.next_to(LBrace,LEFT)
        self.play(GrowFromCenter(LBrace), run_time=2)
        self.play(TransformMatchingShapes(blabel.copy(), cardb), run_time=2)


        fades=[]
        for i in range(9):
            fades.append(FadeOut(BCopies[i][1]))
        self.play(*fades)
        self.wait()

        ADDS=[setAcopy[0].copy() for x in BDots]
        anis2=[]
        for i in range(7):
            ADDS[i].next_to(BCopies[0][0][i],.1*LEFT)
            anis2.append(ReplacementTransform(setAcopy[0].copy(),ADDS[i]))

        self.play(*anis2,FadeOut(setAcopy), run_time=3)

        DBrace=Brace(ADDS[-1],DOWN)
        carda=Tex("|","A","|")
        carda.next_to(DBrace,DOWN)
        self.play(GrowFromCenter(DBrace), run_time=2)
        self.play(TransformMatchingShapes(alabel.copy(), carda), run_time=2)

        self.wait(2)

        self.play(TransformMatchingShapes(axblabel.copy(),finalform[:5]), run_time=2)
        self.play(Write(finalform[5]))
        self.play(TransformMatchingShapes(carda.copy(),finalform[6]), run_time=2)
        self.play(Write(finalform[7]))
        self.play(TransformMatchingShapes(cardb.copy(),finalform[8]), run_time=2)

        self.wait(2)

        finalRect=SurroundingRectangle(finalform,color=WHITE, buff=.3)
        self.play(ShowCreation(finalRect))

        self.wait(5)
