from manimlib import *

def threeRects(thecolor, thewidth):
    D=Polygon((0,0,0), (3,0,0),(3,math.sqrt(3),0),(0,math.sqrt(3),0))
    R1=Polygon((0,0,0), (1,0,0),(1,math.sqrt(3),0),(0,math.sqrt(3),0))
    R1.set_fill(color=thecolor, opacity=.75)
    R2=Polygon((1,0,0), (2,0,0),(2,math.sqrt(3),0),(1,math.sqrt(3),0))
    R3=Polygon((2,0,0), (3,0,0),(3,math.sqrt(3),0),(2,math.sqrt(3),0))
    for x in [D,R1,R2,R3]:
        x.set_stroke(width=thewidth)
    return VGroup(D,R3,R2,R1)

class geosumThree(Scene):
    def construct(self):
        color1="#00FFFF"
        color2="#FF007F"
        frects=[]
        urects=[]
        shells=[]
        theFormula=Tex(r"\frac{1}{3}","+",r"\left(\frac{1}{3}\right)^2","+",r"\left(\frac{1}{3}\right)^3","+",r"\left(\frac{1}{3}\right)^4","+",r"\left(\frac{1}{3}\right)^5","+",r"\cdots","=",r"\frac{1}{2}").scale(.85)
        theFormula.to_edge(UP, buff=.5)
        for i in range(15):
            tempShell=threeRects(color1, 4/(i+1)).scale(2/(math.sqrt(3)**i))
            tempShell.rotate(-PI*i/2)
            tempShell.move_to((0,0,0))
            shells.append(tempShell[0])
            shells.append(tempShell[2])
            frects.append(tempShell[-1])
            urects.append(tempShell[1])
            if i==0:
                self.play(ShowCreation(tempShell[0]), run_time=2)
                self.wait()
                self.play(FadeIn(tempShell[1]),FadeIn(tempShell[2]), run_time=2)
                self.wait()
                self.play(FadeIn(tempShell[-1]), run_time=1)
                self.play(Write(theFormula[i]))
                self.wait(.5)
            elif i>0 and i<=5:
                self.play(FadeIn(tempShell[0]),FadeIn(tempShell[1]),FadeIn(tempShell[2]), run_time=1)
                self.play(FadeIn(tempShell[-1]), run_time=1)
                self.play(Write(theFormula[2*i-1]), run_time=.5)
                self.play(Write(theFormula[2*i]))
                self.wait(.25)
            else:
                self.play(FadeIn(tempShell[0]),FadeIn(tempShell[1]),FadeIn(tempShell[2]), run_time=.25)
                self.play(FadeIn(tempShell[-1]), run_time=.25)
        self.camera.frame.save_state()
        self.play(self.camera.frame.set_height, .33,
                  # Move the camera to the object
                  self.camera.frame.move_to, (0,0,0), run_time=5)
        self.wait(.75)
        self.play(Restore(self.camera.frame), run_time=3)
        self.wait(2)
        self.play(Write(theFormula[-2]))
        anis=[]
        temprects=[]
        for x in urects:
            temp=x.copy()
            temp.set_fill(color=color2,opacity=.75)
            temprects.append(temp)
            anis.append(FadeIn(temp))
        self.play(*anis, run_time=1.5)
        self.wait(1)
        self.play(Rotate(VGroup(*temprects), -PI, about_point=[0,0,0]), run_time=3)
        self.wait(.5)
        self.play(FadeOut(VGroup(*temprects)), run_time=1)
        self.play(Write(theFormula[-1]))
        self.wait(2)
        finalForm=Tex(r"\sum_{i=1}^\infty",r"\left(\frac{1}{3}\right)^i","=",r"\frac{1}{2}").scale(.85)
        finalForm.to_edge(DOWN, buff=.75)
        self.play(Write(finalForm[0]))
        self.play(TransformMatchingShapes(VGroup(*[theFormula[2*i].copy() for i in range(5)]),finalForm[1]), run_time=1.5)
        self.play(Write(finalForm[2]))
        self.play(TransformMatchingShapes(theFormula[-1].copy(),finalForm[3]), run_time=2)
        self.wait(.5)
        finalrect=SurroundingRectangle(finalForm, color=WHITE)
        self.play(ShowCreation(finalrect))
        self.wait(5)