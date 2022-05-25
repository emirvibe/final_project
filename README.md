# final_project

Python version above 3.10 required
To run the program, use the python3 main.py command

The program will merge the selected files
Files may have different extensions
To merge, you must select two or more files, specify the name of the file in which the data will be saved, if the file exists and it contains information, new data will be added to it, if there is no file, it will be created
There is a button for clearing selected files, a button for deleting a file (from the table for merging)

Exceptions:

Deletion error - occurs when no item is selected to delete.

![de](https://user-images.githubusercontent.com/102587539/170175081-99c98084-b03a-489e-82e2-c70eaf6a87c2.png)


Recursion error: occurs when trying to select the same file more than 1 time

![re](https://user-images.githubusercontent.com/102587539/170175112-5036e356-5f46-4c0e-924b-3cb822d94acf.png)


Length error: occurs if less than two files are selected

![count](https://user-images.githubusercontent.com/102587539/170175140-e21aa27a-cec7-4a9a-84bd-23fd6df59931.png)


Name error: occurs if no filename is given

![nam](https://user-images.githubusercontent.com/102587539/170175151-0d019754-b697-4735-b61c-4edde12665b6.png)
