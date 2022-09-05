from manimlib import *

class inradius(Scene):
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
        self.wait()

        self.play(TheTitle[0].animate.become(MVPTitle[0]),TheTitle[1].animate.become(MVPTitle[1]),TheTitle[2].animate.become(MVPTitle[2]))

        episode=Text("Inradius of a Right Triangle", color="#0072B2", font= introfont)

        episode.move_to((0,-.5,0))

        self.play(Write(episode))
        self.wait(2)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects[1:]]
        )
        self.wait(1)


        color1="#009E73"
        colorb="#0072B2"
        colorr="#CC79A7"
        colory="#F0E442"
        play_kw={"run_time":3}

        a=3
        b=4
        c=5
        r=(a+b-c)/2
        Points=[(0,0,0),(b,0,0),(0,a,0),(r,0,0),(0,r,0), (r,r,0), (b*(a-r)/c,a-a*(a-r)/c,0)]
        RightTri=Polygon(Points[0], Points[1], Points[2])
        ALabel=Tex("a", isolate=["a"])
        BLabel=Tex("b", isolate=["b"])
        CLabel=Tex("c", isolate=["c"])
        rLabel=Tex("r", isolate=["r"])
        
        ALabel.move_to((-.3,a/2,0))

        BLabel.move_to((b/2,-.3,0))

        CLabel.move_to((b/2+.1,a/2+.3,0))
        
        ATri=  Polygon(Points[2], Points[-2], Points[-3])
        ATri2=  Polygon(Points[2], Points[-2], Points[-1])
        BTri=  Polygon(Points[3], Points[1], Points[-2])  
        BTri2=  Polygon(Points[-2], Points[1], Points[-1])  
        rsquare=  Polygon(Points[0], Points[3], Points[5], Points[4])  

        ATri.set_fill(color=colorr, opacity=1)
        ATri2.set_fill(color=colorr, opacity=1)
        BTri.set_fill(color=colorb, opacity=1)
        BTri2.set_fill(color=colorb, opacity=1)
        rsquare.set_fill(color=GREY, opacity=1)

        ATri3=ATri.copy()
        ATri3.rotate(PI)
        ATri4=ATri3.copy()
        ATri4.rotate(PI)
        ATri34=VGroup(ATri3,ATri4)
        ATri34.rotate(PI/2)

        ATri5=ATri.copy()
        ATri5.rotate(PI)
        ATri6=ATri5.copy()
        ATri6.rotate(PI)
        ATri56=VGroup(ATri5,ATri6)
        ATri56.rotate(PI/2)
        ATri56.flip(UP)

        BTri3=BTri.copy()
        BTri3.rotate(PI)
        BTri4=BTri3.copy()
        BTri4.rotate(PI)
        BTri34=VGroup(BTri3,BTri4)

        BTri5=BTri.copy()
        BTri5.rotate(PI)
        BTri6=BTri5.copy()
        BTri6.rotate(PI)
        BTri56=VGroup(BTri5,BTri6)
        BTri56.flip(UP)
        
        Rect1=rsquare.copy()
        Rect2=rsquare.copy()
        Rect2.rotate(PI)
        ThinRect=VGroup(ATri34,Rect1 , BTri34,Rect2, ATri56, BTri56)

        ThinRect.arrange(.01*RIGHT)
        ThinRect.move_to((0,0,0))

        ThinRect.to_edge(DOWN, buff=.5)
        
        ALabel2=Tex("a",isolate=["a"])
        BLabel2=Tex("b",isolate=["b"])
        CLabel2=Tex("c", isolate=["c"])
        rLabel2=Tex("r")
        abrace=Brace(ThinRect[:2],UP)      
        bbrace=Brace(ThinRect[2:4],UP)      
        cbrace=Brace(ThinRect[4:],UP)      
        rbrace=Brace(ThinRect[0],LEFT)      
        ALabel2.next_to(abrace,UP)
        BLabel2.next_to(bbrace,UP)
        CLabel2.next_to(cbrace,UP)
        rLabel2.next_to(rbrace,LEFT)
        

        inRad=Line(Points[5], Points[4])
        inCirc=ParametricCurve(
            lambda u: (r+ r*math.cos(u),r+ r*math.sin(u),0), t_min=PI, t_max=3*PI) 
        def update_rad(mob, alpha):
            mob.become(
                Line([r-2,r-1,0], [r-2 + r*math.cos(interpolate(PI, 3*PI, alpha)), r-1+ r*math.sin(interpolate(PI, 3*PI, alpha)),0])
            )

        TriPic=VGroup(RightTri, ATri, ATri2, BTri, BTri2, rsquare, inRad, inCirc, ALabel, BLabel,CLabel)
        TriPic.shift(2*LEFT+DOWN)

        self.play(GrowFromCenter(RightTri), **play_kw)
        rLabel.next_to(inRad,DOWN)
        for x in [-3,-2,-1]:
            self.play(Write(TriPic[x]))
        self.play(ShowCreation(inRad), **play_kw)
        self.wait()

        self.play(
            UpdateFromAlphaFunc(inRad, update_rad), ShowCreation(inCirc),**play_kw
        )
        self.wait(3)
        self.play(Write(rLabel))
        self.wait(3)
        self.play(FadeIn(ATri), FadeIn(ATri2), run_time=2)
        self.play(FadeIn(BTri), FadeIn(BTri2), run_time=2)
        self.play(GrowFromCenter(rsquare), run_time=2)
        self.bring_to_front(rLabel)
        #self.remove(inCirc)
        #self.remove(inRad)
        TriPic.remove(inRad,inCirc, ALabel, BLabel,CLabel)
        self.wait(3)

        TPic2=TriPic.copy()
        self.play(Rotate(TPic2,PI), run_time=3)
        self.wait(3)
        MoveGroup=[VGroup(TriPic[1], TriPic[2]), TriPic[5], VGroup(TriPic[3], TriPic[4]), TPic2[5], VGroup(TPic2[1], TPic2[2]), VGroup(TPic2[3], TPic2[4])]
        for i in range(len(MoveGroup)):
            self.play(ReplacementTransform(MoveGroup[i].copy(), ThinRect[i]), run_time=3) 
            self.wait()
        self.wait(2)
        for x in [[abrace, ALabel2, ALabel],[bbrace, BLabel2,BLabel],[cbrace, CLabel2,CLabel], [rbrace, rLabel2,rLabel]]:
            self.play(GrowFromCenter(x[0]), ReplacementTransform(x[2].copy(),x[1]), run_time=3)
            self.wait(.5)
        TheFormula=[Tex("a"),Tex("\\cdot"), Tex("b"),Tex("="), Tex("r", isolate=["r"]), Tex("\\cdot"), Tex("(a+b+c)", isolate=["a","b","c"])]        
        formula=VGroup(*TheFormula)
        formula.arrange(RIGHT)
        formula.to_edge(UP, buff=.5)
        self.wait()
        self.play(TransformMatchingTex(ALabel.copy(), formula[0]), run_time=2)
        self.play(Write(formula[1]))       
        self.play(TransformMatchingTex(BLabel.copy(), formula[2]), run_time=2)
        
        self.play(Write(formula[3]))       
        self.play(TransformMatchingTex(rLabel2.copy(), formula[4]), run_time=2)        
        self.play(Write(formula[5]))       
        self.play(TransformMatchingTex(ALabel2.copy(), formula[6]),TransformMatchingTex(BLabel2.copy(), formula[6]), TransformMatchingTex(CLabel2.copy(), formula[6]), key_map={"a":"a", "b":"b", "c":"c"}, run_time=2)        
        self.wait(2)
        self.play(FadeOut(ThinRect), FadeOut(abrace), FadeOut(bbrace), FadeOut(cbrace), FadeOut(rbrace), FadeOut(ALabel2),FadeOut(BLabel2),FadeOut(CLabel2),FadeOut(rLabel2),FadeOut(TPic2))
        self.wait()
        self.play(FadeOut(ATri),FadeOut(ATri2),FadeOut(BTri),FadeOut(BTri2), FadeOut(rsquare))

        FinalFormula=[Tex("r", isolate=["r"]),Tex("="), Tex("\\frac{a\\cdot b}{a+b+c}")]
        final=VGroup(*FinalFormula)   
        final.arrange(RIGHT)
        final.to_edge(DOWN, buff=1)
        self.play(TransformMatchingTex(formula[4].copy(), final[0]), key_map={"r":"r"}, run_time=3)              
        self.play(Write(final[1]))       
        self.play(ReplacementTransform(formula[:3].copy(), final[2]),ReplacementTransform(formula[-1].copy(), final[2]), run_time=3)             
        self.wait(3)
        box1=SurroundingRectangle(final,color=WHITE)
        self.play(ShowCreation(box1))
        self.wait(2)
        self.play(VGroup(box1,final).animate.to_edge(LEFT, buff=1), run_time=3)
        self.wait(2)
        
        self.play(FadeIn(ATri), FadeIn(ATri2), FadeIn(BTri), FadeIn(BTri2), run_time=2)
        
        self.wait(2)
        
        newalabel=Tex("a-r", isolate=["a","r"])
        newblabel=Tex("b-r",isolate=["b","r"])
        Abrace=Brace(ATri,LEFT)
        Bbrace=Brace(BTri,DOWN)
        newalabel.next_to(Abrace,LEFT)
        newblabel.next_to(Bbrace,DOWN)
        
        ALabelLast=ALabel.copy()
        BLabelLast=BLabel.copy()

        
        self.play(GrowFromCenter(Abrace))
        self.play(TransformMatchingTex(ALabel, newalabel),TransformMatchingTex(rLabel.copy(), newalabel),key_map={"a":"a","r":"r"}, run_time=2)
        self.wait() 

        self.play(GrowFromCenter(Bbrace))
        self.play(TransformMatchingTex(BLabel, newblabel),TransformMatchingTex(rLabel.copy(), newblabel),key_map={"a":"a","r":"r"}, run_time=2)
        
        self.wait(2)
        
        FinalFormula2=[Tex("c", isolate=["c"]),Tex("="), Tex("a-r", isolate=["a","r"]), Tex("+"), Tex("b-r",isolate=["b","r"])]
        final2=VGroup(*FinalFormula2)   
        final2.arrange(RIGHT)
        final2.to_edge(DOWN, buff=1)

        self.play(TransformMatchingTex(CLabel.copy(), final2[0]), key_map={"c":"c"}, run_time=3)              
        self.play(Write(final2[1]))       
        self.play(TransformMatchingTex(newalabel.copy(), final2[2]), key_map={"a":"a","r":"r"}, run_time=3)              
        self.play(Write(final2[3]))       
        self.play(TransformMatchingTex(newblabel.copy(), final2[4]), key_map={"b":"b","r":"r"}, run_time=3)   
        
        self.wait(3)

        FinalFormula3=[Tex("r", isolate=["r"]),Tex("="), Tex("(a+b-c)/2", isolate=["a","b","c"])]
        final3=VGroup(*FinalFormula3)   
        final3.arrange(RIGHT)
        final3.to_edge(DOWN, buff=1)
        final3.to_edge(RIGHT, buff=1)

        self.play(TransformMatchingTex(rLabel.copy(), final3[0]), key_map={"r":"r"}, run_time=3)              
        self.play(Write(final3[1]))       
        self.play(TransformMatchingTex(final2[0], final3[2]),TransformMatchingTex(final2[2], final3[2]),TransformMatchingTex(final2[4], final3[2]), key_map={"a":"a","b":"b", "c":"c"}, run_time=3)              
        self.play(FadeOut(final2[1]), FadeOut(final2[3]))
        self.wait(3)
        box2=SurroundingRectangle(final3,color=WHITE)
        self.play(ShowCreation(box2))
        self.wait(2)
        self.play(FadeOut(ATri),FadeOut(ATri2),FadeOut(newalabel),FadeOut(BTri),FadeOut(BTri2),FadeOut(newblabel), FadeOut(Abrace),FadeOut(Bbrace))

        self.play(Write(ALabelLast), Write(BLabelLast))

        self.wait(5)
       
        
