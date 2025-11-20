import streamlit as st
import streamlit.components.v1 as components

# -----------------------------
# Shaq height → age data
# -----------------------------
ages = [4, 6, 8, 10, 12, 13, 16, 21]
heights_cm = [118.1, 130.8, 144.1, 160.7, 177.8, 198.1, 200.7, 215.9]

def estimate_age_from_height_cm(H):
    if H <= heights_cm[0]:
        return ages[0]
    if H >= heights_cm[-1]:
        return ages[-1]
    for i in range(len(heights_cm) - 1):
        h0, h1 = heights_cm[i], heights_cm[i + 1]
        a0, a1 = ages[i], ages[i + 1]
        if h0 <= H <= h1:
            t = (H - h0) / (h1 - h0)
            return a0 + t * (a1 - a0)
    return None

def age_to_string(age):
    years = int(age)
    months = round((age - years) * 12)
    if months == 12:
        years += 1
        months = 0
    if months == 0:
        return f"{years} years"
    return f"{years} years {months} months"

# -----------------------------
# Streamlit input
# -----------------------------
st.title("Shaquille O'Neal Age At Every Height")
height = st.number_input("Enter height in cm:", min_value=100.0, max_value=216.0, step=0.1)

if height:
    age = estimate_age_from_height_cm(height)
    age_str = age_to_string(age)

    html_code = f"""
    <html>
    <head>
        <style>
            body {{
                background-color: #552583; /* Lakers Purple */
                font-family: Arial, sans-serif;
                text-align: center;
            }}

            #age-text {{
                color: #FDB927;    /* Lakers Gold */
                font-size: 48px;
                font-weight: bold;
                margin-top: 40px;
            }}
        </style>
    </head>
    <body>
        <p id="age-text">Shaq's age at {height} cm: {age_str}</p>
    </body>
    </html>
    """

    components.html(html_code, height=300)
