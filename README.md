# Lifting_Analytics
```
current version = 1.1
```

### About
This script is designed for tracking compound movements for resistance training. Groups that may find this helpful are powerlifters, bodybuilders, Olympic lifters, and weight training enthusiasts. To implement this script into your training, you should record your best set each workout for each unique barbell lift you do. By only recording the best set you know your data will reflect your best effort. You can create a blank log file within the script and save it on the cloud and edit it while you are in the gym. You can then use the built in functions to make decisions about your training. Such as setting up your diet, creating a program, finding openers, calcuating body fat, ect.

After loading in a log file with the proper headings, you can analyze the log file as a dataset. 

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
  <img alt="log example" src="https://github.com/JakeWnuk/Lifting_Analytics/blob/master/img/log_example.JPG">
</p>

Log files can be either excel or csv files.

After formatting the log file, you can then load it in with <b>load</b> in the file menu.

How to load a log:
<p align="center">
  <img alt="Home Menu" src="https://github.com/JakeWnuk/Lifting_Analytics/blob/master/img/getting_started.JPG">
</p>

You can add entries to the loaded log file with <b>entry</b> in the file menu. You can also add entries manually but remember to increase the index column.

### Running the script

You can either run the script in cmd, or you can run main.py.

You can type <b>help</b> for a list of commands in the current menu or type <b>help command</b>.

The currently available menus are the file, data, and home. Type the name of a menu to access its commands.

Example functions inside <b>Data</b>:
<p align="center">
  <img alt="functions" src="https://github.com/JakeWnuk/Lifting_Analytics/blob/master/img/example_data_functions.JPG">
</p>

Calculating calories and macros inside <b>Data</b>:
<p align="center">
  <img alt="calories and macros" src="https://github.com/JakeWnuk/Lifting_Analytics/blob/master/img/diet_example.JPG">
</p>

Creating a plan using your profile information <b>Data</b>:
<p align="center">
  <img alt="plan" src="https://github.com/JakeWnuk/Lifting_Analytics/blob/master/img/plan_example.JPG">
</p>

Note: to use <b>plan</b> you must first use <b>diet</b> in the data menu

Graphing Examples using <b>graph_maxes</b>:
<p align="center">
  <img alt="Home Menu" src="https://github.com/JakeWnuk/Lifting_Analytics/blob/master/img/graph_example.JPG">
</p>


## Changes Log:

Release 1.0:
<ul>
  <li>Launched with the following functions:</li>
    <ul>
      <li><b>max</b>: finds the top estimated max for a lift in a specified time frame (weeks)</li>
      <li><b>top</b>: finds the top x RM set for a lift in the past y weeks</li>
      <li><b>rm</b>: prints out the estimate RM table for a given weight and reps. Most accurate below 10 reps.</li>
      <li><b>stats</b>: reports stats for a lift in a specified time frame (weeks)</li>
      <li><b>wilks</b>: reports the users estimated wilks score at a certain body weight</li>
      <li><b>past</b>: finds the past sessions within the past x weeks or the past x sessions for y lift</li>
      <li><b>age</b>: prints the first and last entry for the log and how many days are tracked in the log.</li>
      <li><b>pril</b>: generates Prilepin's Chart and a Hypertrophy version. The standard one is considered useful for power movements and the hypertrophy one is good for volume training.</li>
      <li><b>bf</b>: calculates the users bf% using the navy seal method</li>
      <li><b>diet</b>: calculates the users TDEE / recommended caloric intake, Recommends calories for bulking & cutting and recommends macros based on goal.</li>
      <li><b>plan</b>: after creating a diet profile using diet(). Plan() will create a plan for you to achieve your next goal using your profile information.</li>
  </ul>
    <li>Launched with the following file functions:</li>
    <ul>
      <li><b>load</b>: Loads into a df a csv / excel file in a log file format. Launches a file selector.</li>
      <li><b>blank_log</b>: Prints a blank log csv file to the selected dir</li>
      <li><b>save</b>: Saves the sessions items to the selected directory</li>
      <li><b>dir</b>: Changes the directory of the output file.</li>
      <li><b>entry</b>: Creates a new entry in the loaded log file</li>
  </ul>
</ul>
Release 1.1:
<ul>
  <li>Added the following functions:</li>
    <ul>
      <li><b>graph_weight</b>: graphs the users body weight over a specified period</li>
      <li><b>graph_maxes</b>: graphs the users lift max over a specified period</li>
      <li><b>graph_freq</b>: graphs the users lift frequency over a specified period</li>
      <li><b>inol</b>: calculates the weight that should be done for X total reps to achieve the desired INOL. INOL is a formula that gives a relation between
        the intensity(weight) and the number of lifts(NOL) otherwise known as INOL.</li>
      <li><b>sample</b>: creates a sample progression for the requested lift using the INOL chart.</li>
  </ul>
  <li>Improved readability</li>
  <li>Updated documentation</li>
</ul>
