from manimlib import *

def aTriangle(acolor, op):
    T= Polygon((-1,0,0),(1,0,0),(0,math.sqrt(3),0)).set_fill(acolor, opacity=op)
    T.shift((0,-math.tan(PI/6),0))
    return T

def aSquare(acolor, op):
    T= Polygon((-1,-1,0),(1,-1,0),(1,1,0), (-1,1,0)).set_fill(acolor, opacity=op)
    return T

def rotMat(dir, ang):
    if dir=='yz':
        mat = [[1,0,0],[0, math.cos(ang), -math.sin(ang)],[0, math.sin(ang), math.cos(ang)]]
    elif dir=='xz':
        mat = [[math.cos(ang),0, -math.sin(ang)], [0,1,0],[math.sin(ang), 0, math.cos(ang)]]
    else:
        mat = [[math.cos(ang), -math.sin(ang),0],[math.sin(ang), math.cos(ang),0],[0,0,1]]
    return mat

class FoldTetrahedron(ThreeDScene):
    def construct(self):

        frame = self.camera.frame
        frame.set_euler_angles(
            theta = 0*DEGREES,
            phi = 0*DEGREES,
        )

        colors=[BLUE, BLUE, BLUE, GREEN]
        oplevel=0.6

        theTris = VGroup(*[aTriangle(colors[i], oplevel) for i in range(4)])

        a = ValueTracker(0)

        for i in range(1,4):
            theTris[i].rotate(PI, about_point=[0,0,0])
            theTris[i].apply_matrix(rotMat("yz", a.get_value()))
            theTris[i].shift(-theTris[i].get_vertices()[0]+theTris[0].get_vertices()[1])
            theTris[i].rotate(2*PI*(i-1)/3, about_point=[0,0,0])

        self.play(FadeIn(theTris))
        self.wait()
        self.play(frame.animate.set_euler_angles(phi=70*DEGREES), run_time=3)
        self.wait()

        def triUpdater(mob):
            tempTris = VGroup(*[aTriangle(colors[i], oplevel) for i in range(4)])
            for i in range(1, 4):
                tempTris[i].rotate(PI, about_point=[0, 0, 0])
                tempTris[i].apply_matrix(rotMat("yz", a.get_value()))
                tempTris[i].shift(-tempTris[i].get_vertices()[0] + theTris[0].get_vertices()[1])
                tempTris[i].rotate(2 * PI * (i - 1) / 3, about_point=[0, 0, 0])
            mob.become(tempTris)

        theTris.add_updater(triUpdater)

        self.play(LaggedStart(frame.animate.set_euler_angles(theta=360*DEGREES), a.animate.set_value(-(PI-1.23))), lag_ratio=0.1, run_time=8)

        self.wait()

        self.play(a.animate.set_value(0), run_time=4)
        self.play(a.animate.set_value(-(PI-1.23)), run_time=4)
        self.play(a.animate.set_value(0), run_time=4)
        self.play(frame.animate.set_euler_angles(phi=00*DEGREES), run_time=3)


class FoldCube(ThreeDScene):
    def construct(self):

        frame = self.camera.frame
        frame.set_euler_angles(
            theta = 0*DEGREES,
            phi = 0*DEGREES,
        )

        colors=[BLUE, RED, YELLOW, GREEN, GREY, ORANGE]
        oplevel=0.6

        theSquares = VGroup(*[aSquare(colors[i], oplevel) for i in range(6)])

        a = ValueTracker(0)

        for i in range(1,6):
            if i<5:
                theSquares[i].rotate(PI, about_point=[0,0,0])
                theSquares[i].apply_matrix(rotMat("yz", a.get_value()))
                theSquares[i].shift(-theSquares[i].get_vertices()[0]+theSquares[0].get_vertices()[1])
                theSquares[i].rotate(2*PI*(i-1)/4, about_point=[0,0,0])
            else:
                theSquares[i].rotate(PI, about_point=[0, 0, 0])
                theSquares[i].apply_matrix(rotMat("yz", a.get_value()))
                theSquares[i].shift(-theSquares[i].get_vertices()[0] + theSquares[0].get_vertices()[1])
                theSquares[i].rotate(2 * PI * (i) / 4, about_point=[0, 0, 0])
                theSquares[i].shift(-theSquares[i].get_vertices()[0] + theSquares[2].get_vertices()[3])


        self.play(FadeIn(theSquares))
        self.wait()
        self.play(frame.animate.set_euler_angles(phi=70*DEGREES), run_time=3)
        self.wait()

        def sqUpdater(mob):
            tempSquares = VGroup(*[aSquare(colors[i], oplevel) for i in range(6)])
            for i in range(1, 6):
                if i < 5:
                    tempSquares[i].rotate(PI, about_point=[0, 0, 0])
                    tempSquares[i].apply_matrix(rotMat("yz", a.get_value()))
                    tempSquares[i].shift(-tempSquares[i].get_vertices()[0] + tempSquares[0].get_vertices()[1])
                    tempSquares[i].rotate(2 * PI * (i - 1) / 4, about_point=[0, 0, 0])
                else:
                    tempSquares[i].rotate(PI, about_point=[0, 0, 0])
                    tempSquares[i].apply_matrix(rotMat("yz", 2*a.get_value()))
                    tempSquares[i].shift(-tempSquares[i].get_vertices()[0] + tempSquares[0].get_vertices()[1])
                    tempSquares[i].rotate(2 * PI * (i) / 4, about_point=[0, 0, 0])
                    tempSquares[i].shift(-tempSquares[i].get_vertices()[0] + tempSquares[2].get_vertices()[3])
            mob.become(tempSquares)

        theSquares.add_updater(sqUpdater)

        self.play(LaggedStart(frame.animate.set_euler_angles(theta=360*DEGREES), a.animate.set_value(-PI/2)), lag_ratio=0.1, run_time=8)

        self.wait()

        self.play(a.animate.set_value(0), run_time=4)
        self.play(a.animate.set_value(-PI/2), run_time=4)
        self.play(a.animate.set_value(0), run_time=4)
        self.play(frame.animate.set_euler_angles(phi=00*DEGREES), run_time=3)

### Dodecahedron code below, two different options

def pentagon():
    P=Polygon(*[[1.5 * math.cos(2*PI*j/5+PI/2), 1.5 * math.sin(2*PI*j/5+PI/2)+1.2135, 0] for j in range(5)]).set_stroke(width=1)
    return P

class FoldDodecLayers(ThreeDScene):
    def construct(self):
        lgreen = "#44AA99"
        colors = [lgreen, lgreen, lgreen, lgreen, lgreen, lgreen]
        oplevel=1

        frame = self.camera.frame
        frame.set_euler_angles(
            theta=0 * DEGREES,
            phi=0 * DEGREES,
        )


        vertang=ValueTracker(0)

        centralPent=pentagon().set_fill(colors[0], opacity=oplevel)

        Level3=pentagon().set_fill(colors[0], opacity=oplevel)
        Level3.apply_matrix(rotMat("yz", vertang.get_value()))
        Level3.apply_matrix(rotMat("xy", PI))
        Level3.rotate(6 * PI / 5, about_point=[0, 1.2135, 0])
        Level1=VGroup(*[pentagon().set_fill(colors[i%6], opacity=oplevel) for i in range(5)])
        Level2 = VGroup(*[pentagon().set_fill(colors[(i+1) % 6], opacity=oplevel) for i in range(5)])

        for x in Level2[:3]:
            x.apply_matrix(rotMat("yz", vertang.get_value()))
            x.apply_matrix(rotMat("xy", PI))
        VGroup(Level2[3],Level3).apply_matrix(rotMat("yz", vertang.get_value()))
        VGroup(Level2[3], Level3).apply_matrix(rotMat("xy", PI))
        Level2[4].apply_matrix(rotMat("yz", vertang.get_value()))
        Level2[4].apply_matrix(rotMat("xy", PI))

        Doubles=VGroup(*[VGroup(Level1[i],Level2[i]) for i in range(3)])
        Doubles.add(VGroup(Level1[3],Level2[3],Level3))
        Doubles.add(VGroup(Level1[4],Level2[4]))

        Doubles[0].apply_matrix(rotMat("xy", -PI/5))
        Doubles[0].shift(-Doubles[0][0].get_vertices()[0]+centralPent.get_vertices()[3])
        Doubles[0].apply_matrix(rotMat("yz", -vertang.get_value()))

        Doubles[1].apply_matrix(rotMat("xy", -PI / 5))
        Doubles[1].shift(-Doubles[1][0].get_vertices()[0] + centralPent.get_vertices()[3])
        Doubles[1].apply_matrix(rotMat("yz", -vertang.get_value()))
        Doubles[1].rotate(2*PI/5, about_point=[0,1.2135,0])

        Doubles[2].apply_matrix(rotMat("xy", -PI / 5))
        Doubles[2].shift(-Doubles[2][0].get_vertices()[0] + centralPent.get_vertices()[3])
        Doubles[2].apply_matrix(rotMat("yz", -vertang.get_value()))
        Doubles[2].rotate(4 * PI / 5, about_point=[0, 1.2135, 0])

        Doubles[3].apply_matrix(rotMat("xy", -PI / 5))
        Doubles[3].shift(-Doubles[3][0].get_vertices()[0] + centralPent.get_vertices()[3])
        Doubles[3].apply_matrix(rotMat("yz", -vertang.get_value()))
        Doubles[3].rotate(6 * PI / 5, about_point=[0, 1.2135, 0])

        Doubles[4].apply_matrix(rotMat("xy", -PI / 5))
        Doubles[4].shift(-Doubles[4][0].get_vertices()[0] + centralPent.get_vertices()[3])
        Doubles[4].apply_matrix(rotMat("yz", -vertang.get_value()))
        Doubles[4].rotate(8 * PI / 5, about_point=[0, 1.2135, 0])

        FullDodec=VGroup(centralPent,Doubles)
        self.camera.frame.set_height(FullDodec.get_height()*1.15).move_to(FullDodec)

        def DodecUp(mob):
            tcentralPent = pentagon().set_fill(colors[0], opacity=oplevel)

            tLevel3 = pentagon().set_fill(colors[0], opacity=oplevel)
            tLevel3.apply_matrix(rotMat("yz", vertang.get_value()))
            tLevel3.apply_matrix(rotMat("xy", PI))
            tLevel3.rotate(6 * PI / 5, about_point=[0, 1.2135, 0])
            tLevel1 = VGroup(*[pentagon().set_fill(colors[i % 6], opacity=oplevel) for i in range(5)])
            tLevel2 = VGroup(*[pentagon().set_fill(colors[(i + 1) % 6], opacity=oplevel) for i in range(5)])

            for x in tLevel2[:3]:
                x.apply_matrix(rotMat("yz", vertang.get_value()))
                x.apply_matrix(rotMat("xy", PI))
            VGroup(tLevel2[3], tLevel3).apply_matrix(rotMat("yz", vertang.get_value()))
            VGroup(tLevel2[3], tLevel3).apply_matrix(rotMat("xy", PI))
            tLevel2[4].apply_matrix(rotMat("yz", vertang.get_value()))
            tLevel2[4].apply_matrix(rotMat("xy", PI))

            tDoubles = VGroup(*[VGroup(tLevel1[i], tLevel2[i]) for i in range(3)])
            tDoubles.add(VGroup(tLevel1[3], tLevel2[3], tLevel3))
            tDoubles.add(VGroup(tLevel1[4], tLevel2[4]))

            tDoubles[0].apply_matrix(rotMat("xy", -PI / 5))
            tDoubles[0].shift(-tDoubles[0][0].get_vertices()[0] + tcentralPent.get_vertices()[3])
            tDoubles[0].apply_matrix(rotMat("yz", -vertang.get_value()))

            tDoubles[1].apply_matrix(rotMat("xy", -PI / 5))
            tDoubles[1].shift(-tDoubles[1][0].get_vertices()[0] + tcentralPent.get_vertices()[3])
            tDoubles[1].apply_matrix(rotMat("yz", -vertang.get_value()))
            tDoubles[1].rotate(2 * PI / 5, about_point=[0, 1.2135, 0])

            tDoubles[2].apply_matrix(rotMat("xy", -PI / 5))
            tDoubles[2].shift(-tDoubles[2][0].get_vertices()[0] + tcentralPent.get_vertices()[3])
            tDoubles[2].apply_matrix(rotMat("yz", -vertang.get_value()))
            tDoubles[2].rotate(4 * PI / 5, about_point=[0, 1.2135, 0])

            tDoubles[3].apply_matrix(rotMat("xy", -PI / 5))
            tDoubles[3].shift(-tDoubles[3][0].get_vertices()[0] + tcentralPent.get_vertices()[3])
            tDoubles[3].apply_matrix(rotMat("yz", -vertang.get_value()))
            tDoubles[3].rotate(6 * PI / 5, about_point=[0, 1.2135, 0])

            tDoubles[4].apply_matrix(rotMat("xy", -PI / 5))
            tDoubles[4].shift(-tDoubles[4][0].get_vertices()[0] + tcentralPent.get_vertices()[3])
            tDoubles[4].apply_matrix(rotMat("yz", -vertang.get_value()))
            tDoubles[4].rotate(8 * PI / 5, about_point=[0, 1.2135, 0])
            mob.become(VGroup(tcentralPent,tDoubles))

        self.play(FadeIn(FullDodec))
        FullDodec.add_updater(DodecUp)

        self.wait()
        self.play(frame.animate.set_euler_angles(phi=75 * DEGREES), run_time=3)
        self.wait()

        self.play(vertang.animate.set_value((PI-2.03)), run_time=4)
        self.wait()
        self.play(frame.animate.set_euler_angles(theta=360 * DEGREES), run_time=3)
        self.play(frame.animate.set_euler_angles(phi=0 * DEGREES), run_time=3)
        self.play(vertang.animate.set_value(0), run_time=4)
        self.play(vertang.animate.set_value((PI-2.03)), run_time=4)
        self.play(vertang.animate.set_value(0), run_time=4)
        self.wait(3)
        self.wait(3)

class FoldDodecDoubleStack(ThreeDScene):
    def construct(self):
        deepred = "#882255"
        colors = [deepred, deepred, deepred, deepred, deepred, deepred]
        oplevel=.6

        frame = self.camera.frame
        frame.set_euler_angles(
            theta=0 * DEGREES,
            phi=0 * DEGREES,
        )

        vertang=ValueTracker(0)

        PentStack1=VGroup(*[pentagon().set_fill(colors[i%6], opacity=oplevel) for i in range(5)])
        PentStack1[1].apply_matrix(rotMat("xy",PI))
        PentStack1[1].apply_matrix(rotMat("yz",vertang.get_value()))
        PentStack1[1].apply_matrix(rotMat("xy",8*PI/5))
        PentStack1[1].shift(PentStack1[1].get_vertices()[2]+PentStack1[0].get_vertices()[1])
        PentStack1[2].apply_matrix(rotMat("xy", PI))
        PentStack1[2].apply_matrix(rotMat("yz", vertang.get_value()))
        PentStack1[2].apply_matrix(rotMat("xy", 2*PI/5))
        PentStack1[2].shift(PentStack1[2].get_vertices()[2]+PentStack1[0].get_vertices()[3])
        PentStack1[3].apply_matrix(rotMat("xy", PI))
        PentStack1[3].apply_matrix(rotMat("yz", vertang.get_value()))
        PentStack1[3].apply_matrix(rotMat("xy", 4 * PI / 5))
        PentStack1[3].shift(PentStack1[3].get_vertices()[2] + PentStack1[0].get_vertices()[4])
        PentStack1[4].apply_matrix(rotMat("xy", PI))
        PentStack1[4].apply_matrix(rotMat("yz", vertang.get_value()))
        PentStack1[4].apply_matrix(rotMat("xy", 6 * PI / 5))
        PentStack1[4].shift(PentStack1[4].get_vertices()[2] + PentStack1[0].get_vertices()[0])
        centralPent=pentagon().set_fill(colors[0], opacity=oplevel)
        PentStack1.apply_matrix(rotMat("yz", -vertang.get_value()))
        PentStack1.apply_matrix(rotMat("xy", 3* PI / 5))
        PentStack1.shift(-PentStack1[0].get_vertices()[3] + centralPent.get_vertices()[1])

        flower1=VGroup(PentStack1,centralPent)
        flower1.shift(-.5*centralPent.get_vertices()[0] -.5*centralPent.get_vertices()[4])
        flower1.apply_matrix(rotMat("zy", 2*PI / 10))
        flower1.apply_matrix(rotMat("yz", vertang.get_value()))



        centralPent2=pentagon().set_fill(colors[0], opacity=oplevel)
        flower2 = VGroup(PentStack1, centralPent, centralPent2)
        flower2.shift(-.5 * centralPent2.get_vertices()[0] - .5 * centralPent2.get_vertices()[4])
        flower2.apply_matrix(rotMat("zy", 2 * PI / 10))
        flower2.apply_matrix(rotMat("yz", vertang.get_value()))


        centralPent3=pentagon().set_fill(colors[0], opacity=oplevel)
        flower3 = VGroup(PentStack1, centralPent, centralPent2, centralPent3)
        flower3.shift(-.5 * centralPent3.get_vertices()[0] - .5 * centralPent3.get_vertices()[4])
        flower3.apply_matrix(rotMat("zy", 2 * PI / 10))

        PentStack2 = VGroup(*[pentagon().set_fill(colors[i % 6], opacity=oplevel) for i in range(4)])
        PentStack2[0].apply_matrix(rotMat("yz", -vertang.get_value()))
        PentStack2[0].apply_matrix(rotMat("xy", 0 * PI / 5))
        PentStack2[1].apply_matrix(rotMat("yz", -vertang.get_value()))
        PentStack2[1].apply_matrix(rotMat("xy", 2 * PI / 5))
        PentStack2[1].shift(-PentStack2[1].get_vertices()[2] + centralPent3.get_vertices()[1])
        PentStack2[2].apply_matrix(rotMat("yz", -vertang.get_value()))
        PentStack2[2].apply_matrix(rotMat("xy", 4 * PI / 5))
        PentStack2[2].shift(-PentStack2[2].get_vertices()[2] + centralPent3.get_vertices()[2])
        PentStack2[3].apply_matrix(rotMat("yz", -vertang.get_value()))
        PentStack2[3].apply_matrix(rotMat("xy", 8 * PI / 5))
        PentStack2[3].shift(-PentStack2[3].get_vertices()[2] + centralPent3.get_vertices()[4])


        FullDodec=VGroup(PentStack1,centralPent,centralPent2, centralPent3, PentStack2)

        def DodecUpdate(mob):
            tempstack1 = VGroup(*[pentagon().set_fill(colors[i % 6], opacity=oplevel) for i in range(5)])
            tempstack1[1].apply_matrix(rotMat("xy", PI))
            tempstack1[1].apply_matrix(rotMat("yz", vertang.get_value()))
            tempstack1[1].apply_matrix(rotMat("xy", 8 * PI / 5))
            tempstack1[1].shift(tempstack1[1].get_vertices()[2] + tempstack1[0].get_vertices()[1])
            tempstack1[2].apply_matrix(rotMat("xy", PI))
            tempstack1[2].apply_matrix(rotMat("yz", vertang.get_value()))
            tempstack1[2].apply_matrix(rotMat("xy", 2 * PI / 5))
            tempstack1[2].shift(tempstack1[2].get_vertices()[2] + tempstack1[0].get_vertices()[3])
            tempstack1[3].apply_matrix(rotMat("xy", PI))
            tempstack1[3].apply_matrix(rotMat("yz", vertang.get_value()))
            tempstack1[3].apply_matrix(rotMat("xy", 4 * PI / 5))
            tempstack1[3].shift(tempstack1[3].get_vertices()[2] + tempstack1[0].get_vertices()[4])
            tempstack1[4].apply_matrix(rotMat("xy", PI))
            tempstack1[4].apply_matrix(rotMat("yz", vertang.get_value()))
            tempstack1[4].apply_matrix(rotMat("xy", 6 * PI / 5))
            tempstack1[4].shift(tempstack1[4].get_vertices()[2] + tempstack1[0].get_vertices()[0])
            tcentralPent = pentagon().set_fill(colors[0], opacity=oplevel)
            tempstack1.apply_matrix(rotMat("yz", -vertang.get_value()))
            tempstack1.apply_matrix(rotMat("xy", 3 * PI / 5))
            tempstack1.shift(-tempstack1[0].get_vertices()[3] + tcentralPent.get_vertices()[1])

            tflower1 = VGroup(tempstack1, tcentralPent)
            tflower1.shift(-.5 * tcentralPent.get_vertices()[0] - .5 * tcentralPent.get_vertices()[4])
            tflower1.apply_matrix(rotMat("zy", 2 * PI / 10))
            tflower1.apply_matrix(rotMat("yz", vertang.get_value()))

            tcentralPent2 = pentagon().set_fill(colors[0], opacity=oplevel)
            tflower2 = VGroup(tempstack1, tcentralPent, tcentralPent2)
            tflower2.shift(-.5 * tcentralPent2.get_vertices()[0] - .5 * tcentralPent2.get_vertices()[4])
            tflower2.apply_matrix(rotMat("zy", 2 * PI / 10))
            tflower2.apply_matrix(rotMat("yz", vertang.get_value()))

            tcentralPent3 = pentagon().set_fill(colors[0], opacity=oplevel)
            tflower3 = VGroup(tempstack1, tcentralPent, tcentralPent2, tcentralPent3)
            tflower3.shift(-.5 * tcentralPent3.get_vertices()[0] - .5 * tcentralPent3.get_vertices()[4])
            tflower3.apply_matrix(rotMat("zy", 2 * PI / 10))

            tempstack2 = VGroup(*[pentagon().set_fill(colors[i % 6], opacity=oplevel) for i in range(4)])
            tempstack2[0].apply_matrix(rotMat("yz", -vertang.get_value()))
            tempstack2[0].apply_matrix(rotMat("xy", 0 * PI / 5))
            tempstack2[1].apply_matrix(rotMat("yz", -vertang.get_value()))
            tempstack2[1].apply_matrix(rotMat("xy", 2 * PI / 5))
            tempstack2[1].shift(-tempstack2[1].get_vertices()[2] + tcentralPent3.get_vertices()[1])
            tempstack2[2].apply_matrix(rotMat("yz", -vertang.get_value()))
            tempstack2[2].apply_matrix(rotMat("xy", 4 * PI / 5))
            tempstack2[2].shift(-tempstack2[2].get_vertices()[2] + tcentralPent3.get_vertices()[2])
            tempstack2[3].apply_matrix(rotMat("yz", -vertang.get_value()))
            tempstack2[3].apply_matrix(rotMat("xy", 8 * PI / 5))
            tempstack2[3].shift(-tempstack2[3].get_vertices()[2] + tcentralPent3.get_vertices()[4])
            TFullDodec=VGroup(tempstack1,tcentralPent,tcentralPent2, tcentralPent3, tempstack2)

            mob.become(TFullDodec)

        self.camera.frame.move_to(centralPent3.get_center()).set_width(30)

        self.play(FadeIn(FullDodec))
        self.wait()
        self.play(frame.animate.set_euler_angles(phi=75 * DEGREES), run_time=3)
        self.wait()
        FullDodec.add_updater(DodecUpdate)

        self.play(vertang.animate.set_value(-(PI-2.03)), run_time=4)
        self.wait()
        self.play(frame.animate.set_euler_angles(theta=360 * DEGREES), run_time=3)
        self.play(frame.animate.set_euler_angles(phi=0 * DEGREES), run_time=3)
        self.play(vertang.animate.set_value(0), run_time=4)
        self.play(vertang.animate.set_value(-(PI-2.03)), run_time=4)
        self.play(vertang.animate.set_value(0), run_time=4)

        self.wait(3)


