from tkinter import *
from tkcalendar import *
from tkinter import * #dando o alias(apelido) ao pacote
from _datetime import datetime  #importa os modulos necessarios
import time
import numpy as np
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt  
from matplotlib.figure import Figure
import re



###########################################################################################################################################
from tkinter import ttk
import ctypes                                      # Gráfico do projeto by: Bruno W. Cardoso
from tkinter import messagebox                    # Identação e Sumário by: Bruno W. Cardoso 
import tkinter                                        
import tkinter as tk
###########################################################################################################################################






















##########################################################################################################################################################################################
######################################################################## SUMÁRIO DE PROGRAMAÇÃO ##########################################################################################
##########################################################################################################################################################################################



####################################################  MNT001 - AQUI FICA OS ITENS DA TELA DE MONITORAMENTO EM TEMPO REAL
####################################################  ARD001 - AQUI AS CONFIGURAÇÕES DE LOOPING DO ARDUINO
####################################################  TEL001 - CONFIGURAÇÕES GERAIS DA TELA (RESOLUÇÃO, TAMANHO, ETC)
####################################################  POP001 - POPUP DE INFO E CRÉDITOS (ONDE DAMOS OS DEVIDOS CRÉDITOS AOS CRIADORES DAS IMAGENS)
####################################################  INI001 - AQUI FICA OS ITENS DA TELA DE INICIO
####################################################  RST001 - AQUI FICA OS ITENS DA TELA DE RESULTADOS
####################################################  BDD001 - BANCO DE DADOS
####################################################  GRF001 - AQUI FICA OS ITENS DA TELA DE GRÁFICOS
####################################################  GRF002 - AQUI FICA OS ITENS DA TELA QUE GERA OS GRÁFICOS
####################################################  PSQ001 - AQUI FICA OS ITENS DA TELA DE PESQUISA
####################################################  CBX001 - AQUI FICA AS CHECKBOXES DA AREA DE PESQUISA
####################################################  CLD001 - AQUI FICA AS FOTOS DOS CALENDÁRIOS INÍCIO E FIM
####################################################  RLG001 - AQUI FICA AS FOTOS E LABELS DOS RELÓGIOS INÍCIO E FIM
####################################################  GRL001 - CONFIGURAÇÕES QUE VALEM TANTO PARA A TELA DE PESQUISA QUANDO A DE GRÁFICOS
####################################################  BAR001 - BARRAS QUE FICAM NO TOPO E NA PARTE DEBAIXO E SEUS BOTÕES
####################################################  MNU001 - MENU PRINCIPAL
####################################################  CBX002 - COMBOBOX DA TELA DE GRÁFICOS
####################################################  JAN002 - CONFIGURAÇÕES GEAIS DA JANELA 2  
####################################################  SPL001 - TELA DE SPLASH
####################################################  FIM001 - FINAL DA PROGRAMAÇÃO (MAINLOOP FINAL)


##########################################################################################################################################################################################
######################################################################## SUMÁRIO DE PROGRAMAÇÃO ##########################################################################################
##########################################################################################################################################################################################












################################################################################################################################################################################
#OBS: LÉO, TODOS OS COMENTÁRIOS QUE TIVEREM ISSO "<--------------------", VOCÊ DEVE RETIRAR DO COMMENT, PORQUE FUI EU QUE COLOQUEI PRO PROGRAMA FUNCIONAR EM CASA SEM O SQL
################################################################################################################################################################################



import serial 
import mysql.connector 

diasGrafico = []
datesGrafico = []
vagasGrafico = [] 
mesAno = []
quantidade=[]
vagaAnterior='0'
vagaAtual='0'
contaDates = 0
contaVagas = 0
somaVagas = 0
vagapesquisa = 1
x=0
comport = serial.Serial('COM5', 9600) #conexao com a porta usb do pc (arduino)   <--------------------
print ("Serial Iniciada...\n")
cnx = mysql.connector.connect(user='root', password='', host='localhost', database='Linked_Park') #auxilia na conexao com o Banco de dados   <--------------------
cursor = cnx.cursor()    #<--------------------
insert_estacionamento = ("INSERT INTO log (Vaga,Horario_Entrada,Data_Entrada,Horario_Saida,Data_Saida) VALUES (%s,%s,STR_TO_DATE(%s,'%d/%m/%Y'),%s,STR_TO_DATE(%s,'%d/%m/%Y'))")#Define o codigo SQL que sera utilizado      <--------------------
def ___init___():
    def close_window(): 
        global x
        aovivo.destroy()
        x=1
        window.deiconify()
        voltar.place_forget()
    window.withdraw()
    global aovivo
    aovivo = Toplevel()
    aovivo.resizable(width=False, height=False)
    aovivo.overrideredirect(True)
    width = aovivo.winfo_screenwidth()
    height = aovivo.winfo_screenheight()
    aovivo.geometry('%dx%d+%d+%d' % (1150, 720 , width*0.2, height*0.1))



    global vaga1
    global vaga2
    global vaga3
    global vaga4
    global vaga5
    global vaga6
    global vaga7
    global vaga8
    global vaga9
    global vaga10
    global lastSerial
    #vaga1.place(x=125,y=200)
    #vaga2.place(x=300,y=200)
    #vaga3.place(x=480,y=200)
    #vaga4.place(x=670,y=200)
    #vaga5.place(x=860,y=200)
    #vaga6.place(x=125,y=420)
    #vaga7.place(x=300,y=420)
    #vaga8.place(x=480,y=420)
    #vaga9.place(x=670,y=420)
    #vaga10.place(x=860,y=420)
    lastSerial="s"
    global x
    x=0
    #aovivo = Tk()#Tk() significa a janela principal do programa
    aovivo.title("Linked Park - Monitoramento em Tempo Real")
    aovivo.iconbitmap(default="icones/index.ico")
    #aovivo.attributes("-alpha", 0.95)
    aovivo["bg"] = "Lightgrey"#altera a chave bg no dicionario "aovivo"
    # aovivo["background"] = "grey" altera da mesma forma que a chave bg
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    aovivo.geometry('%dx%d+%d+%d' % (1150, 720 , width*0.2, height*0.1))
    
    ''' ("LxA+E+T") Largura X Altura + Distancia da borda esquerda + Dist. borda topo
    pode se omitir alguns atributos
    ("LxA")apenas dimensoes // ("+E+T") apenas distancia da borda
    '''


























    ##################################################################################################################################################################
    ####################################################### MNT001 - AQUI FICA OS ITENS DA TELA DE MONITORAMENTO EM TEMPO REAL  ######################################
    ##################################################################################################################################################################


    AoVivoFrameFundo = Frame(aovivo, width=900, height=470, bg="Lightgrey", relief="raise")
    AoVivoFrameFundo.place(x=70, y=170)
    fundoimagem = PhotoImage(file="Leonardo/PNG/fundo.png")
    fundoimagem = fundoimagem.subsample(1)
    fundolabel = Label(aovivo, image=fundoimagem, bg="lightgrey")
    fundolabel.place(x=50,y=120)




    AoVivoFrameBottom = Frame(aovivo, width=1280, height=45, bg="MidnightBlue", relief="raise") 
    AoVivoFrameBottom.pack(side= BOTTOM)
    
    AoVivoFrameTop = Frame(aovivo, width=1280, height=45, bg="MidnightBlue", relief="raise") 
    AoVivoFrameTop.pack(side= TOP)



    b_sair = ttk.Button(AoVivoFrameBottom)
    bSairFoto = PhotoImage(file="Leonardo/PNG/exit2.png")
    bSairFoto = bSairFoto.subsample(5)
    b_sair.config(image=bSairFoto, command=window.destroy)
    b_sair.place(x=10, y=10)

    b_home = ttk.Button(AoVivoFrameTop)
    bHomeFoto = PhotoImage(file="Leonardo/PNG/voltar.png")
    bHomeFoto = bHomeFoto.subsample(22)
    b_home.config(image=bHomeFoto, command=close_window)
    b_home.place(x=10, y=6)

    ano = Label(AoVivoFrameBottom, text="Linked Park @2020", font=("Century Gothic", 15), bg="MIDNIGHTBLUE", fg="white")
    ano.place(x=950, y=10)












    vaga1imagem = PhotoImage(file="Leonardo/PNG/carrinho.png")
    vaga1 = Label(aovivo, image=vaga1imagem, bg="#1a1919")
    

    vaga2imagem = PhotoImage(file="Leonardo/PNG/carro final2.png")
    vaga2 = Label(aovivo, image=vaga2imagem, bg="#1a1919")
    
    
    vaga3imagem = PhotoImage(file="Leonardo/PNG/carrinhodefici.png")
    vaga3 = Label(aovivo, image=vaga3imagem, bg="#1a1919")
    

    vaga4imagem = PhotoImage(file="Leonardo/PNG/carro final4.png")
    vaga4 = Label(aovivo, image=vaga4imagem, bg="#1a1919")
    

    vaga5imagem = PhotoImage(file="Leonardo/PNG/carro final5.png")
    vaga5 = Label(aovivo, image=vaga5imagem, bg="#1a1919")
    
    
    vaga6imagem = PhotoImage(file="Leonardo/PNG/carro final6.png")
    vaga6 = Label(aovivo, image=vaga6imagem, bg="#1a1919")
    vaga6.place(x=125,y=420)

    vaga7imagem = PhotoImage(file="Leonardo/PNG/carrinhodefici.png")
    vaga7 = Label(aovivo, image=vaga7imagem, bg="#1a1919")
    vaga7.place(x=300,y=420)

    vaga8imagem = PhotoImage(file="Leonardo/PNG/carro final8.png")
    vaga8 = Label(aovivo, image=vaga8imagem, bg="#1a1919")
    vaga8.place(x=480,y=420)

    vaga9imagem = PhotoImage(file="Leonardo/PNG/carrinhodefici.png")
    vaga9 = Label(aovivo, image=vaga9imagem, bg="#1a1919")
    vaga9.place(x=670,y=420)

    vaga10imagem = PhotoImage(file="Leonardo/PNG/carro final10.png")
    vaga10 = Label(aovivo, image=vaga10imagem, bg="#1a1919")
    vaga10.place(x=860,y=420)
  
    
    





    LPFoto = PhotoImage(file="Leonardo/PNG/monitor.png")
    LPFoto = LPFoto.subsample(3)
    LP = Label(aovivo, image=LPFoto, bg="LIGHTGREY")
    LP.place(x=460,y=50)


    
    def mudaCor(vaga,cor):
        vaga["bg"]=cor


    ##################################################################################################################################################################
    ####################################################### MNT001 - AQUI FICA OS ITENS DA TELA DE MONITORAMENTO EM TEMPO REAL  ######################################
    ##################################################################################################################################################################
























    ##################################################################################################################################################################
    ####################################################### ARD001 - AQUI AS CONFIGURAÇÕES DE LOOPING DO ARDUINO  ####################################################
    ##################################################################################################################################################################



    def loopArduino():
     if(x==0):
      global comport
      global cnx
      global cursor
      serialValue = comport.readline() #le a porta serial do arduino
      global lastSerial
      if serialValue!=lastSerial :
        lastSerial=serialValue
        serialValue=str(serialValue)
        dados = serialValue.split(" ") # insere os valores num vetor
        vaga=dados[0].split("'")
        tamanhoEstado=len(dados[1])
        #################################################################################################################################VAGA 1
        if vaga[1]=='1' and tamanhoEstado==12:############################################OCUPADO
          vaga1.place(x=125,y=200)
          global splitEntrada1
          horario_entrada1=datetime.now()
          horario_entrada_string1= horario_entrada1.strftime("%d/%m/%Y %H:%M:%S")
          splitEntrada1=horario_entrada_string1.split(" ")
          time.sleep(1)
        if vaga[1]=='1' and tamanhoEstado==int(10):
          vaga1.place_forget()      #verifica os dados enviados pelo python
          horario_saida1=datetime.now()                     #Obtem a data e o horario da entrada
          horario_saida_string1= horario_saida1.strftime("%d/%m/%Y %H:%M:%S")  #converte a data e o horario de entrada em String
          splitSaida1=horario_saida_string1.split(" ")  # separa a data e o horario
          vaga=dados[0].split("'")
          TodososDados=(str(vaga[1]),str(splitEntrada1[1]),str(splitEntrada1[0]),str(splitSaida1[1]),str(splitSaida1[0]))
          cursor.execute(insert_estacionamento,TodososDados) # define onde e o que sera inserido no banco
          cnx.commit()    #Salva as alteracoes no Banco
          time.sleep(1)
         ##############################################################################################################################VAGA 2
        if vaga[1]=='2' and tamanhoEstado==12:
          vaga2.place(x=300,y=200)   #verifica os dados enviados pelo python
          global splitEntrada2
          horario_entrada1=datetime.now()
          horario_entrada_string1= horario_entrada1.strftime("%d/%m/%Y %H:%M:%S")
          splitEntrada2=horario_entrada_string1.split(" ")
          time.sleep(1)
        if vaga[1]=='2' and tamanhoEstado==int(10):
          vaga2.place_forget()      #verifica os dados enviados pelo python
          horario_saida1=datetime.now()                     #Obtem a data e o horario da entrada
          horario_saida_string1= horario_saida1.strftime("%d/%m/%Y %H:%M:%S")  #converte a data e o horario de entrada em String
          splitSaida1=horario_saida_string1.split(" ")  # separa a data e o horario
          vaga=dados[0].split("'")
          TodososDados=(str(vaga[1]),str(splitEntrada2[1]),str(splitEntrada2[0]),str(splitSaida1[1]),str(splitSaida1[0]))
          cursor.execute(insert_estacionamento,TodososDados) # define onde e o que sera inserido no banco
          cnx.commit()    #Salva as alteracoes no Banco  
          time.sleep(1)
        #################################################################################################################################VAGA 3
        if vaga[1]=='3' and tamanhoEstado==12:
          vaga3.place(x=480,y=200)    #verifica os dados enviados pelo python
          global splitEntrada3
          horario_entrada1=datetime.now()
          horario_entrada_string1= horario_entrada1.strftime("%d/%m/%Y %H:%M:%S")
          splitEntrada3=horario_entrada_string1.split(" ")
          time.sleep(1)
        if vaga[1]=='3' and tamanhoEstado==int(10):
          vaga3.place_forget()      #verifica os dados enviados pelo python
          horario_saida1=datetime.now()                     #Obtem a data e o horario da entrada
          horario_saida_string1= horario_saida1.strftime("%d/%m/%Y %H:%M:%S")  #converte a data e o horario de entrada em String
          splitSaida1=horario_saida_string1.split(" ")  # separa a data e o horario
          vaga=dados[0].split("'")
          TodososDados=(str(vaga[1]),str(splitEntrada3[1]),str(splitEntrada3[0]),str(splitSaida1[1]),str(splitSaida1[0]))
          cursor.execute(insert_estacionamento,TodososDados) # define onde e o que sera inserido no banco
          cnx.commit()    #Salva as alteracoes no Banco 
          time.sleep(1)
        #################################################################################################################################VAGA 4
        if vaga[1]=='4' and tamanhoEstado==12:
          vaga4.place(x=670,y=200)    #verifica os dados enviados pelo python
          global splitEntrada4
          horario_entrada1=datetime.now()
          horario_entrada_string1= horario_entrada1.strftime("%d/%m/%Y %H:%M:%S")
          splitEntrada4=horario_entrada_string1.split(" ")
          time.sleep(1)
        if vaga[1]=='4' and tamanhoEstado==int(10):
          vaga4.place_forget()       #verifica os dados enviados pelo python
          horario_saida1=datetime.now()                     #Obtem a data e o horario da entrada
          horario_saida_string1= horario_saida1.strftime("%d/%m/%Y %H:%M:%S")  #converte a data e o horario de entrada em String
          splitSaida1=horario_saida_string1.split(" ")  # separa a data e o horario
          vaga=dados[0].split("'")
          TodososDados=(str(vaga[1]),str(splitEntrada4[1]),str(splitEntrada4[0]),str(splitSaida1[1]),str(splitSaida1[0]))
          cursor.execute(insert_estacionamento,TodososDados) # define onde e o que sera inserido no banco
          cnx.commit()    #Salva as alteracoes no Banco
          time.sleep(1)
        #################################################################################################################################VAGA 5
        if vaga[1]=='5' and tamanhoEstado==12:
          vaga5.place(x=860,y=200)     #verifica os dados enviados pelo python
          global splitEntrada5
          horario_entrada1=datetime.now()
          horario_entrada_string1= horario_entrada1.strftime("%d/%m/%Y %H:%M:%S")
          splitEntrada5=horario_entrada_string1.split(" ")
          time.sleep(1)
        if vaga[1]=='5' and tamanhoEstado==int(10):
          vaga5.place_forget()      #verifica os dados enviados pelo python
          horario_saida1=datetime.now()                     #Obtem a data e o horario da entrada
          horario_saida_string1= horario_saida1.strftime("%d/%m/%Y %H:%M:%S")  #converte a data e o horario de entrada em String
          splitSaida1=horario_saida_string1.split(" ")  # separa a data e o horario
          vaga=dados[0].split("'")
          TodososDados=(str(vaga[1]),str(splitEntrada5[1]),str(splitEntrada5[0]),str(splitSaida1[1]),str(splitSaida1[0]))
          cursor.execute(insert_estacionamento,TodososDados) # define onde e o que sera inserido no banco
          cnx.commit()    #Salva as alteracoes no Banco
          time.sleep(1)
        """#################################################################################################################################VAGA 6
        if vaga[1]=='6' and tamanhoEstado==12:
          mudaCor(vaga6,"red")     #verifica os dados enviados pelo python
          global splitEntrada6
          horario_entrada1=datetime.now()
          horario_entrada_string1= horario_entrada1.strftime("%d/%m/%Y %H:%M:%S")
          splitEntrada6=horario_entrada_string1.split(" ")
          print(splitEntrada6[0])
          print(splitEntrada6[1])
        if vaga[1]=='6' and tamanhoEstado==int(10):
          mudaCor(vaga6,"green")       #verifica os dados enviados pelo python
          horario_saida1=datetime.now()                     #Obtem a data e o horario da entrada
          horario_saida_string1= horario_saida1.strftime("%d/%m/%Y %H:%M:%S")  #converte a data e o horario de entrada em String
          splitSaida1=horario_saida_string1.split(" ")  # separa a data e o horario
          print(splitSaida1[0])  #Data
          print(splitSaida1[1])  #Horario
          print(dados[0])
          vaga=dados[0].split("'")
          TodososDados=(str(vaga[1]),str(splitEntrada6[1]),str(splitEntrada6[0]),str(splitSaida1[1]),str(splitSaida1[0]))
          cursor.execute(insert_estacionamento,TodososDados) # define onde e o que sera inserido no banco
          cnx.commit()    #Salva as alteracoes no Banco
          print("concluido com sucesso") 
        #################################################################################################################################VAGA 7
        if vaga[1]=='7' and tamanhoEstado==12:
          mudaCor(vaga7,"red")     #verifica os dados enviados pelo python
          global splitEntrada7
          horario_entrada1=datetime.now()
          horario_entrada_string1= horario_entrada1.strftime("%d/%m/%Y %H:%M:%S")
          splitEntrada7=horario_entrada_string1.split(" ")
          print(splitEntrada7[0])
          print(splitEntrada7[1])
        if vaga[1]=='7' and tamanhoEstado==int(10):
          mudaCor(vaga7,"green")       #verifica os dados enviados pelo python
          horario_saida1=datetime.now()                     #Obtem a data e o horario da entrada
          horario_saida_string1= horario_saida1.strftime("%d/%m/%Y %H:%M:%S")  #converte a data e o horario de entrada em String
          splitSaida1=horario_saida_string1.split(" ")  # separa a data e o horario
          print(splitSaida1[0])  #Data
          print(splitSaida1[1])  #Horario
          print(dados[0])
          vaga=dados[0].split("'")
          TodososDados=(str(vaga[1]),str(splitEntrada7[1]),str(splitEntrada7[0]),str(splitSaida1[1]),str(splitSaida1[0]))
          cursor.execute(insert_estacionamento,TodososDados) # define onde e o que sera inserido no banco
          cnx.commit()    #Salva as alteracoes no Banco
          print("concluido com sucesso")
        #################################################################################################################################VAGA 8
        if vaga[1]=='8' and tamanhoEstado==12:
          mudaCor(vaga8,"red")     #verifica os dados enviados pelo python
          global splitEntrada8
          horario_entrada1=datetime.now()
          horario_entrada_string1= horario_entrada1.strftime("%d/%m/%Y %H:%M:%S")
          splitEntrada8=horario_entrada_string1.split(" ")
          print(splitEntrada8[0])
          print(splitEntrada8[1])
        if vaga[1]=='8' and tamanhoEstado==int(10):
          mudaCor(vaga8,"green")       #verifica os dados enviados pelo python
          horario_saida1=datetime.now()                     #Obtem a data e o horario da entrada
          horario_saida_string1= horario_saida1.strftime("%d/%m/%Y %H:%M:%S")  #converte a data e o horario de entrada em String
          splitSaida1=horario_saida_string1.split(" ")  # separa a data e o horario
          print(splitSaida1[0])  #Data
          print(splitSaida1[1])  #Horario
          print(dados[0])
          vaga=dados[0].split("'")
          TodososDados=(str(vaga[1]),str(splitEntrada8[1]),str(splitEntrada8[0]),str(splitSaida1[1]),str(splitSaida1[0]))
          cursor.execute(insert_estacionamento,TodososDados) # define onde e o que sera inserido no banco
          cnx.commit()    #Salva as alteracoes no Banco
          print("concluido com sucesso")
        #################################################################################################################################VAGA 9
        if vaga[1]=='9' and tamanhoEstado==12:
          mudaCor(vaga9,"red")     #verifica os dados enviados pelo python
          global splitEntrada9
          horario_entrada1=datetime.now()
          horario_entrada_string1= horario_entrada1.strftime("%d/%m/%Y %H:%M:%S")
          splitEntrada9=horario_entrada_string1.split(" ")
          print(splitEntrada9[0])
          print(splitEntrada9[1])
        if vaga[1]=='9' and tamanhoEstado==int(10):
          mudaCor(vaga9,"green")       #verifica os dados enviados pelo python
          horario_saida1=datetime.now()                     #Obtem a data e o horario da entrada
          horario_saida_string1= horario_saida1.strftime("%d/%m/%Y %H:%M:%S")  #converte a data e o horario de entrada em String
          splitSaida1=horario_saida_string1.split(" ")  # separa a data e o horario
          print(splitSaida1[0])  #Data
          print(splitSaida1[1])  #Horario
          print(dados[0])
          vaga=dados[0].split("'")
          TodososDados=(str(vaga[1]),str(splitEntrada9[1]),str(splitEntrada9[0]),str(splitSaida1[1]),str(splitSaida1[0]))
          cursor.execute(insert_estacionamento,TodososDados) # define onde e o que sera inserido no banco
          cnx.commit()    #Salva as alteracoes no Banco
          print("concluido com sucesso")   
        #################################################################################################################################VAGA 10
        if vaga[1]=='10' and tamanhoEstado==13:
          mudaCor(vaga10,"red")     #verifica os dados enviados pelo python
          global splitEntrada10
          horario_entrada1=datetime.now()
          horario_entrada_string1= horario_entrada1.strftime("%d/%m/%Y %H:%M:%S")
          splitEntrada10=horario_entrada_string1.split(" ")
          print(splitEntrada10[0])
          print(splitEntrada10[1])
        if vaga[1]=='10' and tamanhoEstado==int(11):
          mudaCor(vaga10,"green")       #verifica os dados enviados pelo python
          horario_saida1=datetime.now()                     #Obtem a data e o horario da entrada
          horario_saida_string1= horario_saida1.strftime("%d/%m/%Y %H:%M:%S")  #converte a data e o horario de entrada em String
          splitSaida1=horario_saida_string1.split(" ")  # separa a data e o horario
          print(splitSaida1[0])  #Data
          print(splitSaida1[1])  #Horario
          print(dados[0])
          vaga=dados[0].split("'")
          TodososDados=(str(vaga[1]),str(splitEntrada10[1]),str(splitEntrada10[0]),str(splitSaida1[1]),str(splitSaida1[0]))
          cursor.execute(insert_estacionamento,TodososDados) # define onde e o que sera inserido no banco
          cnx.commit()    #Salva as alteracoes no Banco
          print("concluido com sucesso") """
      aovivo.after(1000,loopArduino)
    #Tk() significa a janela principal do programa
    #global comport
    voltar.place(x=280,y=500)
    voltar.configure(command=aovivo.destroy) 
    loopArduino()
    aovivo.mainloop()


    ##################################################################################################################################################################
    ####################################################### ARD001 - AQUI AS CONFIGURAÇÕES DE LOOPING DO ARDUINO  ####################################################
    ##################################################################################################################################################################





























##################################################################################################################################################################
#################################################### TEL001 - CONFIGURAÇÕES GERAIS DA TELA (RESOLUÇÃO, TAMANHO, ETC)  ############################################
##################################################################################################################################################################




window = Tk()
window.withdraw()
window.overrideredirect(False)
window.resizable(width=False, height=False)
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry('%dx%d+%d+%d' % (width*0.8, height*0.8, width*0.1, height*0.1))


#window.attributes("-alpha", 0.95)
varTodos=IntVar()
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
listaHora=list(range(00, 24))
listaMin=list(range(00, 60))
print(listaMin)
cnx = mysql.connector.connect(user='root', password='', host='localhost', database='Linked_Park') #auxilia na conexao com o Banco de dados  <--------------------


cursor = cnx.cursor()     #<--------------------


#window = Tk()#Tk() significa a janela principal do programa




##################################################################################################################################################################
#################################################### TEL001 - CONFIGURAÇÕES GERAIS DA TELA (RESOLUÇÃO, TAMANHO, ETC)  ############################################
##################################################################################################################################################################



























##################################################################################################################################################################
###################################### POP001 - POPUP DE INFO E CRÉDITOS (ONDE DAMOS OS DEVIDOS CRÉDITOS AOS CRIADORES DAS IMAGENS) ##############################
##################################################################################################################################################################


# "info" developed by: Bruno Cardoso: Aqui eu coloquei um jeito de mostrar o que cada um fez com uma popup na tela.
def Info():
    ctypes.windll.user32.MessageBoxW(0, "Interface Gráfica Python, Modelo 3D do projeto (Sketchup), Vídeo e Sistema de Cadastro: Bruno Willian Cardoso \n \n \nEscrita do Trabalho de Graduação, Refências e Estatísticas: Bruno Britto Nunes \n \n \nProgramação do arduino e sua integração ao banco de dados: Leonardo Mateus de Carvalho Marques \n \n \nFoto estacionamento: Brett Sayles do Pexels", "Créditos", 0)



##################################################################################################################################################################
###################################### POP001 - POPUP DE INFO E CRÉDITOS (ONDE DAMOS OS DEVIDOS CRÉDITOS AOS CRIADORES DAS IMAGENS) ##############################
##################################################################################################################################################################

























##################################################################################################################################################################
########################################################## INI001 - AQUI FICA OS ITENS DA TELA DE INICIO #########################################################
##################################################################################################################################################################

def telaInicio():
    global ResultFrameFundo
    window.deiconify()
    comboVaga.place_forget()
    b_todosSelect.place_forget()
    if (voltar):
      voltar.place_forget()
    listBox.place_forget()
    LP.place_forget()
    if (ResultFrameFundo):
      ResultFrameFundo.place_forget()
    b_home.place_forget()
    voltar.place_forget()
    pesquisa.place_forget()
    ck1.place_forget()
    ck2.place_forget()
    ck3.place_forget()
    ck4.place_forget()
    ck5.place_forget()
    ck6.place_forget()
    ck7.place_forget()
    ck8.place_forget()
    ck9.place_forget()
    ck10.place_forget()
    calFinal.place_forget()
    calInicial.place_forget()
    selecionaVaga.place_forget()
    l_HoraFinal.place_forget()
    l_MinutoFinal.place_forget()
    l_HoraInicial.place_forget()
    l_MinutoInicial.place_forget()
    dataInicial.place_forget()
    horaFinal.place_forget()
    horaInicial.place_forget()
    e_HoraFinal.place_forget()
    e_MinutoFinal.place_forget()
    e_HoraInicial.place_forget()
    e_MinutoInicial.place_forget()
    dataFinal.place_forget()
    LogoLabel.place(x=330,y=480)
    b_pesquisa.place(x=100,y=200)
    b_graficos.place(x=460,y=200)
    b_atualmente.place(x=800,y=200)
    tituloHome.place(x=465,y=70)
    

##################################################################################################################################################################
########################################################## INI001 - AQUI FICA OS ITENS DA TELA DE INICIO #########################################################
##################################################################################################################################################################


























##################################################################################################################################################################
########################################################## RST001 - AQUI FICA OS ITENS DA TELA DE RESULTADOS ####################################################
##################################################################################################################################################################


def telaResultados():
    b_todosSelect.place_forget()
    pesquisa.place_forget()
    b_home.place_forget()
    ck1.place_forget()
    ck2.place_forget()
    ck3.place_forget()
    ck4.place_forget()
    ck5.place_forget()
    ck6.place_forget()
    ck7.place_forget()
    ck8.place_forget()
    ck9.place_forget()
    ck10.place_forget()
    calFinal.place_forget()
    calInicial.place_forget()
    selecionaVaga.place_forget()
    l_HoraFinal.place_forget()
    l_MinutoFinal.place_forget()
    l_HoraInicial.place_forget()
    l_MinutoInicial.place_forget()
    dataInicial.place_forget()
    horaFinal.place_forget()
    horaInicial.place_forget()
    e_HoraFinal.place_forget()
    e_MinutoFinal.place_forget()
    e_HoraInicial.place_forget()
    e_MinutoInicial.place_forget()
    dataFinal.place_forget()
    listBox.place(x=275,y=110)
    voltar.configure(command=telaPesquisa)
    ResultFrameFundo.place(x=276, y=76)
    l_telaresultados.place(x=300, y=80)
    l_totalRegistros.place(x=100,y=350)
    l_totalRegistrosText.place(x=100,y=300)
    
##################################################################################################################################################################
########################################################## RST001 - AQUI FICA OS ITENS DA TELA DE RESULTADOS ####################################################
##################################################################################################################################################################


ResultFrameFundo = Frame(window, width=662, height=35, bg="MidnightBlue", relief="raise")
l_telaresultados =Label(window,text="         ID      VAGA      Entrada                                          Saida  ",font=("Century Gothic",12),bg="MidnightBlue",fg="white")
















##################################################################################################################################################################
####################################################################### BDD001 - BANCO DE DADOS  ##################################################################
##################################################################################################################################################################


    
def erro(error):
    print('Existem Incoerencias na Consulta em:',error)
def Pesquisa():
  global listBox
  global  varTodos
  global totaldeRegistros
  if varTodos.get()==1:
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM log;")  
    myresult=cursor.fetchall()
    for outro in myresult: 
          replaceoutro=str(outro)##DEIXA MAIS ESPACADO OS RESULTADOS DA LISTBOX
          replaceoutro=replaceoutro.replace(" ","       ")
          replaceoutro=re.sub('|\'|\,|\)|\(','', replaceoutro)
          print(len(replaceoutro))
          if len(replaceoutro)==67:
             replaceoutro="          0"+replaceoutro
             listBox.insert(END,replaceoutro)
          elif len(replaceoutro)==68:
             replaceoutro="          "+replaceoutro
             listBox.insert(END,replaceoutro)
          elif len(replaceoutro)==71:
             replaceoutro="      "+replaceoutro
             listBox.insert(END,replaceoutro)
          elif len(replaceoutro)==70:
             replaceoutro="       "+replaceoutro
             listBox.insert(END,replaceoutro)
          elif len(replaceoutro)==69:
             replaceoutro="         "+replaceoutro
             listBox.insert(END,replaceoutro)
          else :
             listBox.insert(END,replaceoutro)
    totaldeRegistros.set(str(len(myresult)))
    telaResultados()
    cursor.close()    ############################################ADICIONEI AGR
  else:
    getCalendarioInicial=calInicial.selection_get()
    getCalendarioFinal=calFinal.selection_get()
    if getCalendarioInicial and getCalendarioFinal:
     print(getCalendarioInicial, getCalendarioFinal)
    v_HoraInicial=v_HI.get()
    v_VerHoraInicial=v_HoraInicial 
    print (v_HoraInicial)
    v_MinutoInicial=v_MI.get()
    v_VerMinutoInicial=v_MinutoInicial
    print (v_MinutoInicial[0])
    if(v_MinutoInicial[0]=='0'): #consertando a divergencia entre o valor em ('00' à '09')digitado pelo usuario e o valor da lista das horas e minutos(de '0' a '9' )
        v_VerMinutoInicial=v_MinutoInicial[1]
    if(v_HoraInicial[0]=='0'):
        v_VerHoraInicial=v_HoraInicial[1]#VARIAVEIS DE VERIFICACAO TEM O 'VER' NO INICIO
    if v_HoraInicial=='24': # convertendo 24 hrs para 0 hrs
        v_HoraInicial='00'
    v_HoraFinal=v_HF.get() 
    print (v_HoraFinal)
    v_MinutoFinal=v_MF.get()
    print (v_MinutoInicial[0])
    if(v_MinutoFinal[0]=='0'): #consertando a divergencia entre o valor em ('00' à '09')digitado pelo usuario e o valor da lista das horas e minutos(de '0' a '9' )
        v_VerMinutoFinal=v_MinutoFinal[1]
    if(v_HoraFinal[0]=='0'):
        v_VerHoraFinal=v_HoraFinal[1]
    #if v_HoraFinal=='24': # convertendo 24 hrs para 0 hrs #######################################Conserta o erro no SQL mas cria um no verificador de(0 a 23)
    #    v_HoraFinal='0'
    verifyHI=False
    verifyMI=False
    for x in listaHora:
        #print(listaHora)
        print (x)
        print (v_MinutoInicial)
        print(v_HoraInicial)
        if int(v_VerHoraInicial)==x:
            verifyHI=True
            break
        else:
            continue
    for cont in listaMin:
        if int(v_VerMinutoInicial)==cont:
            verifyMI=True
            tempoInicial=(v_HoraInicial+':'+v_MinutoInicial)
            tempoFinal=(v_HoraFinal+':'+v_MinutoFinal)
            preStringVagas=[var1.get(),var2.get(),var3.get(),var4.get(),var5.get(),var6.get(),var7.get(),var8.get(),var9.get(),var10.get()]
            print(preStringVagas)
            StringVagas=[]
            StringVagas[:] = (value for value in preStringVagas if value != 0)
            print(StringVagas)
            SV=str(StringVagas).strip('[]')
            break
        else:
            continue
    if SV != "":
        queryTelaPesquisa=("SELECT * FROM LOG WHERE VAGA IN({})AND Horario_Entrada BETWEEN \"{}\" AND \"{}\" AND DATA_ENTRADA BETWEEN \"{}\" AND \"{}\" AND Horario_Saida BETWEEN \"{}\" AND \"{}\" AND DATA_SAIDA BETWEEN \"{}\" AND \"{}\";")
        DadosSelect=queryTelaPesquisa.format(SV,str(tempoInicial),str(tempoFinal),str(getCalendarioInicial),str(getCalendarioFinal),str(tempoInicial),str(tempoFinal),str(getCalendarioInicial),str(getCalendarioFinal))
        print(DadosSelect)
        cursor = cnx.cursor()
        cursor.execute(DadosSelect)
        myresult=cursor.fetchall()
        totaldeRegistros.set("")
        for outro in myresult:  
          replaceoutro=str(outro)##DEIXA MAIS ESPACADO OS RESULTADOS DA LISTBOX
          replaceoutro=replaceoutro.replace(" ","       ")
          replaceoutro=re.sub('|\'|\,|\)|\(','', replaceoutro)
          print(len(replaceoutro))
          if len(replaceoutro)==67:
             replaceoutro="          0"+replaceoutro
             listBox.insert(END,replaceoutro)
          elif len(replaceoutro)==68:
             replaceoutro="          "+replaceoutro
             listBox.insert(END,replaceoutro)
          elif len(replaceoutro)==71:
             replaceoutro="      "+replaceoutro
             listBox.insert(END,replaceoutro)
          elif len(replaceoutro)==70:
             replaceoutro="       "+replaceoutro
             listBox.insert(END,replaceoutro)
          elif len(replaceoutro)==69:
             replaceoutro="         "+replaceoutro
             listBox.insert(END,replaceoutro)
          else :
             listBox.insert(END,replaceoutro)
        totaldeRegistros.set(str(len(myresult)))
        cursor.close()
        telaResultados()
    else:
        return erro("Selecione ao menos uma vaga")
        

##################################################################################################################################################################
####################################################################### BDD001 - BANCO DE DADOS  ##################################################################
##################################################################################################################################################################


































##################################################################################################################################################################
########################################################## GRF001 - AQUI FICA OS ITENS DA TELA DE GRÁFICOS #######################################################
##################################################################################################################################################################



def telaGraficos() :
    varTodos=0 #reseta o valor para a variavel
    global b_todosSelect  
    global b_atualmente
    global b_graficos
    global b_pesquisa
    global v_combobox
    #####TELA INICIO
    b_todosSelect.place(x=420,y=149)
    b_atualmente.place_forget()
    b_graficos.place_forget()
    b_pesquisa.place_forget()
    LogoLabel.place_forget()
    b_home.place_forget()
    tituloHome.place_forget()
    #######TELA PESQUISA
    listBox.delete(0,END)#limpa as consultas anteriores
    listBox.place_forget()
    LP.place_forget
    selecionaVaga.place(x=250,y=10)
    comboVaga.place(x=330,y=150)
    dataInicial.place(x=50,y=250)
    calInicial.place(x=300,y=240)
    dataFinal.place(x=50,y=475)
    calFinal.place(x=300,y=470)
    horaInicial.place(x=670,y=240)
    horaFinal.place(x=670,y=470)
    e_HoraInicial.place(x=870,y=315)
    e_MinutoInicial.place(x=950,y=315)
    e_HoraFinal.place(x=870,y=550)
    e_MinutoFinal.place(x=950,y=550)
    l_HoraInicial.place(x=870,y=290)
    l_MinutoInicial.place(x=944,y=290)
    l_HoraFinal.place(x=870,y=525)
    l_MinutoFinal.place(x=950,y=525)
    pesquisa.place(x=650,y=100)
    voltar.place(x=10, y=5) 
    pesquisa.configure(command=geraGraficos)
    voltar.configure(command=telaInicio)  



##################################################################################################################################################################
########################################################## GRF001 - AQUI FICA OS ITENS DA TELA DE GRÁFICOS #######################################################
##################################################################################################################################################################
























##################################################################################################################################################################
########################################################## GRF002 - AQUI FICA OS ITENS DA TELA QUE GERA OS GRÁFICOS ##############################################
##################################################################################################################################################################

    
def GetNEW(vagapesquisa,diasGrafico,mesAno):
      if plt :
            plt.close()
      name_list=""
      value_list=""
      print(name_list)
      print(value_list) 
      name_list = diasGrafico
      value_list = mesAno
      pos_list = np.arange(len(name_list))
      print(type(pos_list))
      plt.bar(name_list,value_list, color = '.75')
      #ax= plt.axes()
      #ax.xaxis.set_major_locator(ticker.FixedLocator((pos_list)))
      #ax.xaxis.set_major_formatter(ticker.FixedFormatter((name_list)))
      fig = plt.gcf()
      fig.canvas.set_window_title("Histórico da Vaga"+" "+str(vagapesquisa))
      fig.canvas.manager.window.geometry("1280x720")
      plt.ylabel('Dados')
      plt.xlabel('Datas')
      plt.show()
def geraGraficos():
    #global mesAno
    #global diasGrafico
    #global vagasGrafico
    #global datesGrafico
    somaDates=0
    if varTodos.get()==1:
        mesAno=[]
        diasGrafico=[]
        somaDates=0
        dataAnterior=0
        data=[]
        diasGrafico.clear()
        mesAno.clear()
        datesGrafico.clear()
        vagasGrafico.clear()
        vagatodosgrafico=str(v_combobox.get())
        queryTelaPesquisa=("SELECT VAGA,DATA_ENTRADA FROM LOG WHERE VAGA IN({})")
        DadosSelect=queryTelaPesquisa.format(vagatodosgrafico)
        print(DadosSelect)
        cursor = cnx.cursor()
        cursor.execute(DadosSelect)
        data=cursor.fetchall() ### mudei o valor para "data" 

        for d in data:
          grafico=str(d).split(",")
          vagasGrafico.append(grafico[0][3:-1])
          datesGrafico.append(grafico[1][2:-2])
        print(datesGrafico)
        #print (vagasGrafico)
        # for iniciais para verificar se a quantidade foi extraida corretamente
        for i,dataAtual in enumerate(datesGrafico) :
           if dataAnterior=='0':
             dataAnterior=dataAtual
             diasGrafico.append(dataAtual)
             somaDates=1
           elif dataAtual==dataAnterior :
             somaDates= somaDates+1
             dataAnterior=dataAtual
           elif dataAtual!=dataAnterior and dataAnterior!='0' :
             somaDates= somaDates+1
             diasGrafico.append(dataAtual)
             mesAno.append(somaDates)
             dataAnterior=='0'
             somaDates=0
             dataAnterior=dataAtual
           if i == (len(datesGrafico) - 1) and dataAtual==dataAnterior : ## Verifica se é o ultimo elemento da lista de contagem
             somaDates= somaDates+1 
             mesAno.append(somaDates)
             #diasGrafico.append(dataAtual)  
        print("TAMANHO DOS DADOS __________________________________"+str(len(mesAno))+str(len(diasGrafico)))
        print(str(mesAno)+str(diasGrafico))
        # QUICK FIX
        mesAno.remove(mesAno[0])
        print(str(mesAno)+"RESOLVIDO")
        GetNEW(vagatodosgrafico,diasGrafico,mesAno)   
    else:  
        mesAno=[]
        diasGrafico=[]
        somaDates=0
        dataAnterior=0
        data=[]
        diasGrafico.clear()
        mesAno.clear()
        datesGrafico.clear()
        vagasGrafico.clear()
        SV=str(v_combobox.get()) 
        datesGrafico.clear()
        dataAnterior=0  
        DadosSelect=None
        getCalendarioInicial=calInicial.selection_get()
        getCalendarioFinal=calFinal.selection_get()
        if getCalendarioInicial and getCalendarioFinal:
         print(getCalendarioInicial, getCalendarioFinal)
        v_HoraInicial=v_HI.get()
        v_VerHoraInicial=v_HoraInicial 
        print (v_HoraInicial)
        v_MinutoInicial=v_MI.get()
        v_VerMinutoInicial=v_MinutoInicial
        print (v_MinutoInicial[0])
        if(v_MinutoInicial[0]=='0'): #consertando a divergencia entre o valor em ('00' à '09')digitado pelo usuario e o valor da lista das horas e minutos(de '0' a '9' )
            v_VerMinutoInicial=v_MinutoInicial[1]
        if(v_HoraInicial[0]=='0'):
            v_VerHoraInicial=v_HoraInicial[1]#VARIAVEIS DE VERIFICACAO TEM O 'VER' NO INICIO
        if v_HoraInicial=='24': # convertendo 24 hrs para 0 hrs
            v_HoraInicial='00'
        v_HoraFinal=v_HF.get() 
        print (v_HoraFinal)
        v_MinutoFinal=v_MF.get()
        print (v_MinutoInicial[0])
        if(v_MinutoFinal[0]=='0'): #consertando a divergencia entre o valor em ('00' à '09')digitado pelo usuario e o valor da lista das horas e minutos(de '0' a '9' )
            v_VerMinutoFinal=v_MinutoFinal[1]
        if(v_HoraFinal[0]=='0'):
            v_VerHoraFinal=v_HoraFinal[1]
        #if v_HoraFinal=='24': # convertendo 24 hrs para 0 hrs #######################################Conserta o erro no SQL mas cria um no verificador de(0 a 23)
        #    v_HoraFinal='0'
        verifyHI=False
        verifyMI=False
        for x in listaHora:
            #print(listaHora)
            print (x)
            print (v_MinutoInicial)
            print(v_HoraInicial)
            if int(v_VerHoraInicial)==x:
                verifyHI=True
        for cont in listaMin:
            if int(v_VerMinutoInicial)==cont:
                verifyMI=True
                tempoInicial=(v_HoraInicial+':'+v_MinutoInicial)
                tempoFinal=(v_HoraFinal+':'+v_MinutoFinal)
                preStringVagas=str(v_combobox.get())############ALTEREI PARA A VARIAVEL DO COMBOBOX
                print(preStringVagas)
                SV=preStringVagas
            if (verifyHI==True) and (verifyMI==True):
                break
            else:
                  continue
        if SV != "":
          if (verifyHI==True) and (verifyMI==True) and SV !="":   
            queryTelaPesquisa=("SELECT VAGA,DATA_ENTRADA FROM LOG WHERE VAGA IN({})AND Horario_Entrada BETWEEN \"{}\" AND \"{}\" AND DATA_ENTRADA BETWEEN \"{}\" AND \"{}\" AND Horario_Saida BETWEEN \"{}\" AND \"{}\" AND DATA_SAIDA BETWEEN \"{}\" AND \"{}\";")
            DadosSelect=queryTelaPesquisa.format(SV,str(tempoInicial),str(tempoFinal),str(getCalendarioInicial),str(getCalendarioFinal),str(tempoInicial),str(tempoFinal),str(getCalendarioInicial),str(getCalendarioFinal))
            print(DadosSelect)
            cursor = cnx.cursor()
            cursor.execute(DadosSelect)
            data=cursor.fetchall() ### mudei o valor para "data" 
            print("VALOR ATUAL DE DATA"+str(data)+"VALOR ATUAL DE DATA")
    
            for d in data:
              grafico=str(d).split(",")
              vagasGrafico.append(grafico[0][3:-1])
              datesGrafico.append(grafico[1][2:-2])
            print(datesGrafico)
            #print (vagasGrafico)
            # for iniciais para verificar se a quantidade foi extraida corretamente
            for i,dataAtual in enumerate(datesGrafico) :
                 if dataAnterior=='0':
                   dataAnterior=dataAtual
                   diasGrafico.append(dataAtual)
                   somaDates=1
                 elif dataAtual==dataAnterior :
                   somaDates= somaDates+1
                   dataAnterior=dataAtual
                 elif dataAtual!=dataAnterior and dataAnterior!='0' :
                   somaDates= somaDates+1
                   diasGrafico.append(dataAtual)
                   mesAno.append(somaDates)
                   dataAnterior=='0'
                   somaDates=0
                   dataAnterior=dataAtual
                 if i == (len(datesGrafico) - 1) and dataAtual==dataAnterior : ## Verifica se é o ultimo elemento da lista de contagem
                   somaDates= somaDates+1 
                   mesAno.append(somaDates)
                   #diasGrafico.append(dataAtual)  
            print("TAMANHO DOS DADOS __________________________________"+str(len(mesAno))+str(len(diasGrafico)))
            print(str(mesAno)+str(diasGrafico))
            # QUICK FIX
            if len(mesAno)>1:
              mesAno.remove(mesAno[0])
            print(str(mesAno)+"RESOLVIDO")
            GetNEW(SV,diasGrafico,mesAno)  
                ######################################################################################################### CODIGO DO GRAF
            print("DEU CERTO")
          else:
            return erro("Horario incompativel com o formato de 24:00 horas")
        else:
          return erro("Selecione ao menos uma vaga")
    cursor.close() ##################ADICIONADO NOS ULTIMOS EDITS
    



##################################################################################################################################################################
########################################################## GRF002 - AQUI FICA OS ITENS DA TELA QUE GERA OS GRÁFICOS ##############################################
##################################################################################################################################################################

























##################################################################################################################################################################
########################################################## PSQ001 - AQUI FICA OS ITENS DA TELA DE PESQUISA #######################################################
##################################################################################################################################################################

def telaPesquisa() :
    varTodos=0 #reseta o valor para a variavel
    global b_todosSelect  
    global b_atualmente
    global b_graficos
    global b_pesquisa
    #####TELA INICIO
    b_todosSelect.place(x=280,y=150)
    b_atualmente.place_forget()
    b_graficos.place_forget()
    b_pesquisa.place_forget()
    LogoLabel.place_forget()
    b_home.place_forget()
    tituloHome.place_forget()
    #########TELA RESULTADOS
    ResultFrameFundo.place_forget()
    l_totalRegistros.place_forget()
    l_totalRegistrosText.place_forget()
    l_telaresultados.place_forget()
    #######TELA PESQUISA
    listBox.delete(0,END)#limpa as consultas anteriores
    listBox.place_forget()
    LP.place_forget
    selecionaVaga.place(x=48,y=20)
    ck1.place(x=50,y=150)
    ck2.place(x=95,y=150)
    ck3.place(x=140,y=150)
    ck4.place(x=185,y=150)
    ck5.place(x=232,y=150)
    ck6.place(x=50,y=190)
    ck7.place(x=95,y=190)
    ck8.place(x=140,y=190)
    ck9.place(x=185,y=190)
    ck10.place(x=232,y=190)
    dataInicial.place(x=50,y=250)
    calInicial.place(x=300,y=240)
    dataFinal.place(x=50,y=475)
    calFinal.place(x=300,y=470)
    horaInicial.place(x=670,y=240)
    horaFinal.place(x=670,y=470)
    e_HoraInicial.place(x=870,y=315)
    e_MinutoInicial.place(x=950,y=315)
    e_HoraFinal.place(x=870,y=550)
    e_MinutoFinal.place(x=950,y=550)
    l_HoraInicial.place(x=870,y=290)
    l_MinutoInicial.place(x=944,y=290)
    l_HoraFinal.place(x=870,y=525)
    l_MinutoFinal.place(x=950,y=525)
    pesquisa.place(x=800,y=100)  
    voltar.place(x=10, y=5)   
    voltar.configure(command=telaInicio)
    pesquisa.configure(command=Pesquisa)    



##################################################################################################################################################################
########################################################## PSQ001 - AQUI FICA OS ITENS DA TELA DE PESQUISA #######################################################
##################################################################################################################################################################






























##################################################################################################################################################################
########################################################## CBX001 - AQUI FICA AS CHECKBOXES DA AREA DE PESQUISA ##################################################
##################################################################################################################################################################
totaldeRegistros= StringVar()
v_HI= StringVar()
v_MI= StringVar()
v_HF= StringVar()
v_MF= StringVar()
listBox=Listbox(window,width="60",height="22",bg="LightGrey",font=("Helvetica",15))## PS os valore WIDTH E HEIGHT SAO BASEADOS NO TAMANHO DA FONTE DESSE WIDGET




SelVagaFoto = PhotoImage(file="Leonardo/PNG/vagas.png")
SelVagaFoto = SelVagaFoto.subsample(2)
selecionaVaga = Label(window, image=SelVagaFoto, bg="LightGrey")






ck1 = Checkbutton(window, text="1",variable=var1,offvalue=0,onvalue=1)

ck2 = Checkbutton(window, text="2",variable=var2,offvalue=0,onvalue=2)

ck3 = Checkbutton(window, text="3",variable=var3,offvalue=0,onvalue=3)

ck4 = Checkbutton(window, text="4",variable=var4,offvalue=0,onvalue=4)

ck5 = Checkbutton(window, text="5",variable=var5,offvalue=0,onvalue=5)

ck6 = Checkbutton(window, text="6",variable=var6,offvalue=0,onvalue=6)

ck7 = Checkbutton(window, text="7",variable=var7,offvalue=0,onvalue=7)

ck8 = Checkbutton(window, text="8",variable=var8,offvalue=0,onvalue=8)

ck9 = Checkbutton(window, text="9",variable=var9,offvalue=0,onvalue=9)

ck10 = Checkbutton(window, text="10",variable=var10,offvalue=0,onvalue=10)



##################################################################################################################################################################
########################################################## CBX001 - AQUI FICA AS CHECKBOXES DA AREA DE PESQUISA ##################################################
##################################################################################################################################################################




























##################################################################################################################################################################
########################################################## CLD001 - AQUI FICA AS FOTOS DOS CALENDÁRIOS INÍCIO E FIM ##############################################
##################################################################################################################################################################


dataInicialFoto = PhotoImage(file="Leonardo/PNG/Data Inicio.png")
dataInicialFoto = dataInicialFoto.subsample(8)
dataInicial = Label(window, image=dataInicialFoto, bg="LightGrey")

dataFinalFoto = PhotoImage(file="Leonardo/PNG/Data Fim.png")
dataFinalFoto = dataFinalFoto.subsample(8)
dataFinal = Label(window, image=dataFinalFoto, bg="LightGrey")

calInicial=Calendar(window,width="150",height="150")



calFinal=Calendar(window,width="200",height="200")


##################################################################################################################################################################
########################################################## CLD001 - AQUI FICA AS FOTOS DOS CALENDÁRIOS INÍCIO E FIM ##############################################
##################################################################################################################################################################
































##################################################################################################################################################################
######################################################## RLG001 - AQUI FICA AS FOTOS E LABELS DOS RELÓGIOS INÍCIO E FIM ##########################################
##################################################################################################################################################################



HoraInicialFoto = PhotoImage(file="Leonardo/PNG/HoraInicio.png")
HoraInicialFoto = HoraInicialFoto.subsample(5)
horaInicial = Label(window, image=HoraInicialFoto, bg="LightGrey")

HoraFinalFoto = PhotoImage(file="Leonardo/PNG/HoraFim.png")
HoraFinalFoto = HoraFinalFoto.subsample(5)
horaFinal = Label(window, image=HoraFinalFoto, bg="LightGrey")

e_HoraInicial=Entry(window,width=2,foreground="blue",font=("verdana",36),textvariable=v_HI)
e_MinutoInicial=Entry(window,width=2,foreground="blue",font=("verdana",36),textvariable=v_MI)
v_HI.set( "00")
v_MI.set( "00")

e_HoraFinal=Entry(window,width=2,foreground="blue",font=("verdana",36),textvariable=v_HF )
e_MinutoFinal=Entry(window,width=2,foreground="blue",font=("verdana",36),textvariable=v_MF)
v_HF.set( "23" )
v_MF.set( "59")

l_HoraInicial= Label(window,text="Horas",font=("verdana",16),bg="grey")

l_MinutoInicial= Label(window,text="Minutos",font=("verdana",16),bg="grey")

l_HoraFinal= Label(window,text="Horas",font=("verdana",16),bg="grey")

l_MinutoFinal= Label(window,text="Minutos",font=("verdana",16),bg="grey")



##################################################################################################################################################################
######################################################## RLG001 - AQUI FICA AS FOTOS E LABELS DOS RELÓGIOS INÍCIO E FIM ##########################################
##################################################################################################################################################################


























##################################################################################################################################################################
########################################## GRL001 - CONFIGURAÇÕES QUE VALEM TANTO PARA A TELA DE PESQUISA QUANDO A DE GRÁFICOS ###################################
##################################################################################################################################################################


###################################################################################################VARIAVEL TODOS TELA RESULTADOS
l_totalRegistros=Label(window,font=("Century Gothic",36),bg="lightgrey",fg="black",textvariable=totaldeRegistros)
l_totalRegistrosText=Label(window,font=("Century Gothic",12),bg="lightgrey",fg="black",text="Total de registros")
###################################################################################################VARIAVEL TODOS TELA RESULTADOS

LPfoto= PhotoImage(file="Leonardo/PNG/Logo Principal.png")
LPfoto = LPfoto.subsample(2)
LP = Label(window, image=LPfoto, bg="LightGrey")




pesquisa = ttk.Button(window)
pesquisaBotao = PhotoImage(file="Leonardo/PNG/Search 2.png")
pesquisaBotao = pesquisaBotao.subsample(4)    #Criado por: Bruno Willian Cardoso: Fiz esse para sair do sistema
pesquisa.config(image=pesquisaBotao, command=Pesquisa)





b_home = Button(window,text="inicio",font=("verdana",26),bg="yellow",command=telaInicio)



b_todosSelect=Checkbutton(window, text="Todos os Dados",variable=varTodos,offvalue=0,onvalue=1)

##################################################################################################################################################################
########################################## GRL001 - CONFIGURAÇÕES QUE VALEM TANTO PARA A TELA DE PESQUISA QUANDO A DE GRÁFICOS ###################################
##################################################################################################################################################################



























##################################################################################################################################################################
############################################## BAR001 - BARRAS QUE FICAM NO TOPO E NA PARTE DEBAIXO E SEUS BOTÕES ################################################
##################################################################################################################################################################




##############################################################################################################################################################
#DownFrame by: Bruno Willian Cardoso
#Essa parte do "DownFrame" foi editada por mim Léo. Quando se trata de um Frame, ele é como se fosse uma Label comum, porém, é uma Label que serve como "plano de fundo"
DownFrame = Frame(window, width=1150, height=40, bg="MIDNIGHTBLUE", relief="raise") 
DownFrame.pack(side=BOTTOM)
UpFrame = Frame(window, width=1150, height=40, bg="MIDNIGHTBLUE", relief="raise") 
UpFrame.pack(side=TOP)
# O que eu quero dizer, é que eu posso criar esse quadrado em algum lugar, e escrever por cima dele
##############################################################################################################################################################



SairHome = ttk.Button(window)
SairBotao = PhotoImage(file="Leonardo/PNG/sair.png")
SairBotao = SairBotao.subsample(30)    #Criado por: Bruno Willian Cardoso: Fiz esse para sair do sistema
SairHome.config(image=SairBotao, command=window.destroy)
SairHome.place(x=10, y=687)

InfoHome = ttk.Button(window) 
InfoBotao = PhotoImage(file="Leonardo/PNG/info.png")
InfoBotao = InfoBotao.subsample(65)    #Criado por: Bruno Willian Cardoso: Fiz esse para sair do sistema
InfoHome.config(image=InfoBotao, command=Info)
InfoHome.place(x=50, y=687)


voltar = ttk.Button(window)
VoltarFoto = PhotoImage(file="Leonardo/PNG/voltar.png")
VoltarFoto = VoltarFoto.subsample(25)
voltar.config(image=VoltarFoto, command=telaInicio)
voltar.place(x=280,y=500) 



LinkedPDown= Label(window,text="Linked Park @2020",font=("Century Gothic",15),bg="MIDNIGHTBLUE", fg="LightGrey")
LinkedPDown.place(x=960,y=687)



##################################################################################################################################################################
############################################## BAR001 - BARRAS QUE FICAM NO TOPO E NA PARTE DEBAIXO E SEUS BOTÕES ################################################
##################################################################################################################################################################

























##################################################################################################################################################################
#####################################################################  MNU001 - MENU PRINCIPAL  ##################################################################
##################################################################################################################################################################




########################################## Esta é a parte dos ICONES/BOTÕES EM SI do menu principal do programa #################################################
b_pesquisa = ttk.Button(window)
foto_pesquisa = PhotoImage(file="Leonardo/PNG/Search.png")
foto_pesquisa = foto_pesquisa.subsample(5)                      #Editado por: Bruno Willian Cardoso: Coloquei ícones no Menu principal
b_pesquisa.config(image=foto_pesquisa,command=telaPesquisa)
b_pesquisa.place(x=60, y=500)





b_graficos = ttk.Button(window)
grafico_pesquisa = PhotoImage(file="Leonardo/PNG/graficos.png")
grafico_pesquisa = grafico_pesquisa.subsample(5)                      #Editado por: Bruno Willian Cardoso
b_graficos.config(image=grafico_pesquisa,command=telaGraficos)
b_graficos.place(x=60, y=500)



b_atualmente = ttk.Button(window)
atualmente_pesquisa = PhotoImage(file="Leonardo/PNG/parking.png")
atualmente_pesquisa = atualmente_pesquisa.subsample(4)                      #Editado por: Bruno Willian Cardoso
b_atualmente.config(image=atualmente_pesquisa,command=___init___)
b_atualmente.place(x=60, y=500)
########################################## Esta é a parte dos ICONES/BOTÕES EM SI do menu principal do programa #################################################








titulofoto= PhotoImage(file="Leonardo/PNG/iniciofoto.png")
titulofoto = titulofoto.subsample(4)
tituloHome = Label(window, image=titulofoto, bg="LightGrey")







inicio_LP = PhotoImage(file="Leonardo/PNG/Logo Principal.png")
LogoLabel = Label(window, image=inicio_LP, bg="Lightgrey")



##################################################################################################################################################################
#####################################################################  MNU001 - MENU PRINCIPAL  ##################################################################
##################################################################################################################################################################






























##################################################################################################################################################################
###########################################################  CBX002 -COMBOBOX DA TELA DE GRAFICOS  ###############################################################
##################################################################################################################################################################
v_combobox= StringVar()
comboVaga= ttk.Combobox(window, width = 5,values=[1,2,3,4,5,6,7,8,9,10],state="readonly",textvariable=v_combobox)
##################################################################################################################################################################
###########################################################  CBX002- COMBOBOX DA TELA DE GRAFICOS  ###############################################################
##################################################################################################################################################################



























##################################################################################################################################################################
################################################################# JAN002 - CONFIGURAÇÕES GEAIS DA JANELA 2  ######################################################
##################################################################################################################################################################
#window.overrideredirect(True)
#window.wm_attributes('-type','splash')
window.title("Linked Park")
window["bg"] = "lightgrey"
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry('%dx%d+%d+%d' % (1150, 720 , width*0.2, height*0.1))
##################################################################################################################################################################
################################################################# JAN002 - CONFIGURAÇÕES GEAIS DA JANELA 2  ######################################################
##################################################################################################################################################################






















##################################################################################################################################################################
################################################################ SPL001 - TELA DE SPLASH  ########################################################################
##################################################################################################################################################################

SplashScreen = tk.Toplevel()
SplashScreen.overrideredirect(True)
width = SplashScreen.winfo_screenwidth()
height = SplashScreen.winfo_screenheight()
SplashScreen.geometry('%dx%d+%d+%d' % (width*0.8, height*0.8, width*0.1, height*0.1))
# take a .jpg picture you like, add text with a program like PhotoFiltre
# (free from http://www.photofiltre.com) and save as a .gif image file
image_file = "Leonardo/PNG/Logo Principal.png"
#assert os.path.exists(image_file)
# use Tkinter's PhotoImage for .gif files
image = tk.PhotoImage(file=image_file)
canvas = tk.Canvas(SplashScreen, height=height*0.8, width=width*0.8, bg="lightGrey")
canvas.create_image(width*0.8/2, height*0.8/2, image=image)
canvas.pack()


def DepoisSplash():
  SplashScreen.destroy()
  telaInicio()

# show the splash screen for 5000 milliseconds then destroy
SplashScreen.after(5000, DepoisSplash)

SplashScreen.mainloop()


##################################################################################################################################################################
################################################################ SPL001 - TELA DE SPLASH  ########################################################################
##################################################################################################################################################################

















##################################################################################################################################################################
################################################################ FIM001 - TELA DE FIM  ########################################################################
##################################################################################################################################################################


# window.iconbitmap(default="icones/index.ico") # Esse código é responsável por mudar o ícone do programa

window.mainloop()

##################################################################################################################################################################
################################################################ FIM001 - TELA DE FIM  ########################################################################
##################################################################################################################################################################