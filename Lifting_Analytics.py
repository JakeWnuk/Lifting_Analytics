#! python3

# Author Jake Wnuk
# LinkedIn: www.linkedin.com/in/jakewnuk
# Lifting Analytics

"""
Description: File for the logic used in the main()
"""

import datetime
import math
import pandas as pd


def plan(profile, end, step=1):
    """
    Divides the difference between the current weight from the diet profile and the selected end goal.
    :param step: tells the function how many weeks to step by to create the check ins
    :param profile: a profile generated by diet()
    :param end: the end goal as a float
    :return: a data frame

    note: no need for conversions because it assumes the same units as diet().
    """

    # take parts from profile
    goal = profile['Goal']
    tick = float(profile['Growth/Loss Var'])
    curr_weight = profile['Current Weight']

    # end result df
    df = pd.DataFrame({'Date': pd.to_datetime('today').strftime('%m/%d/%Y'), 'Weight': curr_weight},
                      index=[0])

    # changes ticks and finds the difference between start and end
    diff = abs(float(curr_weight) - float(end))
    if goal == 'bulk':
        tick = tick * 2  # formula assumes muscle and fat are gained 1 to 1 ratio
        tick = tick / 4  # turns the ticks from monthly gain into weekly
    elif goal == 'cut':
        tick = tick * -1  # cutting is already set to weekly loss so just negating the number for easier calculations

    # sets up for iteration
    w = 1 * int(step)
    while diff > 0:
        piece = pd.DataFrame({
            'Date': (pd.Timestamp(df['Date'][0]) + datetime.timedelta(weeks=w)).strftime('M/D/Y %m/%d/%Y'),
            'Weight': curr_weight + (w * tick)
        }, index=[0])
        df = df.append(piece, ignore_index=True)
        w += int(step)
        diff = diff - abs(tick * int(step))

    # generates results
    print('Goal was to: ' + str(goal))
    return df


def macro(profile, metric=False):
    """
    Generates macros for a user based off their diet profile
    :param metric: set true if using metric units
    :param profile: a diet profile df generated by the diet()
    :return: a pd.Series

    Source: https://rippedbody.com/complete-diet-nutrition-set-up-guide/
            https://www.strongerbyscience.com/reflecting-on-five-years-studying-protein/
    """

    # takes parts from profile
    goal = profile['Goal']
    cal = profile['Recommended Calories']
    lbm = profile['Lean Body Mass']
    pro = 0
    carb = 0
    fat = 0

    # does the math
    if goal == 'bulk':
        if metric:
            pro = int(2.4 * lbm)
            fat = int((0.25 * cal) / 9)
            carb = int((cal - ((pro * 4) + (fat * 9))) / 4)
        else:
            pro = int(1.1 * lbm)
            fat = int((0.25 * cal) / 9)
            carb = int((cal - ((pro * 4) + (fat * 9))) / 4)

    elif goal == 'cut':
        if metric:
            pro = int(2.8 * lbm)
            fat = int(1.1 * lbm)
            carb = int((cal - ((pro * 4) + (fat * 9))) / 4)
        else:
            pro = int(1.3 * lbm)
            fat = int(0.5 * lbm)
            carb = int((cal - ((pro * 4) + (fat * 9))) / 4)

    # generates final result
    mac = pd.Series({
        'Recommended Calories': cal,
        'Protein': pro,
        'Carbohydrates': carb,
        'Fat': fat

    })

    return mac


def diet(weight, bfp, goal, metric=False):
    """
    generates a diet profile of a user that is then used in other functions such as macro() and plan()
    :param weight: the users current body weight
    :param bfp: body fat percentage
    :param goal: bulk or to cut, caloric surplus or deficit
    :param metric: if using metric units or freedom units
    :return: a pd.Series with the users diet profile

    Source: https://rippedbody.com/complete-diet-nutrition-set-up-guide/
    """

    # generating TDEE using activity level and last logged body weight
    act = pd.Series({
        'No Exercise': 1.2,
        'Train 2-3 days a week': 1.375,
        'Train 4-5 days a week': 1.55,
        'Train 6-7 days a week': 1.725,
        'Train + other major physical activities': 1.9
    })

    print(act.to_string())
    alvl = input('What is your estimated activity level? \n')
    lbm = float(weight) - (float(weight) * (float(bfp) / 100))

    if metric:
        bmr = 370 + 21.6 * lbm
        tde = float(bmr) * float(alvl)
    else:
        bmr = 370 + 21.6 * (lbm / 2.204)
        tde = float(bmr) * float(alvl)

    # bulk and cut tables. Used to find out expected changed to TDEE.
    b_table = pd.DataFrame({
        'State': pd.Categorical(['Beginner', 'Intermediate', 'Advanced']),
        'Growth a month (lbs)': pd.Categorical(['2-3', '1-2', '0.5']),
        'Growth a month (kgs)': pd.Categorical(['0.8-1.2', '0.45-0.9', '0.22'])
    }, columns=['State', 'Growth a month (lbs)', 'Growth a month (kgs)'])

    c_table = pd.DataFrame({
        'Body Fat %': pd.Categorical(['30%>', '20-30%', '15-20%', '12-15%', '9-12%', '7-9%', '<7%']),
        'Loss a week (lbs)': pd.Categorical(['2.5', '2', '1.25-1.5', '1-1.25', '0.75-1', '0.5-0.75', '~0.5']),
        'Loss a week (kgs)': pd.Categorical(['1.1', '0.9', '0.45-0.7', '0.45-0.6', '0.35-0.45', '0.2-0.35', '0.2'])
    }, columns=['Body Fat %', 'Loss a week (lbs)', 'Loss a week (kgs)'])

    # modifies the TDEE based on goal and estimated rate of change
    rec = 0
    pot = 0

    if goal in ['bulk', 'b']:
        goal = 'bulk'
        print('Muscle Growth Potential \n')
        print(b_table.to_string())
        pot = input('What is your estimated growth a month? \n')

        if metric:
            rec = tde + (float(pot)) * 440
        else:
            rec = tde + (float(pot) * 0.453592) * 440

    if goal in ['cut', 'c']:
        goal = 'cut'
        print('Recommended Fat Loss Based on BF% \n')
        print(c_table.to_string())
        pot = input('What is your estimated fat loss per week? \n')

        if metric:
            rec = tde - ((float(pot)) * (7700 / 7))
        else:
            rec = tde - ((float(pot) * 0.453592) * (7700 / 7))

    # generates final result
    profile = pd.Series({
        'Body fat %': bfp,
        'Current Weight': weight,
        'Lean Body Mass': lbm,
        'BMR': int(bmr),
        'Activity Multiplier': alvl,
        'TDEE': int(tde),
        'Goal': goal,
        'Recommended Calories': int(rec),
        'Growth/Loss Var': pot
    })

    return profile


def bf(log, gender, metric=False):
    """
    calcuates the users body fat % by taking their last weight from the log file.
    :param log: the log file
    :param gender: male or female
    :param metric: set true if using metric units
    :return: string of a pd.Series

    Source: https://rippedbody.com/how-calculate-body-fat-percentage/
    """

    # collecting info
    bfp = 0
    cur_wght = log.loc[0]['Body Weight']
    height = input('What is your current height? In inches or cm  \n')
    waist = input('What is the measurement of your waist at navel? \n')
    neck = input("What is the measurement of your neck at its narrowest? \n")
    hips = 'N/A'

    # filtering for metric and male/female then using the correct formula
    if not metric:
        if gender == 'female':
            hips = input('What is the measurement of your hips at their widest? \n')
            bfp = 495 / (1.29579 - .35004 * math.log10(
                float(waist) * 2.54 + float(hips) * 2.54 - float(neck) * 2.54) + .22100 * math.log10(
                float(height) * 2.54)) - 450
        elif not metric:
            bfp = 495 / ((1.0324 - .19077 * math.log10(float(waist) * 2.54 - float(neck) * 2.54)) + .15456 * math.log10(
                float(height) * 2.54)) - 450
    elif metric:
        if gender == 'female':
            hips = input('What is the measurement of your hips at their widest? \n')
            bfp = 495 / (1.29579 - .35004 * math.log10(
                float(waist) + float(hips) - float(neck)) + .22100 * math.log10(
                float(height))) - 450
        else:
            bfp = 495 / ((1.0324 - .19077 * math.log10(float(waist) - float(neck))) + .15456 * math.log10(
                float(height))) - 450

    fat = float((bfp / 100) * cur_wght)

    # generates final result
    bfs = pd.Series({
        'Gender': gender,
        'Weight': cur_wght,
        'Height': height,
        'Waist': waist,
        'Neck': neck,
        'Hips': hips,
        'Body Fat %': bfp,
        'Fat Mass': fat,
        'Lean Mass': int(cur_wght - fat)
    })

    return bfs.to_string()


def past(log, w, lift=""):
    """
    prints out the past x weeks or the past x weeks with y lift.
    :param log: the log file being used
    :param lift: lift being searched for (could be n/a)
    :param w: how many weeks to look back
    :return: pd.DataFrame
    """

    # error checking the weeks
    if w < 1:
        w = 9999

    # make sure its a datetime
    log['Date'] = pd.to_datetime(log['Date'])

    # filter
    log = log.loc[
        (pd.to_datetime(log['Date']) >= pd.Timestamp(datetime.date.today() - datetime.timedelta(weeks=w))) & (
            log['Lift'].str.contains(lift.lower()))].copy()

    return log


def prilepin(log, lift, w):
    """
    Prints out Prilepin's chart for a requested lift. Normal and hypertrophy table.
    :param log: the log file used
    :param lift: lift being searched for
    :param w: how many weeks to look back
    :return: string with the data frames

    Source: https://www.t-nation.com/training/prilepins-table-for-hypertrophy
    """

    # taking the best lift
    item = top_max(log, lift, w)
    item = item['EST_1RM']

    # getting percentages
    p55 = int(item * .55)
    p65 = int(item * .65)
    p70 = int(item * .70)
    p80 = int(item * .80)
    p90 = int(item * .90)

    # generating prils normal table
    p_table = pd.DataFrame({'Percent of 1RM': pd.Categorical(['55-65%', '70-80%', '80-90%', '90%']),
                            'Weight Range': pd.Categorical(
                                [str(p55) + ' - ' + str(p65), str(p70) + ' - ' + str(p80), str(p80) + ' - ' + str(p90),
                                 str(p90)]),
                            'Reps per Set': pd.Categorical(['3-6', '3-6', '2-4', '1-2']),
                            'Optimal Total Reps': pd.Categorical(['24', '18', '15', '7']),
                            'Range of Reps': pd.Categorical(['18-30', '12-24', '10-20', '4-10'])
                            }, columns=['Percent of 1RM', 'Weight Range', 'Reps per Set', 'Optimal Total Reps',
                                        'Range of Reps'])

    # generating prils hypertrophy altered table
    hp_table = pd.DataFrame({'Percent of 1RM': pd.Categorical(['< 70%', '70-80%', '80-90%', '> 90%']),
                             'Weight Range': pd.Categorical(
                                 [' < ' + str(p70), str(p70) + ' - ' + str(p80), str(p80) + ' - ' + str(p90),
                                  str(p90)]),
                             'Reps per Set': pd.Categorical(['6-10', '5-8', '5-7', '1-2']),
                             'Optimal Total Reps': pd.Categorical(['32', '30', '21', '7']),
                             'Range of Reps': pd.Categorical(['20-40', '20-30', '15-25', '4-10'])
                             }, columns=['Percent of 1RM', 'Weight Range', 'Reps per Set', 'Optimal Total Reps',
                                         'Range of Reps'])

    # generates final result
    return 'Standard Prilepins Chart for ' + str(
        lift) + ': \n' + p_table.to_string() + '\n \n Hypertrophy Prilepins Chart for ' + str(
        lift) + ': \n' + hp_table.to_string()


def stats(log, lift, w):
    """
    Returns stats about a lift in a specified time frame using the est 1rm
    :param log: the log file
    :param lift: the lift being searched
    :param w: weeks to search
    :return: pd.describe()
    """

    # filtering
    log['Date'] = pd.to_datetime(log['Date'])

    log = log.loc[
        (pd.to_datetime(log['Date']) >= pd.Timestamp(datetime.date.today() - datetime.timedelta(weeks=w))) & (
            log['Lift'].str.contains(lift.lower()))].copy()

    # adding the estimated 1rm to a table
    for i, row in log.iterrows():
        est_max = (estimate_rm(1, row['Weight'], row['RM']))
        log.loc[i, 'EST_1RM'] = est_max

    # describing that new col
    col = log["EST_1RM"]

    return col.describe()


def wilks(log, weight, male=True, metric=False):
    """
    Goes through the log to find your best lifts at a certain body weight. Then calculates an estimated wilks score.
    :param metric: set true if numbers are in kg
    :param male: set false if female
    :param log: the log file
    :param weight: this will be rounded to the nearest full digit for search purposes.
    :return: an int representing the wilks score
    """

    # finding and filter for the lifts used in a wilks score
    log = log[(log['Body Weight'] == weight)]

    b_log = log[(log['Lift'].str.contains("bench"))]
    d_log = log[(log['Lift'].str.contains("deadlift"))]
    s_log = log[(log['Lift'].str.contains("squat"))]

    b_log = top_max(b_log, 'bench', 9999)
    d_log = top_max(d_log, 'deadlift', 9999)
    s_log = top_max(s_log, 'squat', 9999)
    total_lbs = b_log['EST_1RM'] + d_log['EST_1RM'] + s_log['EST_1RM']

    # conversions
    if metric:
        total_kg = total_lbs
        weight_kg = weight
    else:
        total_kg = total_lbs / 2.2046
        weight_kg = weight / 2.2046

    # these are the parts that are used to calculate the wilks coefficient.
    a = -216.0475144
    b = 16.2606339
    c = -0.002388645
    d = -0.00113732
    e = 7.01863 * math.pow(10, -6)
    f = -1.291 * math.pow(10, -8)

    if not male:
        a = 594.31747775582
        b = -27.23842536447
        c = 0.82112226871
        d = -0.00930733913
        e = 0.00004731582
        f = -0.00000009054

    coefficient = 500 / (a +
                         b * weight_kg +
                         c * math.pow(weight_kg, 2) +
                         d * math.pow(weight_kg, 3) +
                         e * math.pow(weight_kg, 4) +
                         f * math.pow(weight_kg, 5))

    # generates final result
    print('Your Est. Max Bench is: ' + str(b_log['EST_1RM']) + ' at ' + str(weight) + '\n')
    print('Your Est. Max Squat is: ' + str(s_log['EST_1RM']) + ' at ' + str(weight) + '\n')
    print('Your Est. Max Deadlift is: ' + str(d_log['EST_1RM']) + ' at ' + str(weight) + '\n')
    print('Your Estimated Wilks Score is: \n')
    return int(total_kg * coefficient)


def top_max(log, lift, w, reps=0):
    """
    Estimates the users top 1RM
    :param reps: used in looking for top sets, checks for only sets with x rm
    :param lift: The lift the user is finding
    :param w: How many weeks to search
    :param log: the log file being passed
    :return: df row with the following formatting:
            Headers:
             Date, Lift, RM, Weight, Body Weight, Est_1RM
    """

    if reps != 0:  # this section is used by top() to find a specific RM in the log file
        log = log.loc[
            (pd.to_datetime(log['Date']) >= pd.Timestamp(datetime.date.today() - datetime.timedelta(weeks=w))) & (
                log['Lift'].str.contains(lift.lower())) & (log['RM'] == int(reps))].copy()
    else:
        log = log.loc[  # this section is used by max() to find the best lift of any rm
            (pd.to_datetime(log['Date']) >= pd.Timestamp(datetime.date.today() - datetime.timedelta(weeks=w))) & (
                log['Lift'].str.contains(lift.lower()))].copy()

    for i, row in log.iterrows():
        est_max = (estimate_rm(1, row['Weight'], row['RM']))
        log.loc[i, 'EST_1RM'] = est_max

    best = log.loc[log['EST_1RM'].idxmax()]

    return best


def estimate_rm(req, weight, reps):
    """
    Using Wathan's formula to determine the 1RM
    :param req: requested rm being checked for
    :param weight: the weight of the lift
    :param reps: number of repetitions preformed
    :return: a rounded int value

    Source: https://en.wikipedia.org/wiki/One-repetition_maximum
    """

    one_rm = (100 * weight) / (48.8 + 53.8 * math.exp(-0.075 * reps))

    if req == 1:
        return round(one_rm)

    x_rm = (one_rm * (48.8 + 53.8 * math.exp(-0.075 * req))) / 100

    return round(x_rm)
