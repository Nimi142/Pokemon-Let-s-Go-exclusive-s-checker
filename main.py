from tkinter import *
from PIL import Image, ImageTk

imageSize = 100
build = "v1.1.1"
main = Tk()
main.iconbitmap('res/gamePhotos/logo.ico')
main.title("Pokemon Let's go exclusice checker")
pYesEevee = ImageTk.PhotoImage(Image.open("res/gamePhotos/YesEevee.png").resize((imageSize, imageSize), Image.ANTIALIAS))
pNoEevee = ImageTk.PhotoImage(Image.open("res/gamePhotos/NoEevee.png").resize((imageSize, imageSize), Image.ANTIALIAS))
pYesPickachu = ImageTk.PhotoImage(Image.open("res/gamePhotos/YesPikachu.png").resize((imageSize, imageSize), Image.ANTIALIAS))
pNoPickachu = ImageTk.PhotoImage(Image.open("res/gamePhotos/NoPikachu.png").resize((imageSize, imageSize), Image.ANTIALIAS))

aNames = ["bulbasaur", "ivysaur", "venusaur", "charmander", "charmeleon", "charizard", "squirtle", "wartortle",
          "blastoise", "caterpie", "metapod", "butterfree", "weedle", "kakuna", "beedrill", "pidgey", "pidgeotto",
          "pidgeot", "rattata", "raticate", "spearow", "fearow", "ekans", "arbok", "pikachu", "raichu", "sandshrew",
          "sandslash", "nidoran♀", "nidorina", "nidoqueen", "nidoran♂", "nidorino", "nidoking", "clefairy", "clefable",
          "vulpix", "ninetales", "jigglypuff", "wigglytuff", "zubat", "golbat", "oddish", "gloom", "vileplume", "paras",
          "parasect", "venonat", "venomoth", "diglett", "dugtrio", "meowth", "persian", "psyduck", "golduck", "mankey",
          "primeape", "growlithe", "arcanine", "poliwag", "poliwhirl", "poliwrath", "abra", "kadabra", "alakazam",
          "machop", "machoke", "machamp", "bellsprout", "weepinbell", "victreebel", "tentacool", "tentacruel",
          "geodude", "graveler", "golem", "ponyta", "rapidash", "slowpoke", "slowbro", "magnemite", "magneton",
          "farfetch’d", "doduo", "dodrio", "seel", "dewgong", "grimer", "muk", "shellder", "cloyster", "gastly",
          "haunter", "gengar", "onix", "drowzee", "hypno", "krabby", "kingler", "voltorb", "electrode", "exeggcute",
          "exeggutor", "cubone", "marowak", "hitmonlee", "hitmonchan", "lickitung", "koffing", "weezing", "rhyhorn",
          "rhydon", "chansey", "tangela", "kangaskhan", "horsea", "seadra", "goldeen", "seaking", "staryu", "starmie",
          "mr. mime", "scyther", "jynx", "electabuzz", "magmar", "pinsir", "tauros", "magikarp", "gyarados", "lapras",
          "ditto", "eevee", "vaporeon", "jolteon", "flareon", "porygon", "omanyte", "omastar", "kabuto", "kabutops",
          "aerodactyl", "snorlax", "articuno", "zapdos", "moltres", "dratini", "dragonair", "dragonite", "mewtwo",
          "mew","meltan"]
aPokemon = []
aEevee = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
          True, True, True, True, False, False, True, True, True, True, True, True, True, True, True, True, True, True,
          False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False,
          True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, False,
          True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
          True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
          True, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
          True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
          True, True, True, True, True, True, True, True,False

          ]
aPikachu = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, False, False, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, False, False, False, True, True, True, True, True, True, True,
            True, True, True, False, False, False, False, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True,False

            ]
pPoke = None
ltname = Label(main,text = "Name: ")
ltPokNum = Label(main,text = "Pokedex number: ")
lPokedex = Label(main,text = "Pokedex: ")
lSearchPoke = Label(main,text= "Pokemon:")
sPokedex = Spinbox(main, value=("Kanto","Johto"))
Enum = Entry(main)
fPictures = Frame(main)
Ename = Entry(main)
Epokemon = Entry(main)
lpic = Label(main, text="img", anchor=CENTER)
lenum = Label(main, text="Enter num: ", anchor=N)
lename = Label(main, text="Enter name: ", anchor=CENTER)
ldesc = Label(main, text="Desc", anchor=CENTER)
lname = Label(main, text="Name", anchor=CENTER)
leve = Label(main, image=pNoEevee, anchor= W)
lp = Label(main, image=pNoPickachu, anchor=CENTER)
lBuild = Label(main, text=build)
lCopyright = Label(main, text="Author: Nimrod Rappaport \n All rights belong to Nintendo", anchor=W)
lError = Label(main, text="All clear")

def searchpoke(event = None):
    global Epokemon
    a = Epokemon.get()
    if a.isdigit():
        a = int(a)
        p =ImageTk.PhotoImage(Image.open("res/pokemon/" + str(a) + ".png").resize((imageSize, imageSize), Image.ANTIALIAS))
        changePokemon(aNames[a-1],p)
    else:
        a = str(a)
        if a not in aNames:
            print("")
        num = aNames.index(a)
        p = ImageTk.PhotoImage(Image.open("res/pokemon/"+str(num+1)+".png").resize((imageSize, imageSize), Image.ANTIALIAS))
        changePokemon(a,p)

def capFirstLetter(st):
    st = list(st)
    st[0] = st[0].upper()
    st = "".join(st)
    return st


def changebyname(event=None):
    global lpic
    global pPoke
    st = Ename.get().lower()
    if st not in aNames:
        lError.configure(text="Enter a valid name")
        return
    try:
        pPoke = ImageTk.PhotoImage(
            Image.open("res/pokemon/" + str(aNames.index(st) + 1) + ".png").resize((imageSize, imageSize),
                                                                                   Image.ANTIALIAS))
    except:
        print("ERROR: COULD NOT FIND POKEMON IMAGE")
    changePokemon(st, pPoke)


def changebynumber(event=None):
    global lpic
    global pPoke
    global lError
    try:
        num = int(Enum.get())
    except ValueError:
        lError.configure(text="Enter a valid number")
        return
    if num > 152 or num < 1:
        lError.configure(text="Enter a number within range")
        return
    try:
        pPoke = ImageTk.PhotoImage(
            Image.open("res/pokemon/" + str(num) + ".png").resize((imageSize, imageSize), Image.ANTIALIAS))
    except FileNotFoundError:
        print("ERROR: COULD NOT FIND POKEMON IMAGE")
    changePokemon(aNames[int(Enum.get()) - 1], pPoke)


def changePokemon(pokeName, pPoke=None):
    global aNames
    global aEevee
    global aPikachu
    global lp
    global leve
    global Ename
    global lError
    lError.configure(text="All clear")
    if pPoke is not None:
        lpic.configure(image=pPoke)
        lpic.image = pPoke
    lname.configure(text=capFirstLetter(pokeName))
    ldesc.configure(text=(str(aNames.index(pokeName) + 1)))
    inEevee = aEevee[aNames.index(pokeName) ]
    inPikachu = aPikachu[aNames.index(pokeName)]
    if inEevee is True:
        leve.configure(image=pYesEevee)
    else:
        leve.configure(image=pNoEevee)
    if inPikachu is True:
        lp.configure(image=pYesPickachu)
    else:
        lp.configure(image=pNoPickachu)

lSearchPoke.grid(row = 1, column = 0)
lPokedex.grid(row = 0, column = 0)
sPokedex.grid(row = 0,column = 1)
Epokemon.grid(row = 1,column = 1)
leve.grid(row = 2,column = 0)
lp.grid(row = 2, column = 1)
lpic.grid(row = 3,column =1, rowspan = 4)
ltname.grid(row = 3, column = 0)
lname.grid(row = 4,column = 0)
ltPokNum.grid(row = 5,  column = 0)
ldesc.grid(row = 6, column = 0)
Ename.bind("<Return>", changebyname)
Enum.bind("<Return>", changebynumber)
Epokemon.bind("<Return>", searchpoke)
main.mainloop()
