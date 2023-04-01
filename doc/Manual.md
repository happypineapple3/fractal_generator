Once the user has navigated to the main repository of where the code is found, the user must type in the following command:

'python src/main.py [FRACTAL NAME]'

If the user does not know what fractals are available, then the user should run 'python src/main.py' all by itself. The program will then print out:

USAGE: plase input the name of one of the following fractals as an argument
phoenix
peacock
monkey-knife-fight
shrimp-cocktail
elephants
leaf
mandelbrot
mandelbrot-zoomed
seahorse
spiral0
spiral1
starfish

These are all the possible fractals that the user can use within the program. With this list in mind, the user need only run the same command 'python src/main.py' followed by the name of any of the above fractals. For example, if the user wanted to print out the 'leaf' fractal, then the user would type:

'python src/main.py leaf'

If the user types in a fractal that doesn't appear on the list, or if the user misspells one of the listed fractals (including capitalizions counts as a misspell), then the program will print out 

"ERROR: [argument] is not a valid fractal." 
It will then print out the list of valid fractals.

Once the user has selected a valid fractal and included it in the command, then a separate window will open up and begin drawing the fractal (keep in mind that this will save an image of the fractal into the repository where the user is running the code from). This process may take several seconds depending on the speed of the user's computer. Once the fractal is finished, then the window will remain open until the user closes it by selecting the red 'X' in the top right corner. The user will not be able to input any more commands while the window is open. While the fractal is being produced, a status bar will appear on the terminal indicating the progress of the fractal. Once the production is finished, the program will print out several things to the terminal, including: what it saved the fractal as, how long it took to write the fractal, what it saved the image as, and it will prompt the user to close the image window to exit the program. Only once the program is exited will the user be able to draw another fractal.
