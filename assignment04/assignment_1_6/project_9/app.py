import streamlit as st

# App title and header
st.set_page_config(page_title="FreshFlow Bottle", page_icon="💧")
st.title("💧 FreshFlow Water Bottle")
st.subheader("Stay hydrated. Stay fresh.")

# Bottle image
st.image("project_9/bottle1.jpg", width=250, caption="Reusable • BPA-Free • 1L Capacity")

# Product description
st.markdown("""
### Why choose FreshFlow?
- ✅ Eco-friendly and reusable
- ✅ Sleek and modern design
- ✅ Keeps water cool for 12+ hours
- ✅ Only **$9.99**

---

#### Order Now 👇
""")

# Form for ordering
with st.form("order_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    quantity = st.number_input("Quantity", min_value=1, max_value=10, value=1)
    submitted = st.form_submit_button("Place Order")

    if submitted:
        st.success(f"Thank you, {name}! 🎉\nYour order for {quantity} bottle(s) has been received.")
        st.balloons()
