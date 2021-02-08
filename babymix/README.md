# Babymix

This challenge is a flag checker that will take a single input via fgets.
Taking a quick look at the binary, we can see that this binary will run our input through a set of "check" functions.
If all checks are passed the program will let us know we have the corrrect flag. 
We can also see from looking through the binary that the flag will be between 0x15 and 0x30 chars long.

To solve this challenge, I used Angr as I wanted to learn how to use it.  Using Angr, you can craft a script that will 
avoid the fail condition `0x00102238` and look for the success condition `0x00102225` 
(assuming a 0x00100000 base address).

Once this script with crafted, we can run against the given binary to to find the flag.
