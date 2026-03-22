import pandas as pd

# Load our clean data
all_trips = pd.read_csv(r"C:\Users\Seid\Desktop\cyclist_annual\clean_data.csv",
                        low_memory=False)

# Quick check - make sure data loaded correctly
print("Total rows:", len(all_trips))
print(all_trips.head())
print("Number of rides by user type:")
print(all_trips["member_casual"].value_counts())
print("\nAverage ride length (minutes) by user type:")
print(all_trips.groupby('member_casual')['ride_length'].mean())
print("\nMaximum ride length (minutes) by user type:")
print(all_trips.groupby('member_casual')['ride_length'].max())
print("\nAverage ride length by day of week:")
print(all_trips.groupby(["member_casual", "day_of_week"])['ride_length'].mean())
print("\nNumber of rides by day of week:")
print(all_trips.groupby(["member_casual", "day_of_week"])['ride_id'].count())
#rides count by user type
rides_by_type = all_trips.groupby('member_casual')['ride_id'].count().reset_index()
rides_by_type.columns = ["user_type", "ride_count"]
rides_by_type.to_csv(r"C:\Users\Seid\Desktop\cyclist_annual\rides_by_type.csv", index=False)
#average ride length by user type
avg_ride = all_trips.groupby('member_casual')['ride_length'].mean().reset_index()
avg_ride.columns = ["user_type", "avg_ride_length"]
avg_ride.to_csv(r"C:\Users\Seid\Desktop\cyclist_annual\avg_ride.csv", index=False)
#rides by day of week
rides_by_day = all_trips.groupby(['member_casual', 'day_of_week'])['ride_id'].count().reset_index()
rides_by_day.columns = ["user_type", "day_of_week", "ride_count"]
rides_by_day.to_csv(r"C:\Users\Seid\Desktop\cyclist_annual\rides_by_day.csv", index=False)
print("All summary files saved!")