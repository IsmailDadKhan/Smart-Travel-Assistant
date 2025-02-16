import streamlit as st
import json
import os

# File to store travel plans
TRAVEL_DATA_FILE = "travel_plans.json"


# Function to load saved travel data
def load_travel_data():
    if os.path.exists(TRAVEL_DATA_FILE):
        with open(TRAVEL_DATA_FILE, "r") as file:
            return json.load(file)
    return []


# Function to save travel data
def save_travel_data(data):
    with open(TRAVEL_DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


# Load existing travel plans
travel_data = load_travel_data()

# Streamlit App Title
st.title("✈️ Smart Travel Assistant By Ismail Dad Khan")

# Destination Selection
st.header("🌍 Choose Your Travel Destination")
destinations = ["New York", "London", "Tokyo", "Paris", "Dubai", "Sydney"]
destination = st.selectbox("Select your destination:", destinations)

# Weather Selection
weather_options = ["Sunny", "Rainy", "Cold"]
weather = st.radio("Expected weather condition:", weather_options)

# Travel Expense Calculator
st.header("💰 Travel Expense Calculator")
days = st.number_input("Enter the number of travel days:", min_value=1, step=1)
daily_budget = st.number_input("Enter your daily budget ($):", min_value=0.0, step=10.0)

# Optional Expenses
flight_cost = st.number_input("Enter flight cost (optional):", min_value=0.0, step=50.0)
hotel_cost = st.number_input("Enter hotel cost (optional):", min_value=0.0, step=50.0)

# Calculate total estimated travel cost
total_expense = (days * daily_budget) + flight_cost + hotel_cost

st.write(f"### ✨ Estimated Total Trip Cost: **${total_expense:.2f}**")

# Packing Checklist Generator
st.header("🎒 Packing Checklist")
packing_list = {
    "Sunny": ["Sunglasses", "Sunscreen", "Hat"],
    "Rainy": ["Umbrella", "Raincoat", "Waterproof Shoes"],
    "Cold": ["Jacket", "Gloves", "Warm Clothes"]
}
suggested_items = packing_list.get(weather, [])

# Allow user to modify packing list
custom_packing_list = st.multiselect("Customize your packing list:", 
                                     options=["Sunglasses", "Sunscreen", "Hat", "Umbrella", "Raincoat", 
                                              "Waterproof Shoes", "Jacket", "Gloves", "Warm Clothes"], 
                                     default=suggested_items)

# Travel Summary
st.header("📋 Travel Summary")
st.write(f"**Destination:** {destination}")
st.write(f"**Weather Condition:** {weather}")
st.write(f"**Total Trip Cost:** ${total_expense:.2f}")
st.write("**Packing List:**")
for item in custom_packing_list:
    st.write(f"- {item}")

# Save Travel Details
if st.button("💾 Save Travel Plan"):
    new_plan = {
        "Destination": destination,
        "Weather": weather,
        "Days": days,
        "Daily Budget": daily_budget,
        "Total Expense": total_expense,
        "Packing List": custom_packing_list
    }
    travel_data.append(new_plan)
    save_travel_data(travel_data)
    st.success("✅ Travel Plan Saved Successfully!")

# View Past Travel Plans
st.header("📜 View Past Travel Plans")
if travel_data:
    for i, plan in enumerate(travel_data, 1):
        st.subheader(f"📌 Trip {i}")
        st.write(f"**Destination:** {plan['Destination']}")
        st.write(f"**Weather:** {plan['Weather']}")
        st.write(f"**Days:** {plan['Days']}")
        st.write(f"**Total Cost:** ${plan['Total Expense']:.2f}")
        st.write("**Packing List:**")
        for item in plan["Packing List"]:
            st.write(f"- {item}")
        st.write("---")
else:
    st.write("No travel plans found. Save your first trip now!")

