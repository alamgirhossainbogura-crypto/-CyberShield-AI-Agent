import streamlit as st

# পেজ কনফিগারেশন
st.set_page_config(page_title="CyberShield AI Agent", layout="wide")

# সাইবার ডার্ক ও নিয়ন গ্লো থিম (CSS)
st.markdown("""
    <style>
    .main { 
        background-color: #0B132B; 
        color: #FFFFFF; 
        font-family: 'Courier New', Courier, monospace;
    }
    .main-title {
        color: #48CAE4;
        text-align: center;
        text-shadow: 0 0 10px #48CAE4;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .sub-title {
        color: #90E0EF;
        text-align: center;
        font-size: 14px;
        margin-bottom: 20px;
    }
    .cyber-card {
        background-color: #1C2541;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #00B4D8;
        box-shadow: 0 4px 15px rgba(0, 180, 216, 0.2);
        text-align: center;
        margin-bottom: 15px;
    }
    .cyber-card h4 { color: #90E0EF; margin: 0; font-size: 14px; }
    .cyber-card h2 { margin: 5px 0 0 0; font-size: 24px; font-weight: bold; }
    
    .stButton>button { 
        background-color: transparent; 
        color: #00B4D8; 
        font-weight: bold;
        font-size: 16px;
        border-radius: 8px; 
        border: 2px solid #00B4D8;
        box-shadow: 0 0 10px rgba(0, 180, 216, 0.3);
        width: 100%;
        padding: 10px;
        transition: 0.3s;
        text-transform: uppercase;
    }
    .stButton>button:hover {
        background-color: #00B4D8;
        color: #0B132B;
        box-shadow: 0 0 20px #00B4D8;
    }
    .report-box { 
        background-color: #1C2541; 
        padding: 20px; 
        border-radius: 10px; 
        border: 1px solid #FF3366;
        box-shadow: 0 4px 15px rgba(255, 51, 102, 0.2);
    }
    .report-header {
        color: #FF3366;
        font-size: 18px;
        font-weight: bold;
        text-transform: uppercase;
        border-bottom: 1px solid #FF3366;
        padding-bottom: 5px;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# টাইটেল ও হেডার
st.markdown("<h1 class='main-title'>CYBERSHIELD AI AGENT</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Dynatrace Security Monitoring & AI Threat Analysis</p>", unsafe_allow_html=True)
st.markdown("<hr style='border-color: #1C2541;'>", unsafe_allow_html=True)

# সাইডবার কনফিগারেশন
st.sidebar.header("⚙️ Configuration")
mode = st.sidebar.selectbox("Select Mode", ["Demo Mode (For Presentation)", "Live Dynatrace Mode"])
gemini_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if mode == "Demo Mode (For Presentation)":
    st.sidebar.success("✅ Running on Dashboard Demo Mode")
else:
    st.sidebar.warning("⚠️ Running on Live Mode")

# কলাম/কার্ড
col1, col2 = st.columns(2)

with col1:
    if mode == "Demo Mode (For Presentation)":
        st.markdown("""
            <div class='cyber-card' style='border-color: #FF3366; box-shadow: 0 4px 15px rgba(255, 51, 102, 0.2);'>
                <h4 style='color: #FF3366;'>🔴 ACTIVE VULNERABILITIES</h4>
                <h2 style='color: #FF3366;'>5 Cases</h2>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div class='cyber-card' style='border-color: #00F5D4; box-shadow: 0 4px 15px rgba(0, 245, 212, 0.2);'>
                <h4 style='color: #00F5D4;'>🟢 ACTIVE VULNERABILITIES</h4>
                <h2 style='color: #00F5D4;'>0 Cases</h2>
            </div>
        """, unsafe_allow_html=True)

with col2:
    if mode == "Demo Mode (For Presentation)":
        st.markdown("""
            <div class='cyber-card'>
                <h4>🛡️ SYSTEM SECURITY STATUS</h4>
                <h2 style='color: #FFD166;'>64% SAFE (HIGH THREAT)</h2>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div class='cyber-card'>
                <h4>🛡️ SYSTEM SECURITY STATUS</h4>
                <h2 style='color: #00F5D4;'>100% SECURE</h2>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# থ্রেট রিপোর্ট জেনারেট বাটন
if st.button("Generate Detailed Report"):
    with st.spinner("CyberShield AI is analyzing system logs..."):
        st.markdown("<br>", unsafe_allow_html=True)
        
        if mode == "Demo Mode (For Presentation)":
            st.markdown("""
            <div class='report-box'>
                <div class='report-header'>🛡️ AI Analysis Report</div>
                <strong>Report ID:</strong> CS-AI-2026-05<br>
                <strong>Gemini Security Engine:</strong> Active<br>
                <strong>Dynatrace Data Synced:</strong> YES<br><br>
                
                <span style='color: #FF3366; font-weight: bold;'>⚠️ Key Findings:</span><br>
                • <code>S-2034: CRITICAL</code> - Login Endpoint SQL Injection in 'customer-db-v1'. Immediate patching required.<br>
                • <code>S-2035: HIGH</code> - Remote Code Execution via Log4j on 'internal-app-server'.<br><br>
                
                <span style='color: #00B4D8; font-weight: bold;'>⚙️ Mitigation Plan:</span><br>
                1. Apply WAF rule to block suspicious login patterns.<br>
                2. Sanitize user inputs on 'customer-db' forms.<br>
                3. Update Log4j libraries in 'internal-app-server'.
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class='report-box' style='border-color: #00F5D4; box-shadow: 0 4px 15px rgba(0, 245, 212, 0.2);'>
                <div class='report-header' style='color: #00F5D4; border-color: #00F5D4;'>🛡️ AI Analysis Report</div>
                <strong>Report ID:</strong> CS-AI-2026-05<br>
                <strong>Gemini Security Engine:</strong> Active<br>
                <strong>Dynatrace Data Synced:</strong> YES<br><br>
                
                <span style='color: #00F5D4; font-weight: bold;'>🟢 Core Assessment:</span><br>
                No active threats or data breaches identified in the system profile. System telemetry is stable.
            </div>
            """, unsafe_allow_html=True)
