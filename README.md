# Lifting_Analytics
```
current version = 1.0
```

### About
This script was designed for use in regards to tracking compound movements for resistance training. Groups that may find this helpful are powerlifters, bodybuilders, olmypic lifters, and weight training enthusiests. After loading in a log file with the proper headings you can analyze the log file as a data set. 

Log files must have the following headings:

An unnamed index col, Date, Lift, RM, Weight, and Body Weight

RM represent 'rep max' or 'repetition maxium' this is the maxium number of reps the lifter could do at the given weight.

### Installing

Install requirements.txt using pip:
```
For linux:
python3 -m pip install -r /path/to/requirements.txt

For windows:
pip install -r requirements.txt


*after navigating to the project's directory in cmd
```

Launch by using a cmd or by running main.py


### Log File

A log file is needed to preform actions. You can create a blank log with <b>blank_log</b> in the file menu.

This is the proper formatting of a log file:

<p align="center">
  <img alt="Home Menu" src="https://github.com/JakeWnuk/Lifting_Analytics/blob/master/img/log_example.JPG">
</p>

Log files can be either excel or csv files

After properly formatting the log file you can then load it in with <b>load</b> in the file menu.

You can add entries to the loaded log file with <b>entry</b> in the file menu. You can also add entries manually but remember to increase the index column.

### Running the script

You can either run the script in cmd or you can run main.py

You can type <b>help</b> for a list of commands in the current menu or type <b>help command</b>

The current aviable menus are file, data, and home type the name of a menu to access it's commands

Example functions inside <b>Data</b>:
<p align="center">
  <img alt="Home Menu" src="https://github.com/JakeWnuk/Lifting_Analytics/blob/master/img/example_data_functions.JPG">
</p>

Calculating calories and macros inside <b>Data</b>:
<p align="center">
  <img alt="Home Menu" src="https://github.com/JakeWnuk/Lifting_Analytics/blob/master/img/diet_example.JPG">
</p>

Creating a plan using your profile informatin <b>Data</b>:
<p align="center">
  <img alt="Home Menu" src="https://github.com/JakeWnuk/Lifting_Analytics/blob/master/img/plan_example.JPG">
</p>

Note: to use <b>plan</b> you must first use <b>diet</b> in the data menu


