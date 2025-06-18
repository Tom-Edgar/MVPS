from manimlib import *

class PTHinge(Scene):
    def construct(self):
        blue = "#88CCEE"
        deepred = "#882255"
        a=3
        b=2

        self.wait()
        TheTriangle = Polygon((0,0,0), (b, 0, 0), (0, a, 0)).set_fill(blue, opacity=1)
        ThirdTriangle=TheTriangle.copy()
        self.camera.frame.move_to(TheTriangle)


        ASquare = Polygon((0,0,0), (a,0,0), (a,a,0), (0,a,0)).set_fill(deepred, opacity=1)
        BSquare = Polygon((0,0,0), (b,0,0), (b,b,0), (0,b,0)).set_fill(deepred, opacity=1)
        ASquare.shift(-ASquare.get_vertices()[1])
        BSquare.shift(-BSquare.get_vertices()[3])

        alabel = Tex("a").next_to(TheTriangle, LEFT, buff=.05)
        blabel = Tex("b").next_to(TheTriangle, DOWN, buff=.05)
        clabel = Tex("c").move_to(Line(TheTriangle.get_vertices()[1], TheTriangle.get_vertices()[2])).shift((.4, 0, 0))

        def fronter(mob):
            self.bring_to_front(mob)

        ASquare2=ASquare.copy()
        BSquare2=BSquare.copy()

        Triangle2 = TheTriangle.copy()
        Triangle2.rotate(PI/2)
        Triangle2.shift(-Triangle2.get_vertices()[2]+ TheTriangle.get_vertices()[1])

        self.play(DrawBorderThenFill(TheTriangle), run_time=2)

        for x in [alabel, blabel, clabel]:
            self.play(Write(x), run_time=.5)
            x.add_updater(fronter)

        self.wait()

        self.play(DrawBorderThenFill(ASquare), run_time=2)

        self.play(DrawBorderThenFill(BSquare), run_time=2)

        a2label = Tex("a","^2").move_to(ASquare)
        b2label = Tex("b","^2").move_to(BSquare)

        self.wait(1)
        self.play(TransformMatchingShapes(alabel,a2label[0]), Write(a2label[1]))
        self.wait()
        self.play(TransformMatchingShapes(blabel,b2label[0]), Write(b2label[1]))

        self.wait(2)

        self.play(ReplacementTransform(TheTriangle.copy(), Triangle2), run_time=2)

        self.play(FadeOut(a2label), FadeOut(b2label))

        self.wait()

        TheTriangle.add_updater(fronter)
        Triangle2.add_updater(fronter)

        self.play(ASquare.animate.shift(a*RIGHT), BSquare.animate.shift(a*RIGHT+b*UP), run_time=3)
        self.wait(2)

        TileShape = Polygon(ASquare.get_vertices()[3], ASquare.get_vertices()[2], BSquare.get_vertices()[3], BSquare.get_vertices()[2], TheTriangle.get_vertices()[1]).set_fill(deepred, opacity=1)

        self.play(FadeIn(TileShape))
        self.wait(1)
        self.remove(ASquare,BSquare)
        TheTriangle.remove_updater(fronter)
        Triangle2.remove_updater(fronter)

        self.play(Rotate(TheTriangle, -3*PI/2, about_point=TheTriangle.get_vertices()[2]),Rotate(Triangle2, 3*PI/2, about_point=Triangle2.get_vertices()[1]), run_time=3)
        self.wait()
        CSquare = Polygon(TileShape.get_vertices()[4],TileShape.get_vertices()[3], Triangle2.get_vertices()[2], TileShape.get_vertices()[0]).set_fill(deepred, opacity=1)
        self.play(FadeIn(CSquare))

        c2label = Tex("c","^2").move_to(CSquare)

        self.wait()

        self.play(TransformMatchingShapes(clabel, c2label[0]), Write(c2label[1]))

        self.wait()
        
        self.remove(TheTriangle, Triangle2, TileShape)
        self.play(FadeIn(ThirdTriangle))
        self.play(FadeIn(ASquare2), FadeIn(BSquare2))

        self.wait(2)

        FinalEquality = VGroup(ASquare2, Tex("+"), BSquare2, Tex("="), CSquare).copy()
        FinalEquality.arrange(RIGHT, buff=.5).move_to(self.camera.frame.get_center()-[0,1,0])
        c2label2 = c2label.copy().move_to(FinalEquality[-1])
        a2label2=Tex("a^2")
        b2label2=Tex("b^2")
        a2label2.move_to(FinalEquality[0])
        b2label2.move_to(FinalEquality[2])

        self.play(ReplacementTransform(ASquare2, FinalEquality[0]),
                  ReplacementTransform(BSquare2, FinalEquality[2]),
                  ReplacementTransform(CSquare, FinalEquality[-1]),
                  FadeIn(FinalEquality[1]), FadeIn(FinalEquality[3]), ThirdTriangle.animate.shift(2.25*UP),
                  TransformMatchingShapes(c2label, c2label2),
                  FadeIn(a2label2), FadeIn(b2label2), run_time=2)
        self.bring_to_front(a2label2, b2label2)
        alabel3 = Tex("a").next_to(ThirdTriangle, LEFT, buff=.05)
        blabel3 = Tex("b").next_to(ThirdTriangle, DOWN, buff=.05)
        clabel3 = Tex("c").move_to(Line(ThirdTriangle.get_vertices()[1], ThirdTriangle.get_vertices()[2])).shift((.4, 0, 0))
        self.play(FadeIn(VGroup(alabel3,blabel3,clabel3)))

        self.wait(2)





        
        
