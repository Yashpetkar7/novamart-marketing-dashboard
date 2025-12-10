# 🚀 Deployment Guide - NovaMart Marketing Dashboard

Complete step-by-step guide to deploy your Streamlit dashboard to GitHub and Streamlit Cloud.

---

## 📋 Prerequisites

Before you start, make sure you have:
- [ ] Python 3.8 or higher installed
- [ ] Git installed on your computer
- [ ] A GitHub account (create one at https://github.com)
- [ ] All CSV data files in the `data/` folder
- [ ] `app.py`, `requirements.txt`, and `README.md` files ready

---

## 🔧 Step 1: Local Setup & Testing

### 1.1 Create Project Directory
```powershell
mkdir novamart-dashboard
cd novamart-dashboard
```

### 1.2 Create Virtual Environment
```powershell
python -m venv venv
venv\Scripts\activate
```

### 1.3 Install Dependencies
```powershell
pip install -r requirements.txt
```

### 1.4 Test Dashboard Locally
```powershell
streamlit run app.py
```

Expected output:
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

Visit `http://localhost:8501` in your browser and verify all pages work correctly.

**✓ If successful, proceed to Step 2**

---

## 📁 Step 2: Verify Project Structure

Ensure your directory looks like this:

```
novamart-dashboard/
├── app.py                              # ✓ Created
├── requirements.txt                    # ✓ Verify content
├── README.md                           # ✓ Comprehensive guide
├── DEPLOYMENT.md                       # ✓ This file
├── .gitignore                          # ✓ For GitHub
├── .streamlit/
│   └── config.toml                    # ✓ Streamlit config
└── data/
    ├── campaign_performance.csv        # ✓ Required
    ├── customer_data.csv               # ✓ Required
    ├── product_sales.csv               # ✓ Required
    ├── lead_scoring_results.csv        # ✓ Required
    ├── feature_importance.csv          # ✓ Required
    ├── learning_curve.csv              # ✓ Required
    ├── geographic_data.csv             # ✓ Required
    ├── channel_attribution.csv         # ✓ Required
    ├── funnel_data.csv                 # ✓ Required
    ├── customer_journey.csv            # ✓ Required
    └── correlation_matrix.csv          # ✓ Required
```

**✓ If all files present, proceed to Step 3**

---

## 🔑 Step 3: Initialize Git Repository

### 3.1 Open PowerShell in Project Directory
```powershell
# Navigate to your project
cd C:\path\to\novamart-dashboard
```

### 3.2 Initialize Git
```powershell
git init
git config user.name "Your Name"
git config user.email "your.email@gmail.com"
```

### 3.3 Add Files to Git
```powershell
git add .
git status  # Verify all files are staged
```

Expected output includes all your files listed under "Changes to be committed"

### 3.4 Create Initial Commit
```powershell
git commit -m "Initial NovaMart Marketing Dashboard commit

- Main dashboard with 7 pages
- Campaign, Customer, Geographic, ML, Product, Attribution analysis
- Interactive filters and visualizations"
```

**✓ Commit created successfully**

---

## 🌐 Step 4: Create GitHub Repository

### 4.1 Go to GitHub
Visit https://github.com/new

### 4.2 Create Repository
Fill in the following:
- **Repository name**: `novamart-dashboard`
- **Description**: NovaMart Marketing Analytics Dashboard - Streamlit Application
- **Public**: ✓ Selected (required for free Streamlit Cloud)
- **Add .gitignore**: No (we already have one)
- **Add LICENSE**: Optional (MIT or Apache 2.0 recommended)

Click **Create repository**

### 4.3 Get Repository URL
After creation, you'll see:
```
https://github.com/yourusername/novamart-dashboard.git
```

Copy this URL.

**✓ GitHub repository created**

---

## ⬆️ Step 5: Push to GitHub

### 5.1 Add Remote Origin
Replace `YOUR_USERNAME` with your actual GitHub username:

```powershell
git remote add origin https://github.com/YOUR_USERNAME/novamart-dashboard.git
git branch -M main
```

### 5.2 Push to GitHub
```powershell
git push -u origin main
```

You'll be prompted to authenticate with GitHub:
- Option 1: Use GitHub CLI (recommended)
- Option 2: Use Personal Access Token

**After successful push, verify at**: `https://github.com/YOUR_USERNAME/novamart-dashboard`

**✓ Code pushed to GitHub**

---

## 🚀 Step 6: Deploy to Streamlit Cloud

### 6.1 Visit Streamlit Cloud
Go to https://share.streamlit.io

### 6.2 Sign In with GitHub
Click "Sign in with GitHub" and authorize the application

### 6.3 Create New App
Click the "New app" button

### 6.4 Configure Deployment
Fill in the deployment form:
- **Repository**: Select your `novamart-dashboard` repository
- **Branch**: `main`
- **Main file path**: `app.py`

Click "Deploy"

### 6.5 Wait for Deployment
Streamlit will:
1. Clone your repository
2. Install dependencies from `requirements.txt`
3. Build and deploy the application
4. Provide you with a live URL

This typically takes 2-5 minutes. Watch the "Logs" tab for progress.

**Expected completion**:
```
✓ Successfully created a Streamlit app!
✓ URL: https://yourusername-novamart-dashboard-main.streamlit.app
```

**✓ Dashboard live on Streamlit Cloud**

---

## ✅ Step 7: Verify Live Dashboard

### 7.1 Test the Dashboard
Visit your live URL: `https://yourusername-novamart-dashboard-main.streamlit.app`

### 7.2 Test All Features
- [ ] Home page loads with KPIs
- [ ] Campaign Performance page filters work
- [ ] Customer Analytics displays correctly
- [ ] Geographic Analysis maps render
- [ ] Lead Scoring ML metrics show
- [ ] Product Analysis charts appear
- [ ] Attribution & Journey loads
- [ ] No errors in browser console

### 7.3 Performance Check
- [ ] Dashboard loads in < 10 seconds
- [ ] Filters respond in < 2 seconds
- [ ] Charts render smoothly
- [ ] No missing data or broken visualizations

**✓ All tests passed**

---

## 🔄 Step 8: Future Updates & Maintenance

### 8.1 Making Changes Locally

```powershell
# Activate virtual environment
venv\Scripts\activate

# Make changes to app.py or add new data
# Test locally
streamlit run app.py

# Stage changes
git add .

# Commit with meaningful message
git commit -m "Add feature: new visualization on Campaign Performance page"

# Push to GitHub
git push origin main
```

Streamlit Cloud automatically redeploys when you push to `main` branch.

### 8.2 Check Deployment Status
- Visit https://share.streamlit.io/YOUR_USERNAME/novamart-dashboard
- Check the "Logs" tab for any errors
- Restart app if needed from the "⋮ Manage app" menu

### 8.3 Performance Monitoring
- Monitor data refresh times
- Check resource usage
- Update dependencies monthly

```powershell
# Check for outdated packages
pip list --outdated

# Update specific package
pip install --upgrade streamlit
pip install --upgrade -r requirements.txt
```

---

## 🐛 Troubleshooting

### Issue: "Module not found" error on Streamlit Cloud

**Solution**: Ensure all imports in `app.py` are listed in `requirements.txt`

```powershell
# Find all imports in app.py
findstr /R "^import\|^from" app.py

# Verify each is in requirements.txt
type requirements.txt
```

### Issue: "FileNotFoundError: data/campaign_performance.csv"

**Solution**: CSV files must be in the `data/` folder in GitHub

```powershell
# Verify files are staged
git ls-files | findstr "data/"

# Push again if missing
git add data/*
git commit -m "Add data files"
git push origin main
```

### Issue: Dashboard loads slowly

**Solution**: Check data size and optimize

```powershell
# Check data file sizes
Get-ChildItem -Path data -Recurse | ForEach-Object { Write-Host $_.Name $_.Length }

# If files > 100MB, consider compression or sampling
```

### Issue: Streamlit Cloud says "App is not running"

**Solution**: Check logs and restart app

1. Go to https://share.streamlit.io/YOUR_USERNAME/novamart-dashboard
2. Click "⋮ Manage app" 
3. Click "Reboot" under Actions
4. Check "Logs" tab for errors

---

## 📊 Dashboard URL

Once deployed, share your dashboard at:
```
https://yourusername-novamart-dashboard-main.streamlit.app
```

Example:
```
https://john-novamart-dashboard-main.streamlit.app
```

---

## 📚 Additional Resources

- **Streamlit Docs**: https://docs.streamlit.io
- **Streamlit Cloud Docs**: https://docs.streamlit.io/streamlit-cloud
- **GitHub Docs**: https://docs.github.com
- **Python Pandas**: https://pandas.pydata.org/docs
- **Plotly**: https://plotly.com/python

---

## ✨ Next Steps

After successful deployment:

1. **Share the dashboard** with stakeholders via the live URL
2. **Add more pages** with additional analyses
3. **Connect real databases** instead of CSV files
4. **Implement real-time updates** with scheduled refreshes
5. **Add user authentication** for sensitive data
6. **Set up email alerts** for key metrics

---

## 📧 Support

If you encounter issues:
1. Check the Streamlit Cloud logs for error messages
2. Review this deployment guide
3. Check GitHub/Streamlit documentation
4. Create an issue on your GitHub repository

---

**Happy Deploying! 🎉**

Your NovaMart Marketing Analytics Dashboard is now live and ready to use!
