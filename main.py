#! python3

# Author Jake Wnuk
# LinkedIn: www.linkedin.com/in/jakewnuk
# Lifting Analytics

"""
 Description: A program that reads a predictable template and outputs stats about the user
 Input: A predictable template in a  excel or csv file.
"""

# key error on load if template wrong

import os
import sys
import tkinter
from cmd import Cmd
from datetime import datetime
from pathlib import Path
from tkinter.filedialog import askopenfilename
import pandas as pd
import Lifting_Analytics as log

# checks for latest version
if sys.version_info[0] < 3:  # Tells the user what version is needed.

    raise Exception("Python 3 or a more recent version is required.")

# Makes variables that will be used by multiple functions asynchronously
global curr_directory
global curr_log
global profile

profile = pd.Series()
curr_log = pd.DataFrame(columns=['Date', 'Lift', 'RM', 'Weight', 'Body Weight'])
curr_directory = Path(os.getcwd())  # will get current working directory


class MyPrompt(Cmd):
    """ Core """

    @staticmethod
    def do_home(args):
        """Return home"""
        n_cli = MyPrompt()
        n_cli.prompt = '<Home> '
        f = open('banner.txt', 'r')
        banner = f.read()
        print(banner)
        prompt.cmdloop('\n Jake Wnuk| Type help for commands | Type help <command> for documentation. \n')

    @staticmethod
    def do_file(args):
        """
        Opens the file options for saving/exporting session data
        """

        n_cli = FileCommands()
        n_cli.prompt = '<File> '
        n_cli.cmdloop('\n File Options Menu | type help for commands')

    @staticmethod
    def do_data(args):
        """
        Opens the options for analyzing the data
        """
        n_cli = DataCommands()
        n_cli.prompt = '<Data> '
        n_cli.cmdloop('\n Data Analysis Menu | type help for commands')

    @staticmethod
    def do_author(args):
        """
        About the author.
        """

        if len(args) == 0:
            print(r"""

            This script was written by Jake Wnuk.
            LinkedIn https://www.linkedin.com/in/jakewnuk/
            Git: https://github.com/JakeWnuk
            """)

    @staticmethod
    def do_quit(args):
        """
        Quits the program.
        """
        print("Quitting.")
        raise SystemExit

    @staticmethod
    def do_walkthrough(args):
        """
        Call on me when you do not know what to do
        """
        print(r"""
            
            Lifting Analytics Getting Started:
            
            To use this script you will need to load in a log file with data. After loading a file you can preform tests on that data set.
            
            Functions of the script are separated into different groups type the name of the group to access their commands
            
            Loading a log file:
             - You can load a log with load under the file menu
             - You can also create a new log with blank_log in the file menu
             
            Analyzing Data:
             - You can access the data analysis menu by typing data
             - All options to analyze data are in the data menu
             
            Type help or help <command> to see the full list of commands or information about a specific command
        
        """)


class FileCommands(MyPrompt):
    """ Houses all file commands """

    @staticmethod
    def do_load(args):
        """
        Loads into a df a csv / excel file in a log file format. Launches a file selector.
        example: load -> File Selector -> Results

        Required Table Headers:
        Index, Date, Lift Name, RM, Weight, Body Weight
        """

        global curr_log  # trying to think of a better way to do this
        tkinter.Tk().withdraw()
        file = askopenfilename()

        try:
            # check for csv or excel
            try:
                curr_log = pd.read_csv(file, index_col=[0]).dropna(how='all')
            except UnicodeDecodeError:
                curr_log = pd.read_excel(file, index_col=[0]).dropna(how='all')

            # do some formatting to ensure quality
            curr_log['Lift'] = curr_log['Lift'].str.lower()
            curr_log['Date'] = pd.to_datetime(curr_log.Date)
            curr_log = curr_log.sort_values(by='Date', ascending=False)
            curr_log = curr_log.reset_index(drop=True)
            print("The log has been read in. \n")
        except (FileNotFoundError, AttributeError):
            print("File not found or compatible. Does the file have an unnamed index col? \n")

    @staticmethod
    def do_blank_log(args):
        """
        Prints a blank log csv file to the selected dir
        """

        if query_yes_no("Would you like to create a new blank log to " + str(curr_directory) + '\n'):
            blog = pd.DataFrame(columns=['Date', 'Lift', 'RM', 'Weight', 'Body Weight'])
            blog.to_csv(os.path.join(str(curr_directory), 'Blank Log.csv'))
            print('The log has been saved to' + str(curr_directory) + '\n')

    @staticmethod
    def do_save(args):
        """
        Saves the sessions items to the selected dir
        """

        # if no args are provided do a walk through
        while args == "":
            args = input("What type of file would you like to save? \n log or report?")

        # checks for log
        if str(args).lower() == "log":
            global curr_log

            if query_yes_no("Would you like to save this sessions log to " + str(curr_directory) + '\n'):
                curr_log = curr_log.dropna(how='all')
                curr_log['Lift'] = curr_log['Lift'].str.lower()
                curr_log['Date'] = pd.to_datetime(curr_log.Date)
                curr_log = curr_log.sort_values(by='Date', ascending=False)
                curr_log = curr_log.reset_index(drop=True)

                curr_log.to_csv(
                    os.path.join(str(curr_directory), 'Lifting Log' + str(datetime.now().strftime("_%Y")) + ".csv"),
                    index=[0])
                print('The log has been saved to ' + str(curr_directory) + '\n')
        # checks for report
        elif str(args).lower() == "report":
            print("No print report currently exists. \n")
        else:
            print("Not a valid argument. \n")

    @staticmethod
    def do_dir(args):
        """
        Changes the directory of the output file. Type dir to see the current name without changes. Type dir c to change.
        example: dir -> The current directory is:
                 dir c -> opens a selector for a new path
        """

        global curr_directory  # Trying to think of a better way to do this
        if len(args) == 0:
            print("The current directory is: " + str(curr_directory) + '\n')

        # I don't actually check for 'C' in the args lmao
        else:
            tkinter.Tk().withdraw()
            curr_directory = tkinter.filedialog.askdirectory()
            print("The current directory is: " + str(curr_directory) + '\n')

    @staticmethod
    def do_entry(args):
        """
        Creates a new entry in the log file
        example:
            entry -> walk through

        Note: limited call options to avoid bad entries
        """

        l = input('Lift performed:')
        d = input('Date M/D/Y :')
        r = input('Reps performed:')
        w = input('Weight lifted:')
        b = input('Body weight:')

        new_row = pd.DataFrame({'Date': d, 'Lift': l, 'RM': int(r), 'Weight': int(w), 'Body Weight': float(b)},
                               index=[0])

        global curr_log
        curr_log = curr_log.append(new_row, ignore_index=True, sort=False)

        curr_log['Lift'] = curr_log['Lift'].str.lower()
        curr_log['Date'] = pd.to_datetime(curr_log.Date)
        curr_log = curr_log.sort_values(by='Date', ascending=False)
        curr_log = curr_log.reset_index(drop=True)

        print('The entry has been added. \n')


class DataCommands(MyPrompt):
    """ Houses all functions on data """

    @staticmethod
    def do_max(args):
        """
        Finds the top estimated max for a lift in a specified time frame (weeks)
        example:
                max -> walk through
                max bench -> finds best bench of all time
                max bench, 9 -> finds best bench of past 9 weeks
        """

        try:
            # if no args do a walk through
            if len(args) == 0:
                name = input('What lift would you like to find your top estimated max for? \n')
                weeks = input('How many weeks would you like to look back? Type 0 for max. \n')
            else:
                # if args are provided try to use them
                try:
                    name, weeks = [s for s in args.split(',')]
                # if only one args is provided use none
                except ValueError:
                    name = args
                    weeks = 0

            # error filtering
            if round(float(weeks)) < 1 or round(float(weeks)) > 9999:
                weeks = 9999

            print('\n' + str(log.top_max(curr_log, name, round(float(weeks)))) + '\n')

        except KeyError:
            print("\n Please check syntax or no results found \n")

    @staticmethod
    def do_top(args):
        """
        Finds the top x RM set for a lift in the past y weeks
        example:
                top -> walk through
                top bench, 9 -> finds best bench 9 rm of all time
                top bench, 9, 4 --> finds the best 9 rm of the past 4 weeks
        """

        try:
            # if no args do a walk through
            if len(args) == 0:
                name = input('What lift would you like to find your top set for? \n')
                rm = input('What number of reps would you like to find your top weight for? \n')
                weeks = input('How many weeks would you like to look back? Type 0 for max. \n')
            else:
                # if args are provided try to use them
                try:
                    items = args.split(',')
                    name = items[0]
                    rm = items[1]
                    weeks = items[2]
                # if only one args is provided use none
                except IndexError:
                    items = args.split(',')
                    name = items[0]
                    rm = items[1]
                    weeks = 0

            # error filtering
            if round(float(weeks)) < 1 or round(float(weeks)) > 9999:
                weeks = 9999

            print('\n' + str(log.top_max(curr_log, name, round(float(weeks)), reps=round(float(rm)))) + '\n')

        except (KeyError, UnboundLocalError, IndexError, ValueError):
            print("Please check syntax or no results found \n")

    @staticmethod
    def do_rm(args):
        """
        prints out the estimate RM table for a given weight and reps. Most accurate below 10 reps.
        example:
            rm 400, 5
        """
        try:
            # if no args do a walk through
            if len(args) == 0:
                weight = input('Weight Lifted? \n')
                reps = input('Number of Reps? \n')
            else:
                # try to use args
                weight, reps = [float(s) for s in args.split(',')]

            # making the data frame
            rm_table = pd.DataFrame(columns=["Rep Max", "Weight"])
            for i in range(1, 11):
                rm_table = rm_table.append({'Rep Max': i, "Weight": log.estimate_rm(i, float(weight), int(reps))},
                                           ignore_index=True)
            rm_table = rm_table.set_index('Rep Max')
            print('\n' + str(rm_table) + '\n')

        except ValueError:
            print("Please check syntax \n")

    @staticmethod
    def do_stats(args):
        """
        reports stats for a lift in a specified time frame (weeks)
        example:
                stats -> walk through
                stats bench -> finds stats about bench from all time
                stats bench, 9 -> finds stats about bench from the last 9 weeks
        """

        try:
            # if no args do a walk through
            if len(args) == 0:
                name = input('What lift would you like to find stats for? \n')
                weeks = input('How many weeks would you like to look back? Type 0 for max. \n')
            else:
                # if args are provided try to use them
                try:
                    name, weeks = [s for s in args.split(',')]
                # if only one args is provided use none
                except ValueError:
                    name = args
                    weeks = 0

            # error filtering
            if int(weeks) < 1 or int(weeks) > 9999:
                weeks = 9999
            print('\n Stats using converted 1RMs:')
            print(str(log.stats(curr_log, name, int(weeks))) + '\n')

        except (KeyError, ValueError):
            print("Please check syntax \n")

    @staticmethod
    def do_wilks(args):
        """
        reports the users estimated wilks score at a certain body weight
        example:
                wilks -> walk through
                wilks 185 -> finds the best lifts @ 185 and estimates a wilks score
                wilks 185, f -> finds the best lifts @ 185 and estimates a wilks score for females

                Note: This is set to take in only lbs if you want kgs edit the function in the code
        """

        try:
            # if no args do a walk through
            if len(args) == 0:
                weight = float(input('At what body weight would you like to find your best estimated wilks score? \n'))
                gender = input('Is the lifter considered male or female? \n')
            else:
                # if args are provided try to use them
                try:
                    weight, gender = [s for s in args.split(',')]
                    weight = float(weight)
                # if only one args is provided use none
                except ValueError:
                    weight = float(args)
                    gender = ''

            print()  # for formatting

            # filter for female
            if str(gender).lower().strip() in ['female', 'f']:
                print(str(log.wilks(curr_log, int(round(weight)), male=False)) + '\n')
            else:
                print(str(log.wilks(curr_log, int(round(weight)))) + '\n')

        except (KeyError, ValueError):
            print("Not enough information found at that body weight \n")

    @staticmethod
    def do_past(args):
        """
        Finds the past sessions within the past x weeks or the past x sessions for y lift
        example:
                past -> walk through
                past 9 -> shows the sessions from the past 9 weeks
                past 9, bench -> shows the past 9 weeks sessions for bench
        """

        try:
            # if no args do a walk through
            if len(args) == 0:
                weeks = input('How many weeks would you like to look back? Type 0 for max. \n')
                name = input('What lift would you like to look for? Enter to skip. \n')
            else:
                # if args are provided try to use them
                try:
                    weeks, name = [s for s in args.split(',')]
                # if only one args is provided use none
                except ValueError:
                    weeks = args
                    name = ""
            # error check
            if int(weeks) < 1 or int(weeks) > 9999:
                weeks = 9999

            # if the name exists then pass it
            if name != "":
                print(log.past(curr_log, int(weeks), lift=str(name).strip()))
                return
            else:
                print('\n' + str(log.past(curr_log, int(weeks))) + '\n')

        except (KeyError, ValueError):
            print("Please check syntax \n")

    @staticmethod
    def do_age(args):
        """
        Prints the first and last entry for the log and how many days are tracked in the log.
        """

        last, first = curr_log['Date'].iloc[0], curr_log['Date'].iloc[-1]

        a = pd.Series({
            'First Entry': first.strftime('%m/%d/%Y'),
            'Last Entry': last.strftime('%m/%d/%Y'),
            'Age': (last - first)
        })
        print('\n' + a.to_string() + '\n')

    @staticmethod
    def do_pril(args):
        """
        Generates Prilepin's Chart and a Hypertrophy version. The standard one is considered useful for power movements and the hypertrophy one is good for volume training.
            example:
            pril -> walk through
            pril bench -> generates charts based off your est max bench
            pril bench, 9 -> generates charts based off your est max bench of the past 9 weeks
        """

        try:
            # if no args do a walk through
            if len(args) == 0:
                name = input('What lift would you like to generate Prilepins Chart for? \n')
                weeks = input('How many weeks would you like to look back? Type 0 for max. \n')
            else:
                # if args are provided try to use them
                try:
                    name, weeks = [s for s in args.split(',')]
                # if only one args is provided use the default
                except ValueError:
                    name = args
                    weeks = 0

            # error checking
            if int(weeks) < 1 or int(weeks) > 9999:
                weeks = 9999

            print('\n' + str(log.prilepin(curr_log, name, int(weeks))) + '\n')

        except (KeyError, ValueError):
            print("Please check syntax \n")

    @staticmethod
    def do_bf(args):
        """
        Calculates the users bf% using the navy seal method
            example:
            bf -> walk through
            bf male -> calculates bf% off last weight entry
            bf female -> calculates bf% off last weight entry
        """

        try:
            # if no args do a walk through
            if len(args) == 0:
                gender = input('Is the lifter considered male or female? \n')
            else:
                try:
                    # if args are provided try to use them
                    if args.lower() in ['f', 'female']:
                        gender = 'female'
                    else:
                        gender = 'male'
                except ValueError:
                    print('Value Error \n')

            if gender in ['f', 'female']:
                gender = 'female'
            else:
                gender = 'male'

            bfp = log.bf(curr_log, gender)
            print('\n' + str(bfp) + '\n')

        except (KeyError, ValueError):
            print("Please check syntax \n")

    @staticmethod
    def do_diet(args):
        """
        Calculates the users TDEE / recommended caloric intake, Recommends calories for bulking & cutting and recommends macros based on goal.
            example:
            diet -> walk through
            diet 13 -> calculates the users tdee @ 13% bf with a prompt for bulking or cutting
            diet 13, cut -> calculates the users tdee @ 13% bf for cutting (other args: bulk, b, c)
        """

        try:
            # if no args do a walk through
            if len(args) == 0:
                bf = input('What is your body fat %? \n')
                goal = input('Would you like to bulk or cut? \n')
            else:
                # if args are provided try to use them
                try:
                    bf, goal = [s for s in args.split(',')]
                # if one is provided ask for the other
                except ValueError:
                    bf = args
                    goal = input('Would you like to bulk or cut? \n')

            global profile
            weight = curr_log.loc[0]['Body Weight']  # takes in current body weight from the log
            profile = log.diet(weight, bf, goal)  # assigns the diet profile generated to this sessions profile
            macro = log.macro(profile)  # runs macros

            print('\n Diet Information:')
            print('\n' + profile.to_string())
            print('\n Recommended Macros:')
            print(macro.to_string() + '\n')

        except (KeyError, ValueError, UnboundLocalError):
            print("Please check syntax \n")

    @staticmethod
    def do_plan(args):
        """
        After creating a diet profile using diet(). Plan() will create a plan for you to achieve your next goal using your profile information.
        Example:
            plan -> walk through
            plan 200 -> plans goal til 200 jumping by default (1 week)
            plan 200, 2 -> plans goal til 200 jumping by 2 week intervals
        """

        try:
            # if no args do a walk through
            if len(args) == 0:
                end = input('Enter end goal \n')
                step = input('How many weeks would you like to step by to create the check ins? \n')
            else:
                # if args are provided try to use them
                try:
                    end, step = [int(s) for s in args.split(',')]
                # if only one args is provided use the default
                except ValueError:
                    end = args
                    step = 1

            plan = log.plan(profile, end, step)
            print('\n' + plan.to_string() + '\n')

        except (ValueError, KeyError):
            print('Please check syntax \n Have you run diet() first?')

    @staticmethod
    def do_graph_weight(args):
        """
        Graphs the users body weight over a specified period
        example:
            graph_weight -> walk through
            graph_weight 9 -> graph body weight from the past 9 weeks
        """
        print('WARNING: Creating a graph will interrupt the CLI. Type CTRL+C to escape.')
        try:
            # if no args do a walk through
            if len(args) == 0:
                weeks = input('How many weeks would you like to look back? Type 0 for max. \n')
            else:
                # if args are provided try to use them
                try:
                    weeks = int(args)
                # if only one args is provided use none
                except ValueError:
                    weeks = 0

            # error filtering
            if int(weeks) < 1 or int(weeks) > 9999:
                weeks = 9999

            log.graph_weight(curr_log, int(weeks))

        except (KeyError, ValueError):
            print("Please check syntax \n")

    @staticmethod
    def do_graph_maxes(args):
        """
        Graphs the users lift max over a specified period
        example:
            graph_maxes -> walk through
            graph_maxes 9 -> graph est 1rm from the past 9 weeks
        """
        print('WARNING: Creating a graph will interrupt the CLI. Type CTRL+C to escape.')
        try:
            # if no args do a walk through
            if len(args) == 0:

                weeks = input('How many weeks would you like to look back? Type 0 for max. \n')
            else:
                weeks = int(args)

            # error filtering
            if int(weeks) < 1 or int(weeks) > 9999:
                weeks = 9999

            log.graph_maxes(curr_log, int(weeks))

        except(KeyError, ValueError):
            print("Please check syntax \n")

    @staticmethod
    def do_graph_freq(args):
        """
        Graphs the users lift frequency over a specified period
        example:
            graph_freq -> walk through
            graph_freq 9 -> graph lifts from the past 9 weeks
        """
        print('WARNING: Creating a graph will interrupt the CLI. Type CTRL+C to escape.')
        try:
            # if no args do a walk through
            if len(args) == 0:
                weeks = input('How many weeks would you like to look back? Type 0 for max. \n')
            else:
                # if args are provided try to use them
                try:
                    weeks = int(args)
                # if only one args is provided use none
                except ValueError:
                    weeks = 0

            # error filtering
            if int(weeks) < 1 or int(weeks) > 9999:
                weeks = 9999

            log.graph_freq(curr_log, int(weeks))

        except (KeyError, ValueError):
            print("Please check syntax \n")

    @staticmethod
    def do_inol(args):
        """
        Calculates the weight that should be done for X total reps to achieve the desired INOL. INOL is a formula that gives a relation between
        the Intensity(weight) and the number of lifts(NOL) otherwise known as INOL.

        Recommendations for INOL scores are as following:

        Single Workout INOL of a single exercise:
        <0.4 | Too few reps, not enough stimulus
        0.4-1 | fresh, quite doable and optimal if you are not accumulating fatigue
        1-2 | though, but good for loading phases
        >2 | brutal

        Total Weekly INOL of a single exercise:
        <2 | easy, doable, good to do after more tiring weeks and prepeaking
        2-3 | tough but doable, good for loading phases between
        3-4 | brutal, lots of fatigue, good for a limited time and shock microcycles
        >4 | Are you out of your mind?

        example:
            inol -> walk through (recommended)
            inol bench, 1.8, 25 -> calculates a 1.8 INOL weight for bench for 25 total reps
        """

        # if no args do a walk through
        try:
            if len(args) == 0:
                lift = input('What lift would you like to use? \n')
                score = input("        \n"
                              "                    Recommendations for INOL scores are as following:\n"
                              "            \n"
                              "                    Single Workout INOL of a single exercise:\n"
                              "                    <0.4 | Too few reps, not enough stimulus\n"
                              "                    0.4-1 | fresh, quite doable and optimal if you are not accumulating fatigue\n"
                              "                    1-2 | though, but good for loading phases\n"
                              "                    >2 | brutal\n"
                              "            \n"
                              "                    Total Weekly INOL of a single exercise:\n"
                              "                    <2 | easy, doable, good to do after more tiring weeks and prepeaking\n"
                              "                    2-3 | tough but doable, good for loading phases between\n"
                              "                    3-4 | brutal, lots of fatigue, good for a limited time and shock microcycles\n"
                              "                    >4 | Are you out of your mind?\n"
                              "                            \n"
                              "                    For what INOL score would you like to use? \n")
                reps = input('How many total reps would you like to perform? (1-50) \n')

            else:
                # if args are provided try to use them
                items = args.split(',')
                lift = items[0].strip()
                score = items[1]
                reps = items[2]

            # just checking
            if int(reps) > 50:
                reps = 50
            if int(reps) < 1:
                reps = 1

            x = log.inol(curr_log, lift, float(score), int(reps))
            print('\n Recommended weight for '+ str(lift) + ' over ' + str(reps) + ' total reps for a INOL of ' + str(score))
            print('\n'+str(x)+'\n')

        except ValueError:
            print('Error')

    @staticmethod
    def do_sample(args):
        """
        Creates a sample progression for the requested lift using the INOL chart. Each row represents a new session.

        example:
                sample -> walk through
                sample squat -> shows INOL progression for squat
                sample squat, volume -> shows the volume INOL progression for squat
        """

        try:
            # if no args do a walk through
            if len(args) == 0:
                name = input('What lift would you like to use for a sample? \n')
                template = input('What template would you like to use?')
            else:
                # if args are provided try to use them
                try:
                    name, template = [s for s in args.split(',')]
                # if only one args is provided use none
                except ValueError:
                    name = args
                    template = 'average'


            print('\n' + str(log.sample(curr_log, str(name), str(template).strip())) + '\n')

        except KeyError:
            print("\n Please check syntax or no results found \n")

def query_yes_no(question, default="yes"):
    """Ask a yes/no question via input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        promp = " [y/n] "
    elif default == "yes":
        promp = " [Y/n] "
    elif default == "no":
        promp = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + promp)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")


if __name__ == '__main__':
    prompt = MyPrompt()
    prompt.prompt = '<Home> '
    f = open('banner.txt', 'r')
    banner = f.read()
    print(banner)

    prompt.cmdloop('Jake Wnuk| Type help for commands | Type help <command> for documentation. \n')
