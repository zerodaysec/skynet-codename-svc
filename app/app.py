"""app.py"""
import random
import streamlit as st

st.set_page_config(
    page_title="Codename Generator", page_icon=":bar_chart:", layout="centered"
)

cloud_adj = [
    "Automated",
    "Blue",
    "Cloud-based",
    "Cloud-enabled",
    "Cloud-native",
    "Cloud-optimized",
    "Collaborative",
    "Cost-effective",
    "Distributed",
    "Elastic",
    "Flexible",
    "Green",
    "High-availability",
    "Managed",
    "Multi-tenant",
    "On-demand",
    "Orange",
    "Pink",
    "Virtual",
    "Reliable",
    "Remote",
    "Red",
    "Scalable",
    "Secure",
    "Self-service",
    "Yellow",
]

cyber_adj = [
    "Red",
    "Blue",
    "Secure",
    "Encrypted",
    "Firewall-protected",
    "Vulnerability-scanned",
    "Compliance-compliant",
    "Risk-mitigated",
    "Incident-response-ready",
    "Threat-intelligent",
    "Cybercrime-resistant",
    "Policy-compliant",
    "Threat-aware",
    "Measurement-implemented",
    "Defense-in-depth",
    "Risk-assessed",
    "Awareness-trained",
    "Software-secured",
    "Framework-compliant",
    "Strategically-planned",
    "Best-practice-adherent",
    "Governed",
]

innov_adj = [
    "Purple",
    "Disruptive",
    "Creative",
    "Breakthrough",
    "Game-changing",
    "Pioneering",
    "Forward-thinking",
    "Cutting-edge",
    "Out-of-the-box",
    "Pioneering",
    "Trailblazing",
    "Progressive",
    "Revolutionary",
    "Innovative",
    "Strategic",
    "Progressive",
    "Efficient",
    "Flexible",
    "Agile",
    "Pioneering",
    "Groundbreaking",
]

all_nouns = [
    "Jaguar",
    "Crocodile",
    "Falcon",
    "Wolf",
    "Panther",
    "Tiger",
    "Bear",
    "Shark",
    "Lynx",
    "Eagle",
    "Fox",
    "Lion",
    "Hawk",
    "Cheetah",
    "Gorilla",
    "Cobra",
    "Osprey",
    "Mongoose",
    "Leopard",
    "Weasel",
    "Tomcat",
    "Alleycat",
    "Sniper",
    "Venom",
    "Range",
    "Droid",
]


def suggest_codename(category: str):
    """Suggest codenames."""
    adjs = []
    category = category.lower()
    if category == "cloud":
        adjs = cloud_adj
    elif category == "security":
        adjs = cyber_adj
    elif category == "innovate":
        adjs = cloud_adj + cyber_adj + innov_adj
    else:
        adjs = cloud_adj + cyber_adj + innov_adj
    return f"{random.choice(adjs)} {random.choice(all_nouns)}"


st.write("# Codename")

CATEGORY = st.selectbox("Category", ["All", "Security", "Cloud", "Innovate"])
COUNT = st.number_input('Number of ideas', 1, 5)
START = 1
# if st.button("Generate"):
while START <= COUNT:
    st.write("### ", suggest_codename(CATEGORY))
    START = START + 1
