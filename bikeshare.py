import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input("Would you like to see data for Chicago, New York City, or Washington?\n").lower()
        if city in (CITY_DATA):
            print("You celected {}.\n".format(city).upper())
            break
        else:
            print("Oops! You've entered invalid response. Please try again.\n")
            continue

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        months = ['all', 'january', 'february', 'march', 'april','may','june']
        month = input("Please select which month you would like get data:\nJanuary, February, March, April, May, June, or all of them?\n").lower()
        if month in months:
            print("You selected {}.\n".format(month).upper())
            break
        else:
            print("Oops! You've entered invalid response. Please try again.\n")
            continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday','friday','saturday', 'sunday']
        day = input("Please select which day of week you would like get data:\nMonday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all of them?\n").lower()
        if day in days:
            print("You selected {}.\n".format(day).upper())
            break
        else:
            print("Oops! You've entered invalid response. Please try again.\n")
            continue

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    #load data file into a dataframr
    df = pd.read_csv(CITY_DATA[city])

    #convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    #filter by month if applicable
    if month != 'all':
        #use the index of the month list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        #filter by month to create the new dataframe
        df = df[df['month'] == month]

    #filter by day of week if applicable
    if day.lower() != 'all':
        #filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    common_month = df['month'].mode()[0]
    print("The most common month:", common_month)

    # TO DO: display the most common day of week

    common_day = df['day_of_week'].mode()[0]
    print("The most common day of week:", common_day)

    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("The most common start hour:", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station:", common_start_station)

    # TO DO: display most commonly used end station

    common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station:", common_end_station)

    # TO DO: display most frequent combination of start station and end station trip

    df['combination_station'] = df['Start Station'] + ' ' + df['End Station']
    common_start_end_station = df['combination_station'].mode()[0]
    print("The most frequently combination of start and end station trip:", common_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_time = df['Trip Duration'].sum()
    print("Total travel time:", total_time)

    # TO DO: display mean travel time

    mean_time = df['Trip Duration'].mean().round(1)
    print("Mean travel time:", mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    print("The counts user types:", user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print("The counts of gender:", gender)
    else:
        print("Here is no Gender data for Washington")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        common_year = df['Birth Year'].mode()[0]
        print("The earliest year of birth:", int(earliest_year))
        print("The most recent year of birth:", int(recent_year))
        print("The most common year of birth:", int(common_year))
    else:
        print("Here is no Birth Year data for Washington")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    """ Prompt the user if they want to see 5 lines of raw data, then ask them if they want to see more.
    Continue to display 5 more lines until the user says NO """
    i = 0
    raw = input("\nWould you like to see 5 lines of raw data? Please enter only 'yes' or 'no'.\n").lower() # TO DO: convert the user input to lower case using lower() function
    pd.set_option('display.max_columns',200)

    while True:
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df.iloc[i:(i+5)]) # TO DO: appropriately subset/slice your dataframe to display next five rows
            raw = input("\nWould you like to see 5 more lines of raw data? Please enter only 'yes' or 'no'.\n").lower() # TO DO: convert the user input to lower case using lower() function
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart == 'no':
            break
        elif restart == 'yes':
            main()
        else:
            restart = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()

if __name__ == "__main__":
	main()
