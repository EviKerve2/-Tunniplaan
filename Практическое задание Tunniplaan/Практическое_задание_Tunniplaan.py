from tkinter import*

tunniplaan=Tk()

def log():
    Logis=Tk()
    Logis.geometry("500x90")
    logi=Label(Logis, text="õpetaja: Klimanskaja Inessa B 002", font="Calibri 26")
    logi.pack()
    
def Ees_2():
    Eesti_2=Tk()
    Eesti_2.geometry("500x90")
    Eest_2=Label(Eesti_2, text="õpetaja: Ojamäe Olesja B 234", font="Calibri 26")
    Eest_2.pack()    
    
def mat():
    mate=Tk()
    mate.geometry("500x90")
    matem=Label(mate, text="õpetaja: Voronova Nadezda B 133", font="Calibri 26")
    matem.pack()    

def paus():
    pausi=Tk()
    pausi.geometry("500x90")
    pause=Label(pausi, text="mine sööma", font="Calibri 26")
    pause.pack() 

def keel():
    keeli=Tk()
    keeli.geometry("500x90")
    keele=Label(keeli, text="õpetaja: Mihhailova Ljudmila B 221", font="Calibri 26")
    keele.pack()

def keemia():
    keemi=Tk()
    keemi.geometry("500x90")
    keeme=Label(keemi, text="õpetaja: Pesetskaja Svetlana B 144", font="Calibri 26")
    keeme.pack()

def program():
    programi=Tk()
    programi.geometry("500x90")
    programe=Label(programi, text="õpetaja: Oleinik Marina E 07", font="Calibri 26")
    programe.pack()

def eest_1():
    eesti_1=Tk()
    eesti_1.geometry("550x90")
    eeste_1=Label(eesti_1, text="õpetaja: Laaneväli-Toots Alina B 236", font="Calibri 26")
    eeste_1.pack()

def kunsti():
    kunstii=Tk()
    kunstii.geometry("500x90")
    kunstie=Label(kunstii, text="õpetaja: Norkevit Aleksandra B 232", font="Calibri 26")
    kunstie.pack()

def kehal():
    kehali=Tk()
    kehali.geometry("500x90")
    kehale=Label(kehali, text="õpetaja: Maksõmiv Maksim Võimla A", font="Calibri 26")
    kehale.pack()

def ingl_1():
    ingli_1=Tk()
    ingli_1.geometry("500x90")
    ingle_1=Label(ingli_1, text="õpetaja: Poskotinova Olga B 138", font="Calibri 26")
    ingle_1.pack()

def rakes():
    rakesi=Tk()
    rakesi.geometry("500x90")
    rakese=Label(rakesi, text="õpetaja: Merkulova Irina E 10", font="Calibri 26")
    rakese.pack()

def rüh():
    rühi=Tk()
    rühi.geometry("550x90")
    rühe=Label(rühi, text="õpetaja: Laaneväli-Toots Alina B 236", font="Calibri 26")
    rühe.pack()

def ingl_2():
    ingli_2=Tk()
    ingli_2.geometry("500x90")
    ingle_2=Label(ingli_2, text="õpetaja: Borodina Olga B 227", font="Calibri 26")
    ingle_2.pack()

#######TUND JA KELL#######################################################################

table_esimene=Label(text="")
table_esimene.grid(row=0, column=0)

table_teine=Label(text="1 \n8:30-9:15")
table_teine.grid(row=0, column=1)

table_kolmas=Label(text="2 \n9:20-10:05")
table_kolmas.grid(row=0, column=2)

table_neljas=Label(text="3 \n10:10-10:55")
table_neljas.grid(row=0, column=3)

table_viies=Label(text="4 \n11:00-11:45")
table_viies.grid(row=0, column=4)

table_kuues=Label(text="5 \n11:50-12:35")
table_kuues.grid(row=0, column=5)

table_seitsmes=Label(text="6 \n12:40-13:25")
table_seitsmes.grid(row=0, column=6)

table_kaheksas=Label(text="7 \n13:20-14:15")
table_kaheksas.grid(row=0, column=7)

table_üheksas=Label(text="8 \n14:20-15:05")
table_üheksas.grid(row=0, column=8)

table_kümnes=Label(text="9 \n15:10-15:55")
table_kümnes.grid(row=0, column=9)

table_üheteistkümnes=Label(text="10 \n16:00-16:45")
table_üheteistkümnes.grid(row=0, column=10)

##########PÄEVAD##################################################################

table_esmas=Label(text="Esmaspäev")
table_esmas.grid(row=1,column=0, columnspan=1)

table_teisi=Label(text="Teisipäev")
table_teisi.grid(row=3,column=0, columnspan=1)

table_kolma=Label(text="Kolmapäev")
table_kolma.grid(row=5,column=0, columnspan=1)

table_nelja=Label(text="Neljapäev")
table_nelja.grid(row=7,column=0, columnspan=1)

table_reede=Label(text="Reede")
table_reede.grid(row=9,column=0, columnspan=1)

##########ESMASPÄEV##################################################################

Label(text="").grid(row=2, column=1)

Button(text="Tugiõpe Eesti keel \n2 grupp", bg="#A9A9A9", command=Ees_2).grid(row=2, column=1, sticky=W+E+N+S)

table_log=Button(text="Logistikateenused \nja varude juhtimine", bg="#3CB371", command=log)
table_log.grid(row=1, rowspan=2, column=2, columnspan=2, sticky=W+E+N+S)

table_mat=Button(text="Matemaatika", bg="#FFB6C1", command=mat)
table_mat.grid(row=1, rowspan=2, column=4, columnspan=2, sticky=W+E+N+S)

table_paus=Button(text="", command=paus)
table_paus.grid(row=1, rowspan=2, column=6, columnspan=1, sticky=W+E+N+S)

table_keel=Button(text="Keel ja kirjandus", bg="#00FF7F", command=keel)
table_keel.grid(row=1, rowspan=2, column=7, columnspan=2, sticky=W+E+N+S)

table_tmat=Button(text="Tugiõpe \n(matemaatika)", bg="#FFB6C1", command=mat)
table_tmat.grid(row=1, rowspan=2, column=9, columnspan=2, sticky=W+E+N+S) 

###########TEISIPÄEV#################################################################

table_tkem=Button(text="Tugiõpe \n(keemia)", bg="#FF00FF", command=keemia)
table_tkem.grid(row=3, rowspan=2, column=1, columnspan=1, sticky=W+E+N+S)

table_prog=Button(text="Programmeerimise alused \n(eesti keeles)", bg="#87CEFA", command=program)
table_prog.grid(row=3, rowspan=2, column=2, columnspan=3, sticky=W+E+N+S)

table_pause=Button(text="", command=paus)
table_pause.grid(row=3, rowspan=2, column=5, columnspan=1, sticky=W+E+N+S)

table_füs=Button(text="Füüsika", bg="#FFB6C1", command=mat)
table_füs.grid(row=3, rowspan=2, column=6, columnspan=2, sticky=W+E+N+S)

#########KOLMAPÄEV###################################################################

Label(text="").grid(row=6, column=0)

Button(text="Tugiõpe Eesti keel \n1 grupp", bg="#FF00FF", command=eest_1).grid(row=5, column=1, sticky=W+E+N+S)

table_kunst=Button(text="Kunstiained \n(eesti keeles)", bg="#DA70D6", command=kunsti)
table_kunst.grid(row=5, rowspan=2, column=2, columnspan=2, sticky=W+E+N+S)

table_pausi=Button(text="", command=paus)
table_pausi.grid(row=5, rowspan=2, column=4, columnspan=1, sticky=W+E+N+S)

table_keha=Button(text="Kehaline \nKasvatus", bg="#DA70D6", command=kehal)
table_keha.grid(row=5, rowspan=2, column=5, columnspan=2, sticky=W+E+N+S)

#######NELJAPÄEV######################################################################

table_logis=Button(text="Logistikateenused \nja varude juhtimine", bg="#3CB371", command=log)
table_logis.grid(row=7, rowspan=2, column=1, columnspan=2, sticky=W+E+N+S)

table_pausa=Button(text="", command=paus)
table_pausa.grid(row=7, rowspan=2, column=3, columnspan=1, sticky=W+E+N+S)

table_program=Button(text="Programmeerimise alused \n(eesti keeles)", bg="#87CEFA", command=program)
table_program.grid(row=7, rowspan=2, column=4, columnspan=2, sticky=W+E+N+S)

table_ingl=Button(text="Inglise keel \n1 grupp", bg="#F5F5DC", command=ingl_1)
table_ingl.grid(row=7, rowspan=1, column=6, columnspan=2, sticky=W+E+N+S)

table_rak=Button(text="Rakenduskeskonna ja arenduskeskkonna \nloomine IT valdkonna alusteadmised", bg="#CD5C5C", command=rakes)
table_rak.grid(row=8, rowspan=1, column=6, columnspan=2, sticky=W+E+N+S)

table_are=Button(text="Rakenduskeskonna ja arenduskeskkonna \nloomine IT valdkonna alusteadmised", bg="#CD5C5C", command=rakes)
table_are.grid(row=7, rowspan=1, column=8, columnspan=2, sticky=W+E+N+S)

table_est=Button(text="Eesti keel \n2 grupp",bg="#A9A9A9", command=Ees_2)
table_est.grid(row=8, rowspan=1, column=8, columnspan=2, sticky=W+E+N+S)

table_rüh=Button(text="Rühmajuhataja \ntund", bg="#FF00FF", command=rüh)
table_rüh.grid(row=7, rowspan=2, column=10, columnspan=1, sticky=W+E+N+S)

#####REEDE##########################################################################

table_ja=Button(text="Rakenduskeskonna ja arenduskeskkonna \nloomine IT valdkonna alusteadmised", bg="#CD5C5C", command=rakes)
table_ja.grid(row=10, rowspan=1, column=1, columnspan=2, sticky=W+E+N+S)

table_esti=Button(text="Eesti keel \n1 grupp", bg="#FF00FF", command=eest_1)
table_esti.grid(row=9, rowspan=1, column=1, columnspan=2, sticky=W+E+N+S)

table_progr=Button(text="Programmeerimise alused \n(eesti keeles)", bg="#87CEFA", command=program)
table_progr.grid(row=9, rowspan=2, column=3, columnspan=5, sticky=W+E+N+S)

table_dus=Button(text="Rakenduskeskonna ja arenduskeskkonna \nloomine IT valdkonna alusteadmised", bg="#CD5C5C", command=rakes)
table_dus.grid(row=9, rowspan=1, column=8, columnspan=2, sticky=W+E+N+S)

table_lis=Button(text="Inglise keel \n2 grupp", bg="#00FF7F", command=ingl_2)
table_lis.grid(row=10, rowspan=1, column=8, columnspan=2, sticky=W+E+N+S)

##############################################################################

tunniplaan.mainloop()