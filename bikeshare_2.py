import time
import pandas as pd

CITY_DATA = {
    "chicago": "/Users/ha-joschur/Documents/Udacity/01 - Programming for Data Science with Python/Course 4 - Introduction to Python/Project Bikeshare/chicago.csv",
    "new york": "/Users/ha-joschur/Documents/Udacity/01 - Programming for Data Science with Python/Course 4 - Introduction to Python/Project Bikeshare/new_york_city.csv",
    "washington": "/Users/ha-joschur/Documents/Udacity/01 - Programming for Data Science with Python/Course 4 - Introduction to Python/Project Bikeshare/washington.csv",
}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hello! Let's explore some US bikeshare data!")
    print("-" * 40)
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input(
        "\nWould you like to see data for Chicago, New York, or Washington? Please enter the city name. \n"
    ).lower()
    while city not in ["chicago", "new york", "washington"]:
        city = input(
            "Invalid input. Please enter 'Chicago', 'New York', or 'Washington'. \n"
        ).lower()

    filter_type = input(
        "\nWould you like to filter the data by month, day, both or don't filter at all? Please enter 'month', 'day', 'both' or 'all'. \n"
    ).lower()
    while filter_type not in ["month", "day", "both", "all"]:
        filter_type = input(
            "Invalid input. Please enter 'month', 'day', 'both' or 'all'. \n"
        ).lower()

    if filter_type == "month":
        # get user input for month (all, january, february, ... , june)
        month = input(
            "\nWhich month - January, February, March, April, May, or June?\n"
        ).lower()
        while month not in [
            "january",
            "february",
            "march",
            "april",
            "may",
            "june",
        ]:
            month = input(
                "Invalid input. Please enter 'January', 'February', 'March', 'April', 'May' or 'June'. \n"
            ).lower()
        # if user wants to filter by month, set day to "all"
        day = "all"

    elif filter_type == "day":
        # get user input for day of week (all, monday, tuesday, ... sunday)
        day = input(
            "\nWhich day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? \n"
        ).lower()
        while day not in [
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
            "sunday",
        ]:
            day = input(
                "Invalid input. Please enter 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday' or 'Sunday'. \n"
            ).lower()
        # if user wants to filter by day, set month to "all"
        month = "all"
    elif filter_type == "both":
        # get user input for month (all, january, february, ... , june)
        month = input(
            "\nWhich month - January, February, March, April, May, or June?\n"
        ).lower()
        while month not in [
            "january",
            "february",
            "march",
            "april",
            "may",
            "june",
        ]:
            month = input(
                "Invalid input. Please enter 'January', 'February', 'March', 'April', 'May' or 'June'. \n"
            ).lower()

        # get user input for day of week (all, monday, tuesday, ... sunday)
        day = input(
            "\nWhich day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? \n"
        ).lower()
        while day not in [
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
            "sunday",
        ]:
            day = input(
                "Invalid input. Please enter 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday' or 'Sunday'. \n"
            ).lower()
    # if user doesn't want to filter by month or day, set both to "all"
    else:
        month = "all"
        day = "all"

    # print the chosen filters
    if month == "all" and day == "all":
        print(
            "\nYou have chosen to analyze data for {} without any month or day filter.".format(
                city.title()
            )
        )
    elif month != "all" and day == "all":
        print(
            "\nYou have chosen to analyze data for {} in the month of {} without any day filter.".format(
                city.title(), month.title()
            )
        )
    elif month == "all" and day != "all":
        print(
            "\nYou have chosen to analyze data for {} on {} without any month filter.".format(
                city.title(), day.title()
            )
        )
    else:
        # if both month and day are not "all"
        print(
            "\nYou have chosen to analyze data for {} in the month of {} on {}.".format(
                city.title(), month.title(), day.title()
            )
        )

    print("-" * 40)
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
    df = pd.read_csv(
        CITY_DATA[city], parse_dates=["Start Time", "End Time"]
    )  # parse dates for Start Time and End Time
    # extract month and day of week from Start Time to create new columns
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.day_of_week
    # print(df.head())

    # filter by month if applicable
    if month != "all":
        # use the index of the months list to get the corresponding int
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df["month"] == month]

    # filter by day of week if applicable
    if day != "all":
        # filter by day of week to create the new dataframe
        days = [
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
            "sunday",
        ]
        day = days.index(day)
        df = df[df["day_of_week"] == day]

    return df


def display_data(df):
    """Displays raw data upon user request."""
    start_loc = 0
    number_of_rows = df.shape[0]  # get the number of rows in the dataframe
    display = input(
        f"\nThere are {number_of_rows} row(s) of raw data available. Would you like to see the first 5 rows of raw data? Enter yes ('y'/'yes') or no ('n'/'no').\n"
    ).lower()
    while display not in ["yes", "y", "no", "n"]:
        display = input("\nInvalid input. Please enter 'yes' or 'no'.\n").lower()

    if display == "yes" or display == "y":
        print(df.iloc[start_loc : start_loc + 5])
        start_loc += 5
    else:
        # abort displaying data if user doesn't want to see it
        print("\nYou chose not to display raw data. Continuing with the analysis...\n")
        print("-" * 40)
        return

    while True:
        display = input(
            "\nWould you like to see the next 5 rows of raw data? Enter yes ('y'/'yes') or no ('n'/'no').\n"
        ).lower()
        while display not in ["yes", "y", "no", "n"]:
            display = input("Invalid input. Please enter 'yes' or 'no'.\n").lower()

        if start_loc >= number_of_rows:
            print(
                "\nYou have reached the end of the raw data. No more data to display.\n"
            )
            break
        elif start_loc + 5 >= number_of_rows:
            print(df.iloc[start_loc:])
            print(
                "\nYou have reached the end of the raw data. No more data to display.\n"
            )
            break

        if display in ["yes", "y"]:
            print(df.iloc[start_loc : start_loc + 5])
            start_loc += 5
        else:
            print("-" * 40)
            break


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()
    months = [
        "january",
        "february",
        "march",
        "april",
        "may",
        "june",
    ]
    days = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ]

    # calculate the most common month
    popular_month = df["month"].mode()[0]
    # convert the month number to the month name
    print("Most common month: ", months[popular_month - 1].title())

    # calculate the most common day of week
    popular_day = df["day_of_week"].mode()[0]
    # convert the day number to the day name
    print("Most common day of week: ", days[popular_day].title())

    # display the most common start hour
    print(
        "Most common start hour:",
        df["Start Time"].dt.hour.mode()[0],
    )

    print("\nThis took %s seconds." % (round(time.time() - start_time, 3)))
    print("-" * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    # display most commonly used start station
    print("Most commonly used start station: ", df["Start Station"].mode()[0])
    # display most commonly used end station
    print("Most commonly used end station: ", df["End Station"].mode()[0])

    # display most frequent combination of start station and end station trip
    df["Start End Station"] = (
        df["Start Station"] + " to " + df["End Station"]
    )  # create a new column for start and end station combination
    print(
        "Most frequent combination of start and end station trip: ",
        df["Start End Station"].mode()[0],
    )

    print("\nThis took %s seconds." % (round(time.time() - start_time, 3)))
    print("-" * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    # display total travel time
    total_travel_time = df["End Time"] - df["Start Time"]
    total_travel_time = total_travel_time.sum()
    # print("Total travel time: ", total_travel_time)
    # display total travel time in days, hours, minutes, and seconds
    total_days, remainder = divmod(total_travel_time.total_seconds(), 86400)
    total_hours, remainder = divmod(remainder, 3600)
    total_minutes, total_seconds = divmod(remainder, 60)
    print(
        "Total travel time: %d days, %d hours, %d minutes, and %d seconds"
        % (
            total_days,
            total_hours,
            total_minutes,
            total_seconds,
        )
    )

    # display mean travel time
    mean_travel_time = total_travel_time / len(df)
    # print("Mean travel time: ", mean_travel_time)
    # dispaly mean travel time in minutes and seconds
    mean_minutes, mean_seconds = divmod(mean_travel_time.total_seconds(), 60)
    print("Mean travel time: %d minutes and %d seconds" % (mean_minutes, mean_seconds))

    print("\nThis took %s seconds." % (round(time.time() - start_time, 3)))
    print("-" * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print("\nCalculating User Stats...\n")
    start_time = time.time()

    # Display counts of user types
    user_types = df["User Type"].value_counts()
    # print("Counts of user types:\n", user_types)
    # display all user types of user_types
    print("User types:")
    for user_type, count in user_types.items():
        print(f"- {user_type}: {count} users")

    # Display counts of gender
    # check if the column "Gender" exists in the dataframe
    if "Gender" in df.columns:
        gender_counts = df["Gender"].value_counts()
        print("\nGender counts:")
        for gender, count in gender_counts.items():
            print(f"- {gender}: {count} users")
    else:
        print("\nNo information about gender is available for this city.")
    # print("\nCounts of gender:\n", gender_counts)

    # Display earliest, most recent, and most common year of birth
    # check if the column "Birth Year" exists in the dataframe
    if "Birth Year" in df.columns:
        earliest_year = int(df["Birth Year"].min())
        most_recent_year = int(df["Birth Year"].max())
        most_common_year = int(df["Birth Year"].mode()[0])
        print(
            "\nEarliest year of birth: {}, Most recent year of birth: {}, Most common year of birth: {}".format(
                earliest_year, most_recent_year, most_common_year
            )
        )
    else:
        print("\nNo information about birth year is available for this city.")

    print("\nThis took %s seconds." % (round(time.time() - start_time, 3)))
    print("-" * 40)


def main():
    while True:
        city, month, day = get_filters()  # Get user input for city, month, and day
        df = load_data(city, month, day)  # Load data based on user input

        display_data(df)  # Display raw data upon user request

        time_stats(
            df
        )  # Calculate and display statistics on the most frequent times of travel
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input(
            "\nWould you like to restart? Enter yes ('y'/'yes') or no ('n'/'no').\n"
        )
        while restart not in ["yes", "y", "no", "n"]:
            restart = input("Invalid input. Please enter 'yes' or 'no'. \n")

        if restart.lower() not in ["yes", "y"]:
            break
        else:
            print("=" * 40)
            print()


if __name__ == "__main__":
    main()
