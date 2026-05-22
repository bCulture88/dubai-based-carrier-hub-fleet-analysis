# Dubai Based Carrier Hub Fleet Analysis

**Capstone Project 3 | Python + Pandas + Seaborn**

Analysis of **7,974 flights** from a major Dubai-based carrier to identify which aircraft types perform best across different route categories (short, medium, and long-haul).

## Executive Summary

This capstone project analyzes 2024 flight data from a major Dubai hub carrier to determine optimal aircraft-to-route matching based on profitability, load factor, flight duration, and altitude difference.

**Key Findings:**
- The **Airbus A380** is the strongest overall performer with **23.18%** average profit margin.
- The **Boeing 787-9** excels on long-haul routes (**24.33%** margin).
- Wide-body aircraft significantly outperform narrow-body aircraft in this network.
- Narrow-bodies (A320 & 737-800) are currently unprofitable on short-haul routes.

**Strategic Recommendations**
- Prioritize Boeing 787-9 for ultra long-haul routes
- Deploy Airbus A380 on high-demand medium-haul routes
- Re-evaluate narrow-body operations on short-haul routes
- Implement data-driven aircraft assignment based on route difficulty

---

## 1. Data Overview

- **Total Flights Analyzed**: 7,974
- **Main Focus**: Major Dubai-based carrier operations (DXB hub)
- **Aircraft Types**: Airbus A320, A350-900, A380, Boeing 737-800, 777-300ER, 787-9
- **Key Metrics**: Profit Margin, Load Factor, Flight Hours, Airport Altitude

---

## 2. Methodology

- Loaded and merged route profitability data with OpenFlights airport database
- Enriched routes with altitude difference and flight duration
- Classified routes into Short-haul (<4h), Medium-haul (4-8h), Long-haul (>8h)
- Performed comparative analysis on profitability and operational efficiency

---

## 3. Visualizations

- Average Profit Margin by Aircraft Type
- Profit Margin by Aircraft Type and Route Category
- Average Load Factor vs Profit Margin by Aircraft Type (aggregated)

---

## 4. Key Findings

- **Best Overall**: Airbus A380 (23.18%)
- **Best on Long-Haul**: Boeing 787-9 (24.33%)
- **Best on Medium-Haul**: Airbus A380 (26.91%)
- Wide-body aircraft clearly dominate in profitability
- Narrow-body aircraft show losses on short-haul routes

---

## 5. Limitations

- Dataset is heavily focused on one major Dubai-based carrier (DXB-centric)
- Profitability numbers appear to be synthetic/simulated
- Limited aircraft variants available (no A220, A330, A350-1000, missing many 737/787 variants)
- Lack of detailed technical aircraft performance data (fuel burn, maintenance costs, etc.)
- No external factors included (weather, ATC, real maintenance records)

---

## 6. Conclusion & Business Recommendations

The analysis clearly demonstrates that **wide-body aircraft** significantly outperform narrow-bodies in Dubai-based operations. The performance gap is particularly evident on medium and long-haul routes, where the A380 and 787-9 deliver superior profitability.

**Key Business Recommendations:**

**Fleet Deployment Strategy**
- Prioritize Boeing 787-9 for ultra long-haul routes
- Deploy Airbus A380 on high-demand medium-haul routes

**Operational Optimization**
- Re-evaluate or restructure narrow-body operations on short-haul routes due to consistent losses

**Strategic Implementation**
- Develop a data-driven aircraft assignment system using route difficulty metrics (altitude difference + flight duration)
- Use this type of analysis to support future fleet planning and acquisition decisions for Dubai-based carriers

**Status**: Completed May 2026