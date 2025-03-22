# This code was originally written by Tom Edgar. If you use it, please give attribution.
from manimlib import *

class SineCurve(Scene):
    def construct(self):
        Circ = ParametricCurve(
            lambda u: (math.cos(u), math.sin(u), 0), t_min=0, t_max=2*PI
        ) # created the circle

        sineAxes = Axes(
            x_range = (0,7,1),
            y_range = (-2,2,1),
            height=4,
            width=7,
            axis_config = {
                "include_tip": False
            },
            y_axis_config={
                "include_tip": False
            }
        ) #created the axes

        sineAxes.next_to(Circ,RIGHT, buff=1) #places axes next to circle
        frame = self.camera.frame #renames camera.frame
        frame.move_to(VGroup(Circ,sineAxes)) #centers camera.frame on the circle and axes

        theta = ValueTracker(0.0001) #creates input parameter

        sineCurve = ParametricCurve(
            lambda u: sineAxes.c2p(u, math.sin(u)), t_min=0, t_max=theta.get_value()
        ) #draws sine curve on the axes system


        radius = Line((0,0,0), (1,0,0)) #creates a radius of length 1 centered at circle
        self.play(ShowCreation(radius)) #draws the radius

        def tempRadiusUp(mob):
            mob.become(Line((0,0,0), Circ.get_end()))
        radius.add_updater(tempRadiusUp) #makes the radius keep drawing with base at 0,0 and end attached to the circle
        self.play(ShowCreation(Circ)) #draws the circle
        radius.remove_updater(tempRadiusUp) # removes the redraw updater on radius
        self.play(ShowCreation(sineAxes)) #draws the axes

        label1=Tex(r"\text{angle}").scale(.75).next_to(sineAxes,RIGHT) #creates x-label for the axes
        label2=Tex(r"y-\text{coordinate}").scale(.75).next_to(sineAxes,UP).shift(3*LEFT) #creates y-label for the axes
        self.play(Write(label1)) #writes the x-label
        self.play(Write(label2)) #writes the x-label
        self.wait() #pauses

        self.add(sineCurve) #adds sine curve to the frame, but we can't see it because the theta value is 0.

        def sineCurveUp(mob):
            mob.become(ParametricCurve(
            lambda u: sineAxes.c2p(u, math.sin(u)), t_min=0, t_max=theta.get_value())
            )
        sineCurve.add_updater(sineCurveUp) #makes the sine curve keep drawing but with max parameter depending on theta

        def RadiusUp(mob):
            mob.become(Line((0,0,0), (math.cos(theta.get_value()), math.sin(theta.get_value()),0)))
        radius.add_updater(RadiusUp) #makes the radius keep drawing but with max parameter depending on theta

        connector = DashedLine(radius.get_end(),sineCurve.get_end()).set_stroke(YELLOW, width=3) #draws a line connecting the radius end to sine curve end

        self.play(ShowCreation(connector))

        def connectorUp(mob):
            mob.become(DashedLine(radius.get_end(),sineCurve.get_end()).set_stroke(YELLOW, width=3))
        connector.add_updater(connectorUp) #keeps drawing the line connecting the radius end to sine curve end

        self.play(theta.animate.set_value(2*PI), run_time=6) #increments theta to 2PI, so it will rotate the radius and draw the sine curve

        self.wait(2) #waits 2 seconds

        sineAxes2 = Axes(
            x_range=(0, 32, 1),
            y_range=(-2, 2, 1),
            height=4,
            width=32,
            axis_config={
                "include_tip": False
            },
            y_axis_config={
                "include_tip": False
            }
        )

        sineAxes2.next_to(Circ, RIGHT, buff=1) #creates a much larger axes.
        self.play(FadeIn(sineAxes2), FadeOut(label1), FadeOut(label2)) #fades in the new axes and fades out the labels
        self.remove(sineAxes) #takes away the old axes from visibility

        self.play(
            LaggedStart(frame.animate.set_width(sineAxes2.get_width()*1.2).shift(12*RIGHT), theta.animate.set_value(10*PI), lag_ratio=0.2), run_time=12
        ) #slowly zooms out the camera, and then in 1/5 of the way through that, makes the sine curve draw out to 10Pi (while also rotating the radius of the circle)

        connector.remove_updater(connectorUp) #removes the connector updater
        self.play(FadeOut(connector)) #fades out the connecting line

        radius.remove_updater(RadiusUp) #removes the radius updater
        sineCurve.remove_updater(sineCurveUp) #removes the sine curve updater

        theta.set_value(0) #resets the theta value to 0

        sineLine = Line(radius.get_end(), radius.get_end() - [0, math.sin(theta.get_value()),0]).set_stroke(YELLOW, width=6) #draws a vertical line from the end of the radius to the x-axis of length sin theta
        sineLine2 = Line(sineAxes.c2p(theta.get_value(),0), sineAxes.c2p(theta.get_value(),math.sin(theta.get_value()))).set_stroke(YELLOW, width=6)  #draws a vertical line from the sine x-axis to the sine curve of length sin theta

        self.add(sineLine,sineLine2) #puts these on the canvas, but they are invisible

        def sineLineUp(mob):
            mob.become(Line(radius.get_end(), radius.get_end() - [0, math.sin(theta.get_value()),0]).set_stroke(YELLOW, width=6))
        def sineLine2Up(mob):
            mob.become(Line(sineAxes.c2p(theta.get_value(),0), sineAxes.c2p(theta.get_value(),math.sin(theta.get_value()))).set_stroke(YELLOW, width=6))

        radius.add_updater(RadiusUp) #readds the updater to the radius so it rotates with theta changing.
        sineLine.add_updater(sineLineUp) #adds the updater to the sine line to keep drawing it as theta changes
        sineLine2.add_updater(sineLine2Up) #adds the updater to the sine line2 to keep drawing it as theta changes

        self.wait()
        self.play(theta.animate.set_value(10*PI), run_time=15) #animates theta goig to 10pi; this allows the sine lines to be drawn simultanously in the circle and on the axes to show the corresponding heights.
        self.wait(3) #wait three seconds before ending







        






