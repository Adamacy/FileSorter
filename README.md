# FileSorter

Simple program for sorting files with some separators in file name.<br>
Sorter is creating folder for files with same first part of name.</br>
If name is diffrent and folder doesn't exist sorter will create dir and put file in there.

## How to use

First of all we have to chose our folder with files to sort.
You can do it in this line.
```python

path_to_files = 'F:/Captures'

```

After doing this you must chose separator.

```python
 separator = ' '
```

Separator is chosing us a folder name.<br>
**Separator always chooses the first split part of the name.**

###### Example
example;file;2022_01_12.docx<br>
path_to_folder/example/example;file;2022_01_12.docx

