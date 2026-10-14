#pylint: skip-file

import os
import sys
import urllib

"""This is a test to see if i can update files through the internet if 
something has changed, essentially pushing out an update"""

def main() -> None:
    version:str = "1.0"
    x:int = 1
    y:int = 2
    print(x+y)

if __name__ == "__main__":
    main()
