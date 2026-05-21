# Emirates Fleet Performance Analysis

**Capstone Project 3 | Python + Pandas + Seaborn**

Analysis of **7,974 flights** to identify which aircraft types perform best in Emirates' network across different route types.

## Executive Summary

This project analyzes Emirates' 2024 flight data to determine optimal aircraft-to-route matching based on profitability, load factor, and route characteristics (duration + altitude difference).

**Key Findings**
- **Airbus A380** is the strongest overall performer (**23.18%** average profit margin)
- **Boeing 787-9** excels on long-haul routes (**24.33%** margin)
- Wide-body aircraft significantly outperform narrow-bodies
- Narrow-body aircraft (A320 & 737-800) are currently unprofitable on short-haul routes

## Strategic Recommendations

1. **Fleet Deployment**
   - Prioritize Boeing 787-9 for ultra long-haul routes
   - Deploy Airbus A380 on high-demand medium-haul routes
   - Re-evaluate narrow-body operations on short-haul

2. **Data-Driven Optimization**
   - Implement route difficulty scoring (altitude difference + flight duration)
   - Build an internal aircraft assignment recommendation system

## Technologies Used
- Python, Pandas, Matplotlib, Seaborn
- Jupyter Notebook
- Data merging and feature engineering

## Project Structure
- `airline_capstone_v1.ipynb` → Main analysis notebook
- `data/` → Raw datasets (airports.dat, airline_route_profitability.csv, etc.)
- Visualizations of profitability by aircraft and route type

## Key Visualizations
- Profit Margin by Aircraft Type
- Profit Margin by Aircraft + Route Type (Short/Medium/Long-haul)
- Load Factor vs Flight Duration analysis

## Limitations
- Dataset is Emirates-focused (DXB-centric)
- Profitability numbers appear synthetic
- Limited aircraft technical specifications

---

**Status**: Completed May 2026

Feel free to reach out if you have any questions!

---

Made with ❤️ by Luca Mariani