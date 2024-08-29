# FileSorter

Simple program for sorting files with some separators in file name.<br>
Sorter is creating folder for files with same first part of name.</br>
If name is diffrent and folder doesn't exist sorter will create dir and put file in there.

## How to use

Provide path in text input or choose folder.

Choose separator which is splitting file name to parts<br>

Choose prefix which is used to choose which part of splited name you want to use.

 **See example**

## Example
example;file;2022_01_12.docx<br>
path_to_folder/example/example;file;2022_01_12.docx

##### Too high prefix
File name is *example;file;2022_01_12.docx* you can set maximum prefix to 3.<br>
Because there are 2 semicolons and you're adding 1 to it.<br>
**If number is too high error will raise.**
