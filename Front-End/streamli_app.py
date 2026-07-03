import sys
import os

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.append(project_root)

import streamlit as st
import pandas as pd
import plotly.express as px

from BackEnd.log_analyzer import (
    analyze_logs,
    brute_force_detection
)

from BackEnd.report_generator import generate_report
    

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

    st.divider()

 
    #Threat Trend Data
    threat_data =pd.DataFrame ({
        "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "Threats Detected": [2, 5, 3, 8, 4, 6, 3]

    })

    st.subheader("Threat Activity Trend")

    line_chart = px.line(
        threat_data,
        x="Day",
        y="Threats Detected",
        markers=True

    )
    st.plotly_chart(
        line_chart,
        use_container_width=True
    )

    line_chart.update_layout(
        title="Weekly Threat Activity",
        xaxis_title="Day ",
        yaxis_title=" Threats Counts"
    )

    threat_types =pd.DataFrame ({
        "Threat":[
            "Failed Login",
            "Brute Force",
            "Invalid Password",
            "Authentication Failure",

        ],
        "Count":[
            12,
            4,
            8,
            6
        ]
    })

    pie_chart = px.pie(
        threat_types,
        names="Threat",
        values="Count"
        
    )
   
    st.plotly_chart(
        pie_chart,
        use_container_width=True
    )
    
    pie_chart.update_layout(
        title="Threat Type Distribution" 
  )
    

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Threat Activity Trend")
        st.plotly_chart(line_chart, width="stretch")

    with col2:
        st.subheader("Threat Type Distribution")
        st.plotly_chart(pie_chart, width="stretch")


    #Risk Distribution Chart
    risk_data = pd.DataFrame({
        "Risk": ["Low", "Medium", "High"],
        "Count": [15, 8, 3]

    })

    st.subheader("Risk Distribution")

    bar_chart = px.bar(
        risk_data,
        x="Risk",
        y="Count"
           
    )
    st.plotly_chart(
        bar_chart,
        use_container_width=True
    )
    bar_chart.update_layout(
        title="Risk Level Distribution"
        
    )
elif module == "Threat Intelligence":
    st.header("Threat Intelligence")
    st.write("Monitor cybersecurity threats and indicators.")

elif module == "Log Analysis":

    st.header("Log Analysis")

    uploaded_file = st.file_uploader(
        "Upload Log File",
        type=["txt", "log"]
    )

    if uploaded_file is not None:

        log_content = uploaded_file.read().decode("utf-8")

        if st.button("Analyze Logs"):

            results = analyze_logs(log_content)
            brute_force = brute_force_detection(log_content)

            threat_count = len(results)

            # Threat Summary
            st.subheader("Threat Summary")

            col1, col2 = st.columns(2)

            col1.metric(
                "Threats Detected",
                threat_count
            )

            if threat_count >= 5:
                risk_level = "HIGH"

            elif threat_count >= 3:
                risk_level = "MEDIUM"

            elif threat_count > 0:
                risk_level = "LOW"

            else:
                risk_level = "NONE"

            col2.metric(
                "Risk Level",
                risk_level
            )

            # Risk Banner

            if risk_level == "HIGH":
                st.error("🔴 High Risk Activity Detected")

            elif risk_level == "MEDIUM":
                st.warning("🟡 Medium Risk Activity Detected")

            elif risk_level == "LOW":
                st.info("🟢 Low Risk Activity Detected")

            else:
                st.success("✅ No Threats Detected")

            # Findings

            if results:

                st.subheader("Findings")

                for result in results:
                    st.error(result)

            else:
                st.success("No suspicious activity found")

            # Recommendations

            st.subheader("Recommendations")

            if threat_count >= 5:

                st.write("""
                - Investigate immediately
                - Review failed login attempts
                - Check source IP addresses
                - Consider blocking malicious IPs
                - Review account activity
                """)

            elif threat_count >= 3:

                st.write("""
                - Review failed login attempts
                - Verify account activity
                - Monitor source IP addresses
                - Watch for brute force attacks
                """)

            elif threat_count > 0:

                st.write("""
                - Continue monitoring logs
                - Review suspicious events
                """)

            else:

                st.write("""
                - No action required
                - Continue normal monitoring
                """)
            #Display Brute Force Detection Results
            st.subheader("Brute Force Analysis")  

            if brute_force["detected"]:
                st.error(
                    f"""
                🚨 Possible Brute Force Attack Detected
                Failed Attempts: {brute_force["attempts"]}
                Risk Level: {brute_force["risk"]}
                """
                )
                
            elif brute_force["risk"] == "MEDIUM":
             st.warning(
        f"""
        ⚠️ Elevated Failed Login Activity

        Failed Attempts: {brute_force['attempts']}

        Risk Level: MEDIUM
        """
    )  
            else:
                st.success(
                    f"""
                ✅ No Brute Force Attack Detected
                Failed Attempts: {brute_force["attempts"]}
                Risk Level: {brute_force["risk"]}
                """
                )
    st.subheader("Incident Report ")

    if st.button("Generate Incident Report"):
        results = analyze_logs(log_content)
        brute_force = brute_force_detection(log_content)

        threat_count = len(results)

        if threat_count >= 5:
         risk_level = "HIGH"
        elif threat_count >= 3:
         risk_level = "MEDIUM"
        elif threat_count > 0:
            risk_level = "LOW"
        else:
            risk_level = "NONE"

        generate_report(
            "incident_report.pdf",
            threat_count,
            risk_level,
            results,
            brute_force
        )

        st.success(
            "Incident report generated successfully!"
        )
    

elif module == "Network Monitor":
    st.header("Network Monitoring")
    st.write("Monitor devices and traffic on the network.")

elif module == "Security Reports":
    st.header("Security Reports")
    st.write("Generate automated cybersecurity reports.")

