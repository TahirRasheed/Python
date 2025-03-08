import streamlit as st
# For Title
st.title("Unit Conversion App!")
# 2nd heading 
st.markdown("#Convert Weight, Time and Length")
# writing paragrah
st.write("Welcome! Select a category, enter a value and get the converted result in real-time")


# create select box with values
category = st.selectbox("Please Select Category",["Select Option","Weight","Time","Length"])

# create function for converts unit
def convert_units(category, value, unit):

    if category == "Weight":
        if unit == "Kilogram to pound":
            return value * 2.20462
        elif unit == "Pound to kilogram":
            return value / 2.20462

    elif category == "Time":
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to second":
            return value * 60
        elif unit == "Minutes to hour":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to hours":
            return value * 24

    elif category == "Length":
        if unit == "Kilometer to mile":
            return value * 0.621371
        elif unit == "Mile to kilometer":
            return value / 0.621371

    return None
# user select the unit to be convert 
if category == "Length":
    unit = st.selectbox("📏 Select Conversion", ["Kilometer to mile", "Mile to kilometer"])
elif category == "Weight":
    unit = st.selectbox("⚖️ Select Conversion", ["Kilogram to pound", "Pound to kilogram"])
elif category == "Time":
    unit = st.selectbox("⏳ Select Conversion", ["Seconds to minutes", "Minutes to seconds", "Minutes to hour", 
                                                "Hours to minutes", "Hours to days", "Days to hours"])
# user can inout the value for conversion
value = st.number_input("Enter the value to convert", min_value=0.0, format="%.2f")

# when user click on submit button , then conversion perform
if st.button("Convert"):
    result = convert_units(category, value, unit)
    if result is not None:
        st.success(f"The Conversion result of {unit} is {result:.2f}")
    else:
        st.error("Invalid conversion")