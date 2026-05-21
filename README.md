# Emirates Fleet Performance Analysis

**Capstone Project 3 | Python + Pandas + Seaborn**

Analysis of **7,974 flights** to identify which aircraft types perform best in Emirates' network across different route types.

## Executive Summary

This project analyzes Emirates' 2024 flight data to determine optimal aircraft-to-route matching based on profitability, load factor, and route characteristics (duration + altitude difference).

**Key Findings**
- The **Airbus A380** is the strongest overall performer (**23.18%** average profit margin)
- The **Boeing 787-9** excels on long-haul routes (**24.33%** margin)
- Wide-body aircraft significantly outperform narrow-body aircraft
- Narrow-bodies (A320 & 737-800) are currently unprofitable on short-haul routes

## Strategic Recommendations

1. **Fleet Deployment**
   - Prioritize Boeing 787-9 for ultra long-haul routes
   - Deploy Airbus A380 on high-demand medium-haul routes
   - Re-evaluate narrow-body operations on short-haul routes

2. **Data-Driven Optimization**
   - Implement route difficulty scoring (altitude difference + flight duration)
   - Build an internal aircraft assignment recommendation system

## Technologies Used
- Python, Pandas, Matplotlib, Seaborn
- Jupyter Notebook
- Data merging and feature engineering

## Project Structure
- `airline_capstone_v1.ipynb` → Main analysis notebook
- Raw datasets (airports.dat, airline_route_profitability.csv, aircraft_dataset.csv)

## Key Visualizations
- Profit Margin by Aircraft Type
- Profit Margin by Aircraft + Route Type
- Load Factor vs Flight Duration analysis

## Limitations
- Dataset is heavily Emirates-focused (DXB-centric)
- Profitability numbers appear synthetic
- Limited aircraft variants and technical specifications

## Conclusion & Business Recommendations

Wide-body aircraft significantly outperform narrow-bodies in Emirates' network. Better aircraft-to-route matching represents a major opportunity for profitability improvement.

**Recommendations:**
1. Prioritize **Boeing 787-9** for ultra long-haul routes
2. Deploy **Airbus A380** on high-demand medium-haul routes
3. Re-evaluate or optimize narrow-body operations on short-haul routes
4. Implement a data-driven aircraft assignment system using route difficulty metrics
5. Use this type of analysis to support future fleet planning decisions

**Status**: Completed May 2026