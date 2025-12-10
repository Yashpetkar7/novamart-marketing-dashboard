# NovaMart Marketing Analytics Dataset

## 📊 Masters of AI in Business - Data Visualization Assignment

This dataset simulates 2 years (2023-2024) of marketing data for **NovaMart**, a fictional omnichannel retail company operating across India.

---

## 📁 Dataset Files

| File | Records | Description |
|------|---------|-------------|
| `campaign_performance.csv` | 5,858 | Daily campaign metrics (impressions, clicks, conversions, spend, revenue) |
| `customer_data.csv` | 5,000 | Customer demographics, behavior, and churn indicators |
| `product_sales.csv` | 1,440 | Hierarchical product sales by category/subcategory |
| `lead_scoring_results.csv` | 2,000 | ML model predictions vs actual conversions |
| `feature_importance.csv` | 11 | Pre-calculated feature importance scores |
| `learning_curve.csv` | 11 | Training/validation scores at different data sizes |
| `geographic_data.csv` | 15 | State-level performance metrics with coordinates |
| `channel_attribution.csv` | 8 | Multi-touch attribution model comparison |
| `funnel_data.csv` | 6 | Marketing funnel stages and conversion rates |
| `customer_journey.csv` | 8 | Multi-touchpoint customer paths |
| `correlation_matrix.csv` | 10x10 | Pre-computed metric correlations |

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Up Project Structure
```
your_project/
├── data/
│   ├── campaign_performance.csv
│   ├── customer_data.csv
│   ├── ... (all CSV files)
├── app.py (or streamlit_starter_app.py)
├── requirements.txt
└── README.md
```

### 3. Run the Dashboard
```bash
streamlit run streamlit_starter_app.py
```

---

## 📈 Data Insights Built Into Dataset

### Campaign Performance
- **Seasonality**: Diwali (Oct-Nov) and Christmas (Dec) show 30-40% revenue boost
- **Weekend Effects**: Social media performs better on weekends; LinkedIn drops 40%
- **Channel Patterns**: Email has highest CVR; Google Ads highest volume

### Customer Data
- **Segment Profiles**: Premium customers have 2.5x higher LTV
- **Churn Indicators**: Low satisfaction + high support tickets = churn risk
- **Age-Income Correlation**: Peak income at age 45-50

### Product Sales
- **Category Performance**: Electronics highest volume; Fashion highest margins
- **Regional Variations**: West and South regions outperform
- **Quarterly Patterns**: Q4 electronics surge; Q2-Q3 fashion surge

### ML Model (Lead Scoring)
- **AUC**: ~0.75-0.80 (good predictive performance)
- **Key Features**: Webinar attendance and form submissions are strongest predictors
- **Learning Curve**: Model is well-calibrated, slight variance remains

---

## 🎯 Quick Setup for GitHub & Streamlit Cloud

### Step 1: Organize Files Locally
```
your_project/
├── app.py                    # Main dashboard file
├── requirements.txt          # Python dependencies
├── README.md                 # This documentation
└── data/
    ├── campaign_performance.csv
    ├── customer_data.csv
    ├── product_sales.csv
    ├── lead_scoring_results.csv
    ├── feature_importance.csv
    ├── learning_curve.csv
    ├── geographic_data.csv
    ├── channel_attribution.csv
    ├── funnel_data.csv
    ├── customer_journey.csv
    └── correlation_matrix.csv
```

### Step 2: Deploy to GitHub
```bash
git init
git add .
git commit -m "Add NovaMart Marketing Dashboard"
git branch -M main
git remote add origin https://github.com/yourusername/novamart-dashboard.git
git push -u origin main
```

### Step 3: Deploy to Streamlit Cloud
1. Go to https://streamlit.io/cloud
2. Sign in with GitHub
3. Click "New app"
4. Select your repository, branch, and `app.py` file
5. Click "Deploy"

Your dashboard will be live at: `https://[username]-novamart-dashboard-[branch].streamlit.app`

---

## 📊 Dashboard Features & Visualizations

### 📊 Visualization Mapping

| Chart Type | Data Source | Key Columns |
|------------|-------------|-------------|
| Bar Chart | campaign_performance | channel, revenue |
| Grouped Bar | campaign_performance | region, quarter, revenue |
| Line Chart | campaign_performance | date, revenue |
| Histogram | customer_data | age |
| Box Plot | customer_data | customer_segment, lifetime_value |
| Scatter Plot | customer_data | income, lifetime_value, customer_segment |
| Heatmap | correlation_matrix | all columns |
| Pie/Donut | channel_attribution | channel, model columns |
| Funnel | funnel_data | stage, visitors |
| Confusion Matrix | lead_scoring_results | actual_converted, predicted_class |
| Learning Curve | learning_curve | training_size, train_score, validation_score |
| Feature Importance | feature_importance | feature, importance |

---

## 🎯 Assignment Deliverables

1. **Streamlit Dashboard** - All 20+ visualizations
2. **Source Code** - Well-documented Python files
3. **Insights Report** - 2-page business insights summary
4. **Presentation** - 5-minute video walkthrough

---

## 📧 Questions?

Contact your course instructor.

**Good luck! Let data tell the story.** 📊✨
