# Lifting_Analytics
```
current version = 1.0
```

### About
This script was designed for use in regards to tracking compound movements for resistance training. Groups that may find this helpful are powerlifters, bodybuilders, olympic lifters, and weight training enthusiasts. After loading in a log file with the proper headings, you can analyze the log file as a dataset. 

Log files must have the following headings:

An unnamed index col, Date, Lift, RM, Weight, and Body Weight

RM represent 'rep max' or 'repetition maximum' this is the maximum number of reps the lifter could do at the given weight.

### Installing

Install requirements.txt using pip:
```
For Linux:
python3 -m pip install -r /path/to/requirements.txt

For Windows:
pip install -r requirements.txt


*after navigating to the project's directory in cmd
```

Launch by using a cmd or by running main.py.


### Log File

A log file is needed to perform actions. You can create a blank log with <b>blank_log</b> in the file menu.

This is the proper formatting of a log file:

<p align="center">
  <img alt="Home Menu" src="https://github.com/JakeWnuk/Lifting_Analytics/blob/master/img/log_example.JPG">
</p>

Log files can be either excel or csv files.

After formatting the log file, you can then load it in with <b>load</b> in the file menu.

You can add entries to the loaded log file with <b>entry</b> in the file menu. You can also add entries manually but remember to increase the index column.

### Running the script

You can either run the script in cmd, or you can run main.py.

You can type <b>help</b> for a list of commands in the current menu or type <b>help command</b>.

The currently available menus are the file, data, and home. Type the name of a menu to access its commands.

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


## Changes Log:

Release 1.0:
<ul>
  <li>Launched with the following functions:</li>
    <ul>
      <li>max</li>
      <li>top</li>
      <li>rm</li>
      <li>stats</li>
      <li>wilks</li>
      <li>past</li>
      <li>age</li>
      <li>pril</li>
      <li>bf</li>
      <li>diet</li>
      <li>plan</li>
  </ul>
</ul>
Planned 1.1:
<ul>
  <li>Prints to consoles in different colors</li>
  <li>New graphing functions</li>
</ul>
