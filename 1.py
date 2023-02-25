from tkinter import*
from tkinter import font
import tkinter.messagebox
import pickle
import re
import math
from functions import *

window = Tk()#建立窗口window

ziti=font.Font(family='Freestyle Script',size=30)#设置字体

window.title("login window")#给窗口的可视化起名字

window.geometry('400x300')#设定窗口的大小(长 * 宽)

#加载 wellcome image
canvas = Canvas(window, width=400, height=135, bg='blue')
canvas.pack(side='top')
Label(window, text='Wellcome',font=ziti,bg=None).pack()

#用户信息
Label(window, text='User name:', font=ziti).place(x=10, y=170)
Label(window, text='Password:', font=ziti).place(x=10, y=210)

#用户登录输入框
# 用户名
var_usr_name = StringVar()
var_usr_name.set('example@python.com')
entry_usr_name = Entry(window, textvariable=var_usr_name, font=('Arial', 14))
entry_usr_name.place(x=120,y=175)
# 用户密码
var_usr_pwd = StringVar()
entry_usr_pwd = Entry(window, textvariable=var_usr_pwd, font=('Arial', 14), show='*')
entry_usr_pwd.place(x=120,y=215)

#定义用户登录功能
def usr_login():
    # 这两行代码就是获取用户输入的usr_name和usr_pwd
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
     # 这里设置异常捕获，当第一次访问用户信息文件时是不存在的，所以这里设置异常捕获。
    # 中间的两行是匹配，即程序将输入的信息和文件中的信息匹配。
    try:
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        # 这里是在没有读取到`usr_file`的时候，程序会创建一个`usr_file`这个文件，并将管理员
        # 的用户和密码写入，即用户名为`admin`密码为`admin`。
        with open('usrs_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)
            usr_file.close() 
 
    # 如果用户名和密码与文件中的匹配成功，则会登录成功，并跳出弹窗how are you? 加上你的用户名。
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            window.destroy()
            tkinter.messagebox.showinfo(title='Welcome', message='How are you? ' + usr_name)
            jisuanqi()
        # 如果用户名匹配成功，而密码输入错误，则会弹出'Error, your password is wrong, try again.'
        else:
            tkinter.messagebox.showerror(message='Error, your password is wrong, try again.')
    else:  # 如果发现用户名不存在
        is_sign_up = tkinter.messagebox.askyesno('Welcome! ', 'You have not sign up yet. Sign up now?')
        # 提示需不需要注册新用户
        if is_sign_up:
            usr_sign_up()

# 定义用户注册功能
def usr_sign_up():
    def sign_Website():
        # 以下三行就是获取注册时所输入的信息
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
 
        # 这里是打开记录数据的文件，将注册信息读出
        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        # 这里就是判断，如果两次密码输入不一致，则提示Error, Password and confirm password must be the same!
        if np != npf:
            tkinter.messagebox.showerror('Error', 'Password and confirm password must be the same!')
 
        # 如果用户名已经在数据文件中，则提示Error, The user has already signed up!
        elif nn in exist_usr_info:
            tkinter.messagebox.showerror('Error', 'The user has already signed up!')
 
        # 最后如果输入无以上错误，则将注册输入的信息记录到文件当中，并提示注册成功Welcome！,You have successfully signed up!，然后销毁窗口。
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tkinter.messagebox.showinfo('Welcome', 'You have successfully signed up!')
            # 然后销毁窗口。
            window_sign_up.destroy()
# 定义长在窗口上的窗口
    window_sign_up = Toplevel(window)
    window_sign_up.geometry('300x200')
    window_sign_up.title('Sign up window')
 
    new_name = StringVar()  # 将输入的注册名赋值给变量
    new_name.set('example@python.com')  # 将最初显示定为'example@python.com'
    Label(window_sign_up, text='User name: ').place(x=10, y=10)  # 将`User name:`放置在坐标（10,10）。
    entry_new_name = Entry(window_sign_up, textvariable=new_name)  # 创建一个注册名的`entry`，变量为`new_name`
    entry_new_name.place(x=130, y=10)  # `entry`放置在坐标（150,10）.
 
    new_pwd = StringVar()
    Label(window_sign_up, text='Password: ').place(x=10, y=50)
    entry_usr_pwd = Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=130, y=50)
 
    new_pwd_confirm = StringVar()
    Label(window_sign_up, text='Confirm password: ').place(x=10, y=90)
    entry_usr_pwd_confirm = Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=130, y=90)
 
    # 下面的 sign_Website
    btn_comfirm_sign_up = Button(window_sign_up, text='Sign up', command=sign_Website)
    btn_comfirm_sign_up.place(x=180, y=120)


# login and sign up 按钮
btn_login = Button(window, text='Login', command=usr_login)
btn_login.place(x=120, y=240)
btn_sign_up = Button(window, text='Sign up', command=usr_sign_up)
btn_sign_up.place(x=200, y=240)


def jisuanqi():
  root = Tk()
  root.minsize(300, 400)      # 窗口大小300*400
  root.resizable(0, 0)
  root.title('计算器')    # 计算器名字

  # 运算符号按钮
  # 第一行
  btnac = tkinter.Button(root, text='AC', bd=0.5, font=('黑体', 20), fg='orange', command=lambda \
        x='AC': buttonClick(x))
  btnac.place(x=0, y=150, width=75, height=50)
  btnback = tkinter.Button(root, text='←', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda \
        x='←': buttonClick(x))
  btnback.place(x=75, y=150, width=75, height=50)
  btndivi = tkinter.Button(root, text='^', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda \
        x='^': buttonClick(x))
  btndivi.place(x=150, y=150, width=75, height=50)
  btnmul = tkinter.Button(root, text='+', font=('微软雅黑', 20), fg="#4F4F4F", bd=0.5, command=lambda \
        x='+': buttonClick(x))
  btnmul.place(x=225, y=150, width=75, height=50)
  # 第二行
  btn7 = tkinter.Button(root, text='7', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
        x='7': buttonClick(x))
  btn7.place(x=0, y=200, width=75, height=50)
  btn8 = tkinter.Button(root, text='8', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
        x='8': buttonClick(x))
  btn8.place(x=75, y=200, width=75, height=50)
  btn9 = tkinter.Button(root, text='9', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
        x='9': buttonClick(x))
  btn9.place(x=150, y=200, width=75, height=50)
  btnsub = tkinter.Button(root, text='-', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
        x='-': buttonClick(x))
  btnsub.place(x=225, y=200, width=75, height=50)
  # 第三行
  btn4 = tkinter.Button(root, text='4', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
        x='4': buttonClick(x))
  btn4.place(x=0, y=250, width=75, height=50)
  btn5 = tkinter.Button(root, text='5', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
        x='5': buttonClick(x))
  btn5.place(x=75, y=250, width=75, height=50)
  btn6 = tkinter.Button(root, text='6', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
        x='6': buttonClick(x))
  btn6.place(x=150, y=250, width=75, height=50)
  btnadd = tkinter.Button(root, text='×', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
        x='×': buttonClick(x))
  btnadd.place(x=225, y=250, width=75, height=50)
  # 第四行
  btn1 = tkinter.Button(root, text='1', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
        x='1': buttonClick(x))
  btn1.place(x=0, y=300, width=75, height=50)
  btn2 = tkinter.Button(root, text='2', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
        x='2': buttonClick(x))
  btn2.place(x=75, y=300, width=75, height=50)
  btn3 = tkinter.Button(root, text='3', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
        x='3': buttonClick(x))
  btn3.place(x=150, y=300, width=75, height=50)
  btnechu = tkinter.Button(root, text='÷', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
        x='÷': buttonClick(x))
  btnechu.place(x=225, y=300, width=75, height=50)
  # 第五行
  btnper = tkinter.Button(root, text='高级', font=('微软雅黑', 20), fg='orange', bd=0.5,
                        command=lambda x='高级': buttonClick(x))
  btnper.place(x=0, y=350, width=75, height=50)
  btn0 = tkinter.Button(root, text='0', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
        x='0': buttonClick(x))
  btn0.place(x=75, y=350, width=75, height=50)
  btnpoint = tkinter.Button(root, text='.', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
        x='.': buttonClick(x))
  btnpoint.place(x=150, y=350, width=75, height=50)
  btnequ = tkinter.Button(root, text='=', bg='orange', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5,
                        command=lambda x='=': buttonClick(x))
  btnequ.place(x=225, y=350, width=75, height=50)

  contentVar = tkinter.StringVar(root, '')
  contentEntry = tkinter.Entry(root, textvariable=contentVar, state='readonly', font=("Arial", 12))
  contentEntry.place(x=0, y=45, width=300, height=40)

  def buttonClick(btn):
    content = contentVar.get()
    if content.startswith('.'):  # 小数点前加0
        content = '0' + content
    if btn in '0123456789':
        content += btn
    elif btn == '.':
        lastPart = re.split(r'\+|-|\*|/', content)[-1]
        if '.' in lastPart:
            tkinter.messagebox.showerror('错误', 'Input Error')
            return
        else:
            content += btn

    elif btn == 'AC':
        content = ''
    elif btn == '=':
        try:
            for operat in content:
                if operat == '÷':
                    content = content.replace('÷', '/')
                elif operat == '×':
                    content = content.replace('×', '*')
            value = eval(content)
            content = str(round(value, 10))
        except:
            tkinter.messagebox.showerror('错误', 'VALUE ERROR')
            return
    elif btn in operators:
        if content.endswith(operators):
            tkinter.messagebox.showerror('错误', 'FORMAT ERROR')
            return
        content += btn
    elif btn == '^':
        n = content.split('.')
        if all(map(lambda x: x.isdigit(), n)):
            content = eval(content)*eval(content)
        else:
            tkinter.messagebox.showerror('错误', 'Input Error')
            return
    elif btn == '←':  # 如果按下的是退格‘’，则选取当前数字第一位到倒数第二位
        content = content[0:-1]
    elif btn == '高级':

        #contentEntry.place(x=0, y=45, width=300, height=40) # 重新绘制输出框
        # 运算符号按钮
        # 第一行
        btncsc = tkinter.Button(root, text='csc', font=('微软雅黑', 20), bg=('#96CDCD'), fg=('#4F4F4F'), bd=0.5,
                                command=lambda x='csc': buttonClick1(x))
        btncsc.place(x=0, y=85, width=60, height=45)
        btnrad = tkinter.Button(root, text='rad', font=('微软雅黑', 20), bg=('#96CDCD'), fg=('#4F4F4F'), bd=0.5,
                                command=lambda x='rad': buttonClick1(x))
        btnrad.place(x=60, y=85, width=60, height=45)
        btnsin = tkinter.Button(root, text='sin', font=('微软雅黑', 20), bg=('#96CDCD'), fg=('#4F4F4F'), bd=0.5,
                                command=lambda x='sin': buttonClick1(x))
        btnsin.place(x=120, y=85, width=60, height=45)
        btncos = tkinter.Button(root, text='cos', font=('微软雅黑', 20), bg=('#96CDCD'), fg=('#4F4F4F'), bd=0.5,
                                command=lambda x='cos': buttonClick1(x))
        btncos.place(x=180, y=85, width=60, height=45)
        btntan = tkinter.Button(root, text='tan', font=('微软雅黑', 20), bg=('#96CDCD'), fg=('#4F4F4F'), bd=0.5,
                                command=lambda x='tan': buttonClick1(x))
        btntan.place(x=240, y=85, width=60, height=45)
        # 第二行
        btnxsec = tkinter.Button(root, text='sec', font=('微软雅黑', 20), bg=('#96CDCD'), fg=('#4F4F4F'), bd=0.5,
                                  command=lambda x='sec': buttonClick1(x))
        btnxsec.place(x=0, y=130, width=60, height=45)
        btnlog = tkinter.Button(root, text='lg', font=('微软雅黑', 20), bg=('#96CDCD'), fg=('#4F4F4F'), bd=0.5,
                                command=lambda x='lg': buttonClick1(x))
        btnlog.place(x=60, y=130, width=60, height=45)
        btnln = tkinter.Button(root, text='ln', font=('微软雅黑', 20), bg=('#96CDCD'), fg=('#4F4F4F'), bd=0.5,
                                command=lambda x='ln': buttonClick1(x))
        btnln.place(x=120, y=130, width=60, height=45)
        btnleft = tkinter.Button(root, text='(', font=('微软雅黑', 20), bg=('#96CDCD'), fg=('#4F4F4F'), bd=0.5,
                                  command=lambda x='(': buttonClick1(x))
        btnleft.place(x=180, y=130, width=60, height=45)
        btnrigh = tkinter.Button(root, text=')', font=('微软雅黑', 20), bg=('#96CDCD'), fg=('#4F4F4F'), bd=0.5,
                                  command=lambda x=')': buttonClick1(x))
        btnrigh.place(x=240, y=130, width=60, height=45)
        # 第三行
        btnaxy = tkinter.Button(root, text='x^y', bd=0.5, font=('黑体', 20), bg=('#96CDCD'), command=lambda \
                x='x^y': buttonClick1(x))
        btnaxy.place(x=0, y=175, width=60, height=45)
        btnac.destroy()
        btnac1 = tkinter.Button(root, text='AC', bd=0.5, font=('黑体', 20), fg='orange', command=lambda \
                x='AC': buttonClick1(x))
        btnac1.place(x=60, y=175, width=60, height=45)
        btnback.destroy()
        btnback1 = tkinter.Button(root, text='←', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda \
                x='←': buttonClick1(x))
        btnback1.place(x=120, y=175, width=60, height=45)
        btndivi.destroy()
        btndivi1 = tkinter.Button(root, text='^', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda \
                x='^': buttonClick1(x))
        btndivi1.place(x=180, y=175, width=60, height=45)
        btnmul.destroy()
        btnmul1 = tkinter.Button(root, text='+', font=('微软雅黑', 20), fg="#4F4F4F", bd=0.5, command=lambda \
                x='+': buttonClick1(x))
        btnmul1.place(x=240, y=175, width=60, height=45)
        # 第四行
        btnx = tkinter.Button(root, text='X!', font=('微软雅黑', 20), bg=('#96CDCD'), fg=('#4F4F4F'), bd=0.5, command=lambda \
                  x='X!': buttonClick1(x))
        btnx.place(x=0, y=220, width=60, height=45)
        btn7.destroy()
        btn71 = tkinter.Button(root, text='7', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='7': buttonClick1(x))
        btn71.place(x=60, y=220, width=60, height=45)
        btn8.destroy()
        btn81 = tkinter.Button(root, text='8', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='8': buttonClick1(x))
        btn81.place(x=120, y=220, width=60, height=45)
        btn9.destroy()
        btn91 = tkinter.Button(root, text='9', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='9': buttonClick1(x))
        btn91.place(x=180, y=220, width=60, height=45)
        btnsub.destroy()
        btnsub1 = tkinter.Button(root, text='-', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='-': buttonClick1(x))
        btnsub1.place(x=240, y=220, width=60, height=45)
        # 第五行
        btn4x = tkinter.Button(root, text='1/X', font=('微软雅黑', 20), bg=('#96CDCD'), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='1/X': buttonClick1(x))
        btn4x.place(x=0, y=265, width=60, height=45)
        btn4.destroy()
        btn41 = tkinter.Button(root, text='4', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='4': buttonClick1(x))
        btn41.place(x=60, y=265, width=60, height=45)
        btn5.destroy()
        btn51 = tkinter.Button(root, text='5', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='5': buttonClick1(x))
        btn51.place(x=120, y=265, width=60, height=45)
        btn6.destroy()
        btn61 = tkinter.Button(root, text='6', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='6': buttonClick1(x))
        btn61.place(x=180, y=265, width=60, height=45)
        btnadd.destroy()
        btnadd1 = tkinter.Button(root, text='×', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='×': buttonClick1(x))
        btnadd1.place(x=240, y=265, width=60, height=45)
        # 第六行
        btnpi = tkinter.Button(root, text='π', font=('微软雅黑', 20), bg=('#96CDCD'), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='π': buttonClick1(x))
        btnpi.place(x=0, y=310, width=60, height=45)
        btnpi.flash()
        btn1.destroy()
        btn11 = tkinter.Button(root, text='1', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='1': buttonClick1(x))
        btn11.place(x=60, y=310, width=60, height=45)
        btn2.destroy()
        btn21 = tkinter.Button(root, text='2', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='2': buttonClick1(x))
        btn21.place(x=120, y=310, width=60, height=45)
        btn3.destroy()
        btn31 = tkinter.Button(root, text='3', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='3': buttonClick1(x))
        btn31.place(x=180, y=310, width=60, height=45)
        btnechu.destroy()
        btnechu1 = tkinter.Button(root, text='÷', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='÷': buttonClick1(x))
        btnechu1.place(x=240, y=310, width=60, height=45)
        # 第七行
        btnperr = tkinter.Button(root, text='低级', font=('微软雅黑', 20), fg='orange', bd=0.5,
                                command=lambda x='低级': buttonClick1(x))
        btnperr.place(x=0, y=355, width=60, height=45)
        btnper.destroy()
        btnper1 = tkinter.Button(root, text='e', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5,
                                command=lambda x='e': buttonClick1(x))
        btnper1.place(x=60, y=355, width=60, height=45)
        btn0.destroy()
        btn01 = tkinter.Button(root, text='0', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='0': buttonClick1(x))
        btn01.place(x=120, y=355, width=60, height=45)
        btnpoint.destroy()
        btnpoint1 = tkinter.Button(root, text='.', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='.': buttonClick1(x))
        btnpoint1.place(x=180, y=355, width=60, height=45)
        btnequ.destroy()
        btnequ1 = tkinter.Button(root, text='=', bg='orange', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5,
                                command=lambda x='=': buttonClick1(x))
        btnequ1.place(x=240, y=355, width=60, height=45)

        def buttonClick1(btn):
            content = contentVar.get()
            if content.startswith('.'):  # 小数点前加0
                content = '0' + content
            if btn in '0123456789()':
                content += btn
            elif btn == '.':
                lastPart = re.split(r'\+|-|\*|/', content)[-1]
                if '.' in lastPart:
                    tkinter.messagebox.showerror('错误', 'Input Error')
                    return
                else:
                    content += btn
            elif btn == '^':
                n = content.split('.')
                if all(map(lambda x: x.isdigit(), n)):
                    content = eval(content) * eval(content)
                else:
                    tkinter.messagebox.showerror('错误', 'Input Error')
                    return
            elif btn == 'AC':
                content = ''
            elif btn == '=':
                try:
                    for operat in content:
                        if operat == '÷':
                            content = content.replace('÷', '/')
                        elif operat == '×':
                            content = content.replace('×', '*')
                        elif operat == '^':
                            content = content.replace('^', '**')
                    strsin = r'sin\(\d+\)|sin\(\-?\d+\.\d+\)'
                    if 'sin' in content:
                        m = re.search(strsin, content)
                        if m is not None:
                            exchange = m.group()
                            exchange1 = exchange
                            if '.' in exchange:
                                exchange = re.search("\-?\d+\.\d+", exchange)
                                value = exchange.group()
                                value = str(sin_t(float(value)))
                                content = content.replace(exchange1, value)
                            else:
                                exchange = re.search("\-?\d+", exchange)
                                value = exchange.group()
                                value = str(sin_t(float(value)))
                                content = content.replace(exchange1, value)
                    strcos = r'cos\(\d+\)|cos\(\-?\d+\.\d+\)'
                    if 'cos' in content:
                        m = re.search(strcos, content)
                        if m is not None:
                            exchange = m.group()
                            exchange1 = exchange
                            if '.' in exchange:
                                exchange = re.search("\-?\d+\.\d+", exchange)
                                value = exchange.group()
                                value = str(cos_t(float(value)))
                                content = content.replace(exchange1, value)
                            else:
                                exchange = re.search("\-?\d+", exchange)
                                value = exchange.group()
                                value = str(cos_t(float(value)))
                                content = content.replace(exchange1, value)
                    strtan = r'tan\(\d+\)|tan\(\-?\d+\.\d+\)'
                    if 'tan' in content:
                        m = re.search(strtan, content)
                        if m is not None:
                            exchange = m.group()
                            exchange1 = exchange
                            if '.' in exchange:
                                exchange = re.search("\-?\d+\.\d+", exchange)
                                value = exchange.group()
                                value = str(tan_t(float(value)))
                                content = content.replace(exchange1, value)
                            else:
                                exchange = re.search("\-?\d+", exchange)
                                value = exchange.group()
                                value = str(tan_t(float(value)))
                                content = content.replace(exchange1, value)
                    strsec = r'sec\(\-?\d+\)|sec\(\-?\d+\.\d+\)'
                    if 'sec' in content:
                        m = re.search(strsec, content)
                        if m is not None:
                            exchange = m.group()
                            exchange1 = exchange
                            if '.' in exchange:
                                exchange = re.search("\-?\d+\.\d+", exchange)
                                value = exchange.group()
                                value = str(sec_t(float(value)))
                                content = content.replace(exchange1, value)
                            else:
                                exchange = re.search("\-?\d+", exchange)
                                value = exchange.group()
                                value = str(sec_t(float(value)))
                                content = content.replace(exchange1, value)
                    strcsc = r'csc\(\d+\)'
                    if 'csc' in content:
                        m = re.search(strcsc, content)
                        if m is not None:
                            exchange = m.group()
                            exchange1 = exchange
                            if '.' in exchange:
                                exchange = re.search("\-?\d+\.\d+", exchange)
                                value = exchange.group()
                                value = str(csc_t(float(value)))
                                content = content.replace(exchange1, value)
                            else:
                                exchange = re.search("\-?\d+", exchange)
                                value = exchange.group()
                                value = str(csc_t(float(value)))
                                content = content.replace(exchange1, value)
                    strlg = r'lg\(\-?\d+\)|lg\(\-?\d+\.\d+\)'
                    if 'lg' in content:
                        m = re.search(strlg, content)
                        if m is not None:
                            exchange = m.group()
                            exchange1 = exchange
                            if '.' in exchange:
                                exchange = re.search("\-?\d+\.\d+", exchange)
                                value = exchange.group()
                                if float(value) <= 0:
                                    tkinter.messagebox.showerror('错误', 'FORMAT ERROR')
                                else:
                                    value = str(lg_t(float(value)))
                                    content = content.replace(exchange1, value)
                            else:
                                exchange = re.search("\-?\d+", exchange)
                                value = exchange.group()
                                if int(value)<=0 :
                                    tkinter.messagebox.showerror('错误', 'FORMAT ERROR')
                                else:
                                    value = str(lg_t(float(value)))
                                    content = content.replace(exchange1, value)
                    strln = r'ln\(\-?\d+\)|ln\(\-?\d+\.\d+\)'
                    if 'ln' in content:
                        m = re.search(strln, content)
                        if m is not None:
                            exchange = m.group()
                            exchange1 = exchange
                            if '.' in exchange:
                                exchange = re.search("\-?\d+\.\d+", exchange)
                                value = exchange.group()
                                if float(value) <= 0:
                                    tkinter.messagebox.showerror('错误', 'FORMAT ERROR')
                                else:
                                    value = str(ln_t(float(value)))
                                    content = content.replace(exchange1, value)
                            else:
                                exchange = re.search("\-?\d+", exchange)
                                value = exchange.group()
                                if int(value) <= 0:
                                    tkinter.messagebox.showerror('错误', 'FORMAT ERROR')
                                else:
                                    value = str(ln_t(float(value)))
                                    content = content.replace(exchange1, value)
                    value = eval(content)
                    content = str(round(value, 10))
                except ZeroDivisionError:
                    tkinter.messagebox.showerror('错误', 'VALUE ERROR')
                    return
            elif btn in operators:
                if content.endswith(operators):
                    tkinter.messagebox.showerror('错误', 'FORMAT ERROR')
                    return
                content += btn
            elif btn == 'e':
                content = 2.7182818284
            elif btn == 'π':
                content = 3.1415926535
            elif btn == '1/X':
                content = reciprocal(float(content))
            elif btn == 'X!':
                content = factorial(int(content))
            elif btn == 'x^y':
                content += '^'
            elif btn == 'sin':
                content += 'sin('
            elif btn == 'cos':
                content += 'cos('
            elif btn == 'tan':
                content += 'tan('
            elif btn == 'sec':
                content += 'sec('
            elif btn == 'csc':
                content += 'csc('
            elif btn == 'lg':
                content += 'lg('
            elif btn == 'ln':
                content += 'ln('
            elif btn == '←':  # 如果按下的是退格‘’，则选取当前数字第一位到倒数第二位
                content = content[0:-1]        

            elif btn == '低级':
                #contentEntry.place(x=0, y=110, width=300, height=40)
                #第一行
                btncsc.destroy()
                btnrad.destroy()
                btnsin.destroy()
                btncos.destroy()
                btntan.destroy()
                # 第二行
                btnxsec.destroy()
                btnlog.destroy()
                btnln.destroy()
                btnleft.destroy()
                btnrigh.destroy()
                # 第三行
                btnaxy.destroy()
                btnac1.destroy()
                btnback1.destroy()
                btndivi1.destroy()
                btnmul1.destroy()
                # 第四行
                btnx.destroy()
                btn71.destroy()
                btn81.destroy()
                btn91.destroy()
                btnsub1.destroy()
                # 第五行
                btn4x.destroy()
                btn41.destroy()
                btn51.destroy()
                btn61.destroy()
                btnadd1.destroy()
                # 第六行
                btnpi.destroy()
                btn11.destroy()
                btn21.destroy()
                btn31.destroy()
                btnechu1.destroy()
                # 第七行
                btnperr.destroy()
                btnper1.destroy()
                btn01.destroy()
                btnpoint1.destroy()
                btnequ1.destroy()
                # 第一行
                btnac = tkinter.Button(root, text='AC', bd=0.5, font=('黑体', 20), fg='orange', command=lambda \
                        x='AC': buttonClick(x))
                btnac.flash()
                btnac.place(x=0, y=150, width=75, height=50)
                btnback = tkinter.Button(root, text='←', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda \
                        x='←': buttonClick(x))
                btnback.place(x=75, y=150, width=75, height=50)
                btndivi = tkinter.Button(root, text='^', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda \
                        x='^': buttonClick(x))
                btndivi.place(x=150, y=150, width=75, height=50)
                btnmul = tkinter.Button(root, text='+', font=('微软雅黑', 20), fg="#4F4F4F", bd=0.5, command=lambda \
                        x='+': buttonClick(x))
                btnmul.place(x=225, y=150, width=75, height=50)
                # 第二行
                btn7 = tkinter.Button(root, text='7', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                        x='7': buttonClick(x))
                btn7.place(x=0, y=200, width=75, height=50)
                btn8 = tkinter.Button(root, text='8', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                        x='8': buttonClick(x))
                btn8.place(x=75, y=200, width=75, height=50)
                btn9 = tkinter.Button(root, text='9', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                        x='9': buttonClick(x))
                btn9.place(x=150, y=200, width=75, height=50)
                btnsub = tkinter.Button(root, text='-', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                        x='-': buttonClick(x))
                btnsub.place(x=225, y=200, width=75, height=50)
                # 第三行
                btn4 = tkinter.Button(root, text='4', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                        x='4': buttonClick(x))
                btn4.place(x=0, y=250, width=75, height=50)
                btn5 = tkinter.Button(root, text='5', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                        x='5': buttonClick(x))
                btn5.place(x=75, y=250, width=75, height=50)
                btn6 = tkinter.Button(root, text='6', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                        x='6': buttonClick(x))
                btn6.place(x=150, y=250, width=75, height=50)
                btnadd = tkinter.Button(root, text='×', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                        x='×': buttonClick(x))
                btnadd.place(x=225, y=250, width=75, height=50)
                # 第四行
                btn1 = tkinter.Button(root, text='1', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                        x='1': buttonClick(x))
                btn1.place(x=0, y=300, width=75, height=50)
                btn2 = tkinter.Button(root, text='2', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                        x='2': buttonClick(x))
                btn2.place(x=75, y=300, width=75, height=50)
                btn3 = tkinter.Button(root, text='3', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                        x='3': buttonClick(x))
                btn3.place(x=150, y=300, width=75, height=50)
                btnechu = tkinter.Button(root, text='÷', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                        x='÷': buttonClick(x))
                btnechu.place(x=225, y=300, width=75, height=50)
                # 第五行
                btnper = tkinter.Button(root, text='高级', font=('微软雅黑', 20), fg='orange', bd=0.5,
                                        command=lambda x='高级': buttonClick(x))
                btnper.place(x=0, y=350, width=75, height=50)
                btn0 = tkinter.Button(root, text='0', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                        x='0': buttonClick(x))
                btn0.place(x=75, y=350, width=75, height=50)
                btnpoint = tkinter.Button(root, text='.', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                        x='.': buttonClick(x))
                btnpoint.place(x=150, y=350, width=75, height=50)
                btnequ = tkinter.Button(root, text='=', bg='orange', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5,
                                        command=lambda x='=': buttonClick(x))
                btnequ.place(x=225, y=350, width=75, height=50)
            contentVar.set(content)
    contentVar.set(content)

  operators = ('÷', '×', '-', '+', '=', '.')
  root.mainloop()

window.mainloop()