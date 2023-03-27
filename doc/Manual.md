# Fractal Visualizer User Manual

*   This is the **user manual**, not the **programmer's manual**
    *   Keep your instructions at a user-friendly level.
*   Explain how to run the program
    *   What is the name of the main program file?
    *   What command-line arguments are needed?
*   What output does the program produce?
    *   What is shown when the program works correctly?
    *   What is shown when an error is encountered
    *   Provide examples of both!

* Once the user has navigated to the main repository of where the code is found, the user must type in the following command:
'python src/main.py [FRACTAL NAME]'. If the user does not know what fractals are available, then the user should run 'python src/main.py' all by itself. The program will then print out:

Please provide the name of a fractal as an an argument phoenix                                                                                                             peacock
monkey-knife-fight
shrimp-cocktail                                                                                                     elephants
leaf
mandelbrot
mandelbrot-zoomed
seahorse
spiral0  spiral1                                                                                                             starfish

These are all the possible fractals that the user can use with the program. With this list obtained, the user need only run the same command 'python src/main.py' followed by the name of any of the above fractals. For example, if the user wanted to print out the 'leaf' fractal, then the user would type 'python src/main.py leaf'. If the user types in a fractal that doesn't appear on the list, or if the user misspells one of the listed fractals (including capitalizions counts as a misspell), then the program will print out "ERROR: [command] is not a valid fractal." It will then print out the list of valid fractals.
* Once the user has selected a valid fractal and included it in the command, then a separate window will open up and begin drawing the fractal. This process may take several moments depending on the speed of the user's computer. Once the fractal is finished, then the window will remain open until the user closes it by selecting the red 'X' in the top right corner. The program will continue to run until the user exits the window. Until the user exits the window, the program will print out several things, including: how long it took to write the fractal, what it saved the image as, and it will prompt the user to close the image window to exit the program. Only once the program is exited will the user be able to draw another fractal.
