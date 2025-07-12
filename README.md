### Date created
* This project was created on July, 12th.
* The `bikeshare_2.py` script was created on July, 5th.
* Last update was on July, 12th.

### Project BikeShare
Analysis of the bike rental data for Chicago, New York City and Washington.

### Description
This project is all about the bike use in the cities of Chicago, New York and Washington. The interactive python script asks the user for desired city, month or/and day. 
The result is the use of the bikes in the respective city with information about:
* Most common month, day and start hour
* Total and mean travel time 
* User type and gender counts (if available) as well as most commmon birth year

### Files used
#### Raw data
The .csv files contain data about the bike sharing in the city Chicago, New York City and Washington. Each entry is a bike sharing rent with information about:
* Date
* Start and end time
* Start and end place
* Customer type
* Gender

#### Python script
The `bikeshare_2.py` script is divied into the main part and the different functions to analyse the data.
* Main function loops through: calls first function to get the user input, analysis the data with all the other functions and ask the user to restart to continue with next data analysis
* Functions: get_filters (user input), load_data, display_data, time_stats, stations_stats, trip_duration_stats and user_stats

### Credits
All credits belong to the udacity team. They created such an amazing course to start and dive deep into SQL and Python and even introduce you to version control. Big like!
