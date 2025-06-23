import streamlit as st
from math import log

st.write("Compound interest Application!")
st.write("\n\n  \n\n")

st.write("1. Calculate final amount")
years = st.slider(label = "Years compounded", key="y1")
rate = st.slider(label= "Returns year on year", key = "r1")
amt = st.slider(label= "Principal invested", key = "a1")
final_amt = amt*(1+rate/100)**years
st.write("Final amount = ", round(final_amt, ndigits=3), " , Interest earned = ", round(final_amt-amt, ndigits=3))
st.write("\n\n  \n\n")

st.write("2. Calculate Years Invested")
famt2 = st.slider(label = "Final amount", key="f2")
rate2 = st.slider(label= "Returns year on year", key="r2")
amt2 = st.slider(label= "Principal invested", key="a2")
try:
    number_of_years2 = log(famt2/amt2, 1 + rate2 / 100)
    st.write("Number of years invested = ", round(number_of_years2, ndigits=3))
except ZeroDivisionError:
    st.write("Don't set parameters to 0")
st.write("\n\n  \n\n")

st.write("3. Calculate effective year on year interest rate")
years3 = st.slider(label = "Years compounded", key="y3")
famt3 = st.slider(label= "Final amount", key="f3")
amt3 = st.slider(label= "Principal invested", key="a3")
try:
    rate3 = ((famt3/amt3)**(1/years3) -1)*100
    st.write("Interest rate year on year = ", round(rate3, ndigits=3))
except ZeroDivisionError:
    st.write("Don't set parameters to 0")
st.write("\n\n  \n\n")