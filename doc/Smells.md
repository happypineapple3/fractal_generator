# CS 1440 Assignment 5.0: Refactoring - Code Smells Report

## Instructions

Edit this file and include it in your submission.

For each code smell found in the starter code:

*	Note where you found it (filename + relative information to locate the smell)
    *   You do not need to list code smells in any particular order
*	Describe the smell and why it is a problem
*	Paste up to 10 lines of offensive code between a triple-backtick fence `` ``` ```
    *   If the block of bad code is longer than 10 lines, paste a brief, representative snippet
*	Describe how you can fix it
    *   We will follow up on these notes to make sure it was really fixed!
*   At least *one instance* of each smell is required for full marks
    *   Reporting one smell multiple times does not make up for not reporting another smell
    *   Ex: reporting two global variables does not make it okay to leave spaghetti code blank



## 10 Code Smells

If you find a code smell that is not on this list, please add it to your report.

0.  **Magic** numbers
    *   These are literal values used in critical places without any context or meaning
    *   "Does the `256` right here have anything to do with the `256` over there?"


1.  **Global** variables
    *   Used to avoid passing a parameter into a function
    *   Used to return an extra value from a function
    *   There are better ways to meet both of these needs!
    *   *Note, this does not apply to global `CONSTANTS`!*



2.  **Poorly-named** identifiers
    *   Variable names should strike a good balance between brevity and descriptiveness
    *   Short variable names are okay in some situations:
        *   `i` or `j` as a counter in a brief `for` loop
        *   Variables from well-known math formulae should match the textbook (i.e. `a`, `b` and `c` are familiar in a quadratic or Pythagorean formula)
        *   Otherwise, short names should be avoided
    *   Variables with really, really long names make code harder to read
    *   Variables that override or "shadow" other identifiers
        *   Builtin Python functions such as `input`, `len`, `list`, `max`, `min` and `sum` are especially susceptible to this



3.  **Bad** Comments
    *   Comments are condiments for code; a small amount can enhance a meal, but too much ruins it
    *   Strive to write clear, self-documenting code that speaks for itself; when a line needs an explanatory comment to be understood, it indicates that identifier names were poorly chosen
    *   Delete obsolete remarks that no longer accurately describe the situation
    *   The same goes for blocks of commented-out code that serve no purpose and clutter up the file
    *   Programmers sometimes vent their frustration with snarky or vulgar comments; these add no value, are unprofessional and embarrassing, and only serve to demoralize maintainers




4.  **Too many** arguments
    *   Seen when more than a handful of parameters are passed to a function/method
    *   Parameters that are passed in but never used




5.  Function/Method that is **too long**
    *   Too many lines of code typically happens because the function/method has too many different responsibilities
    *   Generally, a method longer than a dozen lines should make you ask yourself these questions
        *   "Does one function really need to do all of this work?"
        *   "Could I split this into smaller, more focused pieces?"



6.  **Redundant** code
    *   A repeated statement which doesn't have an effect the second time
    *   Ask yourself whether it makes any difference to be run more than once
    *   ```python
        i = 7
        print(i)
        i = 7
        ```



7.  Decision tree that is **too complex**
    *   Too long or deeply nested trees of `if/elif/else`
    *   Are all of the branches truly necessary?
    *   Can all branches even be reached?
    *   Has every branch been tested?



 
8.  **Spaghetti** code
    *   Heaps of meandering code without a clear goal
    *   Functions/objects used in inconsistent ways
    *   Many variables are used to keep track of
    *   Conditional statements with long, confusing Boolean expressions
    *   Boolean expressions expressing double negatives; ex. `if not undone: ...`
    *   Code that makes you say "It would be easier to rewrite this than to understand it"




9.  **Dead** code
    *   Modules that are imported but not used
    *   Variables that are declared but not used
    *   Lines that are *never* run because they are placed in an impossible-to-reach location
        *   Code that appears after a `return` statement
            *   ```python
                return value
                value += 1
                ```
        *   Blocks of code guarded by an impossible-to-satisfy logical test
            *   ```python
                two_bee = True
                if two_bee and not two_bee:
                    print("If can you see this message, it is time to get a new CPU")
                ```
            *   ```python
                counter = 100
                while counter < 0:
                    print(f"T minus {counter}...")
                    counter -= 1
                ```
    *   Functions that are defined but never called *may* or *may not* be dead code
        *   In **Code Libraries** it is normal to define functions that are not meant to be used in the library itself
            *   It is okay to keep these functions
        *   As an **Application** evolves, calls to some of its functions may be removed until only the function's definition remains
            *   Some programmers may keep these functions "just in case" they are needed again
            *   We don't do this at DuckieCorp because we have Git; if we ever need to recover that function, we can find it in the repo's history



### Template

0.  Smell at `file` [lines xx-yy or general location]
    *   [Brief description of smell]
    *   [Code Snippet between triple-backquotes `` ``` ``]
    *   [How to resolve]


### Example

0.  Redundant Code at `src/main.py` [lines 28, 30]
    *   The import statement `import mbrot_fractal` occurs twice.  A second occurrence doesn't do it better than the first
    *   ```python
        import mbrot_fractal
        import phoenix_fractal as phoenix
        import mbrot_fractal
        ```
    *   Remove the second `import` statement



## Code Smells Report*

0.
* In phoenix_fractal.py, there is the statement:
```
print(f"[{fraction_of_pixels_writtenSoFar:>4.0%}"  	  	  
                + f"{'=' * int(34 * fraction_of_pixels_writtenSoFar):<33}]",  	  	  
                end="\r"  # the end  	  	  
                , file=sys.stderr)
```
On the second line in the mentioned code, the number 34 is used in the statement. The reason for using 34 is never listed
and tossed into the code. This will make it hard to debug the code in case a future bug arises in this area of the code. 
The problem might be because of the number 34, or it might be because of something else. This magic number will make it 
hard to debug. To fix this, I'll search the document for the meaning of 34 and replace it with a global
constant or at least a properly named variable. This will make it easier to know what 34 means for future programmers
who will look at this code.

1.
* In phoenix_fractal.py, a number of global variables are used. For example:
```
    global grad  	  	  
    global win  
```
There are many cases throughout where a variable is introduced as 'global'. This is simply not a good practice to have. 
Not only does it raise security risks, but they're very existence is unnecessary; they are simply extra variables that 
do not need to exist. This makes the code more extravagant than it needs to be. To fix this specific smell, I plan
to incorporate 'grad' and 'win' as parameters for the function they're inside of. 

2.
* In phoenix_fractal.py: there is the statement:
```
s = 512
```
Only after reading through the documentation is it clear that 512 is the width and height of the painted fractal image.
Though this didn't affect how the code works, it certainly made it difficult for me to understand exactly what it is. I
wasted time trying to figure out what 's' is. The fix to this is simple. I'll rename 's' into a more descriptive name
and make it a global constant (for example, SCREEN_SIZE). This will make it easier for future programmers to understand
the documentation.

3.
* Though there are unnecessary comments scattered throughout the program, the one that takes the cake is found in
main.py. Too much to directly copy, the commented code is a series of pound symbols forming a design over a few dozen
lines of code. In the middle of this design, there is printed 'CODE IS ART'. This entire comment is bulky and just
adds to the confusion of the code. To fix this, I will merely delete all of the comments that make up the design.

4.
* The most parameters that I've seen in a function can be found in phoenix_fractal.py:
```
def makePictureOfFractal(f, i, e, w, g, p, W, a, b, s):  	  	  
```
Not only are these arguments poorly named, but half of them aren't even used in the program. When this function does
get called, portions of the arguments are passed in as 'None'. This makes for unnecessary code that makes the overall
program harder to understand. I will do two things to fix this function name: first, I will remove the arguments that
are never called. Second, I will rename the arguments so that the function will be self-documenting.

5.
* In the mbrot_fractal.py module, there is a function that serves two purposes depending on what is passed in:
```
def PixelColorOrIndex(c, palette): 
 	  	  
    """  	  	  
    Return the color of the current pixel within the Mandelbrot set  	  	  
    - OR -  	  	  
    Return the INDEX of the color of the pixel within the Mandelbrot set  	  	  
    The INDEX corresponds to the iteration count of the for loop.  	  	  
    """
```
This is a problem because functions should only have one purpose; having multiple moving parts in a single function makes
it harder to debug and understand. To fix this smell, I plan on separating this function into two functions: one for
each purpose as explained in the copied portion of the program.

6.
* In mbrot_fractal.py, there is the statement
```
portion = 512 - row / 512  	  	  
window.update()  # display a row of pixels  	  	  
portion = 512 - row / 512 # prepare for next loop
```
Having portion defined twice twice serves no purpose in changing its value. This is simply acting as an extra line 
that serves to confuse the programmer, and the best way to fix this is to delete one of the two statements. 
Only one statement per variable is necessary.

7.
* One of the biggest decision trees located in this program is found in the module main.py:
```
if PHOENX.count(sys.argv[1])>0: phoenix.phoenix_main(sys.argv[1])  	  	  
elif sys.argv[1] in MBROTS and len(sys.argv) > 1 and 2 <= len(sys.argv[0]):  	  	  
    fractal = sys.argv[1]  	  	  
    mbrot_fractal.mbrot_main(fratcal)  	  	  
elif len(sys.argv) != 0 and fratcal in PHOENX and len(sys.argv) != 1:  	  	  
    phoenix.phoenix_main(fractal)  	  	  
else: print("The fractal given on the command line",  	  	  
            fractal,  	  	  
            "was not found in the command line")
```
This is a confusing bit of logic right here, and that makes it really hard to determine what's going on. There are too
many if/elif/else statements, and it appears to me that some of them are unnecessary. This bit of code makes it difficult
to follow the logic that the program uses. It also makes it difficult to tell if its even possible to reach every decision
in the tree. By the looks of it, there are two statements there that serve the same purpose. To fix this, I'll try
rewriting the tree in pseudocode to make sure I can follow the logic it's using, and then I'll simplify the logic by
using fewer statements in the tree.

8.
* Looking in main.py we find the code:
```
quit = False                                           #  	  	  
    next = ''                                               	  	  
    iter = 0                                                  	  	  
    while not quit:
```
The rest of this portion is more confusing, but it's enough to focus on this section. Here, 'quit' is defined as 'False',
followed by a loop conditioned by 'while not quit'. This is the exact same as saying 'while not false' which is equivalent to
'while true'. It's much more simple to write the last statement there, and writing the code as copied above only serves
to add confusing logic into the program. Sure, it works, but it's much easier and clearer to use concise logic rather
than working with double negatives.

9.
* In phoenix_fractal.py, we find two return statements:
```
return grad[101]           	  	  
return grad[102]
```
Only the first return statement is ever reached. The second one will never get returned and is therefore unnecessary.
Deleting the second statement will not change anything about how the code works.