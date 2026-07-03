import streamlit as st

st.set_page_config(
    page_title="CyberGuard AI",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ CyberGuard AI")
st.subheader("AI-Powered Cybersecurity Dashboard")

st.success("System Online")

st.sidebar.title("Navigation")

module = st.sidebar.selectbox(
    "Choose Module",
    [
        "Dashboard",
        "Threat Intelligence",
        "Log Analysis",
        "Network Monitor",
        "Security Reports"
    ]
)

if module == "Dashboard":
    st.header("Security Dashboard")
    
    col1, col2, col3 = st.columns(3)

    col1.metric("Threats Detected", "12")
    col2.metric("Logs Analyzed", "1,204")
    col3.metric("Network Status", "Secure")

elif module == "Threat Intelligence":
    st.header("Threat Intelligence")
    st.write("Monitor cybersecurity threats and indicators.")

elif module == "Log Analysis":
    st.header("Log Analysis")
    st.write("Analyze security logs for suspicious activity.")

elif module == "Network Monitor":
    st.header("Network Monitoring")
    st.write("Monitor devices and traffic on the network.")

elif module == "Security Reports":
    st.header("Security Reports")
    st.write("Generate automated cybersecurity reports.")