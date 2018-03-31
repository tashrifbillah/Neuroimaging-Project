# Neuroimaging-Project

Instruction for replicating the notebooks in another computer: 

# Part 1:

1. Run "jupyter notebook" on a command prompt

2. Select New>Python 3 to create a notebook

# Part 2:

In the load_file(section) function, the root name has to be changed according to the location of downloaded data set.

# Part 3, step 1:

1. Install MRIcron following this [instruction](http://people.cas.sc.edu/rorden/mricron/install.html)

2. Keep the script part_3_1.py in the mricron folder. Since dcm2nii command is followed by directory name only and not the path to the directory, this step is required

3. Open command prompt

4. cd to \mricron folder

5. Call "python part_3.py CT-Thorax-Abdomen" on the command line. The folder here contains all the dicom images to be converted.

# Part 3, step 2:

 From step 1, a .nii.gz file is created inside the specified source directory. Put the path to that file as the argument of nib.load( ).
 
 # Part 4:
 
 This repository creation is the last part.



