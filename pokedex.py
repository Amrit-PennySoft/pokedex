from tkinter import *
from pokeapi import *

smallFont = ["Helvetica" , 14]
mediumFont = ["Helvetica" , 18]
bigFont = ["Helvetica" , 30]


def showPokemonData():
	#get numbe typed
	pokemonNumber = txtPokemonNo.get()

	#use func in pokeapi to get data
	pokemonDictionary = getPokemonData(pokemonNumber)

	#get data from dict and add it to the labels
	lblNameValue.configure(text = pokemonDictionary["name"])
	lblHpValue.configure(text = pokemonDictionary["hp"])



# GUI window
window = Tk()
window.config(bg='#e0e0ff')
window.title('Pokedex')


# label containing insructions
lblInstruct = Label(window,text='Enter a number between 1 and 718: ')
lblInstruct.pack()

# an entry textbox for the pokemon number
txtPokemonNo = Entry(window)
txtPokemonNo.pack()

# a button that will get the information
btnGetInfo = Button(window, text='Get data! ', command=showPokemonData)
btnGetInfo.pack()

#labels for pokemons
lblNameText = Label(window,text='Name:')
lblNameText.config(bg="#e0e0ff", fg="#111111", font=mediumFont)
lblNameText.pack()
lblNameValue = Label(window,text='???')
lblNameValue.config(bg="#e0e0ff", fg="#111111", font=bigFont)
lblNameValue.pack()

lblHitPoints = Label(window, text='HP: ')
lblHitPoints.pack()
lblHpValue = Label(window, text="0")
lblHpValue.pack()

window.mainloop()
