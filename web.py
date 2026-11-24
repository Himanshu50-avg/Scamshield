

import streamlit as st
from datetime import datetime

# =========================================================
# IMPORT EXISTING DETECTION FUNCTIONS FROM main.py
# =========================================================

from main import (
    analyse_message,
    analyse_email,
    analyse_standalone_url
)


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="ScamShield",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# SESSION STATE
# =========================================================

if "history" not in st.session_state:
    st.session_state.history = []

if "total_scans" not in st.session_state:
    st.session_state.total_scans = 0

if "high_risk" not in st.session_state:
    st.session_state.high_risk = 0

if "suspicious" not in st.session_state:
    st.session_state.suspicious = 0

if "safe_scans" not in st.session_state:
    st.session_state.safe_scans = 0


# =========================================================
# CSS
# =========================================================

st.markdown(
    """
    <style>

    /* MAIN BACKGROUND */
    .stApp {
        background: linear-gradient(
            135deg,
            #f3f9ff 0%,
            #e8f4ff 55%,
            #ffffff 100%
        );
    }

    .block-container {
        max-width: 1250px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    /* SIDEBAR */
    section[data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #082b57 0%,
            #0b477d 100%
        );
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    /* HEADINGS */
    h1 {
        color: #123f72 !important;
        font-weight: 900 !important;
    }

    h2 {
        color: #174d7d !important;
    }

    h3 {
        color: #20587f !important;
    }

    /* NORMAL TEXT */
    p {
        color: #315878;
    }

    /* METRIC CARDS */
    div[data-testid="stMetric"] {
        background: white;
        border: 1px solid #d4e6f4;
        border-radius: 18px;
        padding: 15px;
        box-shadow: 0 8px 25px rgba(30, 90, 140, 0.12);
    }

    div[data-testid="stMetric"] label {
        color: #315878 !important;
        font-weight: 700 !important;
    }

    div[data-testid="stMetric"] [data-testid="stMetricValue"] {
        color: #0b3d70 !important;
    }

    /* INPUTS */
    .stTextInput input,
    .stTextArea textarea {
        background-color: white !important;
        color: #173d5d !important;
        border: 1px solid #b9d5e9 !important;
        border-radius: 10px !important;
    }

    .stTextInput label,
    .stTextArea label {
        color: #234f73 !important;
        font-weight: 700 !important;
    }

    /* BUTTONS */
    .stButton > button {
        width: 100%;
        min-height: 42px;
        border-radius: 10px !important;
        border: none !important;

        background: linear-gradient(
            90deg,
            #087fca,
            #12b9c7
        ) !important;

        color: white !important;
        font-weight: 800 !important;

        box-shadow:
            0 5px 15px rgba(8, 127, 202, 0.20);
    }

    .stButton > button:hover {
        background: linear-gradient(
            90deg,
            #066da9,
            #0c9da9
        ) !important;

        color: white !important;
    }

    /* LINKS */
    a {
        color: #087fca !important;
        font-weight: 700;
    }

    /* TABS */
    button[data-baseweb="tab"] {
        color: #315878 !important;
        font-weight: 700 !important;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        color: #087fca !important;
    }

    /* ALERTS */
    div[data-testid="stAlert"] {
        border-radius: 12px;
    }

    /* CONTAINERS */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 16px !important;
        border-color: #d5e7f5 !important;
        background: rgba(255,255,255,0.80);
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# FUNCTIONS
# =========================================================

def save_scan(scan_type, target, score, warnings):

    if score >= 60:
        risk = "High Risk"
        st.session_state.high_risk += 1

    elif score > 0:
        risk = "Suspicious"
        st.session_state.suspicious += 1

    else:
        risk = "Safe"
        st.session_state.safe_scans += 1

    st.session_state.total_scans += 1

    st.session_state.history.insert(
        0,
        {
            "time": datetime.now().strftime("%d-%m-%Y %H:%M"),
            "type": scan_type,
            "target": target[:80],
            "score": score,
            "risk": risk,
            "warnings": warnings.copy()
        }
    )


# =========================================================
# RESULT DISPLAY
# =========================================================

def display_result(score, warnings):

    if warnings:

        st.error(
            f"🚨 SCAM / SUSPICIOUS CONTENT DETECTED\n\n"
            f"Risk Score: {score}/100"
        )

        st.subheader("🚨 Detection Details")

        for warning in warnings:
            st.error(f"🔴 {warning}")

    else:

        st.success(
            f"✅ NO THREAT DETECTED\n\n"
            f"Risk Score: {score}/100"
        )


# =========================================================
# DISPLAY FOUND URLS
# =========================================================

def display_found_urls(urls):

    if urls:

        st.subheader("🔗 URLs Found")

        for url in urls:
            st.code(url)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        "## 🛡️ ScamShield"
    )

    st.caption(
        "Digital Scam Detection System"
    )

    st.markdown("---")

    page = st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "🔗 URL Scanner",
            "📧 Email Scanner",
            "💬 SMS Scanner",
            "📜 Scan History",
            "📊 Reports",
            "🚨 Report Cybercrime",
            "🛡️ Safety Tips"
        ]
    )

    st.markdown("---")

    st.caption(
        "ScamShield Prototype"
    )


# =========================================================
# DASHBOARD
# =========================================================

if page == "🏠 Dashboard":

    st.title("Welcome to ScamShield 🛡️")

    st.write(
        "Detect suspicious URLs, emails and messages before they become a threat."
    )

    st.markdown("")


    # =====================================================
    # STATISTICS
    # =====================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🔎 Total Scans",
            st.session_state.total_scans
        )

    with col2:
        st.metric(
            "🚨 High Risk",
            st.session_state.high_risk
        )

    with col3:
        st.metric(
            "⚠️ Suspicious",
            st.session_state.suspicious
        )

    with col4:
        st.metric(
            "📄 Reports",
            len(st.session_state.history)
        )


    st.markdown("---")


    # =====================================================
    # THREE SCANNER AREAS
    # =====================================================

    tab_url, tab_email, tab_sms = st.tabs(
        [
            "🔗 URL Scanner",
            "📧 Email Scanner",
            "💬 SMS Scanner"
        ]
    )


    # =====================================================
    # URL SCANNER
    # =====================================================

    with tab_url:

        st.header("🔗 URL Scanner")

        st.write(
            "Check a website link for suspicious URL patterns."
        )

        url = st.text_input(
            "Website URL",
            placeholder="https://example.com",
            key="dashboard_url"
        )

        if st.button(
            "🔍 Scan URL",
            key="dashboard_url_button",
            use_container_width=True
        ):

            if not url.strip():

                st.warning("Please enter a URL.")

            else:

                warnings, urls, score = analyse_standalone_url(url)

                save_scan(
                    "URL",
                    url,
                    score,
                    warnings
                )

                display_result(
                    score,
                    warnings
                )


    # =====================================================
    # EMAIL SCANNER
    # =====================================================

    with tab_email:

        st.header("📧 Email Scanner")

        st.write(
            "Analyze the sender, subject and content of a suspicious email."
        )

        sender = st.text_input(
            "Sender Email",
            placeholder="example@gmail.com",
            key="dashboard_sender"
        )

        subject = st.text_input(
            "Email Subject",
            placeholder="Your account requires verification",
            key="dashboard_subject"
        )

        body = st.text_area(
            "Email Content",
            placeholder="Paste the complete email here...",
            height=180,
            key="dashboard_email_body"
        )

        if st.button(
            "🔍 Scan Email",
            key="dashboard_email_button",
            use_container_width=True
        ):

            if not sender.strip() and not body.strip():

                st.warning(
                    "Please enter the sender or email content."
                )

            else:

                warnings, urls, score = analyse_email(
                    subject,
                    sender,
                    body
                )

                save_scan(
                    "Email",
                    sender if sender else body,
                    score,
                    warnings
                )

                display_result(
                    score,
                    warnings
                )

                display_found_urls(urls)


    # =====================================================
    # SMS SCANNER
    # =====================================================

    with tab_sms:

        st.header("💬 SMS / Message Scanner")

        st.write(
            "Analyze suspicious SMS or messaging content."
        )

        message = st.text_area(
            "Message",
            placeholder=(
                "Example: Congratulations! You are a winner. "
                "Click here to claim your prize."
            ),
            height=180,
            key="dashboard_message"
        )

        if st.button(
            "🔍 Scan Message",
            key="dashboard_sms_button",
            use_container_width=True
        ):

            if not message.strip():

                st.warning(
                    "Please enter a message."
                )

            else:

                warnings, urls, score = analyse_message(
                    message
                )

                save_scan(
                    "SMS",
                    message,
                    score,
                    warnings
                )

                display_result(
                    score,
                    warnings
                )

                display_found_urls(urls)


    # =====================================================
    # SAFETY TIPS
    # =====================================================

    st.markdown("---")

    st.header("🛡️ Quick Safety Tips")

    tip1, tip2, tip3, tip4 = st.columns(4)

    with tip1:

        with st.container(border=True):

            st.subheader("🔐 OTP")

            st.write(
                "Never share your OTP, PIN or password."
            )

    with tip2:

        with st.container(border=True):

            st.subheader("🔗 Links")

            st.write(
                "Check website addresses before clicking."
            )

    with tip3:

        with st.container(border=True):

            st.subheader("📧 Email")

            st.write(
                "Verify suspicious email senders."
            )

    with tip4:

        with st.container(border=True):

            st.subheader("💳 Payments")

            st.write(
                "Never transfer money because of an urgent message."
            )


# =========================================================
# URL SCANNER PAGE
# =========================================================

elif page == "🔗 URL Scanner":

    st.title("🔗 URL Scanner")

    st.write(
        "Enter a website URL to check for suspicious patterns."
    )

    url = st.text_input(
        "Website URL",
        placeholder="https://example.com"
    )

    if st.button(
        "🔍 Scan URL",
        use_container_width=True
    ):

        if not url.strip():

            st.warning("Please enter a URL.")

        else:

            warnings, urls, score = analyse_standalone_url(url)

            save_scan(
                "URL",
                url,
                score,
                warnings
            )

            display_result(
                score,
                warnings
            )


# =========================================================
# EMAIL SCANNER PAGE
# =========================================================

elif page == "📧 Email Scanner":

    st.title("📧 Email Scanner")

    st.write(
        "Analyze a suspicious email using sender, subject and message content."
    )

    sender = st.text_input(
        "Sender Email",
        placeholder="example@gmail.com"
    )

    subject = st.text_input(
        "Subject",
        placeholder="Important account notification"
    )

    body = st.text_area(
        "Email Content",
        placeholder="Paste email content here...",
        height=220
    )

    if st.button(
        "🔍 Scan Email",
        use_container_width=True
    ):

        if not sender.strip() and not body.strip():

            st.warning(
                "Please enter the sender or email content."
            )

        else:

            warnings, urls, score = analyse_email(
                subject,
                sender,
                body
            )

            save_scan(
                "Email",
                sender if sender else body,
                score,
                warnings
            )

            display_result(
                score,
                warnings
            )

            display_found_urls(urls)


# =========================================================
# SMS SCANNER PAGE
# =========================================================

elif page == "💬 SMS Scanner":

    st.title("💬 SMS / Message Scanner")

    st.write(
        "Paste a suspicious SMS or message below."
    )

    message = st.text_area(
        "Message",
        placeholder=(
            "Example: Your account will be suspended. "
            "Verify immediately by clicking here."
        ),
        height=220
    )

    if st.button(
        "🔍 Scan Message",
        use_container_width=True
    ):

        if not message.strip():

            st.warning(
                "Please enter a message."
            )

        else:

            warnings, urls, score = analyse_message(
                message
            )

            save_scan(
                "SMS",
                message,
                score,
                warnings
            )

            display_result(
                score,
                warnings
            )

            display_found_urls(urls)


# =========================================================
# SCAN HISTORY
# =========================================================

elif page == "📜 Scan History":

    st.title("📜 Scan History")

    if not st.session_state.history:

        st.info(
            "No scans have been performed yet."
        )

    else:

        for item in st.session_state.history:

            if item["risk"] == "High Risk":
                icon = "🔴"

            elif item["risk"] == "Suspicious":
                icon = "🟠"

            else:
                icon = "🟢"

            with st.container(border=True):

                st.subheader(
                    f"{icon} {item['type']} Scan"
                )

                st.write(
                    f"**Time:** {item['time']}"
                )

                st.write(
                    f"**Risk:** {item['risk']}"
                )

                st.write(
                    f"**Risk Score:** {item['score']}/100"
                )

                st.write(
                    f"**Target:** {item['target']}"
                )

                if item["warnings"]:

                    st.write("**Warnings:**")

                    for warning in item["warnings"]:

                        st.error(
                            f"🔴 {warning}"
                        )


# =========================================================
# REPORTS
# =========================================================

elif page == "📊 Reports":

    st.title("📊 ScamShield Reports")

    total = st.session_state.total_scans
    high = st.session_state.high_risk
    suspicious = st.session_state.suspicious
    safe = st.session_state.safe_scans

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Scans",
            total
        )

    with col2:
        st.metric(
            "High Risk",
            high
        )

    with col3:
        st.metric(
            "Suspicious",
            suspicious
        )

    with col4:
        st.metric(
            "Safe",
            safe
        )

    st.markdown("")

    if total > 0:

        st.subheader("📊 Scan Distribution")

        chart_data = {
            "Safe": safe,
            "Suspicious": suspicious,
            "High Risk": high
        }

        st.bar_chart(chart_data)

    else:

        st.info(
            "Perform some scans to generate reports."
        )


# =========================================================
# 🚨 REPORT CYBERCRIME INDIA
# =========================================================

elif page == "🚨 Report Cybercrime":

    st.title("🚨 Report Cybercrime India")

    st.write(
        "If ScamShield detects suspicious activity, you can report it "
        "through the official Government of India cybercrime portal."
    )

    st.markdown("")


    # =====================================================
    # EMERGENCY FRAUD BOX
    # =====================================================

    st.error(
        "🚨 FINANCIAL CYBER FRAUD?\n\n"
        "If money has already been lost or a financial fraud has occurred, "
        "call **1930** immediately."
    )


    st.markdown("")


    # =====================================================
    # REPORT FORM
    # =====================================================

    st.subheader("📝 Prepare Your Report")

    report_type = st.selectbox(
        "Type of Cybercrime",
        [
            "Online Financial Fraud",
            "Phishing / Fake Website",
            "Fraudulent Email",
            "Fraudulent SMS / Message",
            "Social Media Scam",
            "Identity Theft",
            "Other Cybercrime"
        ]
    )


    suspicious_item = st.text_input(
        "Suspicious URL / Email / Phone Number",
        placeholder="Paste the suspicious information here"
    )


    description = st.text_area(
        "Describe What Happened",
        placeholder=(
            "Explain what happened, what message you received, "
            "what link you clicked, or what suspicious activity you noticed."
        ),
        height=180
    )


    evidence = st.file_uploader(
        "Upload Evidence",
        type=[
            "png",
            "jpg",
            "jpeg",
            "pdf",
            "txt",
            "doc",
            "docx"
        ]
    )


    st.markdown("")


    if st.button(
        "📋 Prepare Report",
        use_container_width=True
    ):

        if not suspicious_item.strip() and not description.strip():

            st.warning(
                "Please provide the suspicious information or describe the incident."
            )

        else:

            st.success(
                "✅ Report information prepared."
            )

            st.subheader("Report Summary")

            st.write(
                f"**Category:** {report_type}"
            )

            if suspicious_item:

                st.write(
                    f"**Suspicious Information:** {suspicious_item}"
                )

            if description:

                st.write(
                    f"**Description:** {description}"
                )

            if evidence:

                st.write(
                    f"**Evidence:** {evidence.name}"
                )

            st.info(
                "Use the official Government of India portal below "
                "to submit the complaint."
            )


    st.markdown("---")


    # =====================================================
    # OFFICIAL GOVERNMENT PORTAL
    # =====================================================

    st.subheader("🇮🇳 Official Government Portal")

    st.write(
        "Submit your cybercrime complaint through the "
        "National Cyber Crime Reporting Portal."
    )

    st.link_button(
        "🚨 Open National Cyber Crime Reporting Portal",
        "https://www.cybercrime.gov.in/",
        use_container_width=True
    )


    st.markdown("")


    st.subheader("🔎 Report a Suspect")

    st.write(
        "For suspicious URLs, phone numbers, email IDs and other "
        "suspect identifiers, use the official reporting facilities "
        "available on the Government portal."
    )

    st.link_button(
        "🔗 Open Cybercrime Portal",
        "https://www.cybercrime.gov.in/",
        use_container_width=True
    )


    st.markdown("")

    st.caption(
        "ScamShield does not directly submit complaints to the Government. "
        "The official portal is used for actual complaint registration."
    )


# =========================================================
# SAFETY TIPS
# =========================================================

elif page == "🛡️ Safety Tips":

    st.title("🛡️ Scam Prevention Tips")

    tips = [
        (
            "🔐 Protect your OTP",
            "Never share OTPs with anyone, even if they claim to be from your bank."
        ),
        (
            "🔗 Check URLs",
            "Look carefully at the complete website address before entering credentials."
        ),
        (
            "📧 Verify Emails",
            "Check the sender's complete email address instead of trusting the display name."
        ),
        (
            "💳 Be careful with payments",
            "Do not send money because a message creates urgency or threatens account suspension."
        ),
        (
            "🎁 Beware of prizes",
            "Unexpected prize or reward messages can be used to trick you into paying money."
        ),
        (
            "📱 Check suspicious messages",
            "Do not click links in unexpected SMS messages before verifying them."
        ),
        (
            "🏦 Use official channels",
            "Open banking and government websites through official apps or manually entered addresses."
        ),
        (
            "🚨 Stop when unsure",
            "If something feels suspicious, stop and verify it through an official source."
        )
    ]

    for title, description in tips:

        with st.container(border=True):

            st.subheader(title)

            st.write(description)