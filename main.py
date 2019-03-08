from tkinter import *
from PIL import Image, ImageTk

main = Tk()
pYesEevee = ImageTk.PhotoImage(Image.open("res/gamePhotos/YesEevee.png").resize((50, 50), Image.ANTIALIAS))
pNoEevee = ImageTk.PhotoImage(Image.open("res/gamePhotos/NoEevee.png").resize((50, 50), Image.ANTIALIAS))
pYesPickachu = ImageTk.PhotoImage(Image.open("res/gamePhotos/YesPikachu.png").resize((50, 50), Image.ANTIALIAS))
pNoPickachu = ImageTk.PhotoImage(Image.open("res/gamePhotos/NoPikachu.png").resize((50, 50), Image.ANTIALIAS))

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
          "mew" ]
aEevee = ['False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False',
          'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False',
          'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False',
          'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False',
          'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False',
          'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False',
          'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False',
          'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False',
          'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False',
          'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False',
          'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False',
          'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False',
          'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False',
          ]
Enum = Entry(main)
Ename = Entry(main)
lenum = Label(main, text="Enter num: ", anchor=N)
lename = Label(main, text="Enter name: ", anchor=CENTER)
lpic = Label(main, text="img", anchor=CENTER)
ldesc = Label(main, text="Desc", anchor=CENTER)
lname = Label(main, text="Name", anchor=CENTER)
leve = Label(main, image=pNoEevee, anchor=CENTER)
lp = Label(main, image=pNoPickachu, anchor=CENTER)


def changePokemon(event=None):
    global lpic
    st = Ename.get().lower()
    # pPoke = ImageTk.PhotoImage(Image.open("res/pokemon/" + st + ".png").resize((50, 50), Image.ANTIALIAS))
    # lpic.configure(image=pPoke)
    # lpic.image = pPoke
    lpic.grid_forget()
    lpic.grid(row=0, column=0, rowspan=4)
    ldesc.configure(text=("Pokedex num: " + str(aNames.index(st) + 1)))


def changebyname(event=None):
    global lpic
    st = aNames[int(Enum.get()) - 1]
    # pPoke = ImageTk.PhotoImage(Image.open("res/pokemon/" + st + ".png").resize((50, 50), Image.ANTIALIAS))
    # lpic.configure(image=pPoke)
    # lpic.image = pPoke
    lpic.grid_forget()
    lpic.grid(row=0, column=0, rowspan=4)
    lname.configure()
    ldesc.configure(text=("Pokedex num: " + str(aNames.index(st) + 1)))



lpic.grid(row=0, column=0, rowspan=4)
leve.grid(row=4, column=0, rowspan=2)
lp.grid(row=6, column=0, rowspan=2)
lname.grid(row=0, column=1, rowspan=2)
ldesc.grid(row=2, column=1, rowspan=2)
lenum.grid(row=4, column=1)
Enum.grid(row=5, column=1)
lename.grid(row=6, column=1)
Ename.grid(row=7, column=1)
Ename.bind("<Return>", changePokemon)
Enum.bind("<Return>", changebyname)
main.mainloop()
