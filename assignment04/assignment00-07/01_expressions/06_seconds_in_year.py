#06_seconds_in_year.md
#Use Python to calculate the number of seconds in a year.

def main():
      #constants
      days_in_one_year=365 
      hours_in_a_day=24
      minutes_in_an_hour=60
      seconds_in_a_minute=60
      
      #multiplying all the constants to get seconds in a year
      seconds_in_a_year=(days_in_one_year * hours_in_a_day * minutes_in_an_hour * seconds_in_a_minute)

      print(f'There are {seconds_in_a_year} seconds in a year ')#response



if __name__ == '__main__':
    main()