# Lifting_Analytics
```
current version = 1.1
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
      <li>max: finds the top estimated max for a lift in a specified time frame (weeks)</li>
      <li>top: finds the top x RM set for a lift in the past y weeks</li>
      <li>rm: prints out the estimate RM table for a given weight and reps. Most accurate below 10 reps.</li>
      <li>stats: reports stats for a lift in a specified time frame (weeks)</li>
      <li>wilks: reports the users estimated wilks score at a certain body weight</li>
      <li>past: finds the past sessions within the past x weeks or the past x sessions for y lift</li>
      <li>age: prints the first and last entry for the log and how many days are tracked in the log.</li>
      <li>pril: generates Prilepin's Chart and a Hypertrophy version. The standard one is considered useful for power movements and the hypertrophy one is good for volume training.</li>
      <li>bf: calculates the users bf% using the navy seal method</li>
      <li>diet: calculates the users TDEE / recommended caloric intake, Recommends calories for bulking & cutting and recommends macros based on goal.</li>
      <li>plan: after creating a diet profile using diet(). Plan() will create a plan for you to achieve your next goal using your profile information.</li>
  </ul>
    <li>Launched with the following file functions:</li>
    <ul>
      <li>load</li>
      <li>blank_log</li>
      <li>save</li>
      <li>dir</li>
      <li>entry</li>
  </ul>
</ul>
Release 1.1:
<ul>
  <li>Added the following functions:</li>
    <ul>
      <li>graph_weight: graphs the users body weight over a specified period</li>
      <li>graph_maxes: graphs the users lift max over a specified period</li>
      <li>graph_freq: graphs the users lift frequency over a specified period</li>
      <li>inol: calculates the weight that should be done for X total reps to achieve the desired INOL. INOL is a formula that gives a relation between
        the intensity(weight) and the number of lifts(NOL) otherwise known as INOL.</li>
      <li>sample: creates a sample progression for the requested lift using the INOL chart.</li>
  </ul>
  <li>Improved readability</li>
  <li>Updated documentation</li>
</ul>
