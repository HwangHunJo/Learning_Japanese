from functools import partial
import random
import tkinter

window = tkinter.Tk()
window.title("Japanese Quiz")
window.geometry("500x500")
window.resizable(False, False)

content = []
WrongAnsCnt = 0
rd = random.randint(0, 25)
with open("dict_english.txt", "r", encoding = "UTF8") as file:
    for f in file:
        content.append(f.split(" "))
NowLanguage = "English"
QuizText = tkinter.Label(window, font = ("Courier", 30, "bold"), text = content[rd][0])

def CheckText(event):
    global WrongAnsCnt
    global CorrectCnt
    global CorrectCntLabel
    global RightAnswer
    global RightAnswerLabel
    global NowLanguage
    global content
    global rd

    UserAnswer = InputEntry.get().strip()
#     print(content[rd])
    if WrongAnsCnt >= 3:
        if NowLanguage == "English":
            RightAnswer = f"{content[rd][0]}'s Right Answer is {content[rd][1]}"
        elif NowLanguage == "Korean":
            RightAnswer = f"{content[rd][0]}의 정답은 {content[rd][1]}"
        WrongAnsCnt = 0
        RandomChoose()
    elif UserAnswer != "" and UserAnswer in content[rd][1]:
        WrongAnsCnt = 0
        CorrectCnt += 1
        RandomChoose()
    else:
        WrongAnsCnt += 1
    RightAnswerLabel.config(text = RightAnswer)
    CorrectCntLabel.config(text = f"Corrects : {CorrectCnt}")
    MistakeNumLabel.config(text = f"Mistakes : {WrongAnsCnt}")

def OpenFile(choose):
    global content
    global NowLanguage
    content = []

    if choose == 1:
        NowLanguage = "English"
        with open("dict_english.txt", "r", encoding = "UTF8") as file:
            for f in file:
                content.append(f.split(" "))
        
    elif choose == 2:
        NowLanguage = "Korean"
        with open("dict_korean.txt", "r", encoding = "UTF8") as file:
            for f in file:
                content.append(f.split(" "))

    LanguageLabel.config(text = f"Now Language : {NowLanguage}")

def RandomChoose():
    global rd
    rd = random.randint(0, 25)
    QuizText.config(text = content[rd][0])

CorrectCnt = 0
CorrectCntLabel = tkinter.Label(window, text = f"Corrects : {CorrectCnt}", font = ("Courier", 15))
RightAnswer = ""
RightAnswerLabel = tkinter.Label(window, text = RightAnswer, font = ("Courier", 13))
MistakeNumLabel = tkinter.Label(window, text = f"Mistakes : {WrongAnsCnt}", font = ("Courier", 15))
LanguageLabel = tkinter.Label(window, text = f"Now Language : {NowLanguage}", font = ("Courier", 15))
EnglishButton = tkinter.Button(window, text = "English", command = partial(OpenFile, 1))
KoreanButton = tkinter.Button(window, text = "Korean", command = partial(OpenFile, 2))
InputEntry = tkinter.Entry(window, width = 30)
InputEntry.bind("<Return>", CheckText)


RightAnswerLabel.place(x = 100, y = 300)
CorrectCntLabel.place(x = 0, y = 23)
MistakeNumLabel.place(x = 0, y = 0)
LanguageLabel.place(x = 220, y = 0)
QuizText.place(x = 160, y = 170)
EnglishButton.place(x = 440, y = 475)
KoreanButton.place(x = 390, y = 475)
InputEntry.place(x = 140, y = 270)

window.mainloop()
