from tkinter import*
from tkinter.messagebox import*
tunniplaan=Tk()
Capitals={}
Capitals = dict()
Capitals['Tugiõpe Eesti keel 2 grupp'] = 'õpetaja: Ojamäe Olesja B 234'
Capitals['Logistikateenused ja varude juhtmine'] = 'õpetaja: Klimanskaja Inessa B 002'
Capitals['Matemaatika'] = 'õpetaja: Voronova Nadezda B 133'
Capitals['Keel ja kirjandus'] = 'õpetaja: Mihhailova Ljudmila B 221'
Capitals['Tugiõpe Matemaatika'] = 'õpetaja: Voronova Nadezda B 133'
Capitals['Tugiõpe Keemia'] = 'õpetaja: Pesetskaja Svetlana B 144'
Capitals['Programmeerimise alused (eesti keeles)'] = 'õpetaja: Oleinik Marina E 07'
Capitals['Füüsika'] = 'õpetaja: Voronova Nadezda B 133'
Capitals['Tugiõpe Eesti keel 1 grupp'] = 'õpetaja: Laaneväli-Toots Alina B 236'
Capitals['Kunstiained'] = 'õpetaja: Norkevitð Aleksandra B 232'
Capitals['Kehaline Kasvatus'] = 'õpetaja: Maksõmiv Maksim Võimla A'
Capitals['Inglise keel 1 grupp'] = 'õpetaja: Poskotinova Olga B 138'
Capitals['Rakendustarkvara ja arenduskeskkonna loomine (IT valdkonna alusteadmised)'] = 'õpetaja: Merkulova Irina E 10'
Capitals['Eesti keel 2 grupp'] = 'õpetaja: Ojamäe Olesja B 234'
Capitals['Eesti keel 1 grupp'] = 'õpetaja: Laaneväli-Toots Alina B 236'
Capitals['Rühmajuhataja tund'] = 'õpetaja: Laaneväli-Toots Alina B 236'
Capitals['Inglise keel 2 grupp'] = 'õpetaja: Borodina Olga B 227'
if tunniplaan in Capitals:
	def newtunniplaan(a):
		a1=a.replace(" \n", "")
		newtn=Toplevel() 
		abc=Label(newtn,text=Capitals.get(a1),font="Calibri 23",fg="black",justify=CENTER)
		newtn.geometry("500x90")
		abc.pack()
#######TUND JA KELL#######################################################################
table_esimene=Label(text="")
table_esimene.grid(row=0, column=0)
table_teine=Label(text="1 \n8:30-9:15")
table_teine.grid(row=0, column=1, sticky=W+E+N+S)
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
Button(text="Tugiõpe Eesti keel \n2 grupp", bg="#A9A9A9").grid(row=2, column=1, sticky=W+E+N+S)
table_log=Button(text="Logistikateenused \nja varude juhtimine", bg="#3CB371")
table_log.grid(row=1, rowspan=2, column=2, columnspan=2, sticky=W+E+N+S)
table_mat=Button(text="Matemaatika", bg="#FFB6C1")
table_mat.grid(row=1, rowspan=2, column=4, columnspan=2, sticky=W+E+N+S)
table_paus=Button(text="")
table_paus.grid(row=1, rowspan=2, column=6, columnspan=1, sticky=W+E+N+S)
table_keel=Button(text="Keel ja kirjandus", bg="#00FF7F")
table_keel.grid(row=1, rowspan=2, column=7, columnspan=2, sticky=W+E+N+S)
table_tmat=Button(text="Tugiõpe \n(matemaatika)", bg="#FFB6C1")
table_tmat.grid(row=1, rowspan=2, column=9, columnspan=2, sticky=W+E+N+S) 
###########TEISIPÄEV#################################################################
table_tkem=Button(text="Tugiõpe \n(keemia)", bg="#FF00FF")
table_tkem.grid(row=3, rowspan=2, column=1, columnspan=1, sticky=W+E+N+S)
table_prog=Button(text="Programmeerimise alused \n(eesti keeles)", bg="#87CEFA")
table_prog.grid(row=3, rowspan=2, column=2, columnspan=3, sticky=W+E+N+S)
table_pause=Button(text="")
table_pause.grid(row=3, rowspan=2, column=5, columnspan=1, sticky=W+E+N+S)
table_füs=Button(text="Füüsika", bg="#FFB6C1")
table_füs.grid(row=3, rowspan=2, column=6, columnspan=2, sticky=W+E+N+S)
#########KOLMAPÄEV###################################################################
Label(text="").grid(row=6, column=0)
Button(text="Tugiõpe Eesti keel \n1 grupp", bg="#FF00FF").grid(row=5, column=1, sticky=W+E+N+S)
table_kunst=Button(text="Kunstiained \n(eesti keeles)", bg="#DA70D6")
table_kunst.grid(row=5, rowspan=2, column=2, columnspan=2, sticky=W+E+N+S)
table_pausi=Button(text="")
table_pausi.grid(row=5, rowspan=2, column=4, columnspan=1, sticky=W+E+N+S)
table_keha=Button(text="Kehaline \nKasvatus", bg="#DA70D6")
table_keha.grid(row=5, rowspan=2, column=5, columnspan=2, sticky=W+E+N+S)
#######NELJAPÄEV######################################################################
table_logis=Button(text="Logistikateenused \nja varude juhtimine", bg="#3CB371")
table_logis.grid(row=7, rowspan=2, column=1, columnspan=2, sticky=W+E+N+S)
table_pausa=Button(text="")
table_pausa.grid(row=7, rowspan=2, column=3, columnspan=1, sticky=W+E+N+S)
table_program=Button(text="Programmeerimise alused \n(eesti keeles)", bg="#87CEFA")
table_program.grid(row=7, rowspan=2, column=4, columnspan=2, sticky=W+E+N+S)
table_ingl=Button(text="Inglise keel \n1 grupp", bg="#F5F5DC")
table_ingl.grid(row=7, rowspan=1, column=6, columnspan=2, sticky=W+E+N+S)
table_rak=Button(text="Rakenduskeskonna ja arenduskeskkonna \nloomine IT valdkonna", bg="#CD5C5C")
table_rak.grid(row=8, rowspan=1, column=6, columnspan=2, sticky=W+E+N+S)
table_are=Button(text="Rakenduskeskonna ja arenduskeskkonna \nloomine IT valdkonna", bg="#CD5C5C")
table_are.grid(row=7, rowspan=1, column=8, columnspan=2, sticky=W+E+N+S)
table_est=Button(text="Eesti keel \n2 grupp",bg="#A9A9A9")
table_est.grid(row=8, rowspan=1, column=8, columnspan=2, sticky=W+E+N+S)
table_rüh=Button(text="Rühmajuhataja \ntund", bg="#FF00FF")
table_rüh.grid(row=7, rowspan=2, column=10, columnspan=1, sticky=W+E+N+S)
#####REEDE##########################################################################
table_ja=Button(text="Rakenduskeskonna ja arenduskeskkonna \nloomine IT valdkonna", bg="#CD5C5C")
table_ja.grid(row=10, rowspan=1, column=1, columnspan=2, sticky=W+E+N+S)
table_esti=Button(text="Eesti keel \n1 grupp", bg="#FF00FF")
table_esti.grid(row=9, rowspan=1, column=1, columnspan=2, sticky=W+E+N+S)
table_progr=Button(text="Programmeerimise alused \n(eesti keeles)", bg="#87CEFA")
table_progr.grid(row=9, rowspan=2, column=3, columnspan=5, sticky=W+E+N+S)
table_dus=Button(text="Rakenduskeskonna ja arenduskeskkonna \nloomine IT valdkonna", bg="#CD5C5C")
table_dus.grid(row=9, rowspan=1, column=8, columnspan=2, sticky=W+E+N+S)
table_lis=Button(text="Inglise keel \n2 grupp", bg="#00FF7F")
table_lis.grid(row=10, rowspan=1, column=8, columnspan=2, sticky=W+E+N+S)
##############################################################################
tunniplaan.mainloop()