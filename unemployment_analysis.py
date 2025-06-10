# %% [markdown]
# # Data Loading and Exploration

# %%
import pandas as pd
import matplotlib.pyplot as plt
# Load the provided unemployment data
df = pd.read_csv('UNRATE.csv')

# %%
print(df.columns.tolist())

# %%
df['observation_date'] = pd.to_datetime(df['observation_date'])

print("Dataset shape:", df.shape)
print("\nFirst 5 rows:")
df.head()

# %%
print("Data types:")
print(df.dtypes)
print("\nBasic statistics:")
df['UNRATE'].describe()

# %% [markdown]
# # Statistical Analysis

# %% [markdown]
# #### Calculate overall average unemployment rate

# %%
mean_unrate = df['UNRATE'].mean()
print(f"Overall average unemployment rate: {mean_unrate:.2f}%")

# %% [markdown]
# #### Find minimum and maximum unemployment rates with their dates

# %%
min_unrate = df['UNRATE'].min()
max_unrate = df['UNRATE'].max()

# Find all observation_dates corresponding to the minimum unemployment rate
min_dates = df.loc[df['UNRATE'] == min_unrate, 'observation_date']

# maximum
max_dates = df.loc[df['UNRATE'] == max_unrate, 'observation_date']

print(f"Minimum unemployment rate: {min_unrate}%")
print("Occurred on:")
for date in min_dates:
    print(f" - {date}")

print(f"\nMaximum unemployment rate: {max_unrate}%")
print("Occurred on:")
for date in max_dates:
    print(f" - {date}")


# %% [markdown]
# #### Calculate unemployment statistics by decade (1950s, 1960s, etc.)

# %%
df['DECADE'] = (df['observation_date'].dt.year // 10) * 10
decade_stats = df.groupby('DECADE')['UNRATE'].describe()

print(f"Unemployment statistics by era:{decade_stats}")

# %% [markdown]
# #### Identify the year with the highest average unemployment rate

# %%
df['YEAR'] = df['observation_date'].dt.year
year_avg = df.groupby('YEAR')['UNRATE'].mean()
# max unrate
max_year_unrate = year_avg.max()
# all
max_years = year_avg[year_avg == max_year_unrate].index.tolist()
print(f"Maximum average unemployment rate: {max_year_unrate}%")
print("Occurred in year(s):")
for year in max_years:
    print(f" - {year}")

# %% [markdown]
# # Business Questions to Answer

# %% [markdown]
# #### What was the unemployment rate during major economic events (2008 financial crisis, COVID-19 pandemic)?

# %%
crisis_2008 = df[(df['observation_date'] >= '2008-01-01') & (df['observation_date'] <= '2009-12-31')]
covid_2020 = df[(df['observation_date'] >= '2020-01-01') & (df['observation_date'] <= '2022-12-31')]
print(f"2008 Financial Crisis Unemployment Stats:{crisis_2008['UNRATE'].describe()}")
print(f"COVID-19 Pandemic Unemployment Stats:{covid_2020['UNRATE'].describe()}")

# %% [markdown]
# During the 2008 financial crisis, the average unemployment rate was 7.54%, the highest was 10%, and most of the unemployment rates were between 5.75-9.5%. During the COVID 19 pandemic, the average unemployment rate was 5.7%, which was lower than the financial crisis, but the highest was 14.8%(higher than 2008), and most of the unemployment rates were between 3.6-6.48%.

# %% [markdown]
# ####  Which decade had the most stable unemployment rates (lowest standard deviation)?

# %%
most_stable_decade = decade_stats['std'].idxmin()
lowest_std = decade_stats['std'].min()

print(f"\nThe most stable unemployment rates occurred in the {most_stable_decade}s, with a standard deviation of {lowest_std}.")

# %% [markdown]
# The most stable unemployment rates occurred in the 1990s, with a standard deviation of 1.0492944808598896.

# %% [markdown]
# #### What’s the trend in unemployment over the last 10 years?

# %%
recent_df = df[df['observation_date'].dt.year >= 2015]
recent_df['YEAR'] = recent_df['observation_date'].dt.year
yearly_avg = recent_df.groupby('YEAR')['UNRATE'].mean()

plt.figure(figsize=(10, 5))
plt.plot(yearly_avg.index, yearly_avg.values)
plt.title('Unemployment Rate Trend (Last 10 Years)')
plt.xlabel('Year')
plt.ylabel('Average Unemployment Rate (%)')
plt.show()


# %% [markdown]
# In the past decade, the unemployment rate slowly declined from 2015 to 2019, and then rose sharply due to the impact of the COVID-19 pandemic, reaching a peak of 8 in 2020, and then fell sharply to 2022 and then slowly rose again.

# %% [markdown]
# # Data Visualization

# %% [markdown]
# #### Create a line chart showing unemployment rate over time
# #### Create a bar chart showing average unemployment by decade
# #### Save both charts as PNG files
# #### Add proper titles, labels, and formatting

# %%
# Calculate decade averages
df['Decade'] = (df['observation_date'].dt.year // 10) * 10
decade_avg = df.groupby('Decade')['UNRATE'].mean()

# Create visualizations
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

 # Time series plot
ax1.plot(df['observation_date'], df['UNRATE'])
ax1.set_title('US Unemployment Rate Over Time')
ax1.set_xlabel('Year')
ax1.set_ylabel('Unemployment Rate (%)')

# Decade averages
decade_avg.plot(kind='bar', ax=ax2)
ax2.set_title('Average Unemployment Rate by Decade')
ax2.set_xlabel('Decade')
ax2.set_ylabel('Average Unemployment Rate (%)')

# Save and Show
plt.tight_layout()
plt.savefig('unemployment_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

# %% [markdown]
# 


