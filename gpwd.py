# coding=UTF-8

from ast import Delete
import subprocess
import time
from tkinter import ACTIVE, END, Listbox, Tk, TkVersion
from tkinter import ttk
import tkinter as tk
import os.path
import socket
from tkinter import Toplevel
from tkinter import PhotoImage
from tracemalloc import start

import darkdetect
import sv_ttk
import getpass
import platform

nomeapp = 'Gerenciador de Password' #nome que será exibido na janela
versao = 'v1.1.6' #Versão do Programa

list_users = []
list_users3 = []

setores = []

senhapadrao = ''

logo = 'logo_b' #logo padrão (caso não seja possível detectar o tema)

if (os.path.exists('senhapadrao.txt')==True): # se o arquivo.txt da senha existir...
    with open('senhapadrao.txt', 'r') as pd: # lendo o arquivo txt da senha
        senhapadrao = pd.read() # armazenando na variável senhapadrao
else:
    with open('senhapadrao.txt', 'w') as pd:
        pd.write('senhapadrao')
        senhapadrao = 'senhapadrao'

#arquivo de Setores

if (os.path.exists('setores.txt')==True): # se o arquivo.txt da senha existir...
    with open('setores.txt', 'r') as setortxt: # lendo o arquivo txt da senha
        setores = setortxt.read().strip().split(',') # armazenando na variável senhapadrao
else:
    with open('setores.txt', 'w') as setortxt:
        setortxt.write('setor1,setor2,setor3,setor4,setor5,setor6')
        setores = 'setor1,setor2,setor3,setor4,setor5,setor6'.split(',')

if darkdetect.isDark(): #se windows em dark mode...
    tema = 'dark' #tema do programa dark
    logo = 'logo_p.png' #logo dark 
else:  #se tema windows light
    tema = 'light' #tema claro
    logo = 'logo_b.png' #logo clara

def detectDark():
    if darkdetect.isDark(): #se windows em dark mode...
        tema = 'dark' #tema do programa dark
        logo = 'logo_p.png' #logo dark 
        sv_ttk.set_theme(tema)
        img = PhotoImage(file=logo)
    else:  #se tema windows light
        tema = 'light' #tema claro
        logo = 'logo_b.png' #logo clara
        sv_ttk.set_theme(tema)
        img = PhotoImage(file=logo)

entrys = {}

user = getpass.getuser() #usuário do computador que executa o programa
pc = platform.node() #nome-pc ou hostname

#net user /domain #buscar todos os usuários do domínio

def localizar(usuario):
    usuario = usuario.strip()
    output = subprocess.check_output('net user /domain', universal_newlines=True,shell=True,stderr=subprocess.STDOUT, encoding='cp850')
    
    for item in tree_view.get_children():
        tree_view.delete(item)

    #user = output[output.find(usuario):output.find(usuario)+output.find(' ', 15)].strip()
    user = output[206:].replace('\n', '').replace('  ', ' ').replace('   ', ' ').replace('    ', ' ').replace('     ', ' ')
    list_users = user.strip().split(' ')
    
    #entry.delete(0, 'end')
    #entry.insert(0, 'Localizando')
    
    janelaLoc = Toplevel(janela)
    janelaLoc.title('Localizar')
    janelaLoc.iconbitmap('icon.ico')

    janelaLoc_width = 400
    janelaLoc_height = 260

    device_width = janelaLoc.winfo_screenwidth()/2
    device_height = janelaLoc.winfo_screenheight()/2

    device_width = device_width - (janelaLoc_width/2)
    device_height = device_height - (janelaLoc_height/2)

    device_width = int(device_width)
    device_height = int(device_height)

    janelaLoc.geometry(str(janelaLoc_width)+'x'+str(janelaLoc_height)+'+'+str(device_width)+'+'+str(device_height))
    janelaLoc.resizable(0,0)
    
    frame2 = ttk.Frame(janelaLoc)
    frame2.place(relx=0.5,rely=0.45,anchor='center')
    
    entrys['Entry_1'] = ttk.Button(janelaLoc, text='')
    entrys['Entry_2'] = ttk.Button(janelaLoc, text='')
    entrys['Entry_3'] = ttk.Button(janelaLoc, text='')
    entrys['Entry_4'] = ttk.Button(janelaLoc, text='')
    entrys['Entry_5'] = ttk.Button(janelaLoc, text='')
    entrys['Entry_6'] = ttk.Button(janelaLoc, text='')
    entrys['Entry_7'] = ttk.Button(janelaLoc, text='')
    entrys['Entry_8'] = ttk.Button(janelaLoc, text='')
    entrys['Entry_9'] = ttk.Button(janelaLoc, text='')
    entrys['Entry_10'] = ttk.Button(janelaLoc, text='')
    entrys['Entry_11'] = ttk.Button(janelaLoc, text='')
    entrys['Entry_12'] = ttk.Button(janelaLoc, text='')
    entrys['Entry_13'] = ttk.Button(janelaLoc, text='')
    entrys['Entry_14'] = ttk.Button(janelaLoc, text='')
    entrys['Entry_15'] = ttk.Button(janelaLoc, text='')
    
    #button = ttk.Button(frame2, text='OK', command=lambda:janelaLoc.destroy()).grid(column=0, row=1, pady=5)
    
    try:
        while True:
            list_users.remove('')
    except ValueError:
        pass
    
    global i
    global y
    i = 0
    y = 0
    encontrou = False
    
    for list_user in list_users:
        if (i<20):
            if (usuario in list_user or str(usuario).capitalize() in list_user or str(usuario).lower() in list_user):
                i+=1
                y+=1
                
                entrys['Entry_'+str(i)] = ttk.Button(janelaLoc,text=list_user,style="Accent.TButton",command=lambda i=i:escolher(entrys['Entry_'+str(i)]['text']))
                entrys['Entry_'+str(i)].bind("<Return>", (lambda event, i=i: escolher(entrys['Entry_'+str(i)]['text'])))
                encontrou = True
                
                def escolher(text):
                    janelaLoc.destroy()
                    entry.delete(0, 'end')
                    entry.insert(0, text)
                    list_dados = []

                    output2 = subprocess.check_output('net user /domain '+text+' ',universal_newlines=True,shell=True,stderr=subprocess.STDOUT, encoding='cp850')

                    nomecompleto = output2[output2.find('Nome completo')+13:output2.find('Coment')].strip()
                    contaativa = output2[output2.find('Conta ativa')+13:output2.find('Conta expira em')].strip()
                    logon = output2[output2.find('ltimo logon')+13:output2.find('Hor')].strip()
                    grupo = ''
                    for setor in setores:
                        if(str(setor) in output2):
                            grupo = str(setor)
                            break
                    defsenha = output2[output2.find('ltima defini')+24:output2.find('A senha expira')].strip()
                    expira = output2[output2.find('A senha expira')+15:output2.find('Altera')].strip()

                    for item in tree_view.get_children():
                        tree_view.delete(item)
                    tree_view.insert("",'end',iid=1, values=(nomecompleto,contaativa,logon,grupo,defsenha,expira))  # type: ignore
                    
                    #print(nomecompleto)
                    #print(contaativa)
                    #print(logon)
                    #print(grupo)
                    #print(defsenha)
                    #print(expira)

                if usuario=='':
                    frame3 = ttk.Frame(janelaLoc)
                    frame3.place(relx=0.5,rely=0.45,anchor='center')
                    
                    labelLoc = ttk.Label(frame3, text='Preencha o campo usuário', font='Arial 10').grid(column=0, row=0)
                    buttonLoc = ttk.Button(frame3, text='OK', command=lambda:janelaLoc.destroy()).grid(column=0, row=1, pady=5)
                    break
                
                if(i==6 or i==11):
                    y=1
                
                if(i<=5):
                    
                    entrys['Entry_'+str(i)].place(relx=0.2,rely=(y+0.2)/7+0.05,anchor='center')
                elif(i>=6 and i<=10):
                    entrys['Entry_'+str(i)].place(relx=0.5,rely=(y+0.2)/7+0.05,anchor='center')
                elif(i>10):
                    entrys['Entry_'+str(i)].place(relx=0.8,rely=(y+0.2)/7+0.05,anchor='center')
                
    if encontrou==False:
        frame3 = ttk.Frame(janelaLoc)
        frame3.place(relx=0.5,rely=0.45,anchor='center')
        labelLoc = ttk.Label(frame3, text='Não foram encontrados usuários', font='Arial 10').grid(column=0, row=0)
        buttonLoc = ttk.Button(frame3, text='OK', style="Accent.TButton", command=lambda:janelaLoc.destroy()).grid(column=0, row=1, pady=15)
    
    janelaLoc.bind("<Return>", (lambda event: janelaLoc.destroy()))
    janelaLoc.bind("<Escape>", (lambda event: janelaLoc.destroy()))
    
    #sv_ttk.set_theme(tema)
    janelaLoc.wm_attributes("-topmost", 1)
    janelaLoc.after(1, lambda: janelaLoc.focus_force())

def alert(mensagem):
    
    janelaAlert = Toplevel(janela)
    janelaAlert.title(mensagem)
    janelaAlert.iconbitmap('icon.ico')

    janelaAlert_width = 260
    janelaAlert_height = 160

    device_width = janelaAlert.winfo_screenwidth()/2
    device_height = janelaAlert.winfo_screenheight()/2

    device_width = device_width - (janelaAlert_width/2)
    device_height = device_height - (janelaAlert_height/2)

    device_width = int(device_width)
    device_height = int(device_height)
    
    janelaAlert.geometry(str(janelaAlert_width)+'x'+str(janelaAlert_height)+'+'+str(device_width)+'+'+str(device_height))
    janelaAlert.resizable(0,0)  # type: ignore
    
    frame2 = ttk.Frame(janelaAlert)
    frame2.place(relx=0.5,rely=0.45,anchor='center')

    #sv_ttk.set_theme(tema)
    janelaAlert.wm_attributes("-topmost", 1)
    janelaAlert.after(1, lambda: janelaAlert.focus_force())
    
    labelAlert = ttk.Label(frame2, text=mensagem, font='Arial 10')
    labelAlert.grid(column=0, row=0)
    buttonAlert = ttk.Button(frame2, text='OK', style="Accent.TButton", command=lambda: janelaAlert.destroy())
    janelaAlert.bind("<Return>", (lambda event: janelaAlert.destroy()))
    janelaAlert.bind("<Escape>", (lambda event: janelaAlert.destroy()))
    buttonAlert.grid(column=0, row=1, pady=15)

def aviso(mensagem, usuario2):
    
    usuario2 = usuario2.strip()
    
    output2 = subprocess.check_output('net user /domain', universal_newlines=True,shell=True)
    user2 = output2[206:].replace('\n', '').replace('  ', ' ').replace('   ', ' ').replace('    ', ' ').replace('     ', ' ')
    list_users2 = user2.strip().split(' ')
    try:
        while True:
            list_users2.remove('')
    except ValueError:
        pass
    
    r=0
    
    for list_user2 in list_users2:
        if usuario2 == list_user2:
            r+=1
    
    if (r==0):
        mensagem = 'Usuário não encontrado!'
    
    janelaAviso = Toplevel(janela)
    janelaAviso.title(mensagem)
    janelaAviso.iconbitmap('icon.ico')

    janelaAviso_width = 200
    janelaAviso_height = 140

    device_width = janelaAviso.winfo_screenwidth()/2
    device_height = janelaAviso.winfo_screenheight()/2

    device_width = device_width - (janelaAviso_width/2)
    device_height = device_height - (janelaAviso_height/2)

    device_width = int(device_width)
    device_height = int(device_height)
    
    janelaAviso.geometry(str(janelaAviso_width)+'x'+str(janelaAviso_height)+'+'+str(device_width)+'+'+str(device_height))
    janelaAviso.resizable(0,0)  # type: ignore
    
    frame2 = ttk.Frame(janelaAviso)
    frame2.place(relx=0.5,rely=0.45,anchor='center')

    #sv_ttk.set_theme(tema)
    janelaAviso.wm_attributes("-topmost", 1)
    janelaAviso.after(1, lambda: janelaAviso.focus_force())
    
    labelAviso = ttk.Label(frame2, text=mensagem, font='Arial 10')
    labelAviso.grid(column=0, row=0)
    buttonAviso = ttk.Button(frame2, text='OK', style="Accent.TButton", command=lambda: janelaAviso.destroy())
    janelaAviso.bind("<Return>", (lambda event: janelaAviso.destroy()))
    janelaAviso.bind("<Escape>", (lambda event: janelaAviso.destroy()))
    buttonAviso.grid(column=0, row=1, pady=15)

def resetSenha(usuario):
    usuario = usuario.strip()
    try:
        subprocess.Popen('net user '+usuario+' '+senhapadrao+' /domain /logonpasswordChg:yes /active:yes', shell=True)
        aviso('Senha Resetada!', usuario)
    except:
        alert('Ocorreu algum erro! Certifique de estar no domínio/grupo e ter permissões administrativas.')
    
def unlockSenha(usuario):
    usuario = usuario.strip()
    try:
        subprocess.Popen('net user '+usuario+' /domain /active:yes', shell=True)
        aviso('Usuário Desbloqueado!', usuario)
    except:
        alert('Ocorreu algum erro! Certifique de estar no domínio/grupo e ter permissões administrativas.')

usuario = any

janela = Tk()
list_search = Listbox(janela, width=50, height=7,selectmode=tk.EXTENDED)
list_search2 = Listbox(janela, width=50, height=4,selectmode=tk.EXTENDED)

def atualizaSearch(usuario3):
    usuario3 = str(usuario3).strip()
    i=0
    if(len(usuario3)>=2):
        output3 = subprocess.check_output('net user /domain',universal_newlines=True,shell=True)
        user3 = output3[206:].replace('\n', '').replace('  ', ' ').replace('   ', ' ').replace('    ', ' ').replace('     ', ' ')
        list_users3 = user3.strip().split(' ')
        try:
            while True:
                list_users3.remove('')
        except ValueError:
            pass
        list_search.delete(0, END)
        for list_user3 in list_users3:
            if (i<30):
                if (usuario3 in list_user3 or usuario3.upper() in list_user3 or usuario3.lower() in list_user3):
                    list_search.insert(END, list_user3)

    else:
        
        list_search.delete(0, END)
        for item in tree_view.get_children():
            tree_view.delete(item)

def scan(addr):
    s = socket.socket()
    s.bind(('0.0.0.0',0))    
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    generated_port = sock.getsockname()[1]
    result = sock.connect_ex((addr, generated_port))
    if result == 0 :
        return 1
    else :
        return 0

def localizarPc(pc):
    pc = pc.strip()
    output = subprocess.check_output('arp -a', universal_newlines=True,shell=True, encoding='cp850')
    i=0
    cont=0
    #user = output[output.find(usuario):output.find(usuario)+output.find(' ', 15)].strip()
    if(len(pc)>=3):
        ips = output[84:].replace('\n', '').replace('  ', ' ').replace('   ', ' ').replace('    ', ' ').replace('     ', ' ')
        ips.replace('\n', '').replace('dinâmico', '').replace('ff-ff-ff-ff-ff-ff', '').replace('estático', '').replace('IP', '').replace('---', '')
        list_ips = ips.strip().split(' ')

        try:
            while True:
                list_ips.remove('')
        except ValueError:
            pass

        try:
            while True:
                list_ips.remove('dinâmico')
        except ValueError:
            pass

        try:
            while True:
                list_ips.remove('ff-ff-ff-ff-ff-ff')
        except ValueError:
            pass

        try:
            while True:
                list_ips.remove('estático')
        except ValueError:
            pass

        for ip in list_ips:
            if '-' in ip:
                list_ips.remove(ip)

        list_search2.delete(0, END)
        for ip in list_ips:
                if pc in ip:
                    #if(scan(ip)):
                    list_search2.insert(END, ip)
    else:
        
        list_search2.delete(0, END)
        for item in tree_view2.get_children():
            tree_view2.delete(item)

def buscarPc():
    text = entryCota.get().strip()

    namesearch = 0

    letras = []
    letras.append('a')
    letras.append('b')
    letras.append('c')
    letras.append('d')
    letras.append('e')
    letras.append('f')
    letras.append('g')
    letras.append('h')
    letras.append('i')
    letras.append('j')
    letras.append('k')
    letras.append('l')
    letras.append('m')
    letras.append('n')
    letras.append('o')
    letras.append('p')
    letras.append('q')
    letras.append('r')
    letras.append('s')
    letras.append('t')
    letras.append('u')
    letras.append('v')
    letras.append('x')
    letras.append('y')
    letras.append('z')

    for item in tree_view2.get_children():
        tree_view2.delete(item)

    for letra in letras:
        if(letra in text or letra.title() in text):
            namesearch = 1

    if (namesearch==0):
        try:
            output = socket.gethostbyaddr(text)
            outputProceesed = str(output).split("'")[1::2]
            hostname = outputProceesed[0]
            host = outputProceesed[1]
            output_user = subprocess.check_output('qwinsta /server:'+text,universal_newlines=True,shell=True,encoding='cp850')
        except:
            alert('Host não encontrado!')

    else:
        try:
            output = socket.gethostbyname(text)            
            hostname = text
            host = output
            output_user = subprocess.check_output('qwinsta /server:'+host,universal_newlines=True,shell=True,encoding='cp850')
        except:
            alert('Host não encontrado!')
        
    user_log = output_user[output_user.find('console')+7:output_user.find('Ativo')-4].strip()
    
    
    tree_view2.insert("",'end',iid=1, values=(hostname, host, user_log))  # type: ignore


def escolheList(e):
    if list_search.curselection() != ():
        entry.delete(0, END)
        entry.insert(0, list_search.get(list_search.curselection()))
    for item in tree_view.get_children():
        tree_view.delete(item)

    text = entry.get()
    output4 = subprocess.check_output('net user /domain '+text+' ',universal_newlines=True,shell=True,stderr=subprocess.STDOUT, encoding='cp850')

    nomecompleto = output4[output4.find('Nome completo')+13:output4.find('Coment')].strip()
    contaativa = output4[output4.find('Conta ativa')+13:output4.find('Conta expira em')].strip()
    logon = output4[output4.find('ltimo logon')+13:output4.find('Hor')].strip()
    grupo = ''
    for setor in setores:
        if(str(setor) in output4):
            grupo = str(setor)
            break
    defsenha = output4[output4.find('ltima defini')+24:output4.find('A senha expira')].strip()
    expira = output4[output4.find('A senha expira')+15:output4.find('Altera')].strip()

    if list_search.curselection() != ():
        tree_view.insert("",'end',iid=1, values=(nomecompleto,contaativa,logon,grupo,defsenha,expira))  # type: ignore

def escolheList2(e):
    if list_search2.curselection() != ():
        entryCota.delete(0, END)
        entryCota.insert(0, list_search2.get(list_search2.curselection()))

def listBaixo():
    list_search.focus_set()
    list_search.select_set(0)
    escolheList(entry.get())

janela.title(nomeapp+' '+versao)
janela.iconbitmap('icon.ico')

janela_width = 790
janela_height = 770

device_width = janela.winfo_screenwidth()/2
device_height = janela.winfo_screenheight()/2

device_width = device_width - (janela_width/2)
device_height = device_height - (janela_height/2)

device_width = int(device_width)
device_height = int(device_height)

janela.geometry(str(janela_width)+'x'+str(janela_height)+'+'+str(device_width)+'+'+str(device_height))

janela.resizable(True,True)
#janela['bg'] = '#f8f8f8'

frame = ttk.Frame(janela, padding=0)
frame.place(relx=0.515,rely=0.33,anchor='center')

frameCota = ttk.Frame(janela, padding=0)
frameCota.place(relx=0.5,rely=0.73,anchor='center')

frameBt = ttk.Frame(janela, padding=0)
frameBt.place(relx=0.5,rely=0.66,anchor='center')

frame_info = ttk.Frame(janela, padding=15)

img = PhotoImage(file=logo)
label_img = ttk.Label(janela, image=img,borderwidth=0,border=0)

labeluser = ttk.Label(frame_info,text='Usuário: '+user+' | ').grid(column=0,row=0)
labelpc = ttk.Label(frame_info ,text='HostName: '+pc).grid(column=1,row=0)

frame_info.place(relx=0.5,rely=0.97,anchor='center')
label_img.place(relx = 0.5,rely = 0.13,anchor = 'center')

label = ttk.Label(frame, text='Digite o usuário do domínio:',font= ('Arial 14')).grid(column=0, columnspan=2, row=1, pady=3)

entry = ttk.Entry(frame, textvariable=usuario, width=25, font='Arial 14')  # type: ignore
entry.grid(column=0, columnspan=2, row=2, pady=15, ipadx=3)
entry.bind("<KeyRelease>", (lambda event: atualizaSearch(entry.get())))
entry.bind("<Return>", (lambda event: localizar(entry.get())))
entry.bind('<Right>', (lambda event: localizar(entry.get())))

entryCota = ttk.Entry(frameCota, width=17, font='Arial 14')
entryCota.grid(column=0, columnspan=2, row=2, pady=15, ipadx=3)
entryCota.bind("<Return>", (lambda event: localizarPc(entryCota.get())))

buttonCota = ttk.Button(frameCota,text='Pesquisar Host',style="Accent.TButton",
command=lambda: buscarPc())
buttonCota.grid(column=2, row=2, padx=5) #botão lupa
buttonCota.bind("<Return>", (lambda event: buscarPc()))
entryCota.bind("<KeyRelease>", (lambda event: localizarPc(entryCota.get())))
entryCota.bind("<Return>", (lambda event: buscarPc()))

buttonL = ttk.Button(frame,width=2,text='➜',style="Accent.TButton", 
command=lambda: localizar(entry.get()))
buttonL.grid(column=2, row=2, padx=5) #botão lupa
buttonL.bind("<Return>", (lambda event: localizar(entry.get())))

button = ttk.Button(frameBt,width=18,text='Resetar Senha',command=lambda: resetSenha(entry.get()))
button.bind("<Return>", (lambda event: resetSenha(entry.get())))
button.grid(column=0, row=5,pady=1,ipady=3, padx=3) #botão reset

button2 = ttk.Button(frameBt,width=18,text='Desbloquear Usuário', command=lambda: unlockSenha(entry.get()))
button2.bind("<Return>", (lambda event: unlockSenha(entry.get())))
button2.grid(column=1, row=5,pady=1,ipady=3, padx=3) #botão unlock

switch = ttk.Checkbutton(style="Switch.TCheckbutton")

#ListBox

def focalizarEntry():
    indexSearch = list_search.curselection()[0]
    if(indexSearch==0):
        entry.focus_set()

list_search.place(relx = 0.503,rely = 0.47,anchor = 'center')
list_search.bind('<<ListboxSelect>>', escolheList)
list_search.bind('<Right>', (lambda event: localizar(entry.get())))
list_search.bind('<Up>', (lambda event: focalizarEntry()))

#ListBox 2

list_search2.place(relx = 0.503,rely = 0.82,anchor = 'center')
list_search2.bind('<<ListboxSelect>>', escolheList2)

#Tabela Info Usuário
list_columns = ['nome', 'ativo', 'logon', 'grupo', 'defsenha', 'expira']
tree_view = ttk.Treeview(janela, show='headings', columns=list_columns, height='1', selectmode="browse")  # type: ignore

tree_view.heading('nome', text='Nome Completo')
tree_view.heading('ativo', text='Ativo')
tree_view.heading('logon', text='Último Logon')
tree_view.heading('grupo', text='Grupo')
tree_view.heading('defsenha', text='Última Definição de Senha')
tree_view.heading('expira', text='Senha Expira')

tree_view.column('nome', width=200)
tree_view.column('ativo', width=50)
tree_view.column('logon', width=110)
tree_view.column('grupo', width=85)
tree_view.column('defsenha', width=170)
tree_view.column('expira', width=110)

tree_view.place(relx=0.5,rely=0.59,anchor='center')
#tree_view.bind('<<TreeviewSelect>>', def():)

#Tabela Info Host
list_columns = ['hostname', 'ip', 'user']
tree_view2 = ttk.Treeview(janela, show='headings', columns=list_columns, height='1')  # type: ignore

tree_view2.heading('hostname', text='Host Name')
tree_view2.heading('ip', text='Endereço IP')
tree_view2.heading('user', text='Usuário Logado')

tree_view2.column('hostname', width=150)
tree_view2.column('ip', width=150)
tree_view2.column('user', width=150)

tree_view2.place(relx=0.5,rely=0.91,anchor='center')

janela.bind("<Escape>", (lambda event: janela.destroy()))
janela.bind('<FocusIn>', (lambda event: detectDark()))
entry.bind('<Down>', (lambda event: listBaixo()))

#janela.tk.call("source", "azure.tcl")
sv_ttk.set_theme(tema)

#janela.after(1, lambda: janela.focus_force())
#janela.wm_attributes("-topmost", 1)
entry.focus()
janela.mainloop()

