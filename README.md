# capstone-Cyclistes
A capstone project from coursera's google certificate program
[READ_ME.txt](https://github.com/user-attachments/files/26169982/READ_ME.txt)
---

## Phase 1: Ask

### Business Task
Analyze how annual members and casual riders use Cyclistic bikes differently,
in order to help the marketing team design a strategy to convert casual riders
into annual members.

### About the Company
Cyclistic is a bike-share program with more than 5,800 bicycles and 600 docking
stations across Chicago. The company offers three pricing options:
* Single-ride passes
* Full-day passes
* Annual memberships

Riders who use the first two options are called casual riders. Riders with annual
memberships are called members. The finance team found that members are much more
profitable than casual riders.

### Key Stakeholders
* Lily Moreno - Director of Marketing
* Cyclistic Marketing Analytics Team
* Cyclistic Executive Team

# Case Study: Cyclistic Bike-Share Analysis
## Said Gurbanov | Google Data Analytics Certificate | March 2026

---

## Phase 2: Prepare

### Data Sources
The primary data used for this analysis is Cyclistic's historical trip data.
* **Source:** https://divvy-tripdata.s3.amazonaws.com/index.html
* **Format:** Comma-separated values (.CSV)
* **Timeframe:** April 2020 - March 2021 (12 months)
* **License:** The data has been made available by Motivate International Inc.

### Data Organization
The dataset is organized by month. Each file contains the following key variables:
* `ride_id`: Unique identifier for each trip
* `rideable_type`: Type of bike (classic, electric, docked)
* `started_at` / `ended_at`: Timestamps for start and end of trip
* `start_station_name` / `end_station_name`: Station names
* `member_casual`: Indicates whether the rider is a member or casual user

### Data Integrity & Credibility (ROCCC)
I evaluated the data against the ROCCC standards:
* **Reliable:** High. First-party data collected directly from bike-share system sensors.
* **Original:** Yes, sourced directly from the organization's database.
* **Comprehensive:** Contains all necessary parameters to answer the business question.
* **Current:** Covers the most recent 12 months available at the time of analysis.
* **Cited:** Sourced officially through the City of Chicago's open data portal.

### Security and Privacy
The data has been processed to remove personally identifiable information (PII).
No credit card numbers or specific user IDs are present in the public dataset,
ensuring compliance with data privacy regulations.

---

## Phase 3: Process

### Tool Choice
I chose Python with the pandas library because the combined dataset has almost
3.5 million rows. Excel would not handle that volume well.

### Cleaning Steps
1. Loaded all 12 CSV files separately using pd.read_csv() and combined them
   into one dataframe using pd.concat()
2. Checked the data: found no duplicate rows, but noticed some columns had
   missing values (mainly station names)
3. Converted started_at and ended_at from text to proper datetime format
4. Created a new column called ride_length by subtracting started_at from
   ended_at, then converting to minutes
5. Created a new column called day_of_week using dt.dayofweek (1=Monday, 7=Sunday)
6. Removed rows where ride_length was zero or negative (data errors)

### Result
Final clean dataset: 3,478,810 rows x 15 columns. No duplicate rows found.

---

## Phase 4: Analyze

### Key Findings
* Members: 2,051,851 rides | Casual riders: 1,426,959 rides
* Casual riders average 44.97 min per ride vs members at 16.12 min
* Casual riders peak on weekends (Saturday: 335,034 rides)
* Members ride consistently throughout the week (commute pattern)

---

## Phase 5: Share

### Tableau Dashboard
https://public.tableau.com/app/profile/s.id.qurbanov/viz/CapstoneCyclistics/Dashboard1

---

## Phase 6: Act

### Top 3 Recommendations
1. Run weekend membership promotions targeting casual riders on Saturdays/Sundays
2. Show casual riders a cost comparison of per-ride vs annual membership
3. Launch a spring/summer digital media campaign before peak riding season
