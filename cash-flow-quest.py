import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Set page configuration
st.set_page_config(
    page_title="Cash Flow For Kids",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS to make it kid-friendly
st.markdown("""
<style>
    .main {
        background-color: #f0f8ff;
    }
    .stApp {
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    .stButton button {
        border-radius: 20px;
        font-size: 18px;
    }
    h1 {
        color: #4169E1;
    }
    h2 {
        color: #1E90FF;
    }
    h3 {
        color: #4682B4;
    }
    .highlight {
        background-color: #FFFACD;
        padding: 10px;
        border-radius: 10px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Main title
st.title("🌈 Cash Flow Adventure!")
st.markdown("### Learn how money moves in and out - It's like a money river! 🚣‍♀️")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose a section:", 
    ["Cash Flow Basics", "Cash Flow Explorer", "Cash Flow Forecaster"])

# Sample data generation
def generate_sample_data(months=12):
    today = datetime.now()
    dates = [(today - timedelta(days=30*i)).strftime("%b %Y") for i in range(months-1, -1, -1)]
    
    np.random.seed(42)  # For reproducible results
    
    data = {
        'Month': dates,
        'Operating_In': np.random.randint(800, 1200, months),
        'Operating_Out': np.random.randint(700, 1100, months),
        'Investing_In': np.random.randint(100, 300, months),
        'Investing_Out': np.random.randint(200, 500, months),
        'Financing_In': np.random.randint(100, 400, months),
        'Financing_Out': np.random.randint(200, 400, months)
    }
    
    df = pd.DataFrame(data)
    
    # Calculate totals
    df['Total_In'] = df['Operating_In'] + df['Investing_In'] + df['Financing_In']
    df['Total_Out'] = df['Operating_Out'] + df['Investing_Out'] + df['Financing_Out']
    df['Net_Cash_Flow'] = df['Total_In'] - df['Total_Out']
    
    # Calculate running balance
    starting_balance = 1000
    df['Balance'] = starting_balance
    for i in range(len(df)):
        if i > 0:
            df.loc[i, 'Balance'] = df.loc[i-1, 'Balance'] + df.loc[i, 'Net_Cash_Flow']
    
    return df

# Generate sample data once
if 'data' not in st.session_state:
    st.session_state.data = generate_sample_data()

df = st.session_state.data

# Dictionary of explanations for terms
explanations = {
    "Cash Inflows": "Money coming IN to your piggy bank! 💰",
    "Cash Outflows": "Money going OUT from your piggy bank! 💸",
    "Liquidity": "How quickly you can use your money - like having coins ready to buy ice cream! 🍦",
    "Operating Activities": "Everyday money movement - like getting allowance or buying snacks! 🍭",
    "Investing Activities": "Using money to get more money later - like buying seeds to grow plants to sell! 🌱",
    "Financing Activities": "Borrowing money or giving money back that you borrowed! 🏦"
}

#-------------------------
# CASH FLOW BASICS PAGE
#-------------------------
if page == "Cash Flow Basics":
    st.header("Cash Flow Basics")
    st.markdown("### Let's learn about how money moves around! 💫")
    
    # Explanation section with fun visuals
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("What is Cash Flow?")
        st.markdown("""
        <div class="highlight">
        Cash Flow is how money moves IN and OUT of your piggy bank over time.
        It's like watching water flow through a river! 🏞️
        </div>
        """, unsafe_allow_html=True)
        
        st.image("https://via.placeholder.com/400x200?text=Cash+Flow+River", caption="Money flowing like a river!")
    
    with col2:
        st.subheader("Why is Cash Flow Important?")
        st.markdown("""
        <div class="highlight">
        Understanding cash flow helps you:
        <ul>
            <li>Know if you have enough money for ice cream 🍦</li>
            <li>Save for a new toy or game 🎮</li>
            <li>Make smart choices about spending 🧠</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Interactive explanation cards
    st.subheader("Important Cash Flow Words")
    st.markdown("Click on each card to learn what it means:")
    
    # Create three columns for the terms
    col1, col2, col3 = st.columns(3)
    
    # First row of terms
    with col1:
        if st.button("Cash Inflows 💰"):
            st.info(explanations["Cash Inflows"])
    
    with col2:
        if st.button("Cash Outflows 💸"):
            st.info(explanations["Cash Outflows"])
    
    with col3:
        if st.button("Liquidity 🌊"):
            st.info(explanations["Liquidity"])
    
    # Second row of terms
    col4, col5, col6 = st.columns(3)
    
    with col4:
        if st.button("Operating Activities 🍭"):
            st.info(explanations["Operating Activities"])
    
    with col5:
        if st.button("Investing Activities 🌱"):
            st.info(explanations["Investing Activities"])
    
    with col6:
        if st.button("Financing Activities 🏦"):
            st.info(explanations["Financing Activities"])
    
    # Simple quiz
    st.subheader("Test Your Knowledge!")
    
    with st.form("quiz_form"):
        st.markdown("### Quick Quiz!")
        q1 = st.radio("Money coming into your piggy bank is called:", 
                      ["Cash Outflows", "Cash Inflows", "Liquidity"])
        q2 = st.radio("Buying snacks or getting allowance are examples of:", 
                     ["Operating Activities", "Investing Activities", "Financing Activities"])
        
        submitted = st.form_submit_button("Check My Answers!")
        if submitted:
            score = 0
            if q1 == "Cash Inflows":
                st.success("Correct! 🎉")
                score += 1
            else:
                st.error("Not quite right. Money coming IN is called Cash Inflows!")
                
            if q2 == "Operating Activities":
                st.success("Correct! 🎉")
                score += 1
            else:
                st.error("Not quite right. Everyday money like allowance and snacks are Operating Activities!")
            
            st.balloons()
            st.markdown(f"### You scored {score}/2! {'Great job! 🌟' if score == 2 else 'Keep learning! 📚'}")

#-------------------------
# CASH FLOW EXPLORER PAGE
#-------------------------
elif page == "Cash Flow Explorer":
    st.header("Cash Flow Explorer")
    st.markdown("### Let's explore how money moves over time! 📊")
    
    # Time period slider
    st.subheader("Select Time Period")
    months_to_show = st.slider("How many months do you want to see?", 
                             min_value=3, max_value=12, value=6)
    
    filtered_df = df.iloc[-months_to_show:].copy()
    
    # Category selector
    st.subheader("Select Cash Flow Categories")
    category = st.radio("What type of cash flow do you want to explore?",
                       ["All Categories", "Operating", "Investing", "Financing"])
    
    # Plot data based on selection
    if category == "All Categories":
        plot_df = filtered_df[['Month', 'Total_In', 'Total_Out']]
        title = "Total Cash In vs. Cash Out"
        y_column_in = 'Total_In'
        y_column_out = 'Total_Out'
    elif category == "Operating":
        plot_df = filtered_df[['Month', 'Operating_In', 'Operating_Out']]
        title = "Operating Cash In vs. Cash Out"
        y_column_in = 'Operating_In'
        y_column_out = 'Operating_Out'
    elif category == "Investing":
        plot_df = filtered_df[['Month', 'Investing_In', 'Investing_Out']]
        title = "Investing Cash In vs. Cash Out"
        y_column_in = 'Investing_In'
        y_column_out = 'Investing_Out'
    else:
        plot_df = filtered_df[['Month', 'Financing_In', 'Financing_Out']]
        title = "Financing Cash In vs. Cash Out"
        y_column_in = 'Financing_In'
        y_column_out = 'Financing_Out'
    
    # Create bar chart
    st.subheader(f"{title} 📊")
    
    fig = go.Figure()
    
    # Add bars for cash in (green)
    fig.add_trace(go.Bar(
        x=plot_df['Month'],
        y=plot_df[y_column_in],
        name='Cash In 💰',
        marker_color='green',
        text=plot_df[y_column_in],
        textposition='auto'
    ))
    
    # Add bars for cash out (red)
    fig.add_trace(go.Bar(
        x=plot_df['Month'],
        y=plot_df[y_column_out],
        name='Cash Out 💸',
        marker_color='red',
        text=plot_df[y_column_out],
        textposition='auto'
    ))
    
    # Update layout for kid-friendly appearance
    fig.update_layout(
        barmode='group',
        title=f"{title} - Cash In vs Cash Out",
        xaxis_title="Month",
        yaxis_title="Amount ($)",
        legend_title="Cash Flow Type",
        font=dict(
            family="Comic Sans MS, cursive, sans-serif",
            size=14,
        ),
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Line chart for balance
    st.subheader("Your Money Balance Over Time 📈")
    
    fig2 = px.line(
        filtered_df, 
        x='Month', 
        y='Balance',
        markers=True,
        line_shape='linear'
    )
    
    fig2.update_traces(
        line=dict(width=4, color='blue'),
        marker=dict(size=10, symbol='circle', line=dict(width=2, color='DarkSlateGrey')),
    )
    
    fig2.update_layout(
        title="Cash Balance Over Time",
        xaxis_title="Month",
        yaxis_title="Balance ($)",
        font=dict(
            family="Comic Sans MS, cursive, sans-serif",
            size=14,
        ),
        height=400
    )
    
    # Add a horizontal reference line for zero balance
    fig2.add_shape(
        type="line",
        x0=filtered_df['Month'].iloc[0],
        y0=0,
        x1=filtered_df['Month'].iloc[-1],
        y1=0,
        line=dict(color="red", width=2, dash="dash")
    )
    
    st.plotly_chart(fig2, use_container_width=True)
    
    # Automatic insights
    st.subheader("Automatic Money Detective 🔍")
    
    # Calculate insights
    positive_months = (filtered_df['Net_Cash_Flow'] > 0).sum()
    negative_months = (filtered_df['Net_Cash_Flow'] < 0).sum()
    best_month = filtered_df.loc[filtered_df['Net_Cash_Flow'].idxmax(), 'Month']
    worst_month = filtered_df.loc[filtered_df['Net_Cash_Flow'].idxmin(), 'Month']
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(
            label="Months with More Money Coming In",
            value=positive_months,
            delta=positive_months - negative_months
        )
        st.markdown(f"**Best Month**: {best_month} 🌟")
    
    with col2:
        st.metric(
            label="Months with More Money Going Out",
            value=negative_months,
            delta=negative_months - positive_months,
            delta_color="inverse"
        )
        st.markdown(f"**Most Spending**: {worst_month} 💸")
    
    # Simple analysis insights
    st.subheader("Money Detective Insights 💡")
    
    if positive_months > negative_months:
        st.success(f"Great job! In {positive_months} out of {months_to_show} months, more money came IN than went OUT! 🎉")
    elif positive_months < negative_months:
        st.warning(f"Watch out! In {negative_months} out of {months_to_show} months, more money went OUT than came IN! 💸")
    else:
        st.info("Your money in and money out are balanced! That's good budgeting! ⚖️")
    
    # Show detailed table if requested
    if st.checkbox("Show me the detailed numbers!"):
        st.dataframe(filtered_df[['Month', 'Total_In', 'Total_Out', 'Net_Cash_Flow', 'Balance']], height=300)

#-------------------------
# CASH FLOW FORECASTER PAGE
#-------------------------
elif page == "Cash Flow Forecaster":
    st.header("Cash Flow Forecaster")
    st.markdown("### Let's predict your future money! 🔮")
    
    # Get the last month's data as a starting point
    last_month = df.iloc[-1]
    starting_balance = int(last_month['Balance'])
    
    st.subheader("Your Starting Money")
    st.markdown(f"You're starting with **${starting_balance}** in your piggy bank! 🐷")
    
    # Create scenarios
    st.subheader("Create Your Money Plan")
    st.markdown("Let's plan what money might come IN and go OUT next month!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Money Coming IN 💰")
        allowance = st.slider("Allowance", 0, 100, 20, 5)
        birthday = st.slider("Birthday Gift Money", 0, 200, 0, 10)
        chores = st.slider("Extra Chores Money", 0, 50, 10, 5)
        other_in = st.slider("Other Money In", 0, 200, 0, 10)
        
        total_in = allowance + birthday + chores + other_in
        st.success(f"Total Money IN: ${total_in}")
    
    with col2:
        st.markdown("### Money Going OUT 💸")
        toys = st.slider("Toys or Games", 0, 100, 15, 5)
        snacks = st.slider("Snacks or Treats", 0, 50, 10, 1)
        savings = st.slider("Money to Save", 0, 100, 5, 1)
        other_out = st.slider("Other Spending", 0, 100, 0, 5)
        
        total_out = toys + snacks + savings + other_out
        st.error(f"Total Money OUT: ${total_out}")
    
    # Calculate and display new balance
    new_balance = starting_balance + total_in - total_out
    st.subheader("Your Future Money Prediction")
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.metric(
            label="Starting Balance",
            value=f"${starting_balance}"
        )
        st.metric(
            label="Money IN",
            value=f"${total_in}",
            delta=f"{total_in}"
        )
        st.metric(
            label="Money OUT",
            value=f"${total_out}",
            delta=f"-{total_out}",
            delta_color="inverse"
        )
    
    with col4:
        if new_balance > starting_balance:
            st.success(f"## New Balance: ${new_balance}")
            st.markdown("### Your money is growing! 🌱")
        elif new_balance < starting_balance:
            st.warning(f"## New Balance: ${new_balance}")
            st.markdown("### You're spending more than you're getting! 💸")
        else:
            st.info(f"## New Balance: ${new_balance}")
            st.markdown("### Your money is staying the same! ⚖️")
    
    # Visualize with a simple gauge chart
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = new_balance,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Piggy Bank Balance"},
        delta = {'reference': starting_balance},
        gauge = {
            'axis': {'range': [None, max(starting_balance * 2, new_balance * 1.2)]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, starting_balance], 'color': "lightgray"},
                {'range': [starting_balance, new_balance] if new_balance > starting_balance 
                          else [new_balance, starting_balance], 
                 'color': "lightgreen" if new_balance > starting_balance else "pink"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': starting_balance
            }
        }
    ))
    
    fig.update_layout(height=300)
    st.plotly_chart(fig, use_container_width=True)
    
    # Special scenarios
    st.subheader("Special Money Situations")
    st.markdown("Let's try some special situations to see what happens to your money!")
    
    scenario = st.selectbox(
        "Choose a special situation:",
        [
            "Select a situation...",
            "🎁 Birthday with lots of gifts",
            "🧸 Save for a big toy",
            "🚲 Save for a bicycle",
            "🎮 Buying a new video game"
        ]
    )
    
    if scenario != "Select a situation...":
        if scenario == "🎁 Birthday with lots of gifts":
            birthday_money = 100
            new_special_balance = starting_balance + birthday_money
            st.success(f"You got ${birthday_money} for your birthday! Your new balance would be ${new_special_balance}!")
            
        elif scenario == "🧸 Save for a big toy":
            toy_cost = 50
            weeks_to_save = int(np.ceil(toy_cost / (allowance/4)))  # Assuming weekly allowance
            st.info(f"A big toy costs ${toy_cost}. If you save all your allowance, it would take about {weeks_to_save} weeks to save enough!")
            
        elif scenario == "🚲 Save for a bicycle":
            bike_cost = 200
            weeks_to_save = int(np.ceil(bike_cost / (allowance/4)))  # Assuming weekly allowance
            st.warning(f"A bicycle costs ${bike_cost}. That would take about {weeks_to_save} weeks to save all your allowance!")
            st.markdown("That's a long time! Maybe you could do extra chores or save birthday money too!")
            
        elif scenario == "🎮 Buying a new video game":
            game_cost = 60
            remaining = starting_balance - game_cost
            st.info(f"A new video game costs ${game_cost}. If you buy it now, you would have ${remaining} left in your piggy bank.")
            if remaining < 20:
                st.warning("That doesn't leave much money for other things! Think carefully! 🤔")
            else:
                st.success("You would still have money left for other things! 👍")

# Footer
st.markdown("---")
st.markdown("#### Made with ❤️ for learning about money! | Cash Flow Adventure")
st.markdown("👆 Use the navigation menu on the left to explore different sections!")
