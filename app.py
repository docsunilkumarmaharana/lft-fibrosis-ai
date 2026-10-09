
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="LFT Pattern + Fibrosis Risk", layout="centered")

st.title("LFT Pattern Recognition & Fibrosis Risk")
st.caption("Research prototype — synthetic data only. Not for clinical use.")

@st.cache_data
def load_data():
    # Matches your uploaded file name
    return pd.read_csv("lft_data.csv")

df = load_data()

# --- Inputs ---
st.header("1. Patient input")
col1, col2 = st.columns(2)
with col1:
    age = st.number_input("Age (years)", 1, 120, 50)
    ast = st.number_input("AST (U/L)", 0.0, 2000.0, 30.0)
    alt = st.number_input("ALT (U/L)", 0.1, 2000.0, 30.0)
    alp = st.number_input("ALP (U/L)", 0.1, 2000.0, 90.0)
with col2:
    platelets = st.number_input("Platelets (×10⁹/L)", 1.0, 800.0, 250.0)
    ast_uln = st.number_input("AST ULN", 1.0, 200.0, 40.0)
    alt_uln = st.number_input("ALT ULN", 1.0, 200.0, 40.0)
    alp_uln = st.number_input("ALP ULN", 1.0, 400.0, 120.0)

# --- Calculations ---
def fib4(age, ast, alt, plt):
    return (age * ast) / (plt * np.sqrt(alt))

def apri(ast, ast_uln, plt):
    return ((ast / ast_uln) * 100) / plt

def r_ratio(alt, alt_uln, alp, alp_uln):
    return (alt / alt_uln) / (alp / alp_uln)

def pattern(r):
    if r >= 5: return "Hepatocellular"
    if r <= 2: return "Cholestatic"
    return "Mixed"

f4 = fib4(age, ast, alt, platelets)
ap = apri(ast, ast_uln, platelets)
r = r_ratio(alt, alt_uln, alp, alp_uln)
pat = pattern(r)

def fib4_cat(x):
    if x < 1.3: return "Low"
    if x <= 2.67: return "Indeterminate"
    return "High"

def apri_cat(x):
    if x < 0.5: return "Low"
    if x <= 1.5: return "Indeterminate"
    return "High"

st.header("2. Results")
c1, c2, c3 = st.columns(3)
c1.metric("R ratio", f"{r:.2f}")
c2.metric("FIB-4", f"{f4:.2f}", fib4_cat(f4))
c3.metric("APRI", f"{ap:.2f}", apri_cat(ap))

st.info(f"**LFT pattern:** {pat}")

st.header("3. Explanation")
st.write(f"- R = (ALT/{alt_uln}) / (ALP/{alp_uln}) = **{r:.2f}**")
st.write(f"- FIB-4 = (Age × AST) / (Platelets × √ALT) = **{f4:.2f}** → {fib4_cat(f4)}")
st.write(f"- APRI = ((AST/AST-ULN) × 100) / Platelets = **{ap:.2f}** → {apri_cat(ap)}")

st.header("4. Data preview (synthetic)")
st.dataframe(df.head(20))

st.warning(
    "Educational/research prototype only. Scores are not diagnoses. "
    "Do not use for clinical decisions."
)
