import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#v1 is commited
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    try:
        while True:
            city_number = int(input("Would you like to see data for 1. Chicago, 2. New York, or 3. Washington? 'Only enter the city number'\n"))
            if city_number == 1:
                city = "chicago"
                break
            elif city_number == 2:
                city = "new york city"
                break
            elif city_number == 3:
                city = "washington"
                break
            else:
                print('Wrong entry, please only enter the number beside the city!')
    except ValueError:
        print('Wrong entry, please only enter the number beside the city!')

    # get user input for month (all, january, february, ... , june)
    while True:
        month = int(input("Choose a month to filter the data with! 1. January, 2. February, 3. March, 4. April, 5. May, 6. June? Type all for no month filter\n"))
        if month == 1:
            month = "January"
            break
        elif month == 2:
            month = "February"
            break
        elif month == 3:
            month = "March"
            break
        elif month == 4:
            month = "April"
            break
        elif month == 5:
            month = "May"
            break
        elif month == 6:
            month = "June"
            break
        elif month == "all":
            break
        else:
            print('Wrong entry, please only enter the number beside the month!')
        
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = int(input("Choose a day to filter the data with! 1. Saturaday, 2. Sunday, 3. Monday, 4. Tuesday, 5. Wednesday, 6. Thursday, 7. Friday? Type all for no day filter\n"))
        if day == 1:
            day = "Saturaday"
            break
        elif day == 2:
            day = "Sunday"
            break
        elif day == 3:
            day = "Monday"
            break
        elif day == 4:
            day = "Tuesday"
            break
        elif day == 5:
            day = "Wednesday"
            break
        elif day == 6:
            day = "Thursday"
            break
        elif day == 7:
            day = "Friday"
            break
        elif day == "all":
            break
        else:
            print('Wrong entry, please only enter the number beside the day!')


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
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()