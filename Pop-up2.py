import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title('\ ポップアップ出し放題 /')

def show():
  pstyle = dezcbx.get()
  title = popt.get()
  message = popm.get()
  if pstyle == "showinfo(info)":
    messagebox.showinfo(title,message)

  elif pstyle == "showwarning(warning)":
    messagebox.showwarning(title,message)

  elif pstyle == "showerror(error)":
    messagebox.showerror(title,message)

  elif pstyle == "askquestion":
    messagebox.askquestion(title,message)

  elif pstyle == "askokcancel":
    messagebox.askokcancel(title,message)

  elif pstyle == "askyesnocancel":
    messagebox.askyesnocancel(title,message)

  elif pstyle == "askretrycancel":
    messagebox.askretrycancel(title,message)

  else:
    messagebox.showerror("エラー","タイプを選んでください")

def showab():
  messagebox.showinfo("アバウト","ポップアップ出し放題\nポップアップを出しまくれるPythonソフト\nバージョン:2.0\n詳細は以下を参照↓\nhttps://github.com/ii268/Pop-updasihoudai/")

styl = ttk.Style()
# print(styl.theme_names()) #デフォルトテーマ一覧取得
styl.theme_use("xpnative")

memubar = tk.Menu(root)
memubar.add_command(label="About", command=showab)
root.config(menu=memubar)

frm = ttk.Frame(root, padding=5)
frm.grid()

ttk.Label(frm,text="デザインを選びタイトルとメッセージに記入してボタンを押すとポップアップが出ます").grid(column=0, row=0,columnspan=2,pady=3)
ttk.Label(frm, text="デザイン:").grid(column=0, row=1, pady=3, sticky="e")# gridメモ sticky:寄せる向き pady:Y軸の幅
ttk.Label(frm, text="タイトル:").grid(column=0, row=2, pady=3, sticky="e")
ttk.Label(frm, text="メッセージ:").grid(column=0, row=3, pady=3, sticky="e")

dezcbx = ttk.Combobox(frm,values=["showinfo(info)","showwarning(warning)","showerror(error)","askquestion","askokcancel","askyesnocancel","askretrycancel"],state="readonly")
dezcbx.set("選んでください")
dezcbx.grid(column=1, row=1, sticky="w")
popt = ttk.Entry(frm)
popt.grid(column=1, row=2, sticky="w")
popm = ttk.Entry(frm)
popm.grid(column=1, row=3, sticky="w")

ttk.Button(frm, text="表示する", command=show).grid(column=0, row=4,columnspan=2, pady=3)

root.mainloop()