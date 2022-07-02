from manimlib import *

def kxhypocycloid(r,k,t):
    return r*(k-1)*math.cos(t)+r*math.cos((k-1)*t)

def kyhypocycloid(r,k,t):
    return r*(k-1)*math.sin(t)-r*math.sin((k-1)*t)

class hypocycloidPi(Scene):
    def construct(self):
        colors=["#39ff14", "#7DF9FF", "#FF10F0", "#1F51FF","#FFF01F"]
        curves1=[]
        rads=[]
        RR=3.5
        i=0
        fullanis=[]
        align=0

        dotandcurve=colors[i%5]
        k=PI
        rr=RR/k
        rads.append([RR,rr])
        outerCircle = ParametricCurve(
                lambda u: (RR*math.cos(u),RR*math.sin(u), 0), t_min=0, t_max=2 * PI, t_range=[0, 1, .01])

        innerCircle = ParametricCurve(
                lambda u: (rr*math.cos(u)+(RR-rr),rr*math.sin(u), 0), t_min=0, t_max=2 * PI, t_range=[0, 1, .01])
        innerCircle.set_stroke(width=1)
        CC=ParametricCurve(
                lambda u: (kxhypocycloid(rr,k,u), kyhypocycloid(rr,k,u),0), t_min=0, t_max=10*PI, t_range=[0, 1, .01])
        CC.set_stroke(color=dotandcurve, width=1)
        thedot1=Dot(color=dotandcurve)
        thedot1.move_to((RR,0,0))
        Diagram=VGroup(outerCircle,innerCircle,thedot1,CC)
        curves1.append(Diagram)
        i+=1
        sp=5
        anis1=[]
        for y in curves1:
            anis1.append(FadeIn(y[0]))
        self.play(*anis1,run_time=2)
        i=0
        self.wait()

        self.play(ShowCreation(curves1[0][1]))

        for y in curves1:
            now = self.time
            r=rr
            y[2].add_updater(lambda mob: mob.move_to((align + r * (k - 1) * math.cos(
                    sp*self.time - sp*now) + r * math.cos((k - 1) * (sp*self.time - sp*now)),
                                                                     r * (k - 1) * math.sin(
                                                                         sp*self.time - sp*now) - r * math.sin(
                                                                         (k - 1) * (sp*self.time - sp*now)),
                                                                     0)).set_fill(colors[3],opacity=1))
            y[1].add_updater(lambda mob: mob.become(ParametricCurve(
                    lambda u: (
                        y[0].get_center()[0] + rr * math.cos(u) + (RR - rr) * math.cos(sp*self.time-sp*now),
                        y[0].get_center()[1] + rr * math.sin(u) + (RR - rr) * math.sin(sp*self.time-sp*now), 0), t_min=0, t_max=2 * PI,
                    t_range=[0, 1, .01]).set_stroke(width=1)))

            y[3].add_updater(lambda mob: mob.become(ParametricCurve(
                lambda u: (kxhypocycloid(rr,k,u), kyhypocycloid(rr,k,u),0), t_min=0, t_max=sp*self.time-sp*now, t_range=[0, 1, .01]).set_stroke(color=colors[3],width=1)))
            i+=1
        self.add(curves1[0][1],curves1[0][2],curves1[0][3])
        self.wait(40*PI)
        curves1[0][1].suspend_updating()
        curves1[0][2].suspend_updating()
        curves1[0][3].suspend_updating()

        self.play(FadeOut(curves1[0][1]),FadeOut(curves1[0][2]))

        self.wait(5)

