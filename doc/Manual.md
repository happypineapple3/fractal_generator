Once the user has navigated to the main repository of where the code is found, the user must type in the following command:

'python src/main.py [FRACTAL FILE] [PALETTE NAME]'

From the main repository, providing a fractal file will look like:

'data/[FRACTAL NAME].frac'

and providing a palette name would be as simple as typing the name of the palette directly into the command line.

For example, if the user wanted to print an image of the 'julia' fractal, then the user would type:

'python src/main.py data/julia.frac [PALETTE NAME]

Providing a fractal file and palette name is optional for the user. If no file or palette is provided, then the program returns an image of a default fractal and palette. If a fractal file is provided without a palette, then a default palette is chosen. If a palette is provided without a file, then the program will crash. If only one argument is given, then it must be a fractal file. 

In order to see a list of all the fractal files, then the user will need to type:

'ls data'

After running this command, a lot of files will appear for the user to see. Any file that ends in '.frac' will be valid input for the program.

Once the user has selected a valid fractal and included it in the command, then a separate window will open up and begin drawing the fractal (keep in mind that this will save an image of the fractal into the repository where the user is running the code from). This process may take several seconds depending on the speed of the user's computer. Once the fractal is finished, then the window will remain open until the user closes it by selecting the red 'X' in the top right corner. The user will not be able to input any more commands while the window is open. While the fractal is being produced, a status bar will appear on the terminal indicating the progress of the fractal. Once the production is finished, the program will print out several things to the terminal, including: what it saved the fractal as, how long it took to write the fractal, what it saved the image as, and it will prompt the user to close the image window to exit the program. Only once the program is exited will the user be able to draw another fractal.

