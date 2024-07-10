import tkinter
from tkinter import messagebox
import random
import csv
import tkinter as tk

CSV_FILE = "null"

class Quiz():
    def __init__(self, master):
        '''コンストラクタ
            master:クイズ画面を配置するウィジェット
        '''

        # subject = 0
        # level = 0

        # 親ウィジェット
        self.master = master

        # クイズデータリスト
        self.quiz_list = []

        # 現在表示中のクイズ
        self.now_quiz = None

        # 問題の正解数をカウント
        self.count_answer = 0
        # クイズの科目
        self.set_subject = "null"
        # クイズの難易度
        self.set_level = "null"
        # 現在選択中の選択肢番号
        self.choice_value = tkinter.IntVar()
        self.start()
        #self.getQuiz()
        self.createWidgets()
        
        
        

#-----------------start frame------------------------------
    def start(self):
        self.start = tk.Frame()
        self.start.grid(row=0, column=0, sticky="nsew")
        self.titleLabel = tk.Label(self.start, text="スタート画面", font=('Helvetica', '35'))
        self.titleLabel.pack(anchor='center', expand=True)
        self.selectButton1 = tk.Button(self.start, text="next", command=lambda :self.setsubject())
        self.selectButton1.pack()
        self.start.tkraise()
#-----------------start frame------------------------------

#-----------------subject frame---------------------------     
    def callback(self,i):
        self.set_subject = i
        self.setlevel()

    def callback2(self,i):
        self.set_level = i
        self.mode()

    def setsubject(self):
        self.setsubject = tk.Frame()
        self.setsubject.grid(row=0, column=0, sticky="nsew")
        self.titleLabel = tk.Label(self.setsubject, text="科目選択", font=('Helvetica', '35'))
        self.titleLabel.pack(anchor='center', expand=True)
        self.selectButton1 = tk.Button(self.setsubject, text="コンシス",command=lambda :self.callback('c'))
        self.selectButton1.pack()
        self.selectButton2 = tk.Button(self.setsubject, text="アルゴリズム", command=lambda :self.callback('a'))
        self.selectButton2.pack()
        self.selectButton3 = tk.Button(self.setsubject, text="情報ネットワーク", command=lambda :self.callback('n'))
        self.selectButton3.pack()
        self.setsubject.tkraise()
#-----------------subject frame---------------------------  
    
#-----------------level frame------------------------------
    def setlevel(self):
        self.setlevel = tk.Frame()
        self.setlevel.grid(row=0, column=0, sticky="nsew")
        self.titleLabel = tk.Label(self.setlevel, text="難易度選択画面", font=('Helvetica', '35'))
        self.titleLabel.pack(anchor='center', expand=True)
        self.changePageButton = tk.Button(self.setlevel, text="鬼", command=lambda :self.callback2('鬼'))
        self.changePageButton.pack()
        self.changePageButton1 = tk.Button(self.setlevel, text="竜", command=lambda :self.callback2('竜'))
        self.changePageButton1.pack()
        self.changePageButton2 = tk.Button(self.setlevel, text="神", command=lambda :self.callback2('神'))
        self.changePageButton2.pack()
        self.setlevel.tkraise()
#-----------------level frame------------------------------
        
#-----------------mode frame-------------------------------------

    def mode(self):
        def showQuiz(self):
            #'''問題と選択肢を表示'''
            # まだ表示していないクイズからクイズ情報をランダムに取得
            num_quiz = random.randrange(len(self.quiz_list))
            quiz = self.quiz_list[num_quiz]

            # 問題を表示するラベルを作成
            self.problem = tkinter.Label(
                self.frame,
                text=quiz[0]
            )
            self.problem.grid(
                column=0,
                row=0,
                columnspan=4,
                pady=10
            )

            # 選択肢を表示するラジオボタンを４つ作成
            self.choices = []
            for i in range(3):
                # ラジオボタンウィジェットを作成・配置
                choice = tkinter.Radiobutton(
                    self.frame,
                    text=quiz[i+1],
                    variable=self.choice_value,
                    value=i
                )
                choice.grid(
                    row=1,
                    column=i,
                    padx=10,
                    pady=10,
                )
                # ウィジェットを覚えておく
                self.choices.append(choice)

            # 表示したクイズは再度表示しないようにリストから削除
            self.quiz_list.remove(quiz)

        # 現在表示中のクイズを覚えておく
        self.now_quiz = quiz
        self.mode = tk.Frame()
        self.mode.grid(row=0, column=0, sticky="nsew")
        self.titleLabel = tk.Label(self.mode, text=f"これからクイズを始めます\n科目:{self.subject}\nレベル:{self.level}", font=('Helvetica', '30'))
        self.titleLabel.pack(anchor='center', expand=True)
        self.changePageButton = tk.Button(self.mode, text="Go to quiz", command=lambda :self.keeping())
        self.changePageButton.pack()
        self.mode.pack_forget()
        self.getQuiz()
        self.mode.tkraise()
#-----------------mode frame-------------------------------------
    def keeping(self):
        self.setlevel = tk.Frame()
        self.setlevel.grid(row=0, column=0, sticky="nsew")
        self.titleLabel = tk.Label(self.setlevel, text="進行中", font=('Helvetica', '35'))
        self.titleLabel.pack(anchor='center', expand=True)
        self.changePageButton.pack()
        self.showQuiz()

        self.setlevel.tkraise()

    def getQuiz(self):
        '''クイズの情報を取得する'''
        if self.set_subject == "n" and  self.level == "鬼":
            CSV_FILE = "net1.csv"
        elif self.set_subject == "n" and self.level == "竜":
            CSV_FILE = "net2.csv"
        elif self.set_subject == "n" and self.level == "神":
            CSV_FILE = "net3.csv"
        elif self.set_subject == "c" and self.level == "鬼":
            CSV_FILE = "CS1.csv"
        elif self.set_subject == "c" and self.level == "竜":
            CSV_FILE = "CS2.csv"
        elif self.set_subject == "c" and self.level == "神":
            CSV_FILE = "CS3.csv"
        elif self.set_subject == "a" and self.level == "鬼":
            CSV_FILE = "algo1.csv"
        elif self.set_subject == "a" and self.level == "竜":
            CSV_FILE = "algo2.csv"
        elif self.set_subject == "a" and self.level == "神":
            CSV_FILE = "algo3.csv"
        # ファイルを開く
        try:
            f = open(CSV_FILE)
        except FileNotFoundError:
            return None

        # CSVデータとしてファイル読み込み
        csv_data = csv.reader(f)

        # CSVの各行をリスト化
        for quiz in csv_data:
            self.quiz_list.append(quiz)

        f.close()


    def createWidgets(self):
        '''ウィジェットを作成・配置する'''

        # フレームを作成する
        self.frame = tkinter.Frame(
            self.master,
            width=500,
            height=200,
        )
        self.frame.grid()

        # ボタンを作成する
        self.button = tkinter.Button(
            self.master,
            text="OK",
            foreground="#000000",
            command=self.checkAnswer
        )
        self.button.grid()

    def showQuiz(self):
        '''問題と選択肢を表示'''
        # まだ表示していないクイズからクイズ情報をランダムに取得
        num_quiz = random.randrange(len(self.quiz_list))
        quiz = self.quiz_list[num_quiz]

        # 問題を表示するラベルを作成
        self.problem = tkinter.Label(
            self.frame,
            text=quiz[0]
        )
        self.problem.grid(
            column=0,
            row=0,
            columnspan=4,
            pady=10
        )

        # 選択肢を表示するラジオボタンを４つ作成
        self.choices = []
        for i in range(3):
            # ラジオボタンウィジェットを作成・配置
            choice = tkinter.Radiobutton(
                self.frame,
                text=quiz[i+1],
                variable=self.choice_value,
                value=i
            )
            choice.grid(
                row=1,
                column=i,
                padx=10,
                pady=10,
            )
            # ウィジェットを覚えておく
            self.choices.append(choice)

        # 表示したクイズは再度表示しないようにリストから削除
        self.quiz_list.remove(quiz)

        # 現在表示中のクイズを覚えておく
        self.now_quiz = quiz

    def deleteQuiz(self):
        '''問題と選択肢を削除'''

        # 問題を表示するラベルを削除
        self.problem.destroy()

        # 選択肢を表示するラジオボタンを削除
        for choice in self.choices:
            choice.destroy()
            

    def checkAnswer(self):
        '''解答が正解かどうかを表示し、次のクイズを表示する'''

        # 正解かどうかを確認してメッセージを表示
        if self.choice_value.get() == int(self.now_quiz[4]):
            messagebox.showinfo("結果", "正解です！！")
            self.count_answer += 1
        else:
            messagebox.showerror("結果", "不正解です...")

        # 表示中のクイズを非表示にする
        self.deleteQuiz()

        if self.quiz_list:
            # まだクイズがある場合は次のクイズを表示する
            self.showQuiz()
        else:
            # もうクイズがない場合はアプリを終了する
            self.endAppli()

    def endAppli(self):
        '''アプリを終了する'''
        eveal=["勉強しろよ", "勉強しとんか","足りんな","半端やな","爪があめぇ","すごっ"]
        # クイズがもうないことを表示
        self.problem = tkinter.Label(self.frame,text=f"正解数は{self.count_answer}です\n評価:{eveal[self.count_answer]}")
        self.problem.grid(
            column=0,
            row=0,
            padx=10,
            pady=10
        )

        # OKボタンのcommandを変更
        self.button.config(
            command=self.master.destroy
        )

app = tkinter.Tk()
app.geometry("700x400")
quiz = Quiz(app)
app.mainloop()