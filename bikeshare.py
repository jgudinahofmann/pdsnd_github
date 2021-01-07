import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
m = { 'jan': 1,
    'feb': 2,
    'mar': 3,
    'apr':4,
    'may':5,
    'jun':6
    }
d = ['Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday', 'Sunday']


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
        user_input = input("Which city would you like to check the data from? Chicago, New York City or Washington?")
        try:
            city = user_input.lower()
            city = CITY_DATA[city]
            break
        except KeyError:
            print("Sorry, I didn't understand that. Most likely city was misspelled. Please try again.")
        continue
        break
    city = user_input.lower()
    while True:
        month = input("Please type the month you are interested in or type all for no month filter. Data is available from January to June.")
        if month != 'all':
    # use the index of the months list to get the corresponding int
      # TO DO: get user input for month (all, january, february, ... , june)
            s = month.strip()[:3].lower()
            try:
                month = m[s]
            except KeyError:
                print('Not a month. Please try again. Example: for January you can type Jan or January.')
                continue
                break
            break
        elif month == 'all':
            pass
            break
            month = 'all'
            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day do you want to look at? Type all if no filter should be applied or select a day from Monday to Sunday.")
        if day != 'all':
    # use the index of the months list to get the corresponding int
           if day.title() in d:
              day = day.title()
           else:
               print('Not a day. Please try again. Example: for Monday you type monday.')
               continue
           break
        elif day == 'all':
            pass
            break
            day = 'all'
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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if month != 'all':
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

     # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    common_month_count = df['month'].value_counts().nlargest(1)
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].value_counts().nlargest(1)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start = df['hour'].value_counts().nlargest(1)
    print ('The most common month is:\n', common_month_count)
    print ('The most common_day is:\n', common_day)
    print('The most common start hour is:\n', common_start)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_Start_station = df['Start Station'].value_counts().nlargest(1)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().nlargest(1)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start_end_station'] = df['Start Station'] + df['End Station']
    most_common_station_combination = df['Start_end_station'].value_counts().nlargest(1)
    print('Most commonly Start station is:\n', common_Start_station)
    print('Most commonly End Station is:\n', common_end_station)
    print('Most most frequent combination of start station and end station trip is:\n', most_common_station_combination,'\n')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Travel_time'] = df['End Time'] - df['Start Time']
    total_travel_time = df['Travel_time'].sum()

    # TO DO: display mean travel time
    Mean_travel_time = df['Travel_time'].mean()
    print('Total Travel time is:\n ', total_travel_time)
    print('Mean Travel time is:\n', Mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\n What is the breakdown of users?\n ',user_types)
    # TO DO: Display counts of gender
    if 'Birth Year' in df:
           gender = df['Gender'].value_counts()
           print('\n What is the breakdown of gender?\n',gender,'\n')
           # TO DO: Display earliest, most recent, and most common year of birth
           earliest_yob = df['Birth Year']. min()
           max_yob = df['Birth Year'].max()
           most_common_yob = df['Birth Year']. mode()
           print ('Earliest year of birth is:\n', int(earliest_yob))
           print ('Most recent year of birth is:\n', int(max_yob))
           print ('Most common year of birth is:\n', int(most_common_yob))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    show_data = input('\nWould you like to see 5 rows of data? Enter yes or no.\n')
    if show_data.lower() != 'yes':
      pass
    else:
        start_loc = 0
        print(df.iloc[start_loc : (start_loc + 5)])
        view_display = input('\'Do you wish to continue? Please type yes or no.\n').lower()
        while view_display  == 'yes':
            start_loc += 5
            print(df.iloc[start_loc : (start_loc + 5)])
            view_display = input('\'Do you wish to continue? Please type yes or no.\n').lower()
            continue
            break
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
