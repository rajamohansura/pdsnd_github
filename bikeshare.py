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
      while  True:
            town=str(input("PLease Enter your City you would like to explore:")
            town=town.lower()
            if town in ["New York","washington","chicago"]:
                     break
            else:
                     print("The town you enterd is invalid..Enter a valid town or city")

    # TO DO: get user input for month (all, january, february, ... , june)
      while True:
            month=str(input("PLease Enter a month you want:")
            month=month.lower()
            if month in ["All","january","february","march","april","may","june"]:
                     break
            else:
                     print("The month you enterd is invalid..Enter a valid month")             

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        
      while True:
            day=str(input("PLease Enter a day you want:")
            day=day.lower()
            if day in ["all","monday","tuesday","wednesday","thursday","friday","saturday"]:
                     break
            else:
                     print("The day you enterd is invalid..Enter a valid day")  
        
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
          # LOading city data into a dataframe
           city_info=pd.read_csv(CITY_DATA[city])
              
          # changing the start time coulmn in to date time 
           city_info["Start Time"]=pd.to_datetime(city_info["Start Time"])
          # extracting day and month from start time column
           city_info["day"]=city_info["Start Time"].dt.day
                    
           city_info["month"]=city_info["Start Time"].dt.month
                    
           city_info["hour"]=city_info["Start Time"].dt.hour
            
    # filter by month
     if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        city_info= city_info[city_info['month'] == month]

    # filter by day of week 
     if day != 'all':
        # filter by day of week to create the new dataframe
        
        city_info = city_info[city_info['day'] == day.title()]

    return city_info


def time_stats(city_info):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
       print("most common month is:",city_info['month'].mode()[0])


    # TO DO: display the most common day of week
        print("most common day is:",city_info['day'].mode()[0])

    # TO DO: display the most common start hour
         print("most common hour  is:",city_info['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(city_info):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
        print("The most common used start station is:",city_info['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
        print("The most common used start station is:",city_info['Etart Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
        print("displaying most frequent combination of start station and end station trip:",[city_info['Start Station']+" "+city_info['End Station']].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(city_info):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
        print('total travel time:',city_info['Trip Duration'].sum())

    # TO DO: display mean travel time
        print('mean travel time:',city_info['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(city_info,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
        type_of_users=city_info['User Type'].value_counts()
                    
        print(type_of_users,"\n")
                    

    # TO DO: Display counts of gender
                    
         if city !="washington':
                gender=city_info['Gender'].value_counts()
                 print(gender)

    # TO DO: Display earliest, most recent, and most common year of birth
         print('Earliest year of birth is:', sorted(city_info.groupby(['Birth Year'])['Birth Year'], reverse=True)[0][0])
         print('most recent year of birth is:', sorted(city_info.groupby(['Birth Year'])['Birth Year'])[0][0])           
         print('THe most common year of birth is:', sorted(city_info['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        city_info = load_data(city, month, day)

        time_stats(city_info)
        station_stats(city_info)
        trip_duration_stats(city_info)
        user_stats(city_info)

        restart = input('\n Would you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
