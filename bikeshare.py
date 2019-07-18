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
        chosen_city = input("\nWhich city's data would you like me to show you? I have data for new york city, chicago and washington.\n")
        if chosen_city in ('new york city', 'chicago', 'washington'):
            break
        else:
            print("I do not have information on that city, please try again with the three cities mentioned above, thank you")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        chosen_month = input("\nWhich month's data would you like me to show you? I have data for january, february, march, april, may and june. Or please type 'all' if it does not matter to you.\n")
        if chosen_month in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            break
        else:
            print("I do not have information on that month, please try again." )

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        chosen_day = input("\nkindly enter the day of the week you require information for such as: sunday, monday, tuesday, wednesday, thursday, friday or saturday. if you dont have any preference, please just type 'all'.\n")
        if chosen_day in ('sunday', 'monday', 'tuesday','wednesday','thursday', 'friday', 'saturday', 'all'):
            break
        else:
            print("please follow the above instruction and try again, thank you.")

    print('-'*40)
    return chosen_city, chosen_month, chosen_day


def load_data(chosen_city, chosen_month, chosen_day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) chosen_city - name of the city to analyze
        (str) chosen_month - name of the month to filter by, or "all" to apply no month filter
        (str) chosen_day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[chosen_city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if chosen_month != 'all':
        # use the index of the months list to get the corresponding int
        accepted_months = ['january', 'february', 'march', 'april', 'may', 'june']
        chosen_month = accepted_months.index(chosen_month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == chosen_month]

    # filter by day of week if applicable
    if chosen_day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == chosen_day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('the most common month is:', most_common_month)

    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print('the most common day of the week is:', most_common_day_of_week)

    # TO DO: display the most common start hour
    most_common_hour = int(df['Start Time'].dt.hour.mode())
    print('The most common hour of day for start time is:', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    SS = df['Start Station'].value_counts()
    most_common_ss = SS.index[0]
    print('Most commonly used start station is:', most_common_ss)

    # TO DO: display most commonly used end station
    ES = df['End Station'].value_counts()
    most_common_es = ES.index[0]
    print('Most commonly used end station is:', most_common_es)

    # TO DO: display most frequent combination of start station and end station trip
    CS = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False)
    MCS = CS.index[0]
    print("Most frequent combination of start and end station trip is: {} , {}".format(MCS[0], MCS[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time_of_travel = df[('Trip Duration')].sum()
    total_time_of_travel_in_days = total_time_of_travel/(60*60*24)
    print('The total time of travel in days is: {}'.format(total_time_of_travel_in_days) ,'days')


    # TO DO: display mean travel time
    mean_time_of_travel = df[('Trip Duration')].mean()
    mean_time_of_travel_in_minutes = mean_time_of_travel/60
    print('The mean time of travel in minutes is: {}'.format(mean_time_of_travel_in_miutes), 'minutes')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types = df[('User Type')].value_counts()
    print('The counts of different types of users are listed below:\n{}'.format(counts_of_user_types))

    # TO DO: Display counts of gender
    # no gender data for washington

    if 'Gender' in df.keys():
        genders = df[('Gender')].value_counts()
        print('counts of gender data:\n{}'.format(genders))
    else:
        print('\nGender data:\nSorry, no gender data for this city.')


    # TO DO: Display earliest, most recent, and most common year of birth
    # no birth data for washington

    if 'Birth Year' in df.keys():
        oldest = int(df[('Birth Year')].min())
        print('Earliest year of birth is:\n{}'.format(oldest))
    else:
        print('\nEarliest year of birth:\nSorry, no birth data for this city.')



    if 'Birth Year' in df.keys():
        youngest = int(df[('Birth Year')].max())
        print('Most recent year of birth is:\n{}'.format(youngest))
    else:
        print('\nMost recent year of birth:\nSorry, no birth data for this city.')



    if 'Birth Year' in df.keys():
        common_year_rank = df[('Birth Year')].value_counts()
        most_common_birth_year = int(common_year_rank.index[0])
        print('Most common year of birth is:\n{}'.format(most_common_birth_year))
    else:
        print('\nMost common year of birth:\nSorry, no birth data for this city.')


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
