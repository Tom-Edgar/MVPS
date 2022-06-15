from manimlib import *


def linesquares(n):
    sq=Polygon((0,0,0),(1,0,0),(1,1,0),(0,1,0))
    squareline=VGroup(*[sq.copy() for i in range(n)])
    squareline.arrange(.01*RIGHT)
    return squareline


class Intro(Scene):
    def construct(self):
        color1="#39ff14"

        color2="#0072B2"

        color3="#CC79A7"
        color4="#F0E442"

        color5 = "#7DF9FF"
        color6 = "#FF10F0"
        color7 = "#FFF01F"
        color8 = "#39ff14"
        BROWN = "#7B3F00"

        colors=[color4, color5, color6, color7]

        CompDef=VGroup(Text("Recall.", font_size=30, font="Optima", t2c={"Recall.": color3}),
                       TexText(
                           r"We have encountered a few techniques to \textit{find} formulas for various sequences.",
                           font_size=30,
                           font="Optima"),
               TexText(r"How can we be sure that they \textit{hold} for every single value of \(n\)?", font_size=30,
                       font="Optima"),
                       )

        CompDef[0].to_edge(LEFT, buff=.5)
        CompDef[0].to_edge(UP, buff=.5)
        CompDef[1].next_to(CompDef[0], RIGHT)
        CompDef[1].to_edge(UP, buff=.5)
        CompDef[2].next_to(CompDef[0], DOWN+RIGHT)
        self.play(Write(CompDef[:2]), run_time=3)


        self.wait()
        self.play(Write(CompDef[2]), run_time=3)


        Example=VGroup(Text("Example.", font_size=30, font="Optima", t2c={"Example.": color4}),
                       TexText(
                           r"Consider the sum-of-squares sequence \(S_n\) given by \(S_n=1^2+2^2+3^2+\cdots +n^2\).",
                           font_size=30,
                           font="Optima"),
               TexText(r"We encountered two ways to discover a closed formula for \(S_n\).", font_size=30,
                       font="Optima"),
                       )

        Example[0].to_edge(LEFT, buff=.5)
        Example[0].to_edge(UP, buff=1.5)
        Example[1].next_to(Example[0], RIGHT)
        Example[1].to_edge(UP, buff=1.5)
        Example[2].next_to(Example[0], DOWN+RIGHT)
        self.play(Write(Example[:2]), run_time=3)


        self.wait()
        self.play(Write(Example[2]), run_time=3)

        array1=[]
        for i in [0]:
            array1.append([])
            for j in [0]:
                indiv=Square(fill_color=color1,fill_opacity=.9)
                indiv.scale(1/5)
                array1[i].append(indiv.move_to((-6,3,0)))

        array2=[]
        for i in [0,1]:
            array2.append([])
            for j in [0,1]:
                if i!=0 or j!=0:
                    indiv=Square(fill_color=color2,fill_opacity=.9)
                    indiv.scale(1/5)
                else:
                    indiv=Square(fill_color=color1,fill_opacity=.9)
                    indiv.scale(1/5)
                array2[i].append(indiv.move_to((-6+2*i/5,2.2-2*j/5,0)))
        array3=[]
        for i in [0,1,2]:
            array3.append([])
            for j in [0,1,2]:
                if i==0 and j==0:
                    indiv=Square(fill_color=color1,fill_opacity=.9)
                    indiv.scale(1/5)
                elif j==1 and i<=j:
                    indiv=Square(fill_color=color2,fill_opacity=.9)
                    indiv.scale(1/5)
                elif i==1 and j<=i:
                    indiv=Square(fill_color=color2,fill_opacity=.9)
                    indiv.scale(1/5)
                else:
                    indiv=Square(fill_color=color3,fill_opacity=.9)
                    indiv.scale(1/5)
                array3[i].append(indiv.move_to((-6+2*i/5,1-2*j/5,0)))
        array4=[]
        for i in [0,1,2,3]:
            array4.append([])
            for j in [0,1,2,3]:
                if i==0 and j==0:
                    indiv=Square(fill_color=color1,fill_opacity=.9)
                    indiv.scale(1/5)
                elif j==1 and i<=j:
                    indiv=Square(fill_color=color2,fill_opacity=.9)
                    indiv.scale(1/5)
                elif i==1 and j<=i:
                    indiv=Square(fill_color=color2,fill_opacity=.9)
                    indiv.scale(1/5)
                elif i==2 and j<=i:
                    indiv=Square(fill_color=color3,fill_opacity=.9)
                    indiv.scale(1/5)
                elif j==2 and i<=j:
                    indiv=Square(fill_color=color3,fill_opacity=.9)
                    indiv.scale(1/5)
                else:
                    indiv=Square(fill_color=color4,fill_opacity=.9)
                    indiv.scale(1/5)
                array4[i].append(indiv.move_to((-6+2*i/5,-.6-2*j/5,0)))

        onebyone=VGroup(array1[0][0])
        onebyone.scale(.5)
        onebyone.to_edge(LEFT, buff=.75)
        onebyone.to_edge(UP, buff=3)

        self.play(FadeIn(onebyone))
        twobytwo=VGroup(array2[0][0],array2[0][1],array2[1][0],array2[1][1])
        twobytwo.scale(.5)
        twobytwo.next_to(onebyone,DOWN)
        twobytwo.to_edge(LEFT, buff=.75)
        self.play(FadeIn(twobytwo))
        threebythree=VGroup(array3[0][0],array3[0][1],array3[0][2],array3[1][0],array3[1][1],array3[1][2],array3[2][0],array3[2][1],array3[2][2])
        threebythree.scale(.5)
        threebythree.next_to(twobytwo,DOWN)
        threebythree.to_edge(LEFT, buff=.75)
        self.play(FadeIn(threebythree))
        fourbyfour=VGroup(array4[0][0],array4[0][1],array4[0][2],array4[0][3],array4[1][0],array4[1][1],array4[1][2],array4[1][3],array4[2][0],array4[2][1],array4[2][2],array4[2][3],array4[3][0],array4[3][1],array4[3][2],array4[3][3])
        fourbyfour.scale(.5)
        fourbyfour.next_to(threebythree,DOWN)
        fourbyfour.to_edge(LEFT, buff=.75)
        self.play(FadeIn(fourbyfour))
        self.wait(2)
        play_kw={"run_time":3}

        L1=VGroup(array4[0][3],array4[1][3],array4[2][3],array4[3][3],array4[3][2],array4[3][1],array4[3][0])

        Tower1=L1.copy()
        Tower1.arrange(.01*RIGHT)
        Tower1.next_to(array4[3][3],2*RIGHT)
        Tower1.shift(.5*RIGHT)
        self.play(ReplacementTransform(L1.copy(),Tower1), run_time=2)
        self.wait(.5)

        L21=VGroup(array4[0][2],array4[1][2],array4[2][2],array4[2][1],array4[2][0])
        L22=VGroup(array3[0][2],array3[1][2],array3[2][2],array3[2][1],array3[2][0])

        Tower2=VGroup(L21.copy(),L22.copy())
        for x in Tower2:
            x.arrange(.01*RIGHT)
        Tower2.arrange(.01*UP)
        Tower2.next_to(Tower1,.01*UP)

        self.play(ReplacementTransform(VGroup(L21,L22).copy(),Tower2), run_time=2)

        self.wait(.5)

        L31=VGroup(array4[0][1],array4[1][1],array4[1][0])
        L32=VGroup(array3[0][1],array3[1][1],array3[1][0])
        L33=VGroup(array2[0][1],array2[1][1],array2[1][0])

        Tower3=VGroup(L31.copy(),L32.copy(),L33.copy())
        for x in Tower3:
            x.arrange(.01*RIGHT)
        Tower3.arrange(.01*UP)
        Tower3.next_to(Tower2,.01*UP)

        self.play(ReplacementTransform(VGroup(L31,L32,L33).copy(),Tower3), run_time=2)

        self.wait(.5)

        L4=VGroup(array4[0][0],array3[0][0],array2[0][0],array1[0][0])

        Tower4=L4.copy()
        Tower4.arrange(.01*UP)
        Tower4.next_to(Tower3,.01*UP)

        self.play(ReplacementTransform(L4.copy(),Tower4), run_time=2)

        self.wait(.5)

        play_kw2={"run_time":1.5}

        fourfour=fourbyfour.copy()
        threethree=threebythree.copy()
        twotwo=twobytwo.copy()
        oneone=onebyone.copy()
        self.play(fourfour.animate.next_to(Tower4,.01*LEFT), threethree.animate.next_to(Tower3,.01*LEFT), twotwo.animate.next_to(Tower2,.01*LEFT), oneone.animate.next_to(Tower1,.01*LEFT),**play_kw)
        play_kw={"run_time":2}
        self.wait(.5)
        fourfour1=fourbyfour.copy()
        threethree1=threebythree.copy()
        twotwo1=twobytwo.copy()
        oneone1=onebyone.copy()
        self.play(fourfour1.animate.flip(UP),threethree1.animate.flip(UP),twotwo1.animate.flip(UP),oneone1.animate.flip(UP),run_time=1.5)
        self.play(fourfour1.animate.next_to(Tower4,.01*RIGHT), threethree1.animate.next_to(Tower3,.01*RIGHT), twotwo1.animate.next_to(Tower2,.01*RIGHT), oneone1.animate.next_to(Tower1,.01*RIGHT),**play_kw)

        self.wait()
        formula=Tex(r"\sum_{i=0}^ni^2=\frac{n(n+1)(2n+1)}{6}").scale(.65)
        formula.next_to(VGroup(L1,Tower1), DOWN)
        formula.to_edge(DOWN, buff=1)
        self.play(Write(formula))

        self.wait(3)

        TheTable=TexText(r"\begin{tabular}{c||c|c|c|c|c|c|c|c|c|c|c|c} \(n\) & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 & \(\ldots\)\\ \hline \(S_n\) & 0 & 1 & 5 & 14 & 30 & 55 & 91 & 140 & 204 & 285 & 385& \(\ldots\)\\ \hline \(\Delta(S)_n\) & & 1 & 4 & 9 & 16 & 25 & 36 & 49 & 64 & 81 & 100& \(\ldots\) \\ \hline \(\Delta\Delta(S)_n\) & &  & 3 & 5 & 7 & 9 & 11 & 13 & 15 & 17 & 19& \(\ldots\) \\ \hline \(\Delta\Delta\Delta(S)_n\) & &  &  & 2 & 2 & 2 & 2 & 2 & 2 & 2 & 2& \(\ldots\)\\ \end{tabular}").scale(.5)

        TheTable.next_to(VGroup(oneone1,fourfour1),RIGHT)
        TheTable.to_edge(RIGHT, buff=.5)

        self.play(Write(TheTable), run_time=5)
        self.wait(2)

        formula2=Tex("\sum_{i=0}^ni^2","=","an^3+bn^2+cn+d","=","\\frac{1}{3}n^3+\\frac{1}{2}n^2+\\frac{1}{6}n").scale(.65)
        formula2.next_to(TheTable, DOWN)
        formula2.to_edge(DOWN, buff=1)

        self.play(Write(formula2[0:3]))
        self.wait()

        self.play(Write(formula2[3:]))
        self.wait(2)

        Quest=VGroup(Text("Question.", font_size=30, font="Optima", t2c={"Question.": color4}),
                       TexText(
                           r"These are the same, but is it clear these will be the sum of squares?",
                           font_size=30,
                           font="Optima")
                       )

        Quest[0].to_edge(LEFT, buff=.5)
        Quest[0].to_edge(UP, buff=7.35)
        Quest[1].next_to(Quest[0], RIGHT)
        Quest[1].to_edge(UP, buff=7.35)
        self.play(Write(Quest), run_time=3)
        self.wait(5)

class DefInduction(Scene):
    def construct(self):
        color1="#39ff14"

        color2="#0072B2"

        color3="#CC79A7"
        color4="#F0E442"

        color5 = "#7DF9FF"
        color6 = "#FF10F0"
        color7 = "#FFF01F"
        color8 = "#39ff14"
        BROWN = "#7B3F00"

        colors=[color4, color5, color6, color7]



        Recl=VGroup(Text("Recall.", font_size=30, font="Optima", t2c={"Recall.": color3}),
                       TexText(
                           r"The formal law of inference called \textit{modus ponens} states that ",
                           font_size=30,
                           font="Optima")
                       )

        Recl[0].to_edge(LEFT, buff=.5)
        Recl[0].to_edge(UP, buff=.5)
        Recl[1].next_to(Recl[0], RIGHT)
        Recl[1].to_edge(UP, buff=.5)
        self.play(Write(Recl), run_time=3)


        MP=Tex("(","P","\\to ","Q",")","\\wedge ","P","\\Longrightarrow ","Q").scale(.75)

        MP.to_edge(UP, buff=1)
        self.play(Write(MP[:5]))
        self.play(Write(MP[5]))
        self.play(Write(MP[6]))
        self.wait()
        self.play(Write(MP[7]))
        self.wait()
        self.play(TransformMatchingShapes(VGroup(MP[1:4],MP[6]).copy(),MP[-1]), run_time=2)


        self.wait(2)


        CompDef=VGroup(Text("Definition.", font_size=30, font="Optima", t2c={"Definition.": color2}),
                       TexText(
                           r"The principle of \textit{mathematical induction} is a technique that utilizes modus",
                           font_size=30,
                           font="Optima"),
                       TexText(
                           r" ponens",
                           font_size=30,
                           font="Optima"),
               TexText(" to prove statements of the form ", "\(\\forall n\geq n_0 P(n)\)"," where \(P(x)\) is a predicate.", font_size=30,
                       font="Optima"),
                       )

        CompDef[0].to_edge(LEFT, buff=.5)
        CompDef[0].to_edge(UP, buff=1.8)
        CompDef[1].next_to(CompDef[0], RIGHT)
        CompDef[1].to_edge(UP, buff=1.8)
        CompDef[2].next_to(CompDef[1],.5*RIGHT)
        CompDef[2].to_edge(UP, buff=1.87)
        CompDef[3].next_to(CompDef[0], DOWN+RIGHT)
        CompDef[3][1].set_fill(color6, opacity=1)
        self.play(Write(CompDef[:3]), run_time=3)


        self.wait()
        self.play(Write(CompDef[3]), run_time=3)
        self.wait(2)

        Goal=Tex(r"\forall n\geq n_0 P(n)").scale(.75)
        Step1=Tex("P(n_0)").scale(.75)
        Step2=Tex(r"\forall n\geq n_0 [P(n)\to P(n+1)]").scale(.75)


        Goal.to_edge(UP, buff=3)

        Step1.next_to(Goal, 2*DOWN+4*LEFT)
        Step2.next_to(Goal, 2*DOWN+RIGHT)

        self.play(TransformMatchingShapes(CompDef[3][1].copy(),Goal), run_time=2)

        self.wait(2)
        self.play(TransformMatchingShapes(Goal.copy(), VGroup(Step1,Step2)), run_time=2)
        self.wait(2)

        brace1=Brace(Step1,DOWN)
        label1=Text("Base case", font_size=30,font="Optima")
        label11=Text("(a single proposition)", font_size=30,font="Optima")
        label1.next_to(brace1,DOWN)
        label11.next_to(label1,DOWN)

        brace2=Brace(Step2,DOWN)
        label2=Text("Induction step", font_size=30,font="Optima")
        label22=Text("(universal if/then statement)", font_size=30,font="Optima")
        label2.next_to(brace2,DOWN)
        label22.next_to(label2,DOWN)

        self.play(GrowFromCenter(brace1),Write(label1), run_time=2)
        self.wait()
        self.play(Write(label11), run_time=1)
        self.wait()
        self.play(GrowFromCenter(brace2),Write(label2), run_time=2)
        self.wait()
        self.play(Write(label22), run_time=1)
        self.wait(3)
        self.play(FadeOut(VGroup(label11,label22)))
        self.wait(2)

        Exp=VGroup(Text("Example.", font_size=30, font="Optima", t2c={"Example.": color4}),
                       TexText(
                           r"To prove that \(4\) evenly divides \(5^n-1\) for all \(n\geq 0\), we prove",
                           font_size=30,
                           font="Optima"),TexText(
                           r"1) \(5^0-1\) is evenly divisible by \(4\); and",
                           font_size=30,
                           font="Optima"), TexText(
                           r"2) for all \(n\geq 0\), if \(4\) evenly divides \(5^n-1\), then \(4\) evenly",
                           font_size=30,
                           font="Optima"), TexText(
                           r"divides \(5^{n+1}-1.\) ",
                           font_size=30,
                           font="Optima")
                       )

        Exp[0].to_edge(LEFT, buff=.5)
        Exp[0].to_edge(UP, buff=6)
        Exp[1].next_to(Exp[0], RIGHT)
        Exp[1].to_edge(UP, buff=6)
        Exp[2].to_edge(LEFT, buff=2.25)
        Exp[2].to_edge(UP, buff=6.65)
        Exp[3].to_edge(LEFT, buff=2.25)
        Exp[3].to_edge(UP, buff=7.25)
        Exp[4].next_to(Exp[3], .5*RIGHT)
        Exp[4].to_edge(UP, buff=7.225)

        self.play(Write(Exp[:2]), run_time=3)
        self.wait()
        self.play(Write(Exp[2]), run_time=2)
        self.wait(2)
        self.play(Write(Exp[3:]), run_time=2)

        self.wait(5)

class induct(Scene):
    def construct(self):
        color2="#0072B2"

        color3="#CC79A7"
        color4="#F0E442"

        color5 = "#7DF9FF"
        color6 = "#FF10F0"
        color7 = "#FFF01F"
        color8 = "#39ff14"
        BROWN = "#7B3F00"

        play_kw={"run_time":3}

        m=510
        InductText=Text("Induction Step:", font_size=40, font="Optima", color=color2)
        BaseText=Text("Base Case:",font_size=40, font="Optima", color=color3)
        InductText.to_edge(LEFT, buff=1.55)
        InductText.to_edge(UP, buff=.5)

        BaseText.to_edge(LEFT, buff=8)
        BaseText.to_edge(UP, buff=.5)

        SetupText=Tex("\\forall n (P(n)\\to P(n+1))").scale(.75)
        SetupText.to_edge(LEFT, buff=1.5)
        SetupText.to_edge(UP, buff=1.25)

        TheLine=Line((0,0,0), (3.5,0,0))
        TheLine.next_to(SetupText,.5*DOWN)
        
        Implications=[Tex("P(",str(i),")\\to P(",str(i+1),")").scale(.75) for i in range(m)]
        ImplicationText=VGroup(*Implications)
        ImplicationText.arrange(DOWN)
        ImplicationText.next_to(TheLine,DOWN)
        for y in ImplicationText:
            y.to_edge(LEFT, buff=2.1)
        Known=[Tex("P(",str(i),")").scale(.75) for i in range(m+1)]

        KnownText=VGroup(*Known)
        KnownText[0].next_to(SetupText, RIGHT)

        KnownText[0].to_edge(LEFT, buff=8.5)

        for i in range(1,len(KnownText)):
            KnownText[i].next_to(ImplicationText[i-1],RIGHT)
            KnownText[i].to_edge(LEFT, buff=8.5)

        self.play(Write(InductText))

        self.play(Write(SetupText))
        self.play(ShowCreation(TheLine))
        self.wait(3)

        self.play(*[FadeIn(x) for x in ImplicationText], run_time=1.5)

        self.wait(3)

        self.play(Write(BaseText))
        self.wait()
        self.play(Write(KnownText[0]))         
        self.camera.frame.save_state()
        
        self.wait(3)
        p=12
        for i in range(p):
            therun=1
            if i>=8:
                therun=.5
            self.play(TransformMatchingShapes(VGroup(KnownText[i].copy(),ImplicationText[i].copy()), KnownText[i+1]), run_time=therun)
            if i<=4:
                self.wait()
            if i>=5:
                self.play(
                    # Move the camera to the object
                    self.camera.frame.animate.move_to((0,KnownText[i+1].get_y(), 0)),run_time=therun)

        self.wait()

        self.play(FadeIn(KnownText[p+1:101]), self.camera.frame.animate.move_to((0,KnownText[100].get_y(), 0)), run_time=4)

        self.wait(2)
        self.play(FadeIn(KnownText[101:]))
        self.play(self.camera.frame.animate.move_to((0,KnownText[m-10].get_y(), 0)), run_time=8)

        self.wait(3)


        self.play(FadeOut(KnownText[1:]),FadeOut(ImplicationText),Restore(self.camera.frame), run_time = 5)

        self.wait(2)

        Induction=Tex(r"\forall n\geq 0\ P(n)")
        Induction.move_to((0,.5,0))
        self.play(Write(Induction))

        self.wait(2)

        CompDef=VGroup(Text("Remark.", font_size=30, font="Optima", t2c={"Remark.": color3}),
                       TexText(
                           r"We now know \textit{why} the principle of induction works, but we have not",
                           font_size=30,
                           font="Optima"),
               TexText(r"yet seen how to formally implement the technique in a proof.", font_size=30,
                       font="Optima"),
                       )

        CompDef[0].to_edge(LEFT, buff=.5)
        CompDef[0].to_edge(UP, buff=6)
        CompDef[1].next_to(CompDef[0], RIGHT)
        CompDef[1].to_edge(UP, buff=6)
        CompDef[2].next_to(CompDef[0], DOWN+RIGHT)
        self.play(Write(CompDef), run_time=3)



        self.wait(5)

class InductionExample(Scene):
    def construct(self):
        color1="#39ff14"

        color2="#0072B2"

        color3="#CC79A7"
        color4="#F0E442"

        color5 = "#7DF9FF"
        color6 = "#FF10F0"
        color7 = "#FFF01F"
        color8 = "#39ff14"
        BROWN = "#7B3F00"

        colors=[color4, color5, color6, color7]



        Exp=VGroup(Text("Example.", font_size=30, font="Optima", t2c={"Example.": color4}),
                       TexText(
                           r"Let's prove that \(4\) evenly divides \(5^n-1\) for every natural number \(n\). ",
                           font_size=30,
                           font="Optima")
                       )

        Exp[0].to_edge(LEFT, buff=.5)
        Exp[0].to_edge(UP, buff=.5)
        Exp[1].next_to(Exp[0], RIGHT)
        Exp[1].to_edge(UP, buff=.5)
        self.play(Write(Exp), run_time=3)
        self.wait(2)



        Base=VGroup(Text("Base Case.", font_size=30, font="Optima", t2c={"Base Case.": color3}),
                       TexText(
                           r"Let \(n=0\)."," Then \(5^0-1 = 0 \)"," \( = 4\cdot 0\)", " so that \(4\) evenly divides \(5^0-1\).",
                           font_size=30,
                           font="Optima")
                       )

        Base[0].to_edge(LEFT, buff=1)
        Base[0].to_edge(UP, buff=1.25)
        Base[1].next_to(Base[0], RIGHT)
        Base[1].to_edge(UP, buff=1.2)

        self.play(Write(Base[0]), run_time=1)

        self.play(Write(Base[1][0]), run_time=1)
        self.wait(2)
        self.play(Write(Base[1][1]), run_time=1)
        self.wait()
        self.play(Write(Base[1][2]), run_time=1)
        self.wait()
        self.play(Write(Base[1][3]), run_time=1)

        self.wait(4)

        Ind=VGroup(Text("Induction Step.", font_size=30, font="Optima", t2c={"Induction Step.": color2}),
                       TexText(
                           "Let \(n\) be a given, fixed, natural number.", " \\textit{Assume} that \(4\) evenly divides",
                           font_size=30,
                           font="Optima"),
                    TexText(
                        r"\(5^n-1\) for this value of \(n\).", " Then we know ", "\(5^n-1=4k\)"," for some integer \(k\).",
                        font_size=30,
                        font="Optima"),
                   TexText(
                       r"Next we consider the quantity ", "\(5^{n+1}-1\):",
                       font_size=30,
                       font="Optima")
                       )

        Ind[0].to_edge(LEFT, buff=1)
        Ind[0].to_edge(UP, buff=2)
        Ind[1].next_to(Ind[0], RIGHT)
        Ind[1].to_edge(UP, buff=2)
        Ind[2].next_to(Ind[0], DOWN+RIGHT)
        Ind[3].next_to(Ind[0], 3*DOWN+RIGHT)


        self.play(Write(VGroup(Ind[0],Ind[1][0])), run_time=3)
        self.wait(2)
        self.play(Write(VGroup(Ind[1][1],Ind[2][0])), run_time=3)
        self.wait(2)
        self.play(Write(Ind[2][1:]), run_time=2)
        self.wait(2)

        self.play(Write(Ind[3]), run_time=2)
        self.wait(2)

        LeftEq=Tex("5^{n+1}-1").scale(.75)
        RightEq=VGroup(Tex("=","5^{n+1}-5","+5-1"), Tex("=","5(","5^{n}-1",")","+5-1"),Tex("=","5(","5^{n}-1",")","+","4"),Tex("=","5(","4k",")","+","4"),Tex("=","4(","5k","+","1",")."))

        LeftEq.to_edge(UP, buff=3.65)
        LeftEq.to_edge(LEFT, buff=5)
        for i in range(len(RightEq)):
            RightEq[i].scale(.75)
            RightEq[i].next_to(LeftEq,RIGHT)
            RightEq[i].shift(.5*i*DOWN)

        self.play(TransformMatchingShapes(Ind[3][-1].copy(),LeftEq), run_time=2)
        self.wait()
        self.play(Write(RightEq[0][0]))
        self.play(TransformMatchingShapes(LeftEq.copy(),RightEq[0][1:]), run_time=2)
        for i in range(1,len(RightEq)):
            self.wait()
            self.play(Write(RightEq[i][0]))
            if i==2:
                self.play(Write(RightEq[i][1:]))
            elif i==3:
                self.play(Write(VGroup(RightEq[i][1],RightEq[i][3:])))
                self.wait()
                self.play(RightEq[2][2].animate.set_fill(color6))
                self.play(RightEq[2][2].animate.scale(1.5), run_time=.75)
                self.play(RightEq[2][2].animate.scale(1/1.5), run_time=.75)
                self.play(Ind[2][2].animate.set_fill(color6))
                self.play(Ind[2][2].animate.scale(1.5), run_time=.75)
                self.play(Ind[2][2].animate.scale(1 / 1.5), run_time=.75)
                self.wait(2)
                self.play(TransformMatchingShapes(Ind[2][2].copy(),RightEq[i][2]), run_time=3)
                self.play(RightEq[2][2].animate.set_fill(WHITE),Ind[2][2].animate.set_fill(WHITE))


            else:
                self.play(TransformMatchingShapes(RightEq[i-1][1:].copy(), RightEq[i][1:]), run_time=2)

        concl=TexText(r"Because \(k\) is an integer, the quantity \(5k+1\) is an integer. Thus, as ",
                           font_size=30,
                           font="Optima")
        concl2=TexText(r"\(5^{n+1}-1=4(5k+1)\) and \(5k+1\) is an integer, \(4\) evenly divides \(5^{n+1}-1\).",
                           font_size=30,
                           font="Optima")
        concl3=TexText(r"By the process of induction, \(4\) divides \(5^n-1\) for every value of \(n\) greater than 0.",
                           font_size=30,
                           font="Optima")

        concl.next_to(Ind[0], RIGHT)
        concl.to_edge(UP, buff=6.25)

        concl2.next_to(Ind[0], RIGHT)
        concl2.to_edge(UP, buff=6.75)

        concl3.to_edge(UP, buff=7.4)

        concl3.to_edge(LEFT, buff=1)

        for x in [concl,concl2, concl3]:
            self.wait()
            self.play(Write(x), run_time=3)
        self.wait(5)

class SumSquaresInduct(Scene):
    def construct(self):
        color1="#39ff14"

        color2="#0072B2"

        color3="#CC79A7"
        color4="#F0E442"

        color5 = "#7DF9FF"
        color6 = "#FF10F0"
        color7 = "#FFF01F"
        color8 = "#39ff14"
        BROWN = "#7B3F00"

        colors=[color4, color5, color6, color7]



        Exp=VGroup(Text("Theorem.", font_size=30, font="Optima", t2c={"Theorem.": color2}),
                       TexText(
                           r"For every natural number \(n\), \(\displaystyle\sum_{i=0}^n i^2 = \frac{n(n+1)(2n+1)}{6}\).",
                           font_size=30,
                           font="Optima")
                       )

        Exp[0].to_edge(LEFT, buff=.5)
        Exp[0].to_edge(UP, buff=.5)
        Exp[1].next_to(Exp[0], RIGHT)
        Exp[1].to_edge(UP, buff=.25)
        self.play(Write(Exp), run_time=3)
        self.wait(2)



        Base=VGroup(Text("Base Case.", font_size=30, font="Optima", t2c={"Base Case.": color3}),
                       TexText(
                           r"Let \(n=0\)."," Then \(\displaystyle\sum_{i=0}^0 i^2=0^2=0 \)"," \( = \\frac{0(0+1)(2\\cdot 0+ 1)}{6}\)", ".",
                           font_size=30,
                           font="Optima")
                       )

        Base[0].to_edge(LEFT, buff=1)
        Base[0].to_edge(UP, buff=1.3)
        Base[1].next_to(Base[0], RIGHT)
        Base[1].to_edge(UP, buff=1)

        self.play(Write(Base[0]), run_time=1)

        self.play(Write(Base[1][0]), run_time=1)
        self.wait(2)
        self.play(Write(Base[1][1]), run_time=1)
        self.wait()
        self.play(Write(Base[1][2]), run_time=1)
        self.wait()
        self.play(Write(Base[1][3]), run_time=1)

        self.wait(4)

        Ind=VGroup(Text("Induction Step.", font_size=30, font="Optima", t2c={"Induction Step.": color2}),
                       TexText(
                           "Let \(n\) be a given, fixed, natural number.", " \\textit{Assume} ", " \(\displaystyle\sum_{i=0}^n i^2 = \\frac{n(n+1)(2n+1)}{6}\)",
                           font_size=30,
                           font="Optima"),
                   TexText(
                       r"for this \(n\). "," Next we consider the next sum ", "\(\displaystyle\sum_{i=0}^{n+1} i^2\)",":",
                       font_size=30,
                       font="Optima")
                       )

        Ind[0].to_edge(LEFT, buff=1)
        Ind[0].to_edge(UP, buff=2.05)
        Ind[1].next_to(Ind[0], RIGHT)
        Ind[1].to_edge(UP, buff=1.81)
        Ind[2].next_to(Ind[0], DOWN+RIGHT)


        self.play(Write(VGroup(Ind[0],Ind[1][0])), run_time=3)
        self.wait(2)
        self.play(Write(VGroup(Ind[1][1],Ind[1][2], Ind[2][0])), run_time=3)
        self.wait(2)
        self.play(Write(Ind[2][1:]), run_time=2)
        self.wait(2)

        LeftEq=Tex("\sum_{i=0}^{n+1} i^2").scale(.65)
        RightEq=VGroup(Tex("=","\\sum_{i=0}^{n} i^2","+","(n+1)^2"), Tex("=","\\frac{n(n+1)(2n+1)}{6}","+","(n+1)^2"),Tex("=","\\frac{n(n+1)(2n+1)+6(n+1)^2}{6}"),Tex("=","\\frac{(n+1)(n+2)(2n+3)}{6}","."))

        LeftEq.to_edge(UP, buff=3.5)
        LeftEq.to_edge(LEFT, buff=4)
        for i in range(len(RightEq)):
            RightEq[i].scale(.65)
            RightEq[i].next_to(LeftEq,RIGHT)
            RightEq[i].shift(.9*i*DOWN)

        RightEq[-1].next_to(RightEq[-2],RIGHT)

        self.play(TransformMatchingShapes(Ind[2][-2].copy(),LeftEq), run_time=2)
        self.wait()
        self.play(Write(RightEq[0][0]))
        self.play(TransformMatchingShapes(LeftEq.copy(),RightEq[0][1:]), run_time=2)
        for i in range(1,len(RightEq)):
            self.wait()
            self.play(Write(RightEq[i][0]))
            if i==1:
                self.wait()
                self.play(RightEq[0][1].animate.set_fill(color6))
                self.play(RightEq[0][1].animate.scale(1.5), run_time=.75)
                self.play(RightEq[0][1].animate.scale(1/1.5), run_time=.75)
                self.play(Ind[1][-1].animate.set_fill(color6))
                self.play(Ind[1][-1].animate.scale(1.5), run_time=.75)
                self.play(Ind[1][-1].animate.scale(1 / 1.5), run_time=.75)
                self.wait(2)
                self.play(TransformMatchingShapes(Ind[1][-1].copy(),RightEq[i][1]), run_time=3)
                self.play(RightEq[0][1].animate.set_fill(WHITE),Ind[1][-1].animate.set_fill(WHITE))
                self.play(Write(RightEq[i][-2:]))
            else:
                self.play(TransformMatchingShapes(RightEq[i-1][1:].copy(), RightEq[i][1:]), run_time=2)

        concl=TexText(r"Thus the theorem holds by induction.",
                           font_size=30,
                           font="Optima")

        concl3=TexText(r"So \(\displaystyle\sum_{i=0}^{n+1} i^2 = \frac{(n+1)((n+1)+1)(2(n+1)+1)}{6}\) as required.",
                           font_size=30,
                           font="Optima")

        concl.to_edge(LEFT, buff=1)
        concl.to_edge(UP, buff=7.4)


        concl3.next_to(Ind[0], RIGHT)
        concl3.to_edge(UP, buff=6.25)

        for x in [concl3, concl]:
            self.wait()
            self.play(Write(x), run_time=3)
        self.wait(5)

class visualInduct(Scene):
    def construct(self):
        color1="#39ff14"

        color2="#0072B2"

        color3="#CC79A7"
        color4="#F0E442"

        color5 = "#7DF9FF"
        color6 = "#FF10F0"
        color7 = "#FFF01F"
        color8 = "#39ff14"
        colors=[color5,color6]

        Exp=VGroup(Text("Remark.", font_size=30, font="Optima", t2c={"Remark.": color3}),
                       TexText(
                           r"The induction step is a conditional statement; you do NOT \textit{verify} the",
                           font_size=30,
                           font="Optima"),TexText(
                           r" hypothesis.",
                           font_size=30,
                           font="Optima")
                       )

        Exp[0].to_edge(LEFT, buff=.5)
        Exp[0].to_edge(UP, buff=.5)
        Exp[1].next_to(Exp[0], RIGHT)
        Exp[1].to_edge(UP, buff=.5)
        Exp[2].next_to(Exp[1], .5*RIGHT)
        Exp[2].to_edge(UP, buff=.5)

        self.play(Write(Exp), run_time=3)
        self.wait(2)

        Idea=VGroup(Text("Idea.", font_size=30, font="Optima", t2c={"Idea.": color3}),
                       TexText(
                           r"Imagine that someone has verified the hypothesis for you for a fixed \(n\). Use",
                           font_size=30,
                           font="Optima"),
                    TexText(
                        r"that major assumption to explain why the predicate then also holds for \(n+1\). ",
                        font_size=30,
                        font="Optima")
                       )

        Idea[0].to_edge(LEFT, buff=.5)
        Idea[0].to_edge(UP, buff=1.1)
        Idea[1].next_to(Idea[0], RIGHT)
        Idea[1].to_edge(UP, buff=1.1)
        Idea[2].next_to(Idea[0], DOWN+RIGHT)
        self.play(Write(Idea), run_time=3)
        self.wait(2)


        n=4
        rect=[linesquares(20) for i in range(9)]
        Diag=VGroup(*rect)
        for x in Diag:
            x.arrange(.01*RIGHT)
        Diag.arrange(.01*DOWN)
        Diag.move_to((0,-.25,0))
        Diag.scale(.25)

        self.play(ShowCreation(Diag))
        b1=Brace(Diag,UP)
        b2=Brace(Diag,LEFT)
        lab1=Tex("n(n+1)").scale(.6)
        lab2=Tex("2n+1").scale(.6)
        lab2.rotate(PI/2)
        lab1.next_to(b1,UP)
        lab2.next_to(b2,LEFT)

        self.play(GrowFromCenter(b1),Write(lab1))
        self.wait()
        self.play(GrowFromCenter(b2),Write(lab2))



        ULeft=Diag[0][0].get_vertices()[3]
        URight=Diag[0][-1].get_vertices()[2]
        LRight=Diag[-1][-1].get_vertices()[1]
        LLeft=Diag[-1][0].get_vertices()[0]
        bigRect=Polygon(LLeft,LRight,URight,ULeft).set_fill(GREY, opacity=1)
        self.play(FadeIn(bigRect))
        self.wait(2)
        self.remove(Diag)
        self.bring_to_back(bigRect)

        arealabel=Tex("6\sum_{i=1}^ni^2").scale(.6)
        arealabel.move_to((bigRect.get_center()))
        self.play(Write(arealabel))

        self.wait(2)

        self.play(FadeOut(b1),lab1.animate.shift(1.2*DOWN))

        self.play(FadeOut(b2),lab2.animate.shift(1.2*RIGHT))

        self.wait(2)

        Squares=VGroup(*[VGroup(*[linesquares(5) for i in range(5)]) for j in range(6)])
        j=0
        for x in Squares:
            x.arrange(.01*DOWN)
            x.set_fill(colors[j%2], opacity=1)
            j+=1

        Squares.scale(.25)

        Squares.arrange(2*RIGHT)
        Squares.to_edge(DOWN, buff=.25)
        Squares.shift(.5*RIGHT)
        newarea=Tex("6(n+1)^2",":").scale(.6)
        newarea.next_to(Squares,LEFT)
        self.play(Write(newarea))
        self.wait(.5)
        self.play(ShowCreation(Squares), run_time=3)
        self.wait(2)
        Squares2=Squares.copy()
        Squares2[0].next_to(bigRect,.01*LEFT)
        Squares2[0].shift(.5*UP)
        Squares2[1].next_to(bigRect,.01*LEFT)
        Squares2[1].shift(.75*DOWN)

        Squares2[2].next_to(bigRect,.01*RIGHT)
        Squares2[2].shift(.75*UP)
        Squares2[3].next_to(bigRect,.01*RIGHT)
        Squares2[3].shift(.5*DOWN)

        Squares2[4].arrange(.01*RIGHT)
        Squares2[4].next_to(bigRect,.01*DOWN)
        Squares2[4].shift(.25*2.5*RIGHT)

        Squares2[5].arrange(.01*RIGHT)
        Squares2[5].next_to(bigRect,.01*UP)
        Squares2[5].shift(.25*2.5*LEFT)

        for i in [0,1,4,3,2,5]:
            self.play(ReplacementTransform(Squares[i],Squares2[i]), run_time=2)
            self.wait()
        fulldiag=VGroup(bigRect,*Squares2,lab1,lab2,arealabel)
        self.play(fulldiag.animate.shift(.25*DOWN), run_time=2)
        self.wait(.5)

        b3=Brace(VGroup(Squares2[2],Squares2[5]),UP)
        b4=Brace(VGroup(Squares2[0],Squares2[1]),LEFT)
        lab3=Tex("n(n+1)+2(n+1)","=","(n+1)(n+2)").scale(.6)
        lab4=Tex("2n+3").scale(.6)
        lab3.next_to(b3,UP)
        lab4.next_to(b4,LEFT)

        self.play(GrowFromCenter(b3),Write(lab3))
        self.wait()
        self.play(GrowFromCenter(b4),Write(lab4))

        finalformula=Tex("6\sum_{i=1}^{n+1}i^2","=","6(n+1)^2","+","6\sum_{i=1}^ni^2","=","6(n+1)^2","+","n(n+1)(2n+1)","=","(n+1)(n+2)","(2n+3)").scale(.75)

        self.wait(2)


        finalformula.to_edge(DOWN, buff=.75)

        self.play(TransformMatchingShapes(newarea,finalformula[2]), run_time=1)
        self.play(Write(finalformula[3]))
        self.play(TransformMatchingShapes(arealabel.copy(),finalformula[4]), run_time=2)

        self.wait()

        self.play(Write(finalformula[5]))
        self.play(TransformMatchingShapes(finalformula[2].copy(),finalformula[6]), run_time=2)
        self.play(Write(finalformula[7]))

        self.play(finalformula[4].animate.set_fill(color4,opacity=1), run_time=1)
        self.wait()
        self.play(TransformMatchingShapes(VGroup(lab1,lab2).copy(),finalformula[8]), run_time=2)
        self.wait(2)

        self.play(Write(finalformula[9]))
        self.play(TransformMatchingShapes(lab3[-1].copy(),finalformula[10]),TransformMatchingShapes(lab4.copy(),finalformula[11]), run_time=2)
        self.wait(2)
        self.play(Write(finalformula[0:2]))
        self.wait(2)
        self.play(finalformula[10:].animate.next_to(finalformula[1],RIGHT), FadeOut(finalformula[2:10]), run_time=2)
        self.wait(2)

        conclu=TexText("\\textit{as long as} the assumption \(\displaystyle 6\sum_{i=1}^ni^2 =n(n+1)(2n+1)\) holds.",font_size=30,font="Optima")
        conclu.next_to(finalformula[-1], RIGHT)
        self.play(Write(conclu), run_time=3)
        self.wait(2)
        final=VGroup(Text("Technique.", font_size=30, font="Optima", t2c={"Technique.": color2}),
                       TexText(
                           r"Prove the base case and let induction take over.",
                           font_size=30,
                           font="Optima")
                       )

        final[0].to_edge(LEFT, buff=.5)
        final[0].to_edge(UP, buff=7.5)
        final[1].next_to(final[0], RIGHT)
        final[1].to_edge(UP, buff=7.5)
        self.play(Write(final), run_time=3)

        self.wait(5)