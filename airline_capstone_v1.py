#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

base_path = "/Users/lucamariani/Desktop/3rd case study/"

# Load the files
airports = pd.read_csv(base_path + "airports.dat", 
                      header=None, 
                      na_values='\\N',
                      names=['airport_id', 'name', 'city', 'country', 'iata', 'icao', 
                             'lat', 'lon', 'altitude', 'timezone', 'dst', 'tz', 'type', 'source'])

aircraft_wb = pd.read_csv(base_path + "aircraft_dataset.csv")
aircraft_bb = pd.read_csv(base_path + "Aiplane_BlueBook.csv")
routes_profit = pd.read_csv(base_path + "airline_route_profitability.csv")

print("✅ All files loaded successfully!")
print("Airports:", airports.shape)
print("Aircraft Weight & Balance:", aircraft_wb.shape)
print("Aircraft BlueBook:", aircraft_bb.shape)
print("Route Profitability:", routes_profit.shape)


# In[2]:


import pandas as pd

base_path = "/Users/lucamariani/Desktop/3rd case study/"

# Reload (in case kernel restarted)
airports = pd.read_csv(base_path + "airports.dat", header=None, na_values='\\N',
    names=['airport_id', 'name', 'city', 'country', 'iata', 'icao', 'lat', 'lon', 
           'altitude', 'timezone', 'dst', 'tz', 'type', 'source'])

aircraft_wb = pd.read_csv(base_path + "aircraft_dataset.csv")
aircraft_bb = pd.read_csv(base_path + "Aiplane_BlueBook.csv")
routes_profit = pd.read_csv(base_path + "airline_route_profitability.csv")

print("=== AIRCRAFT WEIGHT & BALANCE COLUMNS ===")
print(aircraft_wb.columns.tolist())
print("\nSample models:", aircraft_wb['Aircraft Model'].head(10).tolist() if 'Aircraft Model' in aircraft_wb.columns else "No 'Aircraft Model' column")

print("\n=== AIRCRAFT BLUEBOOK COLUMNS ===")
print(aircraft_bb.columns.tolist())
print("\nSample models:", aircraft_bb.head(5).iloc[:, 0].tolist())

print("\n=== ROUTE PROFITABILITY COLUMNS ===")
print(routes_profit.columns.tolist())
print("\nSample Airlines/Routes:")
print(routes_profit[['Airline', 'Aircraft Type', 'Route', 'Distance (km)']].head(6) if 'Airline' in routes_profit.columns else routes_profit.head(3))


# In[3]:


import pandas as pd

base_path = "/Users/lucamariani/Desktop/3rd case study/"

# Reload datasets
airports = pd.read_csv(base_path + "airports.dat", header=None, na_values='\\N',
    names=['airport_id', 'name', 'city', 'country', 'iata', 'icao', 'lat', 'lon', 
           'altitude', 'timezone', 'dst', 'tz', 'type', 'source'])

aircraft = pd.read_csv(base_path + "aircraft_dataset.csv")
routes = pd.read_csv(base_path + "airline_route_profitability.csv")

# === Filter Aircraft to major manufacturers only ===
major_manufacturers = ['Airbus', 'Boeing', 'Embraer', 'Bombardier']

# Clean model names a bit
aircraft['Manufacturer'] = aircraft['Aircraft Model'].str.extract(r'(Airbus|Boeing|Embraer|Bombardier)', expand=False)

commercial_aircraft = aircraft[aircraft['Manufacturer'].notna()].copy()

print("Commercial aircraft after filtering:", commercial_aircraft.shape[0])
print("\nModels available:")
print(commercial_aircraft['Aircraft Model'].value_counts().head(15))

# === Quick look at routes ===
print("\n=== Top Aircraft Types in Routes dataset ===")
print(routes['Aircraft_Type'].value_counts().head(15))

print("\n=== Top Routes ===")
print(routes['Route'].value_counts().head(10))


# In[4]:


import pandas as pd

base_path = "/Users/lucamariani/Desktop/3rd case study/"

aircraft = pd.read_csv(base_path + "aircraft_dataset.csv")
routes = pd.read_csv(base_path + "airline_route_profitability.csv")

# Better manufacturer detection
def get_manufacturer(model):
    model = str(model).upper()
    if any(x in model for x in ['AIRBUS', 'A3', 'A32', 'A33', 'A34', 'A35', 'A38']):
        return 'Airbus'
    elif any(x in model for x in ['BOEING', 'B73', 'B74', 'B75', 'B76', 'B77', 'B78', 'B787', '737', '747', '757', '767', '777', '787']):
        return 'Boeing'
    elif any(x in model for x in ['EMBRAER', 'E170', 'E175', 'E190', 'E195']):
        return 'Embraer'
    elif any(x in model for x in ['BOMBARDIER', 'CRJ', 'GLOBAL', 'CHALLENGER']):
        return 'Bombardier'
    return None

aircraft['Manufacturer'] = aircraft['Aircraft Model'].apply(get_manufacturer)

commercial_aircraft = aircraft[aircraft['Manufacturer'].notna()].copy()

print("Commercial aircraft after improved filtering:", commercial_aircraft.shape[0])
print("\nModels per manufacturer:")
print(commercial_aircraft['Manufacturer'].value_counts())

print("\n=== Most common models now ===")
print(commercial_aircraft['Aircraft Model'].value_counts().head(20))

# Check overlap with routes dataset
routes_aircraft = routes['Aircraft_Type'].unique()
print("\n=== Some Aircraft in Routes dataset not in our aircraft table? ===")
print([ac for ac in ['A350', 'A330', '767', '757', 'CRJ', 'E175'] if any(ac in str(x) for x in routes_aircraft)])


# In[5]:


import pandas as pd

base_path = "/Users/lucamariani/Desktop/3rd case study/"

airports = pd.read_csv(base_path + "airports.dat", header=None, na_values='\\N',
    names=['airport_id', 'name', 'city', 'country', 'iata', 'icao', 'lat', 'lon', 
           'altitude', 'timezone', 'dst', 'tz', 'type', 'source'])

routes = pd.read_csv(base_path + "airline_route_profitability.csv")
aircraft = pd.read_csv(base_path + "aircraft_dataset.csv")

# Create airport lookup by IATA
airport_lookup = airports[airports['iata'].notna()].copy()
airport_lookup = airport_lookup.set_index('iata')[['name', 'city', 'country', 'altitude', 'lat', 'lon']]

# Add origin and destination airport altitude
routes_enriched = routes.copy()

# Extract origin and destination IATA
routes_enriched['Origin_IATA'] = routes_enriched['Origin']
routes_enriched['Dest_IATA'] = routes_enriched['Destination']

routes_enriched = routes_enriched.merge(
    airport_lookup[['altitude']].add_suffix('_origin'), 
    left_on='Origin_IATA', right_index=True, how='left'
)

routes_enriched = routes_enriched.merge(
    airport_lookup[['altitude']].add_suffix('_dest'), 
    left_on='Dest_IATA', right_index=True, how='left'
)

print("Routes with altitude info:", routes_enriched.shape)
print("\nTop 10 highest origin airports (altitude):")
print(routes_enriched.nlargest(10, 'altitude_origin')[['Origin', 'altitude_origin', 'Aircraft_Type']])

print("\nTop 10 routes with biggest altitude difference:")
routes_enriched['altitude_diff'] = abs(routes_enriched['altitude_origin'] - routes_enriched['altitude_dest'])
print(routes_enriched.nlargest(10, 'altitude_diff')[['Route', 'Aircraft_Type', 'altitude_origin', 'altitude_dest', 'altitude_diff']])


# In[1]:


import pandas as pd

base_path = "/Users/lucamariani/Desktop/3rd case study/"

airports = pd.read_csv(base_path + "airports.dat", header=None, na_values='\\N',
    names=['airport_id', 'name', 'city', 'country', 'iata', 'icao', 'lat', 'lon', 
           'altitude', 'timezone', 'dst', 'tz', 'type', 'source'])

routes = pd.read_csv(base_path + "airline_route_profitability.csv")
aircraft = pd.read_csv(base_path + "aircraft_dataset.csv")

print("We are dropping BlueBook - useless for commercial jets.")

# Create airport lookup
airport_lookup = airports[airports['iata'].notna() & (airports['type'] == 'airport')].copy()
airport_lookup = airport_lookup.set_index('iata')[['name', 'city', 'country', 'altitude', 'lat', 'lon']]

# Enrich routes with airport data
routes_enriched = routes.copy()
routes_enriched['Origin_IATA'] = routes_enriched['Origin']
routes_enriched['Dest_IATA'] = routes_enriched['Destination']

routes_enriched = routes_enriched.merge(airport_lookup.add_suffix('_origin'), 
                                      left_on='Origin_IATA', right_index=True, how='left')

routes_enriched = routes_enriched.merge(airport_lookup.add_suffix('_dest'), 
                                      left_on='Dest_IATA', right_index=True, how='left')

routes_enriched['altitude_diff'] = abs(routes_enriched['altitude_origin'] - routes_enriched['altitude_dest'])

print("Routes enriched with airport data:", routes_enriched.shape)
print("\nTop 10 highest origin airports:")
print(routes_enriched.nlargest(10, 'altitude_origin')[['Origin', 'altitude_origin', 'Aircraft_Type']].drop_duplicates(subset=['Origin']))

print("\nTop 10 biggest altitude difference routes:")
print(routes_enriched.nlargest(10, 'altitude_diff')[['Route', 'Aircraft_Type', 'altitude_origin', 'altitude_dest', 'altitude_diff']])


# In[2]:


import pandas as pd
import numpy as np

base_path = "/Users/lucamariani/Desktop/3rd case study/"

airports = pd.read_csv(base_path + "airports.dat", header=None, na_values='\\N',
    names=['airport_id', 'name', 'city', 'country', 'iata', 'icao', 'lat', 'lon', 
           'altitude', 'timezone', 'dst', 'tz', 'type', 'source'])

routes = pd.read_csv(base_path + "airline_route_profitability.csv")

# Airport lookup
airport_lookup = airports[airports['iata'].notna() & (airports['type'] == 'airport')].copy()
airport_lookup = airport_lookup.set_index('iata')[['name', 'city', 'country', 'altitude', 'lat', 'lon']]

# Enrich routes
routes_enriched = routes.copy()
routes_enriched['Origin_IATA'] = routes_enriched['Origin']
routes_enriched['Dest_IATA'] = routes_enriched['Destination']

routes_enriched = routes_enriched.merge(airport_lookup.add_suffix('_origin'), left_on='Origin_IATA', right_index=True, how='left')
routes_enriched = routes_enriched.merge(airport_lookup.add_suffix('_dest'), left_on='Dest_IATA', right_index=True, how='left')

routes_enriched['altitude_diff'] = abs(routes_enriched['altitude_origin'] - routes_enriched['altitude_dest'])
routes_enriched['distance_km'] = routes_enriched['Distance (km)']   # already exists in the dataset

print("Final enriched dataset shape:", routes_enriched.shape)
print("\nSummary Statistics:")
print(routes_enriched[['altitude_origin', 'altitude_dest', 'altitude_diff', 'distance_km']].describe())

print("\nTop Challenging Routes (high altitude diff + long distance):")
challenging = routes_enriched.nlargest(10, ['altitude_diff', 'distance_km'])
print(challenging[['Route', 'Aircraft_Type', 'altitude_origin', 'altitude_dest', 
                   'altitude_diff', 'distance_km', 'Profit_Margin']])


# In[3]:


import pandas as pd
import numpy as np

base_path = "/Users/lucamariani/Desktop/3rd case study/"

airports = pd.read_csv(base_path + "airports.dat", header=None, na_values='\\N',
    names=['airport_id', 'name', 'city', 'country', 'iata', 'icao', 'lat', 'lon', 
           'altitude', 'timezone', 'dst', 'tz', 'type', 'source'])

routes = pd.read_csv(base_path + "airline_route_profitability.csv")

# Airport lookup
airport_lookup = airports[airports['iata'].notna() & (airports['type'] == 'airport')].copy()
airport_lookup = airport_lookup.set_index('iata')[['name', 'city', 'country', 'altitude', 'lat', 'lon']]

# Enrich routes
routes_enriched = routes.copy()
routes_enriched['Origin_IATA'] = routes_enriched['Origin']
routes_enriched['Dest_IATA'] = routes_enriched['Destination']

routes_enriched = routes_enriched.merge(airport_lookup.add_suffix('_origin'), 
                                        left_on='Origin_IATA', right_index=True, how='left')
routes_enriched = routes_enriched.merge(airport_lookup.add_suffix('_dest'), 
                                        left_on='Dest_IATA', right_index=True, how='left')

routes_enriched['altitude_diff'] = abs(routes_enriched['altitude_origin'] - routes_enriched['altitude_dest'])

# Check the actual distance column name
print("Available columns with 'distance' or 'Distance':")
print([col for col in routes_enriched.columns if 'dist' in col.lower() or 'km' in col.lower()])

# Fix distance assignment
if 'Distance (km)' in routes_enriched.columns:
    routes_enriched['distance_km'] = routes_enriched['Distance (km)']
elif 'Distance_km' in routes_enriched.columns:
    routes_enriched['distance_km'] = routes_enriched['Distance_km']
else:
    print("No distance column found, checking all columns...")
    print(routes_enriched.columns.tolist()[:30])  # first 30 columns

print("\nFinal enriched dataset shape:", routes_enriched.shape)
print("\nSummary Statistics:")
print(routes_enriched[['altitude_origin', 'altitude_dest', 'altitude_diff']].describe())

print("\nTop 10 Most Challenging Routes (by altitude difference):")
challenging = routes_enriched.nlargest(10, 'altitude_diff')
print(challenging[['Route', 'Aircraft_Type', 'altitude_origin', 'altitude_dest', 
                   'altitude_diff', 'Profit_Margin']].head(10))


# In[4]:


import pandas as pd

base_path = "/Users/lucamariani/Desktop/3rd case study/"

airports = pd.read_csv(base_path + "airports.dat", header=None, na_values='\\N',
    names=['airport_id', 'name', 'city', 'country', 'iata', 'icao', 'lat', 'lon', 
           'altitude', 'timezone', 'dst', 'tz', 'type', 'source'])

routes = pd.read_csv(base_path + "airline_route_profitability.csv")

# Airport lookup
airport_lookup = airports[airports['iata'].notna() & (airports['type'] == 'airport')].copy()
airport_lookup = airport_lookup.set_index('iata')[['name', 'city', 'country', 'altitude', 'lat', 'lon']]

# Enrich routes
routes_enriched = routes.copy()
routes_enriched['Origin_IATA'] = routes_enriched['Origin']
routes_enriched['Dest_IATA'] = routes_enriched['Destination']

routes_enriched = routes_enriched.merge(airport_lookup.add_suffix('_origin'), left_on='Origin_IATA', right_index=True, how='left')
routes_enriched = routes_enriched.merge(airport_lookup.add_suffix('_dest'), left_on='Dest_IATA', right_index=True, how='left')

routes_enriched['altitude_diff'] = abs(routes_enriched['altitude_origin'] - routes_enriched['altitude_dest'])

print("Enriched shape:", routes_enriched.shape)

# Route difficulty features
routes_enriched['flight_hours'] = routes_enriched['Flight_Hours']
routes_enriched['route_difficulty'] = (routes_enriched['altitude_diff'] / 1000) + (routes_enriched['flight_hours'] * 0.3)

print("\n=== Summary of Key Metrics ===")
print(routes_enriched[['altitude_diff', 'flight_hours', 'route_difficulty', 'Profit_Margin']].describe())

print("\n=== Top 10 Most Challenging Routes (High altitude diff + longer flight) ===")
challenging = routes_enriched.nlargest(10, 'route_difficulty')
print(challenging[['Route', 'Aircraft_Type', 'altitude_diff', 'flight_hours', 
                   'route_difficulty', 'Profit_Margin', 'Load_Factor']])


# In[5]:


import pandas as pd

# If routes_enriched is not in memory, re-run the enrichment first or just use this full block
base_path = "/Users/lucamariani/Desktop/3rd case study/"

airports = pd.read_csv(base_path + "airports.dat", header=None, na_values='\\N',
    names=['airport_id', 'name', 'city', 'country', 'iata', 'icao', 'lat', 'lon', 
           'altitude', 'timezone', 'dst', 'tz', 'type', 'source'])

routes = pd.read_csv(base_path + "airline_route_profitability.csv")

airport_lookup = airports[airports['iata'].notna() & (airports['type'] == 'airport')].copy()
airport_lookup = airport_lookup.set_index('iata')[['name', 'city', 'country', 'altitude', 'lat', 'lon']]

routes_enriched = routes.copy()
routes_enriched['Origin_IATA'] = routes_enriched['Origin']
routes_enriched['Dest_IATA'] = routes_enriched['Destination']

routes_enriched = routes_enriched.merge(airport_lookup.add_suffix('_origin'), left_on='Origin_IATA', right_index=True, how='left')
routes_enriched = routes_enriched.merge(airport_lookup.add_suffix('_dest'), left_on='Dest_IATA', right_index=True, how='left')

routes_enriched['altitude_diff'] = abs(routes_enriched['altitude_origin'] - routes_enriched['altitude_dest'])
routes_enriched['flight_hours'] = routes_enriched['Flight_Hours']

print("=== Emirates Fleet Performance Comparison ===\n")

# Main comparison table
fleet_performance = routes_enriched.groupby('Aircraft_Type').agg(
    num_flights=('Aircraft_Type', 'count'),
    avg_flight_hours=('flight_hours', 'mean'),
    avg_altitude_diff=('altitude_diff', 'mean'),
    avg_load_factor=('Load_Factor', 'mean'),
    avg_profit_margin=('Profit_Margin', 'mean'),
    avg_total_revenue=('Total_Revenue', 'mean'),
    profit_std=('Profit_Margin', 'std')
).round(3)

fleet_performance = fleet_performance.sort_values('avg_profit_margin', ascending=False)

print(fleet_performance)


# In[6]:


import pandas as pd

# Re-create enriched dataframe (just in case)
base_path = "/Users/lucamariani/Desktop/3rd case study/"
routes = pd.read_csv(base_path + "airline_route_profitability.csv")

routes_enriched = routes.copy()
routes_enriched['flight_hours'] = routes_enriched['Flight_Hours']

# Create route type
routes_enriched['route_type'] = pd.cut(routes_enriched['flight_hours'], 
                                       bins=[0, 4, 8, 20], 
                                       labels=['Short-haul', 'Medium-haul', 'Long-haul'])

print("=== Performance by Route Type ===\n")
performance_by_type = routes_enriched.groupby(['Aircraft_Type', 'route_type']).agg(
    num_flights=('Aircraft_Type', 'count'),
    avg_profit_margin=('Profit_Margin', 'mean'),
    avg_load_factor=('Load_Factor', 'mean')
).round(3)

print(performance_by_type)

print("\n=== Recommendation Summary ===")
print("Best aircraft for Long-haul (>8h):")
long_haul = routes_enriched[routes_enriched['route_type'] == 'Long-haul']
print(long_haul.groupby('Aircraft_Type')['Profit_Margin'].mean().sort_values(ascending=False))


# In[7]:


import pandas as pd

base_path = "/Users/lucamariani/Desktop/3rd case study/"
routes = pd.read_csv(base_path + "airline_route_profitability.csv")

routes_enriched = routes.copy()
routes_enriched['flight_hours'] = routes_enriched['Flight_Hours']
routes_enriched['route_type'] = pd.cut(routes_enriched['flight_hours'], 
                                       bins=[0, 4, 8, 20], 
                                       labels=['Short-haul', 'Medium-haul', 'Long-haul'])

# Final summary table
summary = routes_enriched.groupby('Aircraft_Type').agg(
    num_flights=('Aircraft_Type', 'count'),
    short_haul_pct=('route_type', lambda x: (x == 'Short-haul').mean() * 100),
    med_haul_pct=('route_type', lambda x: (x == 'Medium-haul').mean() * 100),
    long_haul_pct=('route_type', lambda x: (x == 'Long-haul').mean() * 100),
    avg_profit_margin=('Profit_Margin', 'mean'),
    avg_load_factor=('Load_Factor', 'mean'),
    profit_std=('Profit_Margin', 'std')
).round(2)

print("=== FINAL FLEET PERFORMANCE SUMMARY ===")
print(summary.sort_values('avg_profit_margin', ascending=False))


# In[8]:


import pandas as pd

base_path = "/Users/lucamariani/Desktop/3rd case study/"
routes = pd.read_csv(base_path + "airline_route_profitability.csv")

routes_enriched = routes.copy()
routes_enriched['flight_hours'] = routes_enriched['Flight_Hours']
routes_enriched['route_type'] = pd.cut(routes_enriched['flight_hours'], 
                                       bins=[0, 4, 8, 20], 
                                       labels=['Short-haul', 'Medium-haul', 'Long-haul'])

# Detailed view
print("=== AIRCRAFT PERFORMANCE BY ROUTE TYPE (Profit Margin) ===\n")
pivot = routes_enriched.pivot_table(
    values='Profit_Margin',
    index='Aircraft_Type',
    columns='route_type',
    aggfunc='mean'
).round(2)

print(pivot)

print("\n=== Key Takeaways so far ===")
print("- Best overall performer:", "Airbus A380")
print("- Best on Long-haul:", "Boeing 787-9")
print("- Best on Medium-haul:", "Airbus A380 & Boeing 777-300ER")
print("- Narrow-bodies struggling in this dataset")


# In[9]:


print("=== FINAL PROJECT INSIGHTS & RECOMMENDATIONS ===\n")

print("1. Overall Best Performer:")
print("- Airbus A380 leads with highest average profit margin (23.18%)")

print("\n2. Route Type Recommendations:")
print("- Long-haul (>8h)  → Boeing 787-9 (24.33% margin)")
print("- Medium-haul (4-8h) → Airbus A380 (26.91%)")
print("- Short-haul (<4h)  → Boeing 777-300ER surprisingly best (28.07%)")

print("\n3. Key Observations:")
print("- Wide-body aircraft significantly outperform narrow-bodies in this network")
print("- A350-900 underperforms relative to its reputation")
print("- Narrow-body (A320 & 737-800) routes are currently unprofitable")

print("\nBusiness Recommendations for Emirates:")
print("- Prioritize Boeing 787-9 for ultra long-haul routes (e.g. DXB-SFO, DXB-LAX)")
print("- Deploy A380 on high-demand medium-haul routes where it excels")
print("- Re-evaluate narrow-body operations or improve load factors/cost control on short routes")
print("- Consider fleet mix optimization based on route difficulty (altitude + distance)")


# In[10]:


import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12, 6))
sns.barplot(data=routes_enriched, x='Aircraft_Type', y='Profit_Margin', errorbar=None)
plt.title('Average Profit Margin by Aircraft Type - Emirates Network', fontsize=14)
plt.xlabel('Aircraft Type')
plt.ylabel('Average Profit Margin (%)')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()


# In[11]:


plt.figure(figsize=(14, 7))
sns.barplot(data=routes_enriched, x='Aircraft_Type', y='Profit_Margin', hue='route_type')
plt.title('Profit Margin by Aircraft and Route Type')
plt.xlabel('Aircraft Type')
plt.ylabel('Average Profit Margin (%)')
plt.xticks(rotation=45)
plt.legend(title='Route Type')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()


# In[12]:


plt.figure(figsize=(10, 6))
sns.scatterplot(data=routes_enriched, x='Load_Factor', y='Profit_Margin', hue='Aircraft_Type', s=80)
plt.title('Load Factor vs Profit Margin by Aircraft')
plt.xlabel('Load Factor')
plt.ylabel('Profit Margin (%)')
plt.grid(True, alpha=0.3)
plt.show()


# # Emirates Fleet Performance Analysis
# 
# ## Executive Summary
# 
# This capstone project analyzes **7,974 flights** from Emirates' 2024 network to determine which aircraft types deliver the best operational and financial performance across different route categories (short, medium, and long-haul).
# 
# **Key Findings:**
# - The **Airbus A380** is the strongest overall performer with an average profit margin of **23.18%**.
# - The **Boeing 787-9** excels on long-haul routes (**24.33%** margin).
# - Wide-body aircraft significantly outperform narrow-body aircraft in this network.
# - Narrow-bodies (A320 & 737-800) are currently unprofitable on short-haul routes.
# 
# ## Strategic Recommendations
# 
# 1. **Fleet Deployment Strategy**
#    - Prioritize **Boeing 787-9** for ultra long-haul routes (e.g. DXB-SFO, DXB-LAX)
#    - Deploy **Airbus A380** on high-demand medium-haul routes
#    - Re-evaluate narrow-body operations on short-haul routes
# 
# 2. **Route-Aircraft Matching**
#    - Implement data-driven aircraft assignment based on route difficulty (distance + altitude difference)
# 
# 3. **Business Impact**
#    - Better fleet optimization could significantly improve overall profitability
#    - This type of analysis should be considered for future fleet acquisition decisions

# In[13]:


import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12, 8))

# Improved scatterplot
sns.scatterplot(
    data=routes_enriched, 
    x='Load_Factor', 
    y='Profit_Margin', 
    hue='Aircraft_Type',
    size='flight_hours',
    sizes=(50, 300),
    alpha=0.7
)

plt.title('Load Factor vs Profit Margin by Aircraft Type\n(size = flight duration)', fontsize=14)
plt.xlabel('Load Factor')
plt.ylabel('Profit Margin (%)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show


# ## 1. Data Overview
# 
# - **Total Flights**: 7,974
# - **Origin**: Mostly Dubai (DXB) – Emirates-focused dataset
# - **Aircraft Types**: 6 (A320, A350-900, A380, 737-800, 777-300ER, 787-9)
# - **Key Metrics**: Profit Margin, Load Factor, Flight Hours, Airport Altitude
# - **Route Classification**: Short-haul (<4h), Medium-haul (4-8h), Long-haul (>8h)

# ## 1. Data Overview
# 
# - **Total Flights**: 7,974
# - **Origin**: Mostly Dubai (DXB) – Emirates-focused dataset
# - **Aircraft Types**: 6 (A320, A350-900, A380, 737-800, 777-300ER, 787-9)
# - **Key Metrics**: Profit Margin, Load Factor, Flight Hours, Airport Altitude
# - **Route Classification**: Short-haul (<4h), Medium-haul (4-8h), Long-haul (>8h)

# ## 1. Data Overview
# 
# - **Total Flights**: 7,974
# - **Origin**: Mostly Dubai (DXB) – Emirates-focused dataset
# - **Aircraft Types**: 6 (A320, A350-900, A380, 737-800, 777-300ER, 787-9)
# - **Key Metrics**: Profit Margin, Load Factor, Flight Hours, Airport Altitude
# - **Route Classification**: Short-haul (<4h), Medium-haul (4-8h), Long-haul (>8h)

# ## 1. Data Overview
# 
# - **Total Flights**: 7,974
# - **Origin**: Mostly Dubai (DXB) – Emirates-focused dataset
# - **Aircraft Types**: 6 (A320, A350-900, A380, 737-800, 777-300ER, 787-9)
# - **Key Metrics**: Profit Margin, Load Factor, Flight Hours, Airport Altitude
# - **Route Classification**: Short-haul (<4h), Medium-haul (4-8h), Long-haul (>8h)

# ## 2. Methodology
# 
# - Loaded and merged route profitability data with OpenFlights airport database (altitude)
# - Created route difficulty features (altitude difference + flight duration)
# - Classified routes into Short / Medium / Long-haul
# - Performed comparative analysis using profitability, load factor, and operational metrics

# ## 3. Key Findings
# 
# ### Overall Performance Ranking
# - **Best**: Airbus A380 (23.18%)
# - **Second**: Boeing 777-300ER (17.26%)
# - **Worst**: Boeing 737-800 (-9.50%)
# 
# ### By Route Type
# - **Long-haul (>8h)**: Boeing 787-9 leads
# - **Medium-haul (4-8h)**: Airbus A380 dominates
# - **Short-haul**: Boeing 777-300ER performs best (surprisingly)

# ## 4. Visualizations
# 
# - Average Profit Margin by Aircraft Type
# - Profit Margin by Aircraft and Route Type
# - Load Factor vs Flight Duration (sized by Profit Margin)

# ## 5. Limitations
# 
# - Dataset is heavily biased toward Emirates operations (DXB-centric)
# - Profitability figures appear synthetic
# - Limited detailed aircraft performance specifications (weight, fuel burn, etc.)
# - No real weather or maintenance data
#   

# ## 6. Conclusion & Business Recommendations
# 
# The analysis demonstrates that **wide-body aircraft** are significantly more profitable than narrow-bodies in Emirates’ current network.
# 
# **Strategic Recommendations**
# 
# 1. **Fleet Assignment Optimization**
#    - Prioritize **Boeing 787-9** for ultra long-haul routes
#    - Deploy **Airbus A380** on high-demand medium-haul routes
# 
# 2. **Short-haul Strategy**
#    - Re-evaluate narrow-body operations or improve cost control and load factors
# 
# 3. **Long-term Fleet Planning**
#    - Use route difficulty scoring (altitude + distance) when making future aircraft acquisition decisions
# 
# 4. **Implementation**
#    - Build an internal dashboard for real-time aircraft-route recommendation system
