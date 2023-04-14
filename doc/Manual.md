## How to use:
Once the user has navigated to the main repository of where the code is found, the user must type in the following command

'python src/main.py data/[FRACTAL FILE] [PALETTE NAME]'

in order to print out an image of a desired fractal in the desired color palette. 
There are two possible color palettes for the user to choose from: 'America' and 'Birthday'.
The user must capitalize the first letter of each word in order for the program to work. For example, if the user wanted to print out a Spider fractal in the Birthday color scheme, then the user would type:

'python src/main.py data/spider.frac Birthday'

Then, if the user wanted to print out the same image in the America color scheme, the user would type:

'python src/main.py data/spider.frac America'

If the user misspells one of the Paletts or inputs one that doesn't exist, then this error message will appear:

'NotImplementedError: Invalid palette requested'

If the user receives this error message, then double check spelling and capitalization and try again.

Be careful to also note how the file is specified. If the above command is run without including 'data/', then the following error will appear:

'FileNotFoundError: [Errno 2] No such file or directory: "[FRACTAL FILE]"'

The user needn't worry about this error message. To fix it, then the user only need to add 'data/' in front of the desired fractal file.

Providing a fractal file and palette name is optional for the user. If no file and no palette is provided, then the program returns an image of a default fractal and palette. If a fractal file is provided without a palette, then a default palette is chosen. If a palette is provided without a file, the program will crash; if only one argument is given, it must be a fractal file. 

For example, the user can simply type 'python src/main.py' and the program will run as if a file and palette had been provided.

Once a valid command is given by the user, then a separate window will open up and begin printing out the fractal. The time that this takes varies depending on how fast the user's computer is. As the image is printing, a status bar will appear on the terminal indicating the current progress of the print job. Once the image is finished printing, the terminal will print out what it saved the picture as and how long the printing job took. The terminal will also prompt the user to close the image window before continuing on, for the user will not be able to type any more commands until the image window has been closed.

## What are the possible fractals?
In order to view a list of all the possible fractals that can be written by the program, then the user must go into the pain repository and type

'ls data'

After inputting this command, a long list of files will appear. The user need only be concerned with files that end in '.frac'. The user can use any of these files with the program EXCEPT:

mandel-pow3.frac
mandel-pow4.frac
burningshipjulia.frac
braid.frac
newton-zoomed.frac
newton.frac

If the user tries using any of these files in the program, then the program will crash.


## Error messages and their solutions:
In additon to the error messages listed in the 'How to use:' section, there are several others that are possible for the user to see.
If the user tries inputting a file that doesn't exist, or if the user misspells the name of a file, then this error message will appear:

'FileNotFoundError: [Errno 2] No such file or directory: "data/[FILENAME]"'

If the user is met with this error, recheck spelling and ensure the file that you're trying to print does exist.

There are several problems that can occur while reading a valid fractal configuration file. If the user inputs one of the above files that are not compatible with the program, then the followng error message will appear:

'NotImplementedError: The selected fractal type is not supported. Please check the user's manual for a list of valid fractal types'

The user can check the list of valid fractal types by reading the 'What are the possible fractals?' section.

It's also possible for the program to crash if the file it's reading contains erroneous data, such as a missing data member, a misspelt word, or an incorrect data type (a word where a number should be or vice versa). There are many possible errors of this manner, though it sufficeth to provide just one specific example. The following error will occur if the program reads erroneous information from the file:

"RuntimeError: The 'centerx' value should be a floating point number. Make sure there is a colon in between the values and nothing is misspelled."

Though the program does not know exactly what the error is, it aims to be as specific as it can with the error message. From the above example, it can be deduced that there must be some sort of typo next to the 'centerx' field in the configuration file. Similar error messages will occur if any one of the many data fields are incorrect. This allows the user to find where the problem is and fix it. 





