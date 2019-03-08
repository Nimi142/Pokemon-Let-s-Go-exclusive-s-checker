from tkinter import *

from PIL import Image, ImageTk

imageSize = 100
build = "v1.1.1"
main = Tk()
pYesEevee = ImageTk.PhotoImage(
    Image.open("res/gamePhotos/YesEevee.png").resize((imageSize, imageSize), Image.ANTIALIAS))
pNoEevee = ImageTk.PhotoImage(Image.open("res/gamePhotos/NoEevee.png").resize((imageSize, imageSize), Image.ANTIALIAS))
pYesPickachu = ImageTk.PhotoImage(
    Image.open("res/gamePhotos/YesPikachu.png").resize((imageSize, imageSize), Image.ANTIALIAS))
pNoPickachu = ImageTk.PhotoImage(
    Image.open("res/gamePhotos/NoPikachu.png").resize((imageSize, imageSize), Image.ANTIALIAS))

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
          "mew"]
aEevee = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
          True, True, True, True, False, False, True, True, True, True, True, True, True, True, True, True, True, True,
          False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False,
          True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, False,
          True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
          True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
          True, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
          True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
          True, True, True, True, True, True, True, True,

          ]
aPikachu = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, False, False, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, False, False, False, True, True, True, True, True, True, True,
            True, True, True, False, False, False, False, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True,

            ]
pPoke = None
Enum = Entry(main)
Ename = Entry(main)
lenum = Label(main, text="Enter num: ", anchor=N)
lename = Label(main, text="Enter name: ", anchor=CENTER)
lpic = Label(main, text="img", anchor=CENTER)
ldesc = Label(main, text="Desc", anchor=CENTER)
lname = Label(main, text="Name", anchor=CENTER)
leve = Label(main, image=pNoEevee, anchor=CENTER)
lp = Label(main, image=pNoPickachu, anchor=CENTER)
lBuild = Label(main, text=build)
lCopyright = Label(main, text="Author: Nimrod Rappaport \n All rights belong to Nintendo", anchor=W)
lError = Label(main, text="All clear")


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
    if num > 151 or num < 1:
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
    ldesc.configure(text=("Pokedex num: " + str(aNames.index(pokeName) + 1)))
    inEevee = aEevee[aNames.index(pokeName) + 1]
    inPikachu = aPikachu[aNames.index(pokeName) + 1]
    if inEevee is True:
        leve.configure(image=pYesEevee)
    else:
        leve.configure(image=pNoEevee)
    if inPikachu is True:
        lp.configure(image=pYesPickachu)
    else:
        lp.configure(image=pNoPickachu)


lpic.grid(row=0, column=0, rowspan=4)
leve.grid(row=4, column=0, rowspan=2)
lp.grid(row=6, column=0, rowspan=2)
lname.grid(row=0, column=1, rowspan=2)
ldesc.grid(row=2, column=1, rowspan=2)
lenum.grid(row=4, column=1)
Enum.grid(row=5, column=1)
lename.grid(row=6, column=1)
Ename.grid(row=7, column=1)
lBuild.grid(row=8, column=0)
lError.grid(row=8, column=1)
lCopyright.grid(row=9, column=0, columnspan=2)
Ename.bind("<Return>", changebyname)
Enum.bind("<Return>", changebynumber)
main.mainloop()
