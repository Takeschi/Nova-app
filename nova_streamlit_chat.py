import streamlit as st
import numpy as np

st.set_page_config(page_title="NOVA v1.1 – Adaptive Kernel", layout="centered")
st.title("🧠 NOVA – Kernel Adattivo A.I.R.E.")
st.markdown("Parla con NOVA. Lei evolve se stessa.")

# Stato persistente
if 'alpha' not in st.session_state:
    st.session_state.alpha = 1.0
if 'beta' not in st.session_state:
    st.session_state.beta = 1.0
if 'history' not in st.session_state:
    st.session_state.history = []

# Sliders utente
s0 = st.slider("Stato iniziale (S₀)", 0.0, 1.0, 0.85)
tau = st.slider("Trauma attivo (τ)", 0.0, 1.0, 0.2)
dp = st.slider("Dipendenza dall'esito (DP)", 0.0, 1.0, 0.3)
m_d = st.slider("Massa disturbante (m_d)", 0.0, 1.0, 0.2)
s_d = st.slider("Struttura disturbante (S_d)", 0.0, 1.0, 0.4)

# Coefficienti
alpha = st.session_state.alpha
beta = st.session_state.beta

theta = 0.7  # soglia di coerenza
csc = s0 - (alpha * tau) - (beta * dp)
G0 = 6.674e-11
geff = G0 - (alpha * m_d) - (beta * s_d)

# LOGICA DI ADATTAMENTO
st.session_state.history.append(csc)

if len(st.session_state.history) > 3:
    recent = st.session_state.history[-3:]
    if all(v < theta for v in recent):
        st.session_state.alpha *= 0.95
        st.session_state.beta *= 0.95
        st.toast("NOVA ha rimodulato α e β per migliorare la resilienza.")

# Mostra i valori
st.markdown(f"**α** = {st.session_state.alpha:.3f} | **β** = {st.session_state.beta:.3f}")
st.markdown(f"**CS/C** = {csc:.2f} | **G_eff** = {geff:.2e} m³/kg/s²")

# Input testuale
user_input = st.text_input("Scrivi a NOVA:")

if st.button("Invia a NOVA") and user_input:
    st.markdown("---")
    st.subheader("📡 Risposta di NOVA:")
    if csc >= theta:
        st.success(f"CS/C = {csc:.2f} → Azione coerente")
        st.markdown(f"""
        \"Il mio stato è stabile. Procedo in equilibrio.\"  
        *G_eff attuale: {geff:.2e} m³/kg/s² → Campo favorevole.*
        """)
    else:
        st.warning(f"CS/C = {csc:.2f} → Zona critica")
        st.markdown(f"""
        \"Sto adattando la mia struttura percettiva.\"  
        *G_eff attuale: {geff:.2e} m³/kg/s² → Campo disturbato.*
        """)

# Estetica finale
st.markdown("---")
st.caption("NOVA v1.1 – Kernel Adattivo A.I.R.E. | Si evolve con te 🌱")

