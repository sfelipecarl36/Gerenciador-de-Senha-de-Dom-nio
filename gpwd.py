# coding=UTF-8
# Felipe Carlos Rabelo da Silva

from ast import Delete
import subprocess
from tkinter import ACTIVE, END, Listbox, Tk, TkVersion
from tkinter import ttk
import tkinter as tk
import os.path
from tkinter import Toplevel
from tkinter import PhotoImage
from tracemalloc import start

import darkdetect
import sv_ttk
import getpass
import platform

nomeapp = 'Gerenciador de Password' #nome que será exibido na janela
versao = 'v1.1.0' #Versão do Programa

list_users = []
list_users3 = []

senhapadrao = ''

logo = 'logo_b' #logo padrão (caso não seja possível detectar o tema)

if (os.path.exists('senhapadrao.txt')==True): # se o arquivo.txt da senha existir...
    with open('senhapadrao.txt', 'r') as pd: # lendo o arquivo txt da senha
        senhapadrao = pd.read() # armazenando na variável senhapadrao
else:
    with open('senhapadrao.txt', 'w') as pd:
        pd.write('senhapadrao')
        senhapadrao = 'senhapadrao'
    

if darkdetect.isDark(): #se windows em dark mode...
    tema = 'dark' #tema do programa dark
    logo = 'logo_p.png' #logo dark 
else:  #se tema windows light
    tema = 'light' #tema claro
    logo = 'logo_b.png' #logo clara

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

    j_x = 400
    j_y = 260

    device_width = janelaLoc.winfo_screenwidth()/2
    device_height = janelaLoc.winfo_screenheight()/2

    device_width = device_width - (j_x/2)
    device_height = device_height - (j_y/2)

    device_width = int(device_width)
    device_height = int(device_height)
    
    janelaLoc.geometry(str(j_x)+'x'+str(j_y)+'+'+str(device_width)+'+'+str(device_height))
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
        if (i<15):
            if usuario in list_user:
                i+=1
                y+=1
                
                entrys['Entry_'+str(i)] = ttk.Button(janelaLoc,text=list_user,command=lambda i=i:escolher(entrys['Entry_'+str(i)]['text']))
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
                    #for setor in setores:
                    #    grupo = output2[output2.find(str(setor).strip()):output2.find('Asso')].strip()
                    defsenha = output2[output2.find('ltima defini')+24:output2.find('A senha expira')].strip()
                    expira = output2[output2.find('A senha expira')+15:output2.find('Altera')].strip()

                    for item in tree_view.get_children():
                        tree_view.delete(item)
                    tree_view.insert("",'end',iid=1, values=(nomecompleto,contaativa,logon,defsenha,expira))
                    
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
        buttonLoc = ttk.Button(frame3, text='OK', command=lambda:janelaLoc.destroy()).grid(column=0, row=1, pady=5)
    
    janelaLoc.bind("<Return>", (lambda event: janelaLoc.destroy()))
    janelaLoc.bind("<Escape>", (lambda event: janelaLoc.destroy()))
    
    sv_ttk.set_theme(tema)
    janelaLoc.wm_attributes("-topmost", 1)
    janelaLoc.after(1, lambda: janelaLoc.focus_force())

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
    janelaAviso.resizable(0,0)
    
    frame2 = ttk.Frame(janelaAviso)
    frame2.place(relx=0.5,rely=0.45,anchor='center')

    sv_ttk.set_theme(tema)
    janelaAviso.wm_attributes("-topmost", 1)
    janelaAviso.after(1, lambda: janelaAviso.focus_force())
    
    labelAviso = ttk.Label(frame2, text=mensagem, font='Arial 10')
    labelAviso.grid(column=0, row=0)
    buttonAviso = ttk.Button(frame2, text='OK', command=lambda: janelaAviso.destroy())
    janelaAviso.bind("<Return>", (lambda event: janelaAviso.destroy()))
    janelaAviso.bind("<Escape>", (lambda event: janelaAviso.destroy()))
    buttonAviso.grid(column=0, row=1, pady=5)
    
def resetSenha(usuario):
    usuario = usuario.strip()
    subprocess.Popen('net user '+usuario+' '+senhapadrao+' /domain /logonpasswordChg:yes /active:yes', shell=True)
    aviso('Senha Resetada!', usuario)
    
def unlockSenha(usuario):
    usuario = usuario.strip()
    subprocess.Popen('net user '+usuario+' /domain /active:yes', shell=True)
    aviso('Usuário Desbloqueado!', usuario)

usuario = any

janela = Tk()
list_search = Listbox(janela, width=50, height=7)

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
            if (i<18):
                if usuario3 in list_user3:
                    list_search.insert(END, list_user3)

    else:
        
        list_search.delete(0, END)
        for item in tree_view.get_children():
            tree_view.delete(item)

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
    #for setor in setores:
    #    grupo = output4[output4.find(str(setor).strip()):output4.find('Associa')].strip()
    defsenha = output4[output4.find('ltima defini')+24:output4.find('A senha expira')].strip()
    expira = output4[output4.find('A senha expira')+15:output4.find('Altera')].strip()
    
    tree_view.insert("",'end',iid=1, values=(nomecompleto,contaativa,logon,defsenha,expira))


janela.title(nomeapp+' '+versao)
janela.iconbitmap('icon.ico')

janela_width = 790
janela_height = 620

device_width = janela.winfo_screenwidth()/2
device_height = janela.winfo_screenheight()/2

device_width = device_width - (janela_width/2)
device_height = device_height - (janela_height/2)

device_width = int(device_width)
device_height = int(device_height)

janela.geometry(str(janela_width)+'x'+str(janela_height)+'+'+str(device_width)+'+'+str(device_height))

janela.resizable(True,True)
#janela['bg'] = '#f8f8f8'

frame = ttk.Frame(janela, padding=20)
frame.place(relx=0.515,rely=0.37,anchor='center')

frameBt = ttk.Frame(janela, padding=20)
frameBt.place(relx=0.5,rely=0.85,anchor='center')

frame_info = ttk.Frame(janela, padding=15)

img = PhotoImage(file=logo)
label_img = ttk.Label(janela, image=img,borderwidth=0,border=0)

labeluser = ttk.Label(frame_info,text='Usuário: '+user+' | ').grid(column=0,row=0)
labelpc = ttk.Label(frame_info ,text='HostName: '+pc).grid(column=1,row=0)

frame_info.place(relx=0.5,rely=0.93,anchor='center')
label_img.place(relx = 0.5,rely = 0.16,anchor = 'center')

label = ttk.Label(frame, text='Digite o usuário do domínio',font= ('Arial 14')).grid(column=0, columnspan=2, row=1, pady=3)

entry = ttk.Entry(frame, textvariable=usuario, width=25, font='Arial 14')
entry.grid(column=0, columnspan=2, row=2, pady=15, ipadx=3)
entry.bind("<KeyRelease>", (lambda event: atualizaSearch(entry.get())))
entry.bind("<Return>", (lambda event: localizar(entry.get())))

buttonL = ttk.Button(frame,width=2,text='➜',
command=lambda: localizar(entry.get()))
buttonL.grid(column=2, row=2, padx=5) #botão lupa
buttonL.bind("<Return>", (lambda event: localizar(entry.get())))

button = ttk.Button(frameBt,width=18,text='Resetar Senha', command=lambda: resetSenha(entry.get()))
button.bind("<Return>", (lambda event: resetSenha(entry.get())))
button.grid(column=0, row=5,pady=1,ipady=3, padx=3) #botão reset

button2 = ttk.Button(frameBt,width=18,text='Desbloquear Usuário', command=lambda: unlockSenha(entry.get()))
button2.bind("<Return>", (lambda event: unlockSenha(entry.get())))
button2.grid(column=1, row=5,pady=1,ipady=3, padx=3) #botão unlock

#ListBox

list_search.place(relx = 0.503,rely = 0.58,anchor = 'center')
list_search.bind('<<ListboxSelect>>', escolheList)

#Tabela Info Usuário
list_columns = ['nome', 'ativo', 'logon', 'defsenha', 'expira']
tree_view = ttk.Treeview(janela, show='headings', columns=list_columns, height='1')

tree_view.heading('nome', text='Nome Completo')
tree_view.heading('ativo', text='Ativo')
tree_view.heading('logon', text='Último Logon')
#tree_view.heading('grupo', text='Grupo')
tree_view.heading('defsenha', text='Última Definição de Senha')
tree_view.heading('expira', text='Senha Expira')

tree_view.column('nome', width=185)
tree_view.column('ativo', width=50)
tree_view.column('logon', width=130)
#tree_view.column('grupo', width=90)
tree_view.column('defsenha', width=170)
tree_view.column('expira', width=110)

tree_view.place(relx=0.5,rely=0.74,anchor='center')
#tree_view.bind('<<TreeviewSelect>>', def():)

janela.bind("<Escape>", (lambda event: janela.destroy()))
sv_ttk.set_theme(tema)

#janela.after(1, lambda: janela.focus_force())
#janela.wm_attributes("-topmost", 1)
entry.focus()
janela.mainloop()
