# ANALYSIS OF NFL FOURTH DOWN DECISION MAKING.
import nfl_data_py as nfl
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pbp = nfl.import_pbp_data([2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])

# Filter for fourth down plays excluding 'no_play' types
pbp_clean = pbp[(pbp['down'] == 4) & (pbp['play_type'] != "no_play")]

play_types = ['go_for_it', 'punt', 'field_goal']

results = []

# Loop through each year and calculate percentages and average WPA for each play type
for year in range(2014, 2024):
    yearly_data = pbp_clean[pbp_clean['season'] == year]
    total_plays = len(yearly_data)
    if total_plays == 0:
        continue

    for play_type in play_types:
        if play_type == 'go_for_it':
            play_data = yearly_data[yearly_data['play_type'].isin(['run', 'pass'])]
        else:
            play_data = yearly_data[yearly_data['play_type'] == play_type]

        play_count = len(play_data)
        play_percentage = (play_count / total_plays) * 100
        average_wpa = play_data['wpa'].mean() if play_count > 0 else 0
        results.append({'year': year, 'play_type': play_type, 'percentage': play_percentage, 'average_wpa': average_wpa})

results_df = pd.DataFrame(results)


plt.figure(figsize=(14, 8))
sns.lineplot(data=results_df, x='year', y='percentage', hue='play_type', marker='o')


plt.title('Percentage of Fourth Down Decisions Over the Years')
plt.xlabel('Year')
plt.ylabel('Percentage')
plt.legend(title='Play Type')
plt.grid(True)
plt.show()

plt.figure(figsize=(14, 8))
sns.lineplot(data=results_df, x='year', y='average_wpa', hue='play_type', marker='o')


plt.title('Average WPA of Fourth Down Decisions Over the Years')
plt.xlabel('Year')
plt.ylabel('Average WPA')
plt.legend(title='Play Type')
plt.grid(True)
plt.show()