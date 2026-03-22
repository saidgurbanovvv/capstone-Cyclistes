# 🚲 Cyclistic Bike-Share Analysis
### Google Data Analytics Certificate — Capstone Project
**Said Gurbanov | March 2026**

![Python](https://img.shields.io/badge/Python-pandas-blue) ![Tableau](https://img.shields.io/badge/Tableau-Public-orange)

---

## 📌 Overview
This is my capstone project for the Google Data Analytics Professional Certificate on Coursera. I analyzed 12 months of bike-share trip data to understand how annual members and casual riders use Cyclistic bikes differently, and provided recommendations to help convert casual riders into members.

**Tools used:** Python (pandas) · Tableau Public

📊 **[View Tableau Dashboard](https://public.tableau.com/app/profile/s.id.qurbanov/viz/CapstoneCyclistics/Dashboard1)**

---

## Phase 1: Ask

### Business Task
Analyze how annual members and casual riders use Cyclistic bikes differently, in order to help the marketing team design a strategy to convert casual riders into annual members.

### About the Company
Cyclistic is a bike-share program with more than 5,800 bicycles and 600 docking stations across Chicago. The company offers three pricing options:
- Single-ride passes
- Full-day passes
- Annual memberships

Riders who use the first two options are called **casual riders**. Riders with annual memberships are called **members**. The finance team found that members are much more profitable than casual riders.

### Key Stakeholders
- Lily Moreno — Director of Marketing
- Cyclistic Marketing Analytics Team
- Cyclistic Executive Team

---

## Phase 2: Prepare

### Data Source
- **Source:** https://divvy-tripdata.s3.amazonaws.com/index.html
- **Format:** CSV files (one per month)
- **Timeframe:** April 2020 – March 2021 (12 months)
- **License:** Made available by Motivate International Inc.

### Key Variables
- `ride_id` — Unique identifier for each trip
- `rideable_type` — Type of bike (classic, electric, docked)
- `started_at` / `ended_at` — Timestamps for start and end of trip
- `start_station_name` / `end_station_name` — Station names
- `member_casual` — Whether the rider is a member or casual user

### ROCCC Check
| Criteria | Result |
|----------|--------|
| Reliable | ✅ First-party data from bike-share sensors |
| Original | ✅ Directly from the organization's database |
| Comprehensive | ✅ All parameters needed to answer the question |
| Current | ✅ Most recent 12 months available |
| Cited | ✅ City of Chicago's open data portal |

### Privacy
No personally identifiable information (PII) is present in the dataset.

---

## Phase 3: Process

### Tool Choice
I used Python with pandas because the combined dataset has almost 3.5 million rows — too large for Excel.

### Cleaning Steps
1. Loaded all 12 CSV files and combined them into one dataframe using `pd.concat()`
2. Checked for duplicates — none found
3. Converted `started_at` and `ended_at` from text to datetime format
4. Added `ride_length` column (duration in minutes)
5. Added `day_of_week` column using `dt.dayofweek` (1=Monday, 7=Sunday)
6. Removed rows where `ride_length` was zero or negative

**Final dataset: 3,478,810 rows × 15 columns**

---

## Phase 4: Analyze

### Key Findings
| Metric | Casual Riders | Members |
|--------|--------------|---------|
| Total rides | 1,426,959 | 2,051,851 |
| Avg ride length | 44.97 min | 16.12 min |
| Peak day | Saturday | Weekdays |

- Casual riders take **nearly 3x longer trips** than members
- Members ride consistently throughout the week (commute pattern)
- Casual riders are most active on **weekends** (leisure pattern)

---

## Phase 5: Share

📊 **[View Interactive Tableau Dashboard](https://public.tableau.com/app/profile/s.id.qurbanov/viz/CapstoneCyclistics/Dashboard1)**

Charts included:
- Number of rides by user type
- Average ride length by user type
- Rides by day of week

---

## Phase 6: Act

### Top 3 Recommendations

**1. Weekend Membership Promotions**
Run targeted digital ads on weekends when casual riders are most active. Message: *"You already love riding on weekends — save money with an annual membership!"*

**2. Ride Length Savings Campaign**
Show casual riders a cost comparison of paying per ride vs annual membership. A simple calculation showing monthly savings would be very persuasive.

**3. Spring/Summer Seasonal Campaign**
Launch a digital media campaign at the start of spring before peak riding season begins, highlighting the cost savings and convenience of annual membership.
