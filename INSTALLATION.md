# 🛠️ Installation Guide - Local Setup

Complete guide to set up and run the NovaMart Dashboard on your local machine.

---

## 📋 System Requirements

### Minimum Requirements
- **OS**: Windows 7+, macOS 10.12+, or Linux (Ubuntu 16.04+)
- **Python**: 3.8 or higher
- **RAM**: 2GB
- **Disk Space**: 500MB (including dependencies)
- **Internet**: Required for initial setup and Streamlit features

### Recommended Specifications
- **OS**: Windows 10/11, macOS 12+, or Linux (Ubuntu 20.04+)
- **Python**: 3.10 or 3.11
- **RAM**: 4GB or more
- **Disk Space**: 1GB
- **Internet**: High-speed connection preferred

---

## 🔍 Check Your System

### Step 1: Verify Python Installation

Open PowerShell (Windows) or Terminal (Mac/Linux) and run:

```powershell
python --version
```

Expected output:
```
Python 3.10.5
```

If you see "Python is not recognized", you need to install Python.

### Step 2: Verify Python Path

```powershell
python -c "import sys; print(sys.executable)"
```

Should show the path to your Python installation.

### Step 3: Verify pip

```powershell
pip --version
```

Expected output:
```
pip 23.0.1 from C:\Users\YourName\AppData\Local\Programs\Python\Python310\lib\site-packages\python.exe
```

---

## 💻 Install Python (If Needed)

### Windows Installation

1. **Download Python**
   - Visit https://www.python.org/downloads/
   - Click "Download Python 3.11" (or latest 3.10+)
   - Download the Windows executable installer

2. **Run Installer**
   - Double-click the downloaded `.exe` file
   - **IMPORTANT**: Check "Add Python 3.x to PATH" ✅
   - Check "Install pip" ✅
   - Click "Install Now"

3. **Verify Installation**
   ```powershell
   python --version
   pip --version
   ```

### macOS Installation

Using Homebrew (recommended):

```bash
brew install python@3.11
```

Or download from https://www.python.org/downloads/macos/

### Linux Installation

Ubuntu/Debian:
```bash
sudo apt-get update
sudo apt-get install python3.11 python3-pip
```

---

## 📂 Create Project Directory

### Windows (PowerShell)

```powershell
# Create directory
New-Item -ItemType Directory -Path "C:\Users\YourName\Desktop\novamart-dashboard"
cd C:\Users\YourName\Desktop\novamart-dashboard
```

### Mac/Linux (Terminal)

```bash
mkdir ~/Desktop/novamart-dashboard
cd ~/Desktop/novamart-dashboard
```

---

## 🔗 Set Up Git (Optional but Recommended)

### Download Git

Visit https://git-scm.com/download and follow installation instructions for your OS.

### Initialize Git Repository

```powershell
git init
git config user.name "Your Name"
git config user.email "your.email@gmail.com"
```

---

## 🐍 Create Virtual Environment

### Why Virtual Environment?

A virtual environment is an isolated Python environment for this project. It prevents package conflicts and keeps your system Python clean.

### Windows (PowerShell)

```powershell
# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate

# You should see (venv) at the start of your terminal
```

### Mac/Linux (Terminal)

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# You should see (venv) at the start of your terminal
```

### Verify Activation

```powershell
# Windows/Mac/Linux
which python
# Should show path to venv's Python
```

If virtual environment is NOT activated:
```powershell
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

---

## 📦 Install Dependencies

### Step 1: Prepare Requirements File

Create a file named `requirements.txt` in your project directory with:

```
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0
plotly>=5.17.0
scikit-learn>=1.3.0
altair>=5.0.0
```

### Step 2: Install Packages

```powershell
# Make sure (venv) is in your terminal prompt
pip install -r requirements.txt
```

This will download and install all packages (~200MB).

### Step 3: Verify Installation

```powershell
pip list
```

You should see all packages listed:
- streamlit
- pandas
- numpy
- plotly
- scikit-learn
- altair

---

## 📥 Add Project Files

### File Structure to Create

```
novamart-dashboard/
├── app.py                    # Main application
├── requirements.txt          # Dependencies (already created)
├── README.md                 # Documentation
├── DEPLOYMENT.md             # Deployment guide
├── QUICK_REFERENCE.md        # Quick reference
├── .gitignore                # Git exclusions
├── .streamlit/
│   └── config.toml          # Streamlit config
└── data/
    ├── campaign_performance.csv
    ├── customer_data.csv
    ├── product_sales.csv
    ├── lead_scoring_results.csv
    ├── geographic_data.csv
    ├── channel_attribution.csv
    ├── funnel_data.csv
    ├── customer_journey.csv
    ├── feature_importance.csv
    ├── learning_curve.csv
    └── correlation_matrix.csv
```

### Step 1: Create app.py

Copy the complete `app.py` content (provided in this package) to your project directory.

### Step 2: Create data Folder

```powershell
# Windows
New-Item -ItemType Directory -Path "data"

# Mac/Linux
mkdir data
```

### Step 3: Add CSV Files

Copy all 11 CSV files to the `data/` folder:
- campaign_performance.csv
- customer_data.csv
- product_sales.csv
- lead_scoring_results.csv
- geographic_data.csv
- channel_attribution.csv
- funnel_data.csv
- customer_journey.csv
- feature_importance.csv
- learning_curve.csv
- correlation_matrix.csv

### Step 4: Create .streamlit Directory

```powershell
# Windows
New-Item -ItemType Directory -Path ".streamlit"

# Mac/Linux
mkdir .streamlit
```

Create `.streamlit/config.toml` with:

```toml
[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#333333"
font = "sans serif"

[client]
showErrorDetails = true

[logger]
level = "info"

[server]
maxUploadSize = 200
enableXsrfProtection = true
```

---

## ✅ Pre-Launch Checklist

Before running the dashboard, verify:

- [ ] Virtual environment is activated (see `(venv)` in terminal)
- [ ] Python 3.8+ installed (`python --version`)
- [ ] All packages installed (`pip list`)
- [ ] `app.py` exists in project root
- [ ] `data/` folder has all 11 CSV files
- [ ] `requirements.txt` in project root
- [ ] `.streamlit/config.toml` exists

---

## 🚀 Launch the Dashboard

### Step 1: Activate Virtual Environment

```powershell
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

You should see `(venv)` at the start of your terminal line.

### Step 2: Run Streamlit

```powershell
streamlit run app.py
```

### Step 3: Expected Output

```
  Welcome to Streamlit. Check out our demo in your browser.

  URL: http://localhost:8501
  
  Ready to create beautiful apps? Let's get started!
```

### Step 4: Access Dashboard

Automatic browser opening:
- Your default browser should automatically open at `http://localhost:8501`

Manual access:
- Open your browser
- Go to `http://localhost:8501`

---

## 🎯 First Time Setup

### Home Page
You should see:
- Title: "NovaMart Marketing Analytics Dashboard"
- 4 KPI cards (Revenue, Conversions, Spend, Customers)
- 2 charts (Revenue Trend, Channel Performance)

### Sidebar Navigation
You should see:
- 7 pages listed (Home, Campaign Performance, Customer Analytics, etc.)
- Each page clickable

### Test Interactive Features
1. **Click navigation items** - pages should load
2. **Use filters** - dropdowns should work
3. **Hover over charts** - tooltip should appear
4. **Check data table** - should display properly

---

## 🔄 Running the Dashboard

### Every Time You Want to Use It

```powershell
# Navigate to project directory
cd C:\path\to\novamart-dashboard

# Activate virtual environment
venv\Scripts\activate

# Run the app
streamlit run app.py

# Open http://localhost:8501 in your browser
```

### Stopping the Dashboard

Press `Ctrl + C` in the terminal to stop the application.

---

## 🐛 Troubleshooting

### Error: "Python is not recognized"

**Cause**: Python not in system PATH
**Solution**:
1. Reinstall Python
2. Check "Add Python to PATH" during installation
3. Restart terminal and verify with `python --version`

### Error: "No module named 'streamlit'"

**Cause**: Streamlit not installed in virtual environment
**Solution**:
```powershell
# Verify venv is activated (should see (venv))
pip install streamlit>=1.28.0
pip install -r requirements.txt
```

### Error: "FileNotFoundError: data/campaign_performance.csv"

**Cause**: CSV files not in `data/` folder
**Solution**:
```powershell
# Verify folder structure
dir data\

# Should see all 11 CSV files
# If missing, copy them to data/ folder
```

### Error: "Port 8501 is already in use"

**Cause**: Another Streamlit app is running on same port
**Solution**:
```powershell
# Run on different port
streamlit run app.py --server.port 8502

# Or stop the other app (Ctrl + C)
```

### Error: "Pandas import failed"

**Cause**: Incompatible pandas version
**Solution**:
```powershell
pip install --upgrade pandas>=2.0.0
```

### Dashboard loads slowly

**Cause**: Large CSV files or slow computer
**Solution**:
1. Ensure 4GB+ RAM is available
2. Close unnecessary applications
3. Wait 15-20 seconds for first load (caching)
4. Subsequent loads will be faster

### Visualizations not showing

**Cause**: Plotly or data issue
**Solution**:
```powershell
pip install --upgrade plotly>=5.17.0
# Refresh browser (F5)
```

---

## 🔧 Virtual Environment Management

### Deactivate Virtual Environment

```powershell
# When done with the project
deactivate

# (venv) should disappear from terminal
```

### Reactivate Virtual Environment

```powershell
# Next time you want to work on project
venv\Scripts\activate

# (venv) should reappear
```

### Remove Virtual Environment

```powershell
# To free up disk space (you can recreate it)
rmdir /s venv

# Then recreate with: python -m venv venv
```

---

## 📊 Testing the Dashboard

### Test Campaign Performance Page

1. Click "Campaign Performance" in sidebar
2. You should see:
   - 4 filters at top (Channels, Regions, Quarters, Campaign Types)
   - 5 KPI cards
   - 4 charts
   - Data table at bottom

3. Try filtering:
   - Select "Facebook" channel only
   - Revenue should update
   - Charts should refresh

### Test Customer Analytics Page

1. Click "Customer Analytics"
2. You should see:
   - 2 filters (Segments, Regions)
   - 4 KPI cards
   - 6 charts
   - Data table

3. Try filtering:
   - Select "Premium" segment
   - All metrics should update
   - Charts should animate

### Test Other Pages

Each page should load without errors:
- Geographic Analysis (maps and charts)
- Lead Scoring & ML (confusion matrix)
- Product Analysis (bar and scatter plots)
- Attribution & Journey (funnel chart)

---

## 💾 Saving Your Work

### If Using Git

```powershell
git add .
git commit -m "Initial local setup of NovaMart dashboard"
```

### Backup Important Files

```powershell
# Create backup folder
mkdir backup

# Copy key files
copy app.py backup\
copy requirements.txt backup\
copy -r data backup\
```

---

## 🎓 Next Steps

After successful local setup:

1. **Explore the Dashboard**
   - Navigate all 7 pages
   - Test all filters
   - Understand each visualization

2. **Study the Code**
   - Read `app.py` comments
   - Understand Streamlit structure
   - Learn Plotly visualization syntax

3. **Customize for Your Needs**
   - Modify colors and fonts
   - Add new visualizations
   - Create additional pages

4. **Deploy to Cloud**
   - Follow `DEPLOYMENT.md` guide
   - Push to GitHub
   - Deploy to Streamlit Cloud

5. **Share with Others**
   - Give them the live URL
   - Share the GitHub repository
   - Collect feedback

---

## ⚡ Performance Tips

### For Faster Loading

1. **Keep CSV files optimized**
   - Remove unnecessary columns
   - Use appropriate data types
   - Keep under 100MB total

2. **Optimize Streamlit app**
   ```python
   @st.cache_data  # Cache large data loads
   def load_data():
       return pd.read_csv('data/file.csv')
   ```

3. **Use sampling for visualization**
   ```python
   sample_data = full_data.sample(min(1000, len(full_data)))
   ```

### Memory Management

```powershell
# Monitor memory while running
# Task Manager (Windows): Performance tab
# Activity Monitor (Mac): Memory tab
```

---

## 📱 Accessing from Other Devices

After launching with `streamlit run app.py`, you can access from other devices:

### From Same Network

```
http://[YOUR_COMPUTER_IP]:8501
```

To find your IP:
```powershell
# Windows
ipconfig
# Look for IPv4 Address (e.g., 192.168.1.100)
```

### From Internet

Not possible with local Streamlit (use Streamlit Cloud deployment instead).

---

## 🎉 Congratulations!

You now have the NovaMart Marketing Analytics Dashboard running locally!

**Next Steps**:
1. Explore all dashboard pages
2. Test all filters and visualizations
3. Read the code and learn Streamlit
4. Deploy to Streamlit Cloud (see DEPLOYMENT.md)
5. Share with your team

---

## 📞 Getting Help

If you encounter issues:

1. **Check this guide** - Most common issues covered
2. **Review error message** - Usually helpful
3. **Check Streamlit docs** - https://docs.streamlit.io
4. **Search Stack Overflow** - Most Python errors have solutions
5. **Create GitHub issue** - For project-specific problems

---

**Happy dashboarding! 🚀**
