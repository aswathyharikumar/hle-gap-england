# Healthy Life Expectancy Gap Analysis: England 2011-2024

**Interactive Dashboard:** [https://hle-gap-dashboard.onrender.com](https://hle-gap-dashboard.onrender.com)

Analysis of health inequality trends across 218 English local authorities, revealing that 86% are moving away from the UK government's 2035 health equity target.

---

## 🔍 Key Findings

- **86% of areas are worsening** - Only 18 of 128 analyzed local authorities show improving trends (gap shrinking)
- **Average HLE gap will increase from 20.9 to 23.9 years by 2035** - People will spend 3 additional years in poor health
- **England will miss the 2035 target by 1.6 years** - Achieving only 14% reduction in inequality instead of the required 50%
- **Affluent areas declining faster than deprived areas** - Counterintuitively, wealthy areas worsening by 2.65 years vs 2.09 years in deprived areas

---

## 📊 What is the HLE Gap?

The **Healthy Life Expectancy (HLE) Gap** measures how many years people live in poor health:

**HLE Gap = Life Expectancy - Healthy Life Expectancy**

For example:
- Person lives to 80 years (Life Expectancy)
- But only 60 years are in good health (Healthy Life Expectancy)
- **HLE Gap = 20 years** spent living with illness, disability, or health limitations

---

## 📈 Visualizations

### National Trend (2011-2024)
The average HLE gap in England has increased from 19.1 years (2011-2013) to 20.9 years (2022-2024).

### Traffic Light Status
- 🟢 **18 areas** - On track (improving)
- 🟡 **45 areas** - Borderline (slow decline)
- 🔴 **65 areas** - Off track (rapid decline)

### 2035 Projections
If current trends continue, the inequality gap between rich and poor areas will only reduce from 4.4 to 3.8 years - missing the government's target of 2.2 years.

---

## 🗂️ Data Sources

- **Office for National Statistics (ONS)** - Health State Life Expectancy by Local Areas, UK (2011-2024)
- **Ministry of Housing, Communities and Local Government** - Index of Multiple Deprivation 2019
- **Coverage:** 128 English local authorities with complete 12-year data (out of 218 total)

---

## 🛠️ Tech Stack

- **Python** - pandas, NumPy, matplotlib, plotly
- **Dash** - Interactive web dashboard
- **Statistical Analysis** - Trend analysis, linear projection, correlation analysis
- **Deployment** - GitHub, Render (free tier)

---

## 📁 Project Structure
```
hle-gap-england/
├── data/                          # Raw datasets (ONS, IMD)
├── notebooks/                     # Jupyter notebooks with analysis
├── outputs/                       # Generated charts and results
│   ├── chart1_national_trend.png
│   ├── chart2_traffic_light.png
│   ├── chart3_best_worst.png
│   ├── chart4_deprivation_scatter.png
│   ├── chart5_target_vs_reality.png
│   └── final_analysis_with_projections.csv
├── dashboard_app.py              # Interactive Dash application
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

---

## 🚀 How to Run Locally

### Prerequisites
- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/aswathyharikumar/hle-gap-england.git
cd hle-gap-england
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the dashboard:
```bash
python dashboard_app.py
```

4. Open your browser to: `http://127.0.0.1:8050`

---

## 📊 Analysis Methodology

1. **Data Cleaning** - Filtered to 128 English local authorities with complete 12-year data
2. **Trend Analysis** - Calculated annual rate of change (2011-2024) for each area
3. **Projection** - Linear extrapolation to 2035 based on observed trends
4. **Inequality Measurement** - Compared HLE gaps between most and least deprived areas
5. **Status Classification**:
   - 🟢 Improving: Gap shrinking (negative change)
   - 🟡 Borderline: Gap widening 0-3 years
   - 🔴 Off Track: Gap widening 3+ years

---

## 🎯 Policy Implications

### Immediate Actions Needed:
1. **Urgent intervention required** - Current trajectory makes 2035 target unachievable
2. **Focus on 65 "rapid decline" areas** - Deploy emergency funding and resources
3. **Investigate affluent area decline** - Mental health crisis, chronic disease prevention
4. **Quarterly monitoring** - Track progress with corrective action triggers

### Recommended Next Steps:
- Revise 2035 target timeline (current trajectory unachievable)
- Implement "learning from success" program (18 improving areas share strategies)
- Shift NHS funding toward prevention over treatment in high-burden areas

---

## 👤 Author

**Aswathy Harikumar**

Public Health Analyst | Data Science Enthusiast

📧 [Your email if you want to include it]  
💼 [LinkedIn profile if you want to include it]  
🌐 [Portfolio website if you have one]

---

## 📝 License

This project is open source and available for educational and research purposes.

---

## 🙏 Acknowledgments

- Office for National Statistics (ONS) for health data
- UK Health Security Agency (UKHSA) for inequality metrics
- Ministry of Housing, Communities and Local Government for deprivation indices

---

**Last Updated:** March 2026
