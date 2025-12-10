# 🎯 Quick Reference Guide - NovaMart Dashboard

## 📁 Project Files Checklist

| File | Purpose | Status |
|------|---------|--------|
| `app.py` | Main Streamlit application (900+ lines) | ✅ Ready |
| `requirements.txt` | Python package dependencies | ✅ Ready |
| `README.md` | Comprehensive documentation | ✅ Ready |
| `DEPLOYMENT.md` | Step-by-step GitHub/Streamlit deployment guide | ✅ Ready |
| `.gitignore` | Exclude unnecessary files from Git | ✅ Ready |
| `.streamlit/config.toml` | Streamlit configuration | ✅ Ready |
| `data/` folder | Contains all 11 CSV files | ✅ Required |

---

## 🚀 Quick Deploy (3 Steps)

### Step 1: Push to GitHub
```powershell
cd novamart-dashboard
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/novamart-dashboard.git
git push -u origin main
```

### Step 2: Connect to Streamlit Cloud
- Visit https://share.streamlit.io
- Sign in with GitHub
- Click "New app"
- Select your repository and `app.py`
- Click "Deploy"

### Step 3: Share the URL
Your dashboard is live at:
```
https://yourusername-novamart-dashboard-main.streamlit.app
```

---

## 📊 Dashboard Pages Overview

| Page | Focus | Key Visualizations |
|------|-------|-------------------|
| 🏠 Home | Executive Summary | KPIs, Revenue Trend, Channel Performance |
| 📈 Campaign Performance | Marketing Metrics | Revenue by Channel, ROAS, Spend vs Revenue |
| 👥 Customer Analytics | Customer Segments | Age Distribution, LTV, Churn Risk, Satisfaction |
| 🗺️ Geographic Analysis | Regional Performance | Revenue by State, YoY Growth, Market Penetration |
| 🎯 Lead Scoring & ML | Predictive Model | Confusion Matrix, Feature Importance, AUC Score |
| 🛍️ Product Analysis | Product Performance | Sales by Category, Top Products, Price Elasticity |
| 🔗 Attribution & Journey | Customer Paths | Attribution Models, Funnel Stages, Journey Paths |

---

## 💾 Data Files (11 CSV Files)

Place all these in the `data/` folder:

```
campaign_performance.csv      5,858 records  - Daily campaign metrics
customer_data.csv            5,000 records  - Customer demographics & behavior
product_sales.csv            1,440 records  - Product sales by category
lead_scoring_results.csv     2,000 records  - ML model predictions
geographic_data.csv             15 records  - State-level metrics
channel_attribution.csv            8 records  - Multi-touch attribution
funnel_data.csv                   6 records  - Marketing funnel stages
customer_journey.csv               8 records  - Customer path sequences
feature_importance.csv            11 records  - ML feature scores
learning_curve.csv                11 records  - Model learning curves
correlation_matrix.csv         10x10 matrix  - Metric correlations
```

---

## 🔑 Key Metrics Tracked

### Campaign Performance
- Total Revenue: ₹2.5B+
- Total Conversions: 500K+
- Average ROAS: 3.2x
- Average CTR: 3.4%

### Customer Analytics
- Active Customers: 5,000
- Average LTV: ₹24,500
- Churn Rate: 12-15%
- Avg Satisfaction: 3.5/5.0

### Geographic Coverage
- States: 15 major Indian states
- YoY Growth: 13-20% average
- Market Penetration: 7-30% by state
- Total Stores: 180+

### ML Model Performance
- AUC Score: 0.75-0.80
- Precision: 0.70-0.75
- Recall: 0.65-0.70
- Accuracy: 72-78%

---

## 🎨 Color Scheme & Theming

The dashboard uses Plotly's built-in color scales:
- **Primary**: `#1f77b4` (Blue)
- **Secondary**: `#f0f2f6` (Light Gray)
- **Success**: `#2ca02c` (Green) - for positive metrics
- **Warning**: `#ff7f0e` (Orange) - for caution
- **Danger**: `#d62728` (Red) - for negative metrics

Streamlit config location: `.streamlit/config.toml`

---

## 🔍 Filter Options Available

### By Channel
- Facebook, Google Ads, Instagram, LinkedIn, Email, Twitter

### By Region
- East, West, South, North, Central

### By Time Period
- Quarters: Q1-Q4
- Months: All 12 months
- Years: 2023, 2024

### By Customer Segment
- Premium, Regular, Budget

### By Campaign Type
- Brand Awareness, Performance, Retargeting

---

## ⚙️ System Requirements

### Minimum
- Python 3.8+
- 2GB RAM
- 500MB disk space
- Internet connection

### Recommended
- Python 3.10+
- 4GB+ RAM
- 1GB disk space
- Fast internet (for Streamlit Cloud)

---

## 📦 Dependencies

Key packages used:
```
streamlit          - Web framework
pandas             - Data manipulation
numpy              - Numerical computing
plotly             - Interactive charts
scikit-learn       - ML metrics
altair             - Alternative charting
```

All versions pinned in `requirements.txt` for consistency.

---

## 🛠️ Customization Tips

### Change Colors
```python
# In app.py, find the color_discrete_sequence
color_discrete_sequence=['#1f77b4']  # Change to your color
```

### Add New Page
```python
elif page == "📄 New Page":
    st.markdown('<div class="header-title">New Page Title</div>', unsafe_allow_html=True)
    # Add your visualizations here
```

### Add New Filter
```python
selected = st.multiselect("Select Items", 
                         data['column'].unique(),
                         default=data['column'].unique())
```

### Load More Data
```python
@st.cache_data
def load_more_data():
    return pd.read_csv('data/new_file.csv')

new_data = load_more_data()
```

---

## 🧪 Testing Checklist

Before deploying:
- [ ] All CSV files exist in `data/` folder
- [ ] `app.py` runs without errors locally
- [ ] All page filters work correctly
- [ ] Charts render properly
- [ ] No console errors in browser
- [ ] Dashboard loads in < 10 seconds
- [ ] All KPIs display correct values
- [ ] README.md is comprehensive
- [ ] requirements.txt has all packages
- [ ] .gitignore excludes `__pycache__` and `.streamlit`

---

## 📱 Browser Compatibility

Tested and working on:
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- Mobile browsers (iOS Safari, Chrome Mobile)

---

## 🔒 Security Notes

### Data Privacy
- All data is CSV-based (no database credentials needed)
- No API keys required for base functionality
- GitHub repository is public (ensure no sensitive data)

### Best Practices
- Use environment variables for sensitive data
- Never commit credentials to GitHub
- Use `.gitignore` to exclude sensitive files
- Monitor Streamlit Cloud logs for errors

---

## 📈 Performance Tips

### For Local Development
1. Use `st.cache_data` for large CSV loads
2. Filter data before visualization
3. Use `.head(n)` to limit rows in displays
4. Close unnecessary browser tabs

### For Streamlit Cloud
1. Keep CSVs under 500MB total
2. Cache data with TTL (time-to-live)
3. Use `.sample()` for large datasets
4. Pre-aggregate data when possible

---

## 🆘 Common Errors & Fixes

| Error | Fix |
|-------|-----|
| `ModuleNotFoundError: streamlit` | Run `pip install -r requirements.txt` |
| `FileNotFoundError: data/file.csv` | Check file exists in `data/` folder |
| `TypeError: expected string or bytes-like object` | Ensure CSV columns are correct data type |
| `Connection refused` | Dashboard not running, run `streamlit run app.py` |
| `Out of Memory` | Reduce dataset size or increase cache TTL |

---

## 📞 Support Resources

- **Documentation**: See `README.md` and `DEPLOYMENT.md`
- **Streamlit Docs**: https://docs.streamlit.io
- **GitHub Issues**: Create issue in your repo
- **Streamlit Community**: https://discuss.streamlit.io

---

## 📝 Version Info

- **Dashboard Version**: 1.0.0
- **Release Date**: December 2024
- **Python Version**: 3.8+
- **Streamlit Version**: 1.28.0+
- **Data Period**: 2023-2024 (2 years)

---

## 🎓 Learning Resources

### To understand the code:
1. Read `app.py` - Well-commented main application
2. Check Streamlit documentation for specific functions
3. Review Plotly documentation for chart customization
4. Explore data by printing DataFrames

### To extend the dashboard:
1. Add new pages following existing structure
2. Create new visualizations with Plotly
3. Implement advanced filtering
4. Connect to live data sources
5. Add machine learning predictions

---

## ✅ Deployment Checklist

- [ ] All files created and tested
- [ ] Data folder with 11 CSV files ready
- [ ] GitHub account created
- [ ] Repository created on GitHub
- [ ] Code pushed to GitHub
- [ ] Streamlit Cloud account ready
- [ ] Dashboard deployed
- [ ] Live URL tested and working
- [ ] README shared with stakeholders
- [ ] DEPLOYMENT.md saved for reference

---

**Ready to Deploy? Follow the DEPLOYMENT.md guide step-by-step!**

🚀 Your dashboard will be live in < 15 minutes!
