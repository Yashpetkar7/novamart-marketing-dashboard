import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

# Page Configuration
st.set_page_config(
    page_title="NovaMart Marketing Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .header-title {
        color: #1f77b4;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Load Data
@st.cache_data
def load_data():
    campaign = pd.read_csv('data/campaign_performance.csv')
    customer = pd.read_csv('data/customer_data.csv')
    product = pd.read_csv('data/product_sales.csv')
    lead_score = pd.read_csv('data/lead_scoring_results.csv')
    geographic = pd.read_csv('data/geographic_data.csv')
    channel_attr = pd.read_csv('data/channel_attribution.csv')
    funnel = pd.read_csv('data/funnel_data.csv')
    customer_journey = pd.read_csv('data/customer_journey.csv')
    feature_imp = pd.read_csv('data/feature_importance.csv')
    correlation = pd.read_csv('data/correlation_matrix.csv')
    learning_curve = pd.read_csv('data/learning_curve.csv')
    
    return {
        'campaign': campaign,
        'customer': customer,
        'product': product,
        'lead_score': lead_score,
        'geographic': geographic,
        'channel_attr': channel_attr,
        'funnel': funnel,
        'customer_journey': customer_journey,
        'feature_imp': feature_imp,
        'correlation': correlation,
        'learning_curve': learning_curve
    }

data = load_data()

# Sidebar Navigation
st.sidebar.markdown("# 📊 Navigation")
page = st.sidebar.radio(
    "Select a Dashboard",
    ["🏠 Home", "📈 Campaign Performance", "👥 Customer Analytics", 
     "🗺️ Geographic Analysis", "🎯 Lead Scoring & ML", "🛍️ Product Analysis",
     "🔗 Attribution & Journey"]
)

# ============================================================================
# HOME PAGE
# ============================================================================
if page == "🏠 Home":
    st.markdown('<div class="header-title">🎯 NovaMart Marketing Analytics Dashboard</div>', unsafe_allow_html=True)
    st.markdown("### Masters of AI in Business - Data Visualization Assignment")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Revenue", f"₹{data['campaign']['revenue'].sum()/1e6:.1f}M", 
                  f"{(data['campaign']['revenue'].sum()/data['campaign']['revenue'].shift().sum()-1)*100:.1f}%")
    with col2:
        st.metric("Total Conversions", f"{data['campaign']['conversions'].sum():,.0f}", 
                  f"{data['campaign']['ctr'].mean():.2f}% CTR")
    with col3:
        st.metric("Total Spend", f"₹{data['campaign']['spend'].sum()/1e6:.1f}M", 
                  f"ROAS: {data['campaign']['roas'].mean():.2f}x")
    with col4:
        st.metric("Active Customers", f"{data['customer'].shape[0]:,}", 
                  f"Churn: {(data['customer']['is_churned'].sum()/len(data['customer'])*100):.2f}%")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Revenue Trend (2023-2024)")
        daily_revenue = data['campaign'].groupby('date')['revenue'].sum().reset_index()
        daily_revenue['date'] = pd.to_datetime(daily_revenue['date'])
        
        fig = px.line(daily_revenue, x='date', y='revenue', 
                     labels={'date': 'Date', 'revenue': 'Revenue (₹)'},
                     color_discrete_sequence=['#1f77b4'])
        fig.update_layout(hovermode='x unified', showlegend=False, height=350)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("📱 Channel Performance")
        channel_perf = data['campaign'].groupby('channel').agg({
            'revenue': 'sum',
            'spend': 'sum',
            'conversions': 'sum'
        }).reset_index()
        channel_perf['ROAS'] = channel_perf['revenue'] / channel_perf['spend']
        
        fig = px.bar(channel_perf, x='channel', y='revenue',
                    color='ROAS', color_continuous_scale='Viridis',
                    labels={'channel': 'Channel', 'revenue': 'Revenue (₹)'},
                    hover_data=['ROAS', 'spend', 'conversions'])
        fig.update_layout(height=350, showlegend=True)
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    st.subheader("📈 Key Features")
    st.write("""
    - **Campaign Performance**: Deep dive into campaign metrics, ROI, and channel analysis
    - **Customer Analytics**: Segment analysis, churn prediction, and customer lifetime value
    - **Geographic Analysis**: State-level performance with interactive maps
    - **Lead Scoring & ML**: Predictive model performance, feature importance, and ROC curves
    - **Product Analysis**: Sales by category, regional variations, and trends
    - **Attribution & Journey**: Multi-touch attribution and customer journey mapping
    """)

# ============================================================================
# CAMPAIGN PERFORMANCE
# ============================================================================
elif page == "📈 Campaign Performance":
    st.markdown('<div class="header-title">📈 Campaign Performance Analysis</div>', unsafe_allow_html=True)
    
    campaign_df = data['campaign'].copy()
    campaign_df['date'] = pd.to_datetime(campaign_df['date'])
    
    # Filters
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        channels = st.multiselect("Select Channels", campaign_df['channel'].unique(), 
                                 default=campaign_df['channel'].unique())
    with col2:
        regions = st.multiselect("Select Regions", campaign_df['region'].unique(), 
                                default=campaign_df['region'].unique())
    with col3:
        quarters = st.multiselect("Select Quarters", campaign_df['quarter'].unique(), 
                                 default=campaign_df['quarter'].unique())
    with col4:
        campaign_types = st.multiselect("Select Campaign Types", campaign_df['campaign_type'].unique(), 
                                       default=campaign_df['campaign_type'].unique())
    
    # Apply filters
    filtered_df = campaign_df[
        (campaign_df['channel'].isin(channels)) &
        (campaign_df['region'].isin(regions)) &
        (campaign_df['quarter'].isin(quarters)) &
        (campaign_df['campaign_type'].isin(campaign_types))
    ]
    
    # KPIs
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("Total Revenue", f"₹{filtered_df['revenue'].sum()/1e6:.2f}M")
    with col2:
        st.metric("Total Conversions", f"{filtered_df['conversions'].sum():,.0f}")
    with col3:
        st.metric("Avg ROAS", f"{filtered_df['roas'].mean():.2f}x")
    with col4:
        st.metric("Avg CTR", f"{filtered_df['ctr'].mean():.2f}%")
    with col5:
        st.metric("Total Spend", f"₹{filtered_df['spend'].sum()/1e6:.2f}M")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Revenue by Channel")
        channel_rev = filtered_df.groupby('channel')['revenue'].sum().sort_values(ascending=False)
        fig = px.bar(x=channel_rev.index, y=channel_rev.values, 
                    labels={'x': 'Channel', 'y': 'Revenue (₹)'},
                    color=channel_rev.values, color_continuous_scale='Blues')
        fig.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Spend vs Revenue by Channel")
        spend_rev = filtered_df.groupby('channel')[['spend', 'revenue']].sum()
        fig = go.Figure(data=[
            go.Bar(name='Spend', x=spend_rev.index, y=spend_rev['spend']),
            go.Bar(name='Revenue', x=spend_rev.index, y=spend_rev['revenue'])
        ])
        fig.update_layout(barmode='group', height=400, hovermode='x unified')
        st.plotly_chart(fig, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Revenue Trend Over Time")
        daily_trend = filtered_df.groupby('date')['revenue'].sum().reset_index()
        fig = px.line(daily_trend, x='date', y='revenue', 
                     labels={'date': 'Date', 'revenue': 'Revenue (₹)'},
                     color_discrete_sequence=['#1f77b4'])
        fig.update_layout(height=400, hovermode='x unified', showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("ROAS Distribution by Channel")
        fig = px.box(filtered_df, x='channel', y='roas',
                    color='channel', labels={'channel': 'Channel', 'roas': 'ROAS'},
                    height=400)
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Campaign Performance Table")
    display_cols = ['date', 'campaign_name', 'channel', 'region', 'impressions', 
                   'clicks', 'conversions', 'spend', 'revenue', 'roas', 'ctr']
    st.dataframe(filtered_df[display_cols].sort_values('date', ascending=False).head(100), 
                use_container_width=True)

# ============================================================================
# CUSTOMER ANALYTICS
# ============================================================================
elif page == "👥 Customer Analytics":
    st.markdown('<div class="header-title">👥 Customer Analytics & Segmentation</div>', unsafe_allow_html=True)
    
    customer_df = data['customer'].copy()
    
    col1, col2 = st.columns(2)
    with col1:
        segments = st.multiselect("Select Customer Segments", 
                                 customer_df['customer_segment'].unique(),
                                 default=customer_df['customer_segment'].unique())
    with col2:
        regions_cust = st.multiselect("Select Regions", 
                                     customer_df['region'].unique(),
                                     default=customer_df['region'].unique())
    
    filtered_cust = customer_df[
        (customer_df['customer_segment'].isin(segments)) &
        (customer_df['region'].isin(regions_cust))
    ]
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Active Customers", len(filtered_cust))
    with col2:
        st.metric("Avg LTV", f"₹{filtered_cust['lifetime_value'].mean():,.0f}")
    with col3:
        st.metric("Churn Rate", f"{(filtered_cust['is_churned'].sum()/len(filtered_cust)*100):.2f}%")
    with col4:
        st.metric("Avg Satisfaction", f"{filtered_cust['satisfaction_score'].mean():.2f}/5.0")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Customer Distribution by Age")
        fig = px.histogram(filtered_cust, x='age', nbins=30,
                          labels={'age': 'Age', 'count': 'Number of Customers'},
                          color_discrete_sequence=['#1f77b4'])
        fig.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("LTV by Customer Segment")
        seg_ltv = filtered_cust.groupby('customer_segment')['lifetime_value'].mean().sort_values(ascending=False)
        fig = px.bar(x=seg_ltv.index, y=seg_ltv.values,
                    labels={'x': 'Segment', 'y': 'Avg LTV (₹)'},
                    color=seg_ltv.values, color_continuous_scale='Greens')
        fig.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Income vs LTV Scatter Plot")
        fig = px.scatter(filtered_cust.sample(min(1000, len(filtered_cust))), 
                        x='income', y='lifetime_value', color='customer_segment',
                        labels={'income': 'Income (₹)', 'lifetime_value': 'LTV (₹)'},
                        height=400, opacity=0.6)
        fig.update_layout(hovermode='closest')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Satisfaction Score Distribution")
        fig = px.box(filtered_cust, x='customer_segment', y='satisfaction_score',
                    color='customer_segment', height=400,
                    labels={'customer_segment': 'Segment', 'satisfaction_score': 'Satisfaction'})
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Churn Distribution by NPS Category")
        churn_nps = filtered_cust.groupby('nps_category')['is_churned'].sum()
        fig = px.bar(x=churn_nps.index, y=churn_nps.values,
                    labels={'x': 'NPS Category', 'y': 'Churned Customers'},
                    color=churn_nps.values, color_continuous_scale='Reds')
        fig.update_layout(height=350, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Customer Segment Distribution")
        seg_dist = filtered_cust['customer_segment'].value_counts()
        fig = px.pie(values=seg_dist.values, names=seg_dist.index,
                    hole=0.3, height=350)
        st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Customer Data Sample")
    display_cols_cust = ['customer_id', 'age', 'income', 'customer_segment', 'region', 
                        'lifetime_value', 'satisfaction_score', 'is_churned']
    st.dataframe(filtered_cust[display_cols_cust].head(50), use_container_width=True)

# ============================================================================
# GEOGRAPHIC ANALYSIS
# ============================================================================
elif page == "🗺️ Geographic Analysis":
    st.markdown('<div class="header-title">🗺️ Geographic Performance Analysis</div>', unsafe_allow_html=True)
    
    geo_df = data['geographic'].copy()
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total States", len(geo_df))
    with col2:
        st.metric("Total Revenue", f"₹{geo_df['total_revenue'].sum()/1e9:.2f}B")
    with col3:
        st.metric("Avg Satisfaction", f"{geo_df['customer_satisfaction'].mean():.2f}/5.0")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Revenue by State")
        top_states = geo_df.nlargest(10, 'total_revenue')
        fig = px.bar(top_states.sort_values('total_revenue'), 
                    x='total_revenue', y='state',
                    labels={'state': 'State', 'total_revenue': 'Revenue (₹)'},
                    color='total_revenue', color_continuous_scale='Blues',
                    orientation='h')
        fig.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Revenue vs Penetration")
        fig = px.scatter(geo_df, x='market_penetration', y='total_revenue',
                        size='store_count', hover_name='state',
                        color='customer_satisfaction', color_continuous_scale='Viridis',
                        labels={'market_penetration': 'Market Penetration (%)', 
                               'total_revenue': 'Revenue (₹)'},
                        height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("YoY Growth Rate")
        fig = px.bar(geo_df.sort_values('yoy_growth', ascending=False),
                    x='state', y='yoy_growth',
                    labels={'state': 'State', 'yoy_growth': 'YoY Growth (%)'},
                    color='yoy_growth', color_continuous_scale='RdYlGn',
                    height=400)
        fig.update_xaxes(tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Store Distribution by Region")
        region_stores = geo_df.groupby('region')['store_count'].sum()
        fig = px.pie(values=region_stores.values, names=region_stores.index,
                    hole=0.3, height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Geographic Data Table")
    st.dataframe(geo_df.sort_values('total_revenue', ascending=False), use_container_width=True)

# ============================================================================
# LEAD SCORING & ML
# ============================================================================
elif page == "🎯 Lead Scoring & ML":
    st.markdown('<div class="header-title">🎯 Lead Scoring & ML Model Performance</div>', unsafe_allow_html=True)
    
    lead_df = data['lead_score'].copy()
    
    col1, col2, col3, col4 = st.columns(4)
    
    # Calculate metrics
    conversion_rate = (lead_df['actual_converted'].sum() / len(lead_df)) * 100
    from sklearn.metrics import confusion_matrix, roc_auc_score, precision_score, recall_score
    
    cm = confusion_matrix(lead_df['actual_converted'], lead_df['predicted_class'])
    precision = precision_score(lead_df['actual_converted'], lead_df['predicted_class'])
    recall = recall_score(lead_df['actual_converted'], lead_df['predicted_class'])
    auc = roc_auc_score(lead_df['actual_converted'], lead_df['predicted_probability'])
    
    with col1:
        st.metric("Total Leads", len(lead_df))
    with col2:
        st.metric("Conversion Rate", f"{conversion_rate:.2f}%")
    with col3:
        st.metric("Precision", f"{precision:.3f}")
    with col4:
        st.metric("AUC Score", f"{auc:.3f}")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Confusion Matrix")
        fig = go.Figure(data=go.Heatmap(
            z=cm,
            x=['Not Converted', 'Converted'],
            y=['Predicted Not Converted', 'Predicted Converted'],
            colorscale='Blues',
            text=cm,
            texttemplate='%{text}',
            textfont={"size": 16}
        ))
        fig.update_layout(height=350)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Model Performance Metrics")
        metrics_dict = {
            'Precision': precision,
            'Recall': recall,
            'AUC': auc,
            'Accuracy': (cm[0,0] + cm[1,1]) / cm.sum()
        }
        fig = px.bar(x=list(metrics_dict.keys()), y=list(metrics_dict.values()),
                    labels={'x': 'Metric', 'y': 'Score'},
                    color=list(metrics_dict.values()),
                    color_continuous_scale='Viridis',
                    height=350)
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Conversion by Lead Source")
        source_conv = lead_df.groupby('lead_source')['actual_converted'].agg(['sum', 'count'])
        source_conv['rate'] = (source_conv['sum'] / source_conv['count'] * 100)
        fig = px.bar(source_conv, y='rate',
                    labels={'index': 'Lead Source', 'rate': 'Conversion Rate (%)'},
                    color='rate', color_continuous_scale='Greens',
                    height=350)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Predicted Probability Distribution")
        fig = px.histogram(lead_df, x='predicted_probability', nbins=30,
                          color='actual_converted',
                          labels={'predicted_probability': 'Predicted Probability', 'count': 'Count'},
                          height=350)
        st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Feature Importance")
    feature_df = data['feature_imp'].copy()
    if 'importance' in feature_df.columns:
        fig = px.bar(feature_df.nlargest(10, 'importance' if 'importance' in feature_df.columns else feature_df.columns[1]),
                    x=feature_df.columns[1], y='feature',
                    labels={'feature': 'Feature', feature_df.columns[1]: 'Importance'},
                    height=350, orientation='h')
        st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Lead Scoring Results Sample")
    st.dataframe(lead_df.head(50), use_container_width=True)

# ============================================================================
# PRODUCT ANALYSIS
# ============================================================================
elif page == "🛍️ Product Analysis":
    st.markdown('<div class="header-title">🛍️ Product Sales Analysis</div>', unsafe_allow_html=True)
    
    product_df = data['product'].copy()
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Sales", f"₹{product_df['sales'].sum()/1e6:.2f}M")
    with col2:
        st.metric("Avg Price", f"₹{product_df['price'].mean():,.0f}")
    with col3:
        st.metric("Total Products", product_df['product_name'].nunique())
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Sales by Category")
        cat_sales = product_df.groupby('category')['sales'].sum().sort_values(ascending=False)
        fig = px.bar(x=cat_sales.index, y=cat_sales.values,
                    labels={'x': 'Category', 'y': 'Sales (₹)'},
                    color=cat_sales.values, color_continuous_scale='Blues',
                    height=400)
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Top 10 Products")
        top_products = product_df.nlargest(10, 'sales')
        fig = px.bar(top_products.sort_values('sales'),
                    x='sales', y='product_name',
                    labels={'sales': 'Sales (₹)', 'product_name': 'Product'},
                    color='sales', color_continuous_scale='Greens',
                    orientation='h', height=400)
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Price vs Quantity Sold")
        fig = px.scatter(product_df, x='price', y='quantity_sold',
                        size='sales', hover_name='product_name',
                        color='category',
                        labels={'price': 'Price (₹)', 'quantity_sold': 'Quantity Sold'},
                        height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Sales Distribution by Subcategory")
        top_subcat = product_df.groupby('subcategory')['sales'].sum().nlargest(10)
        fig = px.pie(values=top_subcat.values, names=top_subcat.index,
                    height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Product Data Sample")
    display_cols_prod = ['product_name', 'category', 'subcategory', 'price', 'quantity_sold', 'sales']
    st.dataframe(product_df[display_cols_prod].nlargest(50, 'sales'), use_container_width=True)

# ============================================================================
# ATTRIBUTION & JOURNEY
# ============================================================================
elif page == "🔗 Attribution & Journey":
    st.markdown('<div class="header-title">🔗 Attribution & Customer Journey</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Multi-Touch Attribution")
        channel_attr = data['channel_attribution'].copy()
        # Reshape for visualization
        attr_cols = [col for col in channel_attr.columns if col not in ['channel', 'touchpoints']]
        
        if len(channel_attr) > 0:
            fig = px.bar(channel_attr, x='channel', y=attr_cols[0:3] if len(attr_cols) >= 3 else attr_cols,
                        labels={'channel': 'Channel'},
                        height=400, barmode='group')
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Marketing Funnel")
        funnel_df = data['funnel'].copy()
        
        if 'stage' in funnel_df.columns and 'visitors' in funnel_df.columns:
            fig = px.funnel(funnel_df, x='visitors', y='stage',
                          labels={'visitors': 'Number of Visitors', 'stage': 'Funnel Stage'},
                          height=400, color_discrete_sequence=['#1f77b4'])
            st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    st.subheader("Customer Journey Paths")
    journey_df = data['customer_journey'].copy()
    
    if 'touchpoint_sequence' in journey_df.columns:
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Sample Customer Journeys:**")
            st.dataframe(journey_df.head(10), use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666; font-size: 0.85rem;'>
    📊 NovaMart Marketing Analytics Dashboard | Data Visualization Assignment
    </div>
""", unsafe_allow_html=True)
