from manimlib import *

def acirc(thecolor, radius):
    C=ParametricCurve(
                lambda u: (radius * math.cos(u), radius* math.sin(u), 0), t_min=0, t_max=2 * PI)
    C.set_stroke(thecolor, width=2)
    return C

def circRing(radius, distance, thecolor,n):
    thering=[acirc(thecolor, radius) for i in range(n)]
    for i in range(n):
        thering[i].move_to((distance*math.cos(2*PI*i/n),distance*math.sin(2*PI*i/n),0))

    return VGroup(*thering)
class GeoSimSeven(Scene):
    def construct(self):
        color1="#00FFFF"
        color2="#FF007F"
        color3="#39FF14"

        n=6
        self.wait()

        firstcirc=acirc(color1, 1)
        ring1=circRing(.3,1.5,color1,n)
        newring=[VGroup(firstcirc,ring1).copy() for i in range(n)]
        for i in range(n):
            newring[i].scale(.3)
            newring[i].move_to((2.5 * math.cos(2 * PI * i / n), 2.5 * math.sin(2 * PI * i / n), 0))

        finalring=[VGroup(firstcirc,ring1,*newring).copy() for i in range(n)]
        for i in range(n):
            finalring[i].scale(.3)
            finalring[i].move_to((4.2 * math.cos(2 * PI * i / n), 4.2 * math.sin(2 * PI * i / n), 0))

        Pic=VGroup(firstcirc.copy(), VGroup(firstcirc,ring1).copy(),VGroup(firstcirc,ring1,*newring).copy(),VGroup(firstcirc,ring1,*newring,*finalring).copy())
        Pic[:3].arrange(5*RIGHT)
        Pic.scale(.5)
        Pic[:3].to_edge(UP, buff=1)
        Pic[:3].to_edge(LEFT, buff=.5)

        Labels=[Tex("1"),Tex(str(n+1)),Tex(str(n+1),"^{n-1}"),Tex(str(n+1),"^n")]
        cdots=Tex(r"\cdots")

        for i in range(4):
            if i!=3:
                Labels[i].next_to(Pic[i],UP)
            if i==0:
                self.play(ShowCreation(Pic[i]))
                self.play(Write(Labels[i]))
            elif i==1:
                self.play(ReplacementTransform(Pic[i-1].copy(),Pic[i][0]))
                for j in range(n):
                    self.play(ReplacementTransform(Pic[i-1].copy(),Pic[i][1][j]))
                self.play(TransformMatchingShapes(Labels[i-1].copy(),Labels[i]), run_time=2)
            elif i==2:
                cdots.move_to((.5*Labels[1].get_x()+.5*Labels[2].get_x(),.5*Labels[1].get_y()+.5*Labels[2].get_y(),0))
                self.play(Write(cdots))
                self.wait()
                self.play(ReplacementTransform(Pic[i-1].copy(),Pic[i][0:2]))
                for j in range(n):
                    self.play(ReplacementTransform(Pic[i-1].copy(),Pic[i][2+j]))
                self.play(TransformMatchingShapes(Labels[i-1].copy(),Labels[i]), run_time=2)
            elif i==3:
                self.wait(2)
                Pic[i].move_to((0,-1,0))
                Pic[i].to_edge(RIGHT, buff=.5)
                Labels[i].next_to(Pic[i],3*UP)
                self.play(ReplacementTransform(Pic[i-1].copy(),Pic[i][0:n+2]))
                for j in range(n):
                    self.play(ReplacementTransform(Pic[i-1].copy(),Pic[i][n+2+j]))
                self.play(TransformMatchingShapes(Labels[i-1].copy(),Labels[i]), run_time=2)

            self.wait()
            self.wait()

        Formula=Tex("2\cdot ","(","1","+",str(n+1),"+",r"\cdots","+",str(n+1)+"^{n-1}",")","+","1")

        Second=Pic[-1].copy()
        Second.set_stroke(color3)
        Second.to_edge(LEFT, buff=.5)
        Formula.next_to(Second,3*UP)
        wings=[VGroup(Second[1][0],Second[2], Second[n+2]).copy()]
        self.play(ReplacementTransform(Pic[:-1], wings[-1]), run_time=2)

        self.play(TransformMatchingShapes(Labels[0], Formula[2]),TransformMatchingShapes(Labels[1], Formula[4]),TransformMatchingShapes(cdots, Formula[6]),TransformMatchingShapes(Labels[2], Formula[8]), FadeIn(VGroup(*[Formula[i] for i in [3,5,7]])), run_time=3)
        lastform=[Formula[0]]
        for i in range(n-1):
            newwing = wings[-1].copy()
            self.play(Rotate(newwing, 2 * PI / n, about_point=Second[0].get_center()), run_time=2)
            if i==0:
                self.play(Write(Formula[0]), FadeIn(Formula[1]), FadeIn(Formula[9]))
            else:
                astring=str(i+2)
                thetex=Tex(astring+"\cdot ")
                thetex.move_to(Formula[0].get_center())
                self.play(TransformMatchingShapes(lastform[-1],thetex))
                lastform.append(thetex)

            wings.append(newwing)

        self.wait()

        self.play(FadeIn(Second[0]))
        self.play(Write(Formula[-2:]))
        self.add(Second[1:])
        self.remove(*wings)
        self.wait(2)
        Final=Pic[-1].copy()
        Final.move_to((0,-1,0))
        Final.set_stroke(color2)

        equals=Tex("=")
        equals.next_to(Final,5*UP)
        equals.shift(2*RIGHT)

        self.play(ReplacementTransform(Pic[-1], Final), ReplacementTransform(Second,Final), VGroup(lastform[-1], *Formula[1:]).animate.next_to(equals,LEFT), Labels[-1].animate.next_to(equals,RIGHT), run_time=3)
        self.wait()
        self.play(Write(equals))

        self.wait(5)

class GeoSimNine(Scene):
    def construct(self):
        color2="#00FFFF"
        color3="#FF007F"
        color1="#39FF14"

        n=8
        self.wait()
        firstcirc=acirc(color1, 1)
        ring1=circRing(.3,1.5,color1,n)
        newring=[VGroup(firstcirc,ring1).copy() for i in range(n)]
        for i in range(n):
            newring[i].scale(.3)
            newring[i].move_to((2.5 * math.cos(2 * PI * i / n), 2.5 * math.sin(2 * PI * i / n), 0))

        finalring=[VGroup(firstcirc,ring1,*newring).copy() for i in range(n)]
        for i in range(n):
            finalring[i].scale(.3)
            finalring[i].move_to((4.2 * math.cos(2 * PI * i / n), 4.2 * math.sin(2 * PI * i / n), 0))

        Pic=VGroup(firstcirc.copy(), VGroup(firstcirc,ring1).copy(),VGroup(firstcirc,ring1,*newring).copy(),VGroup(firstcirc,ring1,*newring,*finalring).copy())
        Pic[:3].arrange(5*RIGHT)
        Pic.scale(.5)
        Pic[:3].to_edge(UP, buff=1)
        Pic[:3].to_edge(LEFT, buff=.5)

        Labels=[Tex("1"),Tex(str(n+1)),Tex(str(n+1),"^{n-1}"),Tex(str(n+1),"^n")]
        cdots=Tex(r"\cdots")

        for i in range(4):
            if i!=3:
                Labels[i].next_to(Pic[i],UP)
            if i==0:
                self.play(ShowCreation(Pic[i]))
                self.play(Write(Labels[i]))
            elif i==1:
                self.play(ReplacementTransform(Pic[i-1].copy(),Pic[i][0]))
                for j in range(n):
                    self.play(ReplacementTransform(Pic[i-1].copy(),Pic[i][1][j]))
                self.play(TransformMatchingShapes(Labels[i-1].copy(),Labels[i]), run_time=2)
            elif i==2:
                cdots.move_to((.5*Labels[1].get_x()+.5*Labels[2].get_x(),.5*Labels[1].get_y()+.5*Labels[2].get_y(),0))
                self.play(Write(cdots))
                self.wait()
                self.play(ReplacementTransform(Pic[i-1].copy(),Pic[i][0:2]))
                for j in range(n):
                    self.play(ReplacementTransform(Pic[i-1].copy(),Pic[i][2+j]))
                self.play(TransformMatchingShapes(Labels[i-1].copy(),Labels[i]), run_time=2)
            elif i==3:
                self.wait(2)
                Pic[i].move_to((0,-1,0))
                Pic[i].to_edge(RIGHT, buff=.5)
                Labels[i].next_to(Pic[i],3*UP)
                self.play(ReplacementTransform(Pic[i-1].copy(),Pic[i][0:n+2]))
                for j in range(n):
                    self.play(ReplacementTransform(Pic[i-1].copy(),Pic[i][n+2+j]))
                self.play(TransformMatchingShapes(Labels[i-1].copy(),Labels[i]), run_time=2)

            self.wait()
            self.wait()

        Formula=Tex("2\cdot ","(","1","+",str(n+1),"+",r"\cdots","+",str(n+1)+"^{n-1}",")","+","1")

        Second=Pic[-1].copy()
        Second.set_stroke(color3)
        Second.to_edge(LEFT, buff=.5)
        Formula.next_to(Second,3*UP)
        wings=[VGroup(Second[1][0],Second[2], Second[n+2]).copy()]
        self.play(ReplacementTransform(Pic[:-1], wings[-1]), run_time=2)

        self.play(TransformMatchingShapes(Labels[0], Formula[2]),TransformMatchingShapes(Labels[1], Formula[4]),TransformMatchingShapes(cdots, Formula[6]),TransformMatchingShapes(Labels[2], Formula[8]), FadeIn(VGroup(*[Formula[i] for i in [3,5,7]])), run_time=3)
        lastform=[Formula[0]]
        for i in range(n-1):
            newwing = wings[-1].copy()
            self.play(Rotate(newwing, 2 * PI / n, about_point=Second[0].get_center()), run_time=2)
            if i==0:
                self.play(Write(Formula[0]), FadeIn(Formula[1]), FadeIn(Formula[9]))
            else:
                astring=str(i+2)
                thetex=Tex(astring+"\cdot ")
                thetex.move_to(Formula[0].get_center())
                self.play(TransformMatchingShapes(lastform[-1],thetex))
                lastform.append(thetex)

            wings.append(newwing)

        self.wait()

        self.play(FadeIn(Second[0]))
        self.play(Write(Formula[-2:]))
        self.add(Second[1:])
        self.remove(*wings)
        self.wait(2)
        Final=Pic[-1].copy()
        Final.move_to((0,-1,0))
        Final.set_stroke(color2)

        equals=Tex("=")
        equals.next_to(Final,5*UP)
        equals.shift(2*RIGHT)

        self.play(ReplacementTransform(Pic[-1], Final), ReplacementTransform(Second,Final), VGroup(lastform[-1], *Formula[1:]).animate.next_to(equals,LEFT), Labels[-1].animate.next_to(equals,RIGHT), run_time=3)
        self.wait()
        self.play(Write(equals))

        self.wait(5)

class GeoSimCitation(Scene):
    def construct(self):
        color2="#00FFFF"
        color3="#FF007F"
        color1="#39FF14"

        n=8
        self.wait()
        Setup=TexText("Modifying the image appropriately shows that for \(n\geq 4\) and \(k\geq 1\)",font_size=40)
        Setup.to_edge(LEFT, buff=.75)
        Setup.shift(3*UP)

        FinalFormula=Tex("(n-1)\cdot(1+n+n^2+\cdots +n^{k-1}) +1 = n^k")
        FinalFormula.shift(2*UP)
        self.play(Write(Setup), run_time=2)
        self.wait()
        self.play(Write(FinalFormula), run_time=3)
        self.wait()

        self.wait(1)

        CitationText=TexText("This animation is based on a visual proof by Mingjang Chen.", font_size=40, font="Arial",t2c={"Mingjang Chen" : "#0072B2"})
        CitationText[0][-13:].set_fill(color="#0072B2",opacity=1)

        CitationText2=TexText("Check the description for more information.", font_size=40, font="Arial",t2c={"Edgar A. Ramos" : "#0072B2"})

        CitationText.shift(.5*UP)

        CitationText2.next_to(CitationText,DOWN)

        self.play(Write(CitationText))

        self.play(Write(CitationText2))

        self.wait(7)

