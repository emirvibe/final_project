# final_project

Python version above 3.10 required
To run the program, use the python3 main.py command

The program will merge the selected files
Files may have different extensions
To merge, you must select two or more files, specify the name of the file in which the data will be saved, if the file exists and it contains information, new data will be added to it, if there is no file, it will be created
There is a button for clearing selected files, a button for deleting a file (from the table for merging)

Exceptions:

Deletion error - occurs when no item is selected to delete.

Recursion error: occurs when trying to select the same file more than 1 time

Length error: occurs if less than two files are selected

Name error: occurs if no filename is given