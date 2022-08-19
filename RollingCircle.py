from manimlib import *

class roll(Scene):
    def construct(self):
        fontcol=WHITE
        credittext=Text("MVPs",font_size=17, font="Arial", color=fontcol)
        credittext.move_to((6.7,-3.75,0))
        self.add(credittext)

        introfont="Imprint MT Shadow"
        thesize=60
        TheTitle=[Text("MICRO", font=introfont, font_size=thesize,color=WHITE),Text("VISUAL", font=introfont, font_size=thesize,color=WHITE),Text("PROOFS", font= introfont, font_size=thesize,color=WHITE)]
 
        MVPs=VGroup(*TheTitle)
        MVPs.arrange(RIGHT)
        MVPs.move_to((0,.5,0))

        self.play(FadeIn(MVPs))

        MVPTitle=VGroup(Text("M", font= introfont, font_size=thesize, color=WHITE), Text("V", font= introfont, font_size=thesize, color=WHITE),Text("P s", font= introfont, font_size=thesize, color=WHITE))
        MVPTitle.arrange(RIGHT)
        MVPTitle.move_to((0,.5,0))

        

        episode=Text("A Rolling Circle Squares Itself", color="#0072B2", font= introfont, font_size=thesize)


        episode.move_to((0,-.5,0))

        self.play(TheTitle[0].animate.become(MVPTitle[0]),TheTitle[1].animate.become(MVPTitle[1]),TheTitle[2].animate.become(MVPTitle[2]),Write(episode))
        self.wait(2)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects[1:]]
        )

        self.wait()

        color1="#009E73"
        color2="#0072B2"
        color3="#CC79A7"
        color4="#F0E442"

        self.play(
            # Set the size with the width of a object
            self.camera.frame.set_width,10,
            # Move the camera to the object
        )

        thesize=17

        thalesText=Text("Thales triangle theorem forces this triangle to be right-angled.", font_size=thesize, font="Arial")
        thalesText.move_to((-1.5,-2.5,0))

  
        congtext=VGroup(Text("Thus, these two triangles are similar:", font_size=thesize, font="Arial"),Tex("{{\\frac{\\pi r}{x}}}").scale(.6),Tex("{{=}}").scale(.6),Tex("{{\\frac{x}{r}}}").scale(.6))

        congtext.arrange(RIGHT)
        congtext.move_to((-1.5,-2.5,0))
        ztext=Tex("{{x^2=\pi r^2}}").scale(.6)
        ztext.next_to(congtext[0],RIGHT)
        play_kw={"run_time":3}

        unitcirc=Circle(color=WHITE)


        unitcirc.move_to((-PI/2,1,0))

        circarea=Tex("A=\\pi r^2").scale(.7)
        circarea.move_to((-4,1.8,0))
        
        topdot=Dot(color=color2)
        topdot.move_to((-PI/2+math.cos(PI/2),1+math.sin(PI/2),0))

        radius=Line((unitcirc.get_x(),unitcirc.get_y(),0),(topdot.get_x(),topdot.get_y(),0))
        BigRadius=Line((-PI/2,0,0),(PI/2,0,0))
        BigRadius.set_stroke(color2)

        semicirc = ParametricCurve(
            lambda u: (-PI/2+math.cos(PI/2-u),1+math.sin(PI/2-u),0), t_min=0, t_max=PI) 
        semicirc.set_stroke(color2, width=4)
        self.play(ShowCreation(radius))

        self.play(ShowCreation(unitcirc))
        self.play(ShowCreation(topdot))

        fradlabel=Tex("r").scale(.7)
        fradlabel.next_to(radius,.7*LEFT)



        self.play(Write(fradlabel))
        self.wait()

        self.play(unitcirc.animate.set_fill(color1,opacity=.7))

        unitcirc.set_stroke(WHITE)


        self.play(TransformMatchingTex(fradlabel,circarea))

        self.bring_to_front(radius) 

        self.wait(2)


        self.play(unitcirc.animate.set_fill(BLACK,opacity=1))

        unitcirc.set_stroke(WHITE)

        self.wait(2)

        self.play(ShowCreation(semicirc))

        self.wait(1)    

        def update_circ(mob, alpha):
            mob.become(
                Circle(color=WHITE).move_to([-PI/2+interpolate(0, PI, alpha), 1, 0]).rotate(interpolate(0, -180*DEGREES, alpha))
            )
        def update_dot(mob, alpha):
            mob.become(
                Dot(color=color2).move_to([-PI/2+interpolate(0, PI, alpha)+math.cos(PI/2-alpha*PI), 1+math.sin(PI/2-alpha*PI), 0])
            )

        def update_rad(mob, alpha):
            mob.become(
                Line([-PI/2+interpolate(0, PI, alpha), 1, 0],[-PI/2+interpolate(0, PI, alpha)+math.cos(PI/2-alpha*PI), 1+math.sin(PI/2-alpha*PI), 0])
            )

        def update_semi(mob, alpha):
            mob.become(
                ParametricCurve(
            lambda u: (interpolate(0,PI,alpha)-PI/2+math.cos(PI/2-u-interpolate(0,PI,alpha)),1+math.sin(PI/2-u-interpolate(0,PI,alpha)),0), t_min=0, t_max=PI)
            )

        self.play(
            UpdateFromAlphaFunc(unitcirc, update_circ),UpdateFromAlphaFunc(topdot, update_dot),UpdateFromAlphaFunc(radius, update_rad),UpdateFromAlphaFunc(semicirc, update_semi),ShowCreation(BigRadius),**play_kw
        )

        bradbracelabel=Tex("\\pi r").scale(.7)
        bradbracelabel.next_to(BigRadius,.7*DOWN)
   
        self.play(Write(bradbracelabel))
        self.wait()
        
        NewRadius=Line((unitcirc.get_x(),unitcirc.get_y(),0),(unitcirc.get_x()+1,unitcirc.get_y(),0))
        self.play(ShowCreation(NewRadius))

        nradbracelabel=Tex("r").scale(.7)
        nradbracelabel.next_to(NewRadius,.7*DOWN)

        self.play(Write(nradbracelabel))
        self.wait()

        self.play(NewRadius.animate.shift(DOWN), nradbracelabel.animate.shift(DOWN))

        self.wait(2)

        Bigsemicirc = ParametricCurve(
            lambda u: (.5+(1+PI/2-.5)*math.cos(u),(1+PI/2-.5)*math.sin(u),0), t_min=-PI, t_max=0) 
        Bigsemicirc.set_stroke(WHITE, width=4)

        self.play(FadeIn(Bigsemicirc),**play_kw)
        self.wait()

        SquareLine=Line((topdot.get_x(),topdot.get_y(),0),(topdot.get_x(),topdot.get_y()-math.sqrt(PI),0))
        self.play(ShowCreation(SquareLine))

        self.wait()

        squarebracelabel=Tex("x").scale(.7)
        squarebracelabel.next_to(NewRadius,.7*LEFT+3*DOWN)

        self.play(Write(squarebracelabel))
        self.wait(2)


        thales1=DashedLine((unitcirc.get_x()+1,unitcirc.get_y()-1,0),(topdot.get_x(),topdot.get_y()-math.sqrt(PI),0))
        thales2=DashedLine((topdot.get_x(),topdot.get_y()-math.sqrt(PI),0),(-PI/2,0,0))

        self.play(ShowCreation(thales1))
        self.play(ShowCreation(thales2))

        bigTriangle=Polygon((unitcirc.get_x()+1,unitcirc.get_y()-1,0),(topdot.get_x(),topdot.get_y()-math.sqrt(PI),0),(-PI/2,0,0))

        leftTriangle=Polygon((topdot.get_x(),topdot.get_y(),0),(topdot.get_x(),topdot.get_y()-math.sqrt(PI),0),(-PI/2,0,0))

        rightTriangle=Polygon((unitcirc.get_x()+1,unitcirc.get_y()-1,0),(topdot.get_x(),topdot.get_y()-math.sqrt(PI),0),(topdot.get_x(),topdot.get_y(),0))


        bigTriangle.set_fill(color3,opacity=.7)

        leftTriangle.set_fill(color4,opacity=.7)

        rightTriangle.set_fill(color2,opacity=.7)


        self.play(Write(thalesText),FadeIn(bigTriangle))
        self.wait(4)

        self.play(FadeOut(thalesText),FadeOut(bigTriangle))

        self.wait()

        self.play(Write(congtext[0]),FadeIn(leftTriangle),FadeIn(rightTriangle))
        self.wait(3)
        self.play(TransformMatchingTex(bradbracelabel.copy(),congtext[1]),TransformMatchingTex(squarebracelabel.copy(),congtext[1]))
        self.wait(3)
        self.play(Write(congtext[2]))
        self.wait()
        self.play(TransformMatchingTex(nradbracelabel.copy(),congtext[3]),TransformMatchingTex(squarebracelabel.copy(),congtext[3]))

        self.wait(2)
        self.play(FadeOut(leftTriangle),FadeOut(rightTriangle))

        resultx=Tex("x^2=\pi r^2").scale(.7)
        resultx.next_to(congtext[0],RIGHT)

        resultx.shift(.1*UP)

        self.play(ReplacementTransform(VGroup(congtext[1],congtext[2],congtext[3]), resultx))

        self.wait(3)


        TheSquare=Polygon((topdot.get_x(),topdot.get_y(),0),(topdot.get_x(),topdot.get_y()-math.sqrt(PI),0),(topdot.get_x()+math.sqrt(PI),topdot.get_y()-math.sqrt(PI),0),(topdot.get_x()+math.sqrt(PI),topdot.get_y(),0))
        TheSquare.set_fill(color1,opacity=.7)

        self.play(ShowCreation(TheSquare), **play_kw)

        self.wait(2)


        sqarea=Tex("A=x^2").scale(.7)
        sqarea.move_to((-4.1,1.2,0))

        self.play(TransformMatchingTex(squarebracelabel.copy(),sqarea))

        self.wait(2)


        sqarea2=Tex("=\pi r^2").scale(.7)
        sqarea2.next_to(sqarea, .7*RIGHT)

        
        self.play(TransformMatchingTex(resultx.copy(),sqarea2))

        self.wait(2)


        self.play(unitcirc.animate.set_fill(color1,opacity=.7),**play_kw)

        self.wait(2)

        unitcirc.set_stroke(WHITE)

        FinalText=Text("We have constructed a square with the area of the original circle.", font_size=thesize, font="Arial")

        FinalText.move_to((0,2.5,0))

        self.play(Write(FinalText),**play_kw)

        self.wait(2)

        finalbox=SurroundingRectangle(FinalText,color=WHITE)

        self.play(ShowCreation(finalbox))
        self.wait(10)

        

        

