import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

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
        month = input("Choose a month to filter the data with! January, February, March, April, May, June? Type all for no month filter\n").lower()
        if month == 'all':
            break
        elif month in MONTHS:
            break
        else:
            print('Wrong entry, please enter the month name as it is in the question!')
        
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Choose a day to filter the data with! 1. Saturaday, 2. Sunday, 3. Monday, 4. Tuesday, 5. Wednesday, 6. Thursday, 7. Friday? Type all for no day filter\n")
        if day == '1':
            day = "Saturaday"
            break
        elif day == '2':
            day = "Sunday"
            break
        elif day == '3':
            day = "Monday"
            break
        elif day == '4':
            day = "Tuesday"
            break
        elif day == '5':
            day = "Wednesday"
            break
        elif day == '6':
            day = "Thursday"
            break
        elif day == '7':
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
    df['day_of_week'] = df['Start Time'].dt.day_name()

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
    popular_month = df['month'].mode()[0]
    popular_month_count = len(df[df['month'] == popular_month])

    # display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    popular_day_of_week_count = len(df[df['day_of_week'] == popular_day_of_week])

    #if the client choose to filter the data by a month or a day the lines won't printed
    if df['month'].nunique() != 1:
        print("Most popular month: {}, Count: {}".format(popular_month, popular_month_count))
    if df['day_of_week'].nunique() != 1:
        print("Most popular day of week: {}, Count: {}".format(popular_day_of_week, popular_day_of_week_count))

    # find the most common hour (from 0 to 23)
    df['hour'] = df['Start Time'].dt.hour
    
    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    popular_hour_count = len(df[df['hour'] == popular_hour])
    print("Most popular hour: {}, Count: {}".format(popular_hour, popular_hour_count))

    print("\nThis took %0.3f seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    popular_start_station_count = len(df[df['Start Station'] == popular_start_station])
    print("Most popular Start Station: {}, Count: {}".format(popular_start_station, popular_start_station_count))

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    popular_end_station_count = len(df[df['End Station'] == popular_end_station])
    print("Most popular End Station: {}, Count: {}".format(popular_end_station, popular_end_station_count))

    # display most frequent combination of start station and end station trip
    df['Combination'] = "FROM " + df['Start Station'] + " TO " + df['End Station']
    popular_combination = df['Combination'].mode()[0]
    popular_combination_count = len(df[df['Combination'] == popular_combination])
    print("Most frequent combination of start station and end station trip: {}, Count: {}".format(popular_combination, popular_combination_count))

    print("\nThis took %0.3f seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time: {}, number of travels: {}".format(total_travel_time, len(df['Trip Duration'])))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time: {}".format(mean_travel_time))

    print("\nThis took %0.3f seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    subscribers_count = df['User Type'].value_counts()['Subscriber']
    customers_count = df['User Type'].value_counts()['Customer']
    print("Subscribers: {}, Customers: {}".format(subscribers_count, customers_count))

    # Display counts of gender
    if 'Gender' in df:
        males_count = df['Gender'].value_counts()['Male']
        females_count = df['Gender'].value_counts()['Female']
        print("Males: {}, Females: {}".format(males_count, females_count))
        

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        most_recent = df['Birth Year'].max()
        earliest = df['Birth Year'].min()
        most_common = df['Birth Year'].mode()[0]
        print("Most Recent year of birth: {}\nEarliest year of birth: {}\nMost common year of birth: {}".format(most_recent, earliest, most_common))

    print("\nThis took %0.3f seconds." % (time.time() - start_time))
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