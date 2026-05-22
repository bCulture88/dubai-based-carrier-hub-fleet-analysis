# Dubai Based Carrier Hub Fleet Analysis

**Capstone Project 3 | Python + Pandas + Seaborn**

Analysis of **7,974 flights** from a major Dubai-based carrier to identify which aircraft types perform best across different route categories.

## Executive Summary

This project analyzes 2024 flight data from a major Dubai hub carrier to determine optimal aircraft-to-route matching based on profitability, load factor, and route characteristics (flight duration + altitude difference).

**Key Findings:**
- The **Airbus A380** is the strongest overall performer (**23.18%** average profit margin)
- The **Boeing 787-9** excels on long-haul routes (**24.33%** margin)
- Wide-body aircraft significantly outperform narrow-body aircraft
- Narrow-bodies (A320 & 737-800) are currently unprofitable on short-haul routes

## Strategic Recommendations

1. **Fleet Deployment Strategy**
   - Prioritize Boeing 787-9 for ultra long-haul routes
   - Deploy Airbus A380 on high-demand medium-haul routes
   - Re-evaluate narrow-body operations on short-haul routes

2. **Data-Driven Optimization**
   - Implement route difficulty scoring (altitude difference + flight duration)
   - Build internal tools for aircraft-route recommendation

## Technologies Used
- Python, Pandas, Matplotlib, Seaborn
- Jupyter Notebook
- Data merging and feature engineering

## Project Structure
- `Dubai_Based_Carrier_Hub_Fleet_Analysis.ipynb` → Main analysis notebook
- Raw datasets (airports.dat, airline_route_profitability.csv, aircraft_dataset.csv)

## Key Visualizations
- Profit Margin by Aircraft Type
- Profit Margin by Aircraft and Route Type
- Average Load Factor vs Profit Margin by Aircraft Type

## Limitations
- Dataset is focused on one major Dubai-based carrier
- Profitability numbers appear synthetic
- Limited aircraft variants and technical specifications

**Status**: Completed May 2026