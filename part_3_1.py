from sys import argv
import os

def main( ):
    # cd to C:\Users\Tashrif Billah\Downloads\mricron
    # Call "python part_3.py CT-Thorax-Abdomen" on the command line
    os.system("dcm2nii"+' '+argv[1])

if __name__== "__main__":
    # Part 3, step 1
    main( )