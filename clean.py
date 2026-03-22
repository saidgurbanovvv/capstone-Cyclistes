import pandas as pd

df1  = pd.read_csv(r"C:\Users\Seid\Desktop\cyclist_annual\2020_04-divvy-tripdata.csv")
df2  = pd.read_csv(r"C:\Users\Seid\Desktop\cyclist_annual\2020_05-divvy-tripdata.csv")
df3  = pd.read_csv(r"C:\Users\Seid\Desktop\cyclist_annual\2020_06-divvy-tripdata.csv")
df4  = pd.read_csv(r"C:\Users\Seid\Desktop\cyclist_annual\2020_07-divvy-tripdata.csv")
df5  = pd.read_csv(r"C:\Users\Seid\Desktop\cyclist_annual\2020_08-divvy-tripdata.csv")
df6  = pd.read_csv(r"C:\Users\Seid\Desktop\cyclist_annual\2020_09-divvy-tripdata.csv")
df7  = pd.read_csv(r"C:\Users\Seid\Desktop\cyclist_annual\2020_10-divvy-tripdata.csv")
df8  = pd.read_csv(r"C:\Users\Seid\Desktop\cyclist_annual\2020_11-divvy-tripdata.csv")
df9  = pd.read_csv(r"C:\Users\Seid\Desktop\cyclist_annual\2020_12-divvy-tripdata.csv")
df10 = pd.read_csv(r"C:\Users\Seid\Desktop\cyclist_annual\2021_01-divvy-tripdata.csv")
df11 = pd.read_csv(r"C:\Users\Seid\Desktop\cyclist_annual\2021_02-divvy-tripdata.csv")
df12 = pd.read_csv(r"C:\Users\Seid\Desktop\cyclist_annual\2021_03-divvy-tripdata.csv")

all_trips = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12], ignore_index=True)
print("Total rows:", len(all_trips))
print("Total columns:", len(all_trips.columns))
print("Duplicate rows:", all_trips.duplicated().sum())
print(all_trips.head())
print(all_trips.dtypes)

all_trips['started_at'] = pd.to_datetime(all_trips['started_at'])
all_trips['ended_at'] = pd.to_datetime(all_trips['ended_at'])

all_trips['ride_length'] = (all_trips['ended_at'] - all_trips['started_at']).dt.total_seconds() / 60
all_trips['day_of_week'] = all_trips['started_at'].dt.dayofweek + 1
all_trips = all_trips[all_trips['ride_length'] > 0]

print('Clean rows:', len(all_trips))
print(all_trips[["started_at", "ended_at", "ride_length", "day_of_week"]].head())

all_trips.to_csv(r"C:\Users\Seid\Desktop\cyclist_annual\clean_data.csv", index=False)

print("File saved successfully!")