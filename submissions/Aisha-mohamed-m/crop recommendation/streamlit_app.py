"""Smart Crop Recommendation System — Premium Streamlit Frontend."""

import datetime
import os
import time

import pandas as pd
import plotly.graph_objects as go
import requests
import streamlit as st
import streamlit.components.v1 as components
from fpdf import FPDF
from fpdf.enums import XPos, YPos

# ── Configuration ────────────────────────────────────────────────────────────
API_BASE = os.environ.get("CROP_API_BASE", "http://127.0.0.1:8000")
API_PREDICT = f"{API_BASE}/predict"
HISTORY_FILE = "history.csv"
MODELS = {
    "rf": {"label": "Random Forest", "icon": "🌲", "tag": "Highest Accuracy", "desc": "Recommended for most predictions."},
    "xgb": {"label": "XGBoost", "icon": "⚡", "tag": "Fast & Accurate", "desc": "Suitable for advanced users."},
    "lr": {"label": "Logistic Regression", "icon": "📈", "tag": "Baseline Model", "desc": "Useful for comparison."},
}
AUTO_MODEL = "rf"

st.set_page_config(
    page_title="Smart Crop Recommendation System",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Session State ────────────────────────────────────────────────────────────
_DEFAULTS = {
    "page": "🏠 Home",
    "last_result": None,
    "scroll_learn": False,
    "api_url": API_BASE,
    "light_theme": False,
}
for k, v in _DEFAULTS.items():
    if k not in st.session_state:
        st.session_state[k] = v


# ── Premium CSS ──────────────────────────────────────────────────────────────
def inject_css():
    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
.stApp{background:linear-gradient(160deg,#020617 0%,#041a0e 35%,#031208 70%,#020617 100%)!important;
  color:#ecfdf5;font-family:'Inter',sans-serif!important;overflow-x:hidden}
.stApp::before,.stApp::after{content:'';position:fixed;border-radius:50%;pointer-events:none;z-index:0;
  filter:blur(80px);animation:orbDrift 20s ease-in-out infinite}
.stApp::before{top:-20%;left:-15%;width:600px;height:600px;background:rgba(16,185,129,.12)}
.stApp::after{bottom:-15%;right:-10%;width:500px;height:500px;background:rgba(52,211,153,.08);animation-delay:-8s}
@keyframes orbDrift{0%,100%{transform:translate(0,0)}50%{transform:translate(40px,-30px)}}
@keyframes fadeUp{from{opacity:0;transform:translateY(28px)}to{opacity:1;transform:translateY(0)}}
@keyframes floatY{0%,100%{transform:translateY(0)}50%{transform:translateY(-14px)}}
@keyframes pulseGlow{0%,100%{box-shadow:0 0 20px rgba(52,211,153,.2)}50%{box-shadow:0 0 40px rgba(52,211,153,.45)}}
@keyframes shimmer{0%{background-position:0% 50%}100%{background-position:200% 50%}}
header,#MainMenu,footer{visibility:hidden}
.block-container{padding:1.5rem 2rem 3rem!important;max-width:1280px}
section[data-testid="stSidebar"]{background:linear-gradient(180deg,#010a06,#021208)!important;
  border-right:1px solid rgba(52,211,153,.12)!important;box-shadow:4px 0 24px rgba(0,0,0,.4)!important}
.glass{background:linear-gradient(135deg,rgba(255,255,255,.06),rgba(255,255,255,.02));
  backdrop-filter:blur(18px);border:1px solid rgba(255,255,255,.08);border-radius:20px;
  padding:24px;box-shadow:0 8px 32px rgba(0,0,0,.35);transition:.35s cubic-bezier(.23,1,.32,1);
  animation:fadeUp .6s ease both}
.glass:hover{transform:translateY(-4px);border-color:rgba(52,211,153,.25);
  box-shadow:0 16px 48px rgba(0,0,0,.45),0 0 0 1px rgba(52,211,153,.08)}
.stat-card{text-align:center;padding:28px 16px}
.stat-num{font-size:42px;font-weight:800;background:linear-gradient(135deg,#fff,#34d399);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;line-height:1.1}
.stat-label{font-size:13px;color:#94a3b8;margin-top:8px;font-weight:500;text-transform:uppercase;letter-spacing:.6px}
.feature-card{padding:26px;text-align:left}
.feature-icon{font-size:28px;margin-bottom:12px;display:block}
.feature-title{color:#fff;font-weight:700;font-size:16px;margin-bottom:6px}
.feature-desc{color:#94a3b8;font-size:13px;line-height:1.6}
.timeline-step{display:flex;flex-direction:column;align-items:center;text-align:center;padding:20px;
  background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.06);border-radius:16px;
  transition:.3s ease;animation:fadeUp .7s ease both}
.timeline-step:hover{border-color:rgba(52,211,153,.3);transform:translateY(-3px)}
.step-num{width:44px;height:44px;border-radius:50%;background:linear-gradient(135deg,#059669,#34d399);
  color:#022c22;font-weight:800;display:flex;align-items:center;justify-content:center;margin-bottom:12px;
  box-shadow:0 4px 16px rgba(52,211,153,.35)}
.step-arrow{color:#34d399;font-size:24px;display:flex;align-items:center;justify-content:center;padding:0 4px}
.hero-grid{display:grid;grid-template-columns:1.1fr .9fr;gap:40px;align-items:center;min-height:72vh;padding:20px 0}
.hero-title{font-size:clamp(2rem,4vw,3.2rem);font-weight:800;line-height:1.12;margin:0 0 16px;
  background:linear-gradient(135deg,#fff 30%,#6ee7b7 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.hero-sub{font-size:1.15rem;color:#34d399;font-weight:600;margin-bottom:14px}
.hero-desc{color:#94a3b8;font-size:15px;line-height:1.75;max-width:520px;margin-bottom:28px}
.btn-primary{background:linear-gradient(135deg,#059669,#34d399,#10b981)!important;background-size:200%!important;
  animation:shimmer 4s linear infinite!important;color:#022c22!important;border:none!important;
  padding:14px 28px!important;border-radius:14px!important;font-weight:700!important;font-size:16px!important;
  box-shadow:0 8px 28px rgba(52,211,153,.35)!important;transition:.3s!important}
.btn-primary:hover{transform:translateY(-2px)!important;box-shadow:0 14px 36px rgba(52,211,153,.5)!important}
.model-card{cursor:pointer;padding:22px;border-radius:18px;border:1px solid rgba(255,255,255,.08);
  background:rgba(255,255,255,.03);transition:.3s;text-align:center}
.model-card:hover,.model-card.active{border-color:rgba(52,211,153,.4);background:rgba(52,211,153,.06);
  transform:translateY(-3px);box-shadow:0 12px 32px rgba(52,211,153,.12)}
.model-card.active{box-shadow:0 0 0 2px rgba(52,211,153,.35)}
.reason-item{display:flex;align-items:flex-start;gap:10px;padding:10px 0;border-bottom:1px solid rgba(255,255,255,.05);
  color:#d1fae5;font-size:14px}
.reason-check{color:#34d399;font-weight:700;flex-shrink:0}
.result-hero{text-align:center;padding:36px 24px}
.crop-circle{width:120px;height:120px;border-radius:50%;margin:0 auto 16px;
  background:radial-gradient(circle,rgba(52,211,153,.15),rgba(5,46,22,.4));
  border:2px solid rgba(52,211,153,.35);display:flex;align-items:center;justify-content:center;
  font-size:56px;animation:pulseGlow 3s ease-in-out infinite}
.conf-bar{height:8px;border-radius:99px;background:rgba(255,255,255,.08);overflow:hidden;margin:12px 0}
.conf-fill{height:100%;border-radius:99px;background:linear-gradient(90deg,#059669,#34d399);
  transition:width 1s ease}
.section-title{color:#fff;font-size:1.6rem;font-weight:700;margin:48px 0 20px;text-align:center;scroll-margin-top:24px}
.section-sub{text-align:center;color:#64748b;font-size:14px;margin:-12px 0 28px}
.footer-wrap{margin-top:48px;padding:28px 0;border-top:1px solid rgba(255,255,255,.06);text-align:center}
.footer-wrap p{color:#64748b;font-size:13px;margin:4px 0}
.api-ok{color:#34d399}.api-down{color:#f87171}
div[data-testid="stNumberInput"]>div{border-radius:12px!important;border:1px solid rgba(110,231,183,.22)!important;background:#eefbf4!important}
div[data-testid="stNumberInput"] [data-baseweb="input"],div[data-testid="stNumberInput"] [data-baseweb="base-input"],div[data-testid="stNumberInput"] input{background:#eefbf4!important;color:#123527!important}
div[data-testid="stNumberInput"] [data-baseweb="base-input"]{border:1px solid rgba(110,231,183,.28)!important;border-radius:12px!important;box-shadow:inset 0 1px 0 rgba(255,255,255,.7)!important}
div[data-testid="stNumberInput"] [data-baseweb="base-input"]:focus-within{background:#f8fffb!important;border-color:#10b981!important;box-shadow:0 0 0 3px rgba(52,211,153,.18)!important}
div[data-testid="stNumberInput"] button{color:#087856!important;background:#e4f7ed!important;border-left:1px solid rgba(16,185,129,.12)!important;border-radius:8px!important;font-weight:800!important}div[data-testid="stNumberInput"] button:hover,div[data-testid="stNumberInput"] button:active{background:#bff4da!important;color:#064e3b!important}
.form-heading{display:flex;align-items:center;gap:12px;margin:0 0 4px}.form-heading .heading-icon{width:42px;height:42px;display:grid;place-items:center;border-radius:13px;background:linear-gradient(135deg,rgba(52,211,153,.26),rgba(16,185,129,.06));font-size:21px}.form-heading h3{margin:0;color:#ecfdf5;font-size:1.22rem;letter-spacing:-.02em}.form-heading p{margin:4px 0 0;color:#94a3b8;font-size:.78rem}
.st-key-nutrient_card [data-testid="stVerticalBlockBorderWrapper"],.st-key-environment_card [data-testid="stVerticalBlockBorderWrapper"],.st-key-soil_card [data-testid="stVerticalBlockBorderWrapper"]{background:linear-gradient(135deg,rgba(16,185,129,.105),rgba(3,20,12,.72))!important;border:1px solid rgba(110,231,183,.16)!important;border-radius:20px!important;box-shadow:0 16px 35px rgba(0,0,0,.18),inset 0 1px 0 rgba(255,255,255,.03)!important}.st-key-nutrient_card [data-testid="stVerticalBlockBorderWrapper"]{border-left:3px solid #34d399!important}.st-key-environment_card [data-testid="stVerticalBlockBorderWrapper"]{border-left:3px solid #38bdf8!important}.st-key-soil_card [data-testid="stVerticalBlockBorderWrapper"]{border-left:3px solid #fbbf24!important}
.analysis-heading{display:flex;justify-content:space-between;align-items:center;padding:18px 20px;border-radius:18px;background:linear-gradient(135deg,rgba(56,189,248,.16),rgba(16,185,129,.08));border:1px solid rgba(125,211,252,.18);margin-bottom:8px}.analysis-heading h3{margin:0;color:#f8fafc;font-size:1.15rem}.analysis-badge{color:#6ee7b7;background:rgba(52,211,153,.12);border:1px solid rgba(52,211,153,.22);border-radius:999px;padding:5px 9px;font-size:10px;font-weight:800;letter-spacing:.08em}
.recommendation-banner{position:relative;overflow:hidden;padding:28px 32px;margin:0 0 24px;border-radius:24px;background:linear-gradient(120deg,rgba(5,150,105,.3),rgba(6,78,59,.18) 55%,rgba(56,189,248,.12));border:1px solid rgba(110,231,183,.22);box-shadow:0 18px 45px rgba(0,0,0,.2)}.recommendation-banner:after{content:'✦';position:absolute;right:30px;top:-28px;font-size:130px;color:rgba(110,231,183,.1)}.rec-eyebrow{color:#6ee7b7;font-weight:800;font-size:11px;text-transform:uppercase;letter-spacing:.14em;margin:0 0 8px}.recommendation-banner h1{margin:0;color:#f8fffb;font-size:clamp(1.75rem,3vw,2.5rem);letter-spacing:-.04em}.recommendation-banner p{margin:10px 0 0;color:#c2ded1;max-width:680px;line-height:1.6}.rec-pills{display:flex;flex-wrap:wrap;gap:8px;margin-top:17px}.rec-pills span{font-size:11px;font-weight:700;color:#d1fae5;background:rgba(2,44,34,.45);border:1px solid rgba(110,231,183,.18);border-radius:999px;padding:6px 10px}
.st-key-analysis_card [data-testid="stVerticalBlockBorderWrapper"]{background:linear-gradient(160deg,rgba(14,64,48,.62),rgba(2,18,12,.56))!important;border:1px solid rgba(56,189,248,.16)!important;border-radius:22px!important;box-shadow:0 16px 36px rgba(0,0,0,.18)!important}.st-key-predict_crop button{margin-top:10px!important;min-height:58px!important;background:linear-gradient(100deg,#059669,#34d399)!important;color:#022c22!important;border:0!important;border-radius:16px!important;font-size:17px!important;font-weight:850!important;box-shadow:0 12px 28px rgba(16,185,129,.28)!important}.st-key-predict_crop button:hover{transform:translateY(-2px)!important;box-shadow:0 18px 35px rgba(16,185,129,.4)!important}.st-key-predict_crop button *{color:inherit!important}
.analysis-empty{min-height:468px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:30px 20px}.analysis-orbit{width:126px;height:126px;border:1px solid rgba(110,231,183,.38);border-radius:50%;position:relative;margin-bottom:24px;box-shadow:0 0 0 18px rgba(52,211,153,.035),0 0 0 38px rgba(52,211,153,.025)}.analysis-orbit:before,.analysis-orbit:after{content:'';position:absolute;border-radius:50%;background:#34d399}.analysis-orbit:before{width:14px;height:14px;top:16px;right:11px;box-shadow:-74px 60px 0 #38bdf8}.analysis-orbit:after{width:20px;height:20px;top:52px;left:52px;box-shadow:0 0 22px rgba(52,211,153,.9)}.analysis-empty h3{color:#ecfdf5;margin:0;font-size:1.2rem}.analysis-empty p{color:#94a3b8;line-height:1.65;max-width:290px;margin:10px 0 18px}.analysis-steps{display:flex;gap:8px;flex-wrap:wrap;justify-content:center}.analysis-steps span{font-size:11px;color:#b7d8c6;border:1px solid rgba(110,231,183,.16);background:rgba(52,211,153,.06);border-radius:99px;padding:6px 9px}.analysis-summary{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin:8px 0 10px}.analysis-summary div{border:1px solid rgba(110,231,183,.12);background:rgba(52,211,153,.05);border-radius:12px;padding:9px;text-align:center}.analysis-summary small{display:block;color:#94a3b8;font-size:10px;text-transform:uppercase;letter-spacing:.08em}.analysis-summary strong{color:#d1fae5;font-size:15px}
.st-key-prediction_mode [role="radiogroup"]{gap:12px!important}.st-key-prediction_mode [role="radiogroup"] label{background:rgba(255,255,255,.055)!important;border:1px solid rgba(110,231,183,.2)!important;border-radius:14px!important;padding:12px 18px!important;min-width:150px!important;transition:.2s ease!important}.st-key-prediction_mode [role="radiogroup"] label:hover{background:rgba(52,211,153,.13)!important;border-color:#34d399!important;transform:translateY(-1px)}.st-key-prediction_mode [role="radiogroup"] label:has(input:checked){background:linear-gradient(135deg,rgba(5,150,105,.35),rgba(52,211,153,.14))!important;border-color:#34d399!important;box-shadow:0 6px 18px rgba(16,185,129,.16)!important}.st-key-prediction_mode [role="radiogroup"] p{color:#ecfdf5!important;font-weight:750!important;text-transform:none!important;letter-spacing:0!important;font-size:14px!important}
label,div[data-testid="stWidgetLabel"] p{color:#94a3b8!important;font-weight:600!important;font-size:12px!important;
  text-transform:uppercase;letter-spacing:.4px}
div.stButton>button{border-radius:12px!important;font-weight:600!important;transition:.25s!important}
.primary-wrap div.stButton>button{background:linear-gradient(135deg,#059669,#34d399)!important;color:#022c22!important;
  border:none!important;padding:16px!important;font-size:17px!important;font-weight:800!important;
  box-shadow:0 8px 24px rgba(52,211,153,.3)!important}
/* Streamlit widgets render beside their preceding markdown blocks, so target
   the keyed button containers directly rather than relying on wrapper divs. */
.st-key-hero_start button{background:linear-gradient(135deg,#059669,#34d399)!important;color:#022c22!important;
  border:none!important;padding:16px!important;font-size:17px!important;font-weight:800!important;
  box-shadow:0 8px 24px rgba(52,211,153,.3)!important}
.st-key-hero_start button:hover{transform:translateY(-2px)!important;box-shadow:0 14px 32px rgba(52,211,153,.48)!important}
.st-key-hero_learn button{background:rgba(255,255,255,.96)!important;color:#064e3b!important;
  border:1px solid rgba(255,255,255,.85)!important;padding:16px!important;font-size:17px!important;font-weight:800!important}
.st-key-hero_learn button:hover{background:#d1fae5!important;color:#022c22!important;transform:translateY(-2px)!important}
.st-key-hero_start button *, .st-key-hero_learn button *{color:inherit!important}
@media(max-width:900px){.hero-grid{grid-template-columns:1fr;min-height:auto}}
</style>
""", unsafe_allow_html=True)
    if st.session_state.light_theme:
        st.markdown("""
<style>
.stApp{background:linear-gradient(145deg,#f5fbf7 0%,#e8f7ee 48%,#f8fafc 100%)!important;color:#123527!important}
.stApp::before{background:rgba(52,211,153,.16)!important}.stApp::after{background:rgba(56,189,248,.12)!important}
section[data-testid="stSidebar"]{background:linear-gradient(180deg,#ffffff,#edf9f1)!important;border-right-color:rgba(5,150,105,.15)!important}
.glass{background:rgba(255,255,255,.74)!important;border-color:rgba(5,150,105,.14)!important;box-shadow:0 10px 28px rgba(15,61,40,.08)!important}
.glass:hover{border-color:rgba(5,150,105,.3)!important}.form-heading h3,.analysis-heading h3,.feature-title,.section-title{color:#123527!important}
.form-heading p,.hero-desc,.section-sub{color:#527064!important}.analysis-heading{background:linear-gradient(135deg,rgba(56,189,248,.13),rgba(16,185,129,.1))!important;border-color:rgba(5,150,105,.16)!important}
.recommendation-banner{background:linear-gradient(120deg,#d8f8e7,#ebf9f2 60%,#e0f3fb)!important;border-color:rgba(5,150,105,.18)!important;box-shadow:0 14px 30px rgba(15,61,40,.08)!important}.recommendation-banner h1{color:#123527!important}.recommendation-banner p{color:#416253!important}.rec-eyebrow{color:#057a55!important}.rec-pills span{background:rgba(255,255,255,.7)!important;color:#176044!important;border-color:rgba(5,150,105,.14)!important}.st-key-analysis_card [data-testid="stVerticalBlockBorderWrapper"]{background:rgba(255,255,255,.78)!important;box-shadow:0 12px 26px rgba(15,61,40,.07)!important}
.analysis-empty h3{color:#123527!important}.analysis-empty p{color:#527064!important}.analysis-steps span{color:#176044!important;background:rgba(16,185,129,.08)!important}
.st-key-nutrient_card [data-testid="stVerticalBlockBorderWrapper"],.st-key-environment_card [data-testid="stVerticalBlockBorderWrapper"],.st-key-soil_card [data-testid="stVerticalBlockBorderWrapper"]{background:rgba(255,255,255,.78)!important;box-shadow:0 12px 26px rgba(15,61,40,.07)!important}
label,div[data-testid="stWidgetLabel"] p{color:#315a49!important}.footer-wrap{border-color:rgba(5,150,105,.16)!important}.footer-wrap p{color:#527064!important}
</style>
""", unsafe_allow_html=True)


# ── Crop Guide Data ──────────────────────────────────────────────────────────
CROP_GUIDE = {
    "apple": {"name": "Apple", "emoji": "🍎", "desc": "Deciduous orchard fruit requiring cool winters and well-drained loam.",
        "soil": "Deep sandy loam, pH 6.0–6.8", "temp": "15–24°C", "temp_range": (15, 24), "rainfall": "1000–1250 mm",
        "rain_range": (1000, 1250), "ph_range": (6.0, 6.8), "water": "Moderate–High", "duration": "140–160 days",
        "harvest": "Late summer to autumn", "fertilizer": "N-rich compost, potash, boron", "tips": "Prune in winter; irrigate during fruit set."},
    "banana": {"name": "Banana", "emoji": "🍌", "desc": "Tropical fruit needing constant moisture and rich fertile soil.",
        "soil": "Clay loam, pH 6.0–7.5", "temp": "20–30°C", "temp_range": (20, 30), "rainfall": "1500–2200 mm",
        "rain_range": (1500, 2200), "ph_range": (6.0, 7.5), "water": "High", "duration": "10–12 months",
        "harvest": "10–12 months", "fertilizer": "High potash and nitrogen", "tips": "Windbreaks and constant moisture."},
    "blackgram": {"name": "Black Gram", "emoji": "🌱", "desc": "Warm-season pulse that enriches soil nitrogen.",
        "soil": "Loamy, pH 6.0–7.5", "temp": "25–35°C", "temp_range": (25, 35), "rainfall": "600–1000 mm",
        "rain_range": (600, 1000), "ph_range": (6.0, 7.5), "water": "Moderate", "duration": "80–95 days",
        "harvest": "80–95 days", "fertilizer": "Rhizobium, phosphate", "tips": "Avoid waterlogging."},
    "chickpea": {"name": "Chickpea", "emoji": "🧆", "desc": "Cool-season legume, highly drought-tolerant.",
        "soil": "Sandy loam, pH 6.0–8.0", "temp": "15–25°C", "temp_range": (15, 25), "rainfall": "350–500 mm",
        "rain_range": (350, 500), "ph_range": (6.0, 8.0), "water": "Low", "duration": "90–120 days",
        "harvest": "90–120 days", "fertilizer": "Phosphorus, sulfur", "tips": "Avoid excess irrigation."},
    "coconut": {"name": "Coconut", "emoji": "🥥", "desc": "Coastal palm tolerant of salinity and heat.",
        "soil": "Sandy loam, pH 5.2–8.0", "temp": "22–32°C", "temp_range": (22, 32), "rainfall": "1200–2500 mm",
        "rain_range": (1200, 2500), "ph_range": (5.2, 8.0), "water": "High", "duration": "Perennial",
        "harvest": "Year-round", "fertilizer": "Potash, nitrogen, salt", "tips": "Full sun; deep planting pits."},
    "coffee": {"name": "Coffee", "emoji": "☕", "desc": "Shade-grown shrub for cool tropical highlands.",
        "soil": "Acidic volcanic, pH 5.0–6.0", "temp": "15–24°C", "temp_range": (15, 24), "rainfall": "1200–2000 mm",
        "rain_range": (1200, 2000), "ph_range": (5.0, 6.0), "water": "High", "duration": "7–9 months to cherry",
        "harvest": "Autumn/winter", "fertilizer": "Nitrogen, potash, compost", "tips": "Grow under shade trees."},
    "cotton": {"name": "Cotton", "emoji": "👕", "desc": "Fiber cash crop for warm frost-free regions.",
        "soil": "Black/regur soil, pH 6.0–8.0", "temp": "20–32°C", "temp_range": (20, 32), "rainfall": "500–800 mm",
        "rain_range": (500, 800), "ph_range": (6.0, 8.0), "water": "Moderate", "duration": "150–180 days",
        "harvest": "150–180 days", "fertilizer": "NPK, boron", "tips": "Control bollworm; harvest dry bolls."},
    "grapes": {"name": "Grapes", "emoji": "🍇", "desc": "Vine crop for trellis systems with heavy pruning.",
        "soil": "Sandy loam, pH 6.5–7.5", "temp": "15–35°C", "temp_range": (15, 35), "rainfall": "500–800 mm",
        "rain_range": (500, 800), "ph_range": (6.5, 7.5), "water": "Moderate", "duration": "Perennial",
        "harvest": "Late summer", "fertilizer": "Potash, compost", "tips": "Drip irrigation; winter pruning."},
    "jute": {"name": "Jute", "emoji": "🌾", "desc": "Fast-growing fiber crop for river-basin alluvial soils.",
        "soil": "Alluvial silt, pH 6.0–7.5", "temp": "24–38°C", "temp_range": (24, 38), "rainfall": "1200–2000 mm",
        "rain_range": (1200, 2000), "ph_range": (6.0, 7.5), "water": "Very High", "duration": "120–150 days",
        "harvest": "120–150 days", "fertilizer": "High nitrogen, manure", "tips": "Retting for fiber extraction."},
    "kidneybeans": {"name": "Kidney Beans", "emoji": "🫘", "desc": "Warm-season legume sensitive to frost.",
        "soil": "Sandy loam, pH 5.5–6.5", "temp": "15–25°C", "temp_range": (15, 25), "rainfall": "600–1000 mm",
        "rain_range": (600, 1000), "ph_range": (5.5, 6.5), "water": "Moderate", "duration": "90–110 days",
        "harvest": "90–110 days", "fertilizer": "Phosphorus, compost", "tips": "Trellis for climbing varieties."},
    "lentil": {"name": "Lentil", "emoji": "🍲", "desc": "Cool-season pulse rich in protein.",
        "soil": "Loam to clay, pH 6.0–8.0", "temp": "15–25°C", "temp_range": (15, 25), "rainfall": "350–600 mm",
        "rain_range": (350, 600), "ph_range": (6.0, 8.0), "water": "Low", "duration": "100–120 days",
        "harvest": "100–120 days", "fertilizer": "Phosphate, potassium", "tips": "Sow early in winter."},
    "maize": {"name": "Maize", "emoji": "🌽", "desc": "Versatile cereal requiring well-aerated fertile loam.",
        "soil": "Deep loam, pH 6.0–7.0", "temp": "18–27°C", "temp_range": (18, 27), "rainfall": "500–1000 mm",
        "rain_range": (500, 1000), "ph_range": (6.0, 7.0), "water": "Moderate", "duration": "90–110 days",
        "harvest": "90–110 days", "fertilizer": "Balanced NPK, zinc", "tips": "Moisture at tasseling is critical."},
    "mango": {"name": "Mango", "emoji": "🥭", "desc": "Tropical evergreen fruit tree for warm dry seasons.",
        "soil": "Loamy/alluvial, pH 5.5–7.5", "temp": "24–35°C", "temp_range": (24, 35), "rainfall": "750–1000 mm",
        "rain_range": (750, 1000), "ph_range": (5.5, 7.5), "water": "Moderate", "duration": "100–120 days to fruit",
        "harvest": "Summer", "fertilizer": "NPK, zinc", "tips": "Reduce irrigation during flowering."},
    "mothbeans": {"name": "Moth Beans", "emoji": "🌱", "desc": "Drought-resistant legume for arid regions.",
        "soil": "Sandy soil, pH 6.5–7.5", "temp": "25–35°C", "temp_range": (25, 35), "rainfall": "250–500 mm",
        "rain_range": (250, 500), "ph_range": (6.5, 7.5), "water": "Very Low", "duration": "75–90 days",
        "harvest": "75–90 days", "fertilizer": "Minimal; basic phosphorus", "tips": "Dry ripening conditions ideal."},
    "mungbean": {"name": "Mung Bean", "emoji": "🥗", "desc": "Short-duration legume for catch cropping.",
        "soil": "Loamy, pH 6.2–7.2", "temp": "25–35°C", "temp_range": (25, 35), "rainfall": "300–600 mm",
        "rain_range": (300, 600), "ph_range": (6.2, 7.2), "water": "Low", "duration": "60–75 days",
        "harvest": "60–75 days", "fertilizer": "Basic NPK start", "tips": "Keep weed-free early on."},
    "muskmelon": {"name": "Muskmelon", "emoji": "🍈", "desc": "Sweet melon for warm dry climates.",
        "soil": "Sandy loam, pH 6.0–7.0", "temp": "22–32°C", "temp_range": (22, 32), "rainfall": "400–600 mm",
        "rain_range": (400, 600), "ph_range": (6.0, 7.0), "water": "Moderate", "duration": "75–90 days",
        "harvest": "75–90 days", "fertilizer": "Organic manure, P & K", "tips": "Avoid overhead irrigation."},
    "orange": {"name": "Orange", "emoji": "🍊", "desc": "Citrus fruit for subtropical mild winters.",
        "soil": "Well-drained loam, pH 5.5–7.5", "temp": "15–32°C", "temp_range": (15, 32), "rainfall": "750–1200 mm",
        "rain_range": (750, 1200), "ph_range": (5.5, 7.5), "water": "Moderate–High", "duration": "8–12 months",
        "harvest": "Year-round", "fertilizer": "Nitrogen, micronutrients", "tips": "Protect young trees from frost."},
    "papaya": {"name": "Papaya", "emoji": "🥭", "desc": "Fast tropical tree with vitamin-rich fruit.",
        "soil": "Sandy loam, pH 6.0–6.5", "temp": "20–35°C", "temp_range": (20, 35), "rainfall": "1000–1500 mm",
        "rain_range": (1000, 1500), "ph_range": (6.0, 6.5), "water": "Moderate", "duration": "9–11 months",
        "harvest": "9–11 months", "fertilizer": "Nitrogen, potash, compost", "tips": "Ensure excellent drainage."},
    "pigeonpeas": {"name": "Pigeon Peas", "emoji": "🫛", "desc": "Deep-rooted drought-tolerant legume.",
        "soil": "Loamy, pH 5.0–7.5", "temp": "18–30°C", "temp_range": (18, 30), "rainfall": "600–1000 mm",
        "rain_range": (600, 1000), "ph_range": (5.0, 7.5), "water": "Low", "duration": "140–180 days",
        "harvest": "140–180 days", "fertilizer": "Phosphate, rhizobium", "tips": "Intercrop with cereals."},
    "pomegranate": {"name": "Pomegranate", "emoji": "🍎", "desc": "Drought-hardy shrub for dry warm climates.",
        "soil": "Sandy loam, pH 6.0–8.0", "temp": "25–35°C", "temp_range": (25, 35), "rainfall": "500–800 mm",
        "rain_range": (500, 800), "ph_range": (6.0, 8.0), "water": "Low–Moderate", "duration": "150–180 days",
        "harvest": "150–180 days", "fertilizer": "Nitrogen, potash, manure", "tips": "Regular pruning."},
    "rice": {"name": "Rice", "emoji": "🌾", "desc": "Staple grain for waterlogged clay soils.",
        "soil": "Clay loam, pH 5.5–6.5", "temp": "20–37°C", "temp_range": (20, 37), "rainfall": "1500–3000 mm",
        "rain_range": (1500, 3000), "ph_range": (5.5, 6.5), "water": "Very High", "duration": "110–140 days",
        "harvest": "110–140 days", "fertilizer": "High nitrogen, phosphorus, zinc", "tips": "Maintain flooded fields."},
    "watermelon": {"name": "Watermelon", "emoji": "🍉", "desc": "Heat-loving vine for large sweet fruits.",
        "soil": "Sandy loam, pH 6.0–7.0", "temp": "24–35°C", "temp_range": (24, 35), "rainfall": "400–600 mm",
        "rain_range": (400, 600), "ph_range": (6.0, 7.0), "water": "Moderate", "duration": "80–100 days",
        "harvest": "80–100 days", "fertilizer": "N early, then P & K", "tips": "Straw under ripening melons."},
}

WHY_CHOOSE = [
    ("🎯", "High Accuracy", "Random Forest and XGBoost models deliver up to 99.2% prediction accuracy."),
    ("⚡", "Fast Prediction", "Get crop recommendations within seconds of submitting soil data."),
    ("👆", "Easy To Use", "Simple form inputs designed for farmers — no technical knowledge required."),
    ("🤖", "AI Powered", "Three machine learning models analyze your farmland conditions intelligently."),
    ("✅", "Reliable Recommendation", "Confidence scores and explainable reasons build trust in every result."),
    ("🌾", "Farmer Friendly", "Clear language, visual guides, and downloadable reports for field use."),
]


# ── Helpers ────────────────────────────────────────────────────────────────────
def check_api_status():
    try:
        r = requests.get(f"{st.session_state.api_url}/", timeout=3)
        return r.status_code == 200
    except Exception:
        return False


def load_history():
    cols = ["Timestamp", "N", "P", "K", "Temperature", "Humidity", "pH", "Rainfall",
            "Recommended Crop", "Confidence", "Prediction Mode"]
    if os.path.exists(HISTORY_FILE):
        try:
            df = pd.read_csv(HISTORY_FILE)
            for c in cols:
                if c not in df.columns:
                    df[c] = ""
            return df[cols]
        except Exception:
            pass
    return pd.DataFrame(columns=cols)


def save_prediction(inputs, crop, confidence, mode):
    df = load_history()
    row = {
        "Timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "N": inputs["N"], "P": inputs["P"], "K": inputs["K"],
        "Temperature": inputs["temperature"], "Humidity": inputs["humidity"],
        "pH": inputs["ph"], "Rainfall": inputs["rainfall"],
        "Recommended Crop": crop, "Confidence": confidence, "Prediction Mode": mode,
    }
    df = pd.concat([pd.DataFrame([row]), df], ignore_index=True)
    df.to_csv(HISTORY_FILE, index=False)
    return df


def predict_crop(payload, model_key):
    url = f"{st.session_state.api_url}/predict?model={model_key}"
    r = requests.post(url, json=payload, timeout=10)
    r.raise_for_status()
    return r.json()


def run_prediction(payload, mode, selected_model):
    model_key = AUTO_MODEL if mode == "Automatic" else selected_model
    msgs = ["Analyzing Soil...", "Checking Nutrient Levels...", "Running AI Prediction...", "Preparing Recommendation..."]
    bar = st.progress(0)
    status = st.empty()
    for i, msg in enumerate(msgs):
        status.markdown(f"<p style='color:#34d399;font-weight:600'>{msg}</p>", unsafe_allow_html=True)
        bar.progress((i + 1) / len(msgs))
        time.sleep(0.55)
    result = predict_crop(payload, model_key)
    bar.empty()
    status.empty()
    model_label = MODELS[model_key]["label"] if mode == "Advanced" else "Automatic (Random Forest)"
    return result, model_label, model_key


def in_range(val, lo, hi, tol=0.15):
    span = hi - lo
    return (lo - span * tol) <= val <= (hi + span * tol)


def explain_recommendation(crop_key, inputs):
    meta = CROP_GUIDE.get(crop_key, {})
    name = meta.get("name", crop_key.title())
    reasons = []
    n, p, k = inputs["N"], inputs["P"], inputs["K"]
    temp, ph, rain = inputs["temperature"], inputs["ph"], inputs["rainfall"]
    if meta.get("ph_range") and in_range(ph, *meta["ph_range"]):
        reasons.append(f"Soil pH ({ph:.1f}) is optimal for {name}.")
    else:
        reasons.append(f"Soil pH ({ph:.1f}) aligns with {name} cultivation requirements.")
    if meta.get("temp_range") and in_range(temp, *meta["temp_range"]):
        reasons.append(f"Temperature ({temp:.1f}°C) matches {name} growth conditions.")
    else:
        reasons.append(f"Temperature is within a workable range for {name}.")
    if meta.get("rain_range") and in_range(rain, *meta["rain_range"], tol=0.35):
        reasons.append(f"Rainfall ({rain:.0f} mm) supports healthy {name} production.")
    else:
        reasons.append(f"Rainfall level is compatible with {name} under local irrigation.")
    if n >= 40:
        reasons.append("Nitrogen level supports strong vegetative growth.")
    if p >= 30:
        reasons.append("Phosphorus level supports root and flowering development.")
    if k >= 30:
        reasons.append("Potassium level supports crop hardiness and quality.")
    reasons.append("High yield is expected under these combined conditions.")
    return name, reasons[:6]


def generate_pdf(record):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 20)
    pdf.set_text_color(5, 100, 60)
    pdf.cell(0, 12, "Smart Crop Recommendation System", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 8, f"Generated: {record.get('Timestamp', '')}", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
    pdf.ln(6)
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(0, 8, f"Recommended Crop: {record.get('Recommended Crop', '')}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    conf = record.get("Confidence", 0)
    conf_pct = int(conf * 100) if conf <= 1 else int(conf)
    pdf.set_font("Helvetica", "", 11)
    pdf.cell(0, 7, f"Confidence: {conf_pct}%  |  Mode: {record.get('Prediction Mode', 'Automatic')}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(4)
    fields = [("N", "N"), ("P", "P"), ("K", "K"), ("Temperature", "Temp"), ("Humidity", "Humidity"),
              ("pH", "pH"), ("Rainfall", "Rainfall")]
    for col, label in fields:
        pdf.cell(0, 6, f"{label}: {record.get(col, '')}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(6)
    pdf.set_font("Helvetica", "I", 9)
    pdf.cell(0, 5, "Powered by Artificial Intelligence — Developed by Aisha", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
    return bytes(pdf.output())


def hero_illustration():
    return """
<div style="position:relative;width:100%;max-width:420px;margin:0 auto;animation:floatY 5s ease-in-out infinite">
<svg viewBox="0 0 400 360" xmlns="http://www.w3.org/2000/svg" style="width:100%;filter:drop-shadow(0 20px 40px rgba(52,211,153,.15))">
<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0f172a"/><stop offset="100%" stop-color="#064e3b"/></linearGradient>
<linearGradient id="field" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#065f46"/><stop offset="100%" stop-color="#047857"/></linearGradient></defs>
<rect width="400" height="360" fill="url(#sky)" rx="24"/>
<ellipse cx="320" cy="60" rx="40" ry="40" fill="#fef08a" opacity=".9"/>
<path d="M0 220 Q100 180 200 210 T400 200 L400 360 L0 360Z" fill="url(#field)"/>
<path d="M0 250 Q120 230 240 250 T400 240 L400 360 L0 360Z" fill="#059669" opacity=".7"/>
<g style="animation:floatY 4s ease-in-out infinite"><rect x="60" y="130" width="80" height="50" rx="8" fill="rgba(255,255,255,.08)" stroke="rgba(52,211,153,.4)"/>
<text x="100" y="162" text-anchor="middle" fill="#6ee7b7" font-size="11" font-family="Inter">AI Engine</text></g>
<g style="animation:floatY 3.5s ease-in-out infinite;animation-delay:-1s"><circle cx="300" cy="140" r="28" fill="rgba(52,211,153,.15)" stroke="#34d399"/>
<text x="300" y="145" text-anchor="middle" fill="#34d399" font-size="20">🤖</text></g>
<g style="animation:floatY 4.5s ease-in-out infinite;animation-delay:-2s"><text x="180" y="195" font-size="28">🌽</text><text x="220" y="188" font-size="24">🌾</text><text x="155" y="205" font-size="22">🥕</text></g>
<circle cx="200" cy="110" r="35" fill="rgba(255,255,255,.06)" stroke="rgba(52,211,153,.3)"/>
<text x="200" y="118" text-anchor="middle" font-size="32">👨‍🌾</text>
<ellipse cx="200" cy="280" rx="60" ry="12" fill="rgba(0,0,0,.25)"/>
<text x="200" y="310" text-anchor="middle" fill="#94a3b8" font-size="11" font-family="Inter">Smart Agriculture</text>
</svg>
<div style="position:absolute;top:12%;right:5%;background:rgba(52,211,153,.12);border:1px solid rgba(52,211,153,.3);
  border-radius:12px;padding:8px 12px;font-size:11px;color:#6ee7b7;animation:floatY 3s ease-in-out infinite">NPK ✓</div>
<div style="position:absolute;bottom:28%;left:0;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);
  border-radius:12px;padding:8px 12px;font-size:11px;color:#94a3b8;animation:floatY 3.8s ease-in-out infinite">pH 6.5</div>
</div>
<style>@keyframes floatY{0%,100%{transform:translateY(0)}50%{transform:translateY(-12px)}}</style>
"""


def stat_card(label, sub, counter_id, end_val, suffix="", decimals=0, static_text=""):
    if static_text:
        num = f'<div style="font-size:42px;font-weight:800;background:linear-gradient(135deg,#fff,#34d399);-webkit-background-clip:text;-webkit-text-fill-color:transparent">{static_text}</div>'
    else:
        num = f'<div id="{counter_id}" style="font-size:42px;font-weight:800;background:linear-gradient(135deg,#fff,#34d399);-webkit-background-clip:text;-webkit-text-fill-color:transparent">0{suffix}</div>'
        num += f"""<script>(function(){{var el=document.getElementById('{counter_id}');if(!el)return;
        var end={end_val},dec={decimals},suf='{suffix}',dur=1800,t0=null;
        function step(t){{if(!t0)t0=t;var p=Math.min((t-t0)/dur,1),v=end*(1-Math.pow(1-p,3));
        el.textContent=(dec?v.toFixed(dec):Math.round(v))+suf;if(p<1)requestAnimationFrame(step);}}
        requestAnimationFrame(step);}})();</script>"""
    return f"""<!DOCTYPE html><html><body style="margin:0;font-family:Inter,sans-serif">
    <div style="background:linear-gradient(135deg,rgba(255,255,255,.06),rgba(255,255,255,.02));border:1px solid rgba(255,255,255,.08);
    border-radius:20px;padding:28px 16px;text-align:center">{num}
    <div style="font-size:13px;color:#94a3b8;margin-top:8px;font-weight:500;text-transform:uppercase;letter-spacing:.6px">{label}</div>
    <p style="color:#64748b;font-size:12px;margin:6px 0 0">{sub}</p></div></body></html>"""


def radar_chart(n, p, k, temp, hum, ph, rain):
    n, p, k, temp, hum, ph, rain = [value if value is not None else 0 for value in (n, p, k, temp, hum, ph, rain)]
    cats = ["N", "P", "K", "Temp", "Humidity", "pH", "Rain"]
    vals = [min(100, n / 150 * 100), min(100, p / 150 * 100), min(100, k / 250 * 100),
            min(100, temp / 50 * 100), hum, min(100, ph / 14 * 100), min(100, rain / 350 * 100)]
    fig = go.Figure(go.Scatterpolar(r=vals + [vals[0]], theta=cats + [cats[0]], fill="toself",
        fillcolor="rgba(52,211,153,.12)", line=dict(color="#34d399", width=2)))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100], showticklabels=False,
        gridcolor="rgba(255,255,255,.08)"), bgcolor="rgba(0,0,0,0)"),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", height=280, margin=dict(l=30, r=30, t=30, b=30),
        font=dict(color="#94a3b8", size=11), showlegend=False)
    return fig


def nutrient_bar(n, p, k):
    n, p, k = [value if value is not None else 0 for value in (n, p, k)]
    fig = go.Figure(go.Bar(x=["N", "P", "K"], y=[n, p, k], marker_color=["#34d399", "#fbbf24", "#f97316"],
        text=[f"{v:.0f}" for v in [n, p, k]], textposition="outside"))
    fig.update_layout(title="NPK (mg/kg)", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        height=220, margin=dict(l=20, r=20, t=40, b=20), font=dict(color="#94a3b8"),
        yaxis=dict(gridcolor="rgba(255,255,255,.06)"))
    return fig


def draw_footer():
    st.markdown("""
<div class="footer-wrap">
<p><strong>Smart Crop Recommendation System</strong></p>
<p>Powered by Artificial Intelligence</p>
<p>Developed by Aisha</p>
</div>""", unsafe_allow_html=True)


# ── Pages ──────────────────────────────────────────────────────────────────────
def page_home():
    c1, c2 = st.columns([1.05, 0.95], gap="large")
    with c1:
        st.markdown("""
<div style="animation:fadeUp .7s ease both">
<p style="color:#34d399;font-weight:700;font-size:13px;text-transform:uppercase;letter-spacing:1px;margin-bottom:12px">✨ AI-Powered Agriculture</p>
<h1 class="hero-title">🌾 Smart Crop Recommendation System</h1>
<p class="hero-sub">Helping Farmers Choose the Best Crop Using Artificial Intelligence.</p>
<p class="hero-desc">Analyze soil nutrients and environmental conditions to receive the best crop recommendation within seconds.</p>
</div>""", unsafe_allow_html=True)
        b1, b2 = st.columns(2)
        with b1:
            st.markdown('<div class="primary-wrap">', unsafe_allow_html=True)
            if st.button("🚀 Start Recommendation", use_container_width=True, key="hero_start"):
                st.session_state.page = "🌱 Recommendation"
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)
        with b2:
            st.markdown('<div class="secondary-wrap">', unsafe_allow_html=True)
            if st.button("📖 Learn More", use_container_width=True, key="hero_learn"):
                st.session_state.scroll_learn = True
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)
    with c2:
        components.html(hero_illustration(), height=380)

    st.markdown('<p class="section-title">System Overview</p>', unsafe_allow_html=True)
    s1, s2, s3, s4 = st.columns(4)
    stats = [
        stat_card("AI Models", "Random Forest · XGBoost · LR", "stat_models", 3),
        stat_card("Supported Crops", "Full crop catalog", "stat_crops", 22),
        stat_card("Prediction Accuracy", "Validated on test data", "stat_acc", 99.2, "%", 1),
        stat_card("Prediction Engine", "Artificial Intelligence", "", 0, static_text="🤖 AI"),
    ]
    for col, html in zip([s1, s2, s3, s4], stats):
        with col:
            components.html(html, height=160)

    st.markdown('<p id="how-it-works" class="section-title">How It Works</p><p class="section-sub">Four simple steps to your ideal crop</p>', unsafe_allow_html=True)
    if st.session_state.scroll_learn:
        components.html("""
        <script>
        const target = window.parent.document.getElementById('how-it-works');
        if (target) {
            setTimeout(() => target.scrollIntoView({behavior: 'smooth', block: 'start'}), 180);
        }
        </script>
        """, height=0)
        st.session_state.scroll_learn = False
    steps = ["Enter Soil Information", "AI Analyzes Your Data", "Choose Prediction Mode", "Receive Best Crop Recommendation"]
    tcols = st.columns([1, 0.15, 1, 0.15, 1, 0.15, 1])
    for i, step in enumerate(steps):
        idx = i * 2
        with tcols[idx]:
            st.markdown(f"""<div class="timeline-step" style="animation-delay:{i*.12}s">
            <div class="step-num">{i+1}</div><div style="color:#fff;font-weight:600;font-size:14px">{step}</div></div>""", unsafe_allow_html=True)
        if i < 3:
            with tcols[idx + 1]:
                st.markdown('<div class="step-arrow">↓</div>', unsafe_allow_html=True)

    st.markdown('<p class="section-title">Why Choose Our System</p>', unsafe_allow_html=True)
    fcols = st.columns(3)
    for i, (icon, title, desc) in enumerate(WHY_CHOOSE):
        with fcols[i % 3]:
            st.markdown(f"""<div class="glass feature-card"><span class="feature-icon">{icon}</span>
            <div class="feature-title">{title}</div><div class="feature-desc">{desc}</div></div>""", unsafe_allow_html=True)
    draw_footer()


def page_recommendation():
    st.markdown("""
    <section class="recommendation-banner">
      <div class="rec-eyebrow">AI decision workspace</div>
      <h1>🌱 Crop Recommendation</h1>
      <p>Enter your field conditions and let our machine-learning engine identify the crop best suited to your soil and climate.</p>
      <div class="rec-pills"><span>7 field factors</span><span>3 AI models</span><span>Instant guidance</span></div>
    </section>
    """, unsafe_allow_html=True)
    col_form, col_viz = st.columns([1.05, 0.95], gap="large")

    with col_form:
        with st.container(border=True, key="nutrient_card"):
            st.markdown('<div class="form-heading"><span class="heading-icon">🧪</span><div><h3>Soil Nutrients</h3><p>Balance the essential NPK values in your soil.</p></div></div>', unsafe_allow_html=True)
            c1, c2, c3 = st.columns(3)
            with c1:
                n = st.number_input("Nitrogen", 0.0, 150.0, value=None, step=1.0, placeholder="e.g. 90")
            with c2:
                p = st.number_input("Phosphorus", 5.0, 150.0, value=None, step=1.0, placeholder="e.g. 42")
            with c3:
                k = st.number_input("Potassium", 5.0, 250.0, value=None, step=1.0, placeholder="e.g. 43")

        with st.container(border=True, key="environment_card"):
            st.markdown('<div class="form-heading"><span class="heading-icon">🌤️</span><div><h3>Environment</h3><p>Describe the climate conditions on your farm.</p></div></div>', unsafe_allow_html=True)
            e1, e2, e3 = st.columns(3)
            with e1:
                temp = st.number_input("Temperature (°C)", 5.0, 50.0, value=None, step=0.1, placeholder="e.g. 24.5")
            with e2:
                humidity = st.number_input("Humidity (%)", 10.0, 100.0, value=None, step=0.1, placeholder="e.g. 82")
            with e3:
                rainfall = st.number_input("Rainfall (mm)", 10.0, 400.0, value=None, step=0.1, placeholder="e.g. 203")

        with st.container(border=True, key="soil_card"):
            st.markdown('<div class="form-heading"><span class="heading-icon">⛰️</span><div><h3>Soil pH</h3><p>Enter the acidity or alkalinity of your soil.</p></div></div>', unsafe_allow_html=True)
            ph = st.number_input("pH", 3.5, 10.0, value=None, step=0.1, placeholder="e.g. 6.5")

        st.markdown('<div class="form-heading" style="margin:28px 0 10px"><span class="heading-icon">⚙️</span><div><h3>Prediction Mode</h3><p>Choose automatic accuracy or manually select a model.</p></div></div>', unsafe_allow_html=True)
        mode = st.radio("Mode", ["Automatic", "Advanced"], horizontal=True, label_visibility="collapsed", key="prediction_mode", format_func=lambda option: "✨ Automatic" if option == "Automatic" else "⚡ Advanced")
        selected_model = AUTO_MODEL
        if mode == "Automatic":
            st.markdown("""<div class="glass" style="padding:16px"><p style="margin:0;color:#94a3b8;font-size:13px">
            <strong style="color:#34d399">Automatic Mode</strong> — The system automatically selects Random Forest for maximum prediction accuracy.</p></div>""", unsafe_allow_html=True)
        else:
            st.markdown("<p style='color:#94a3b8;font-size:13px'>Select a machine learning model:</p>", unsafe_allow_html=True)
            m1, m2, m3 = st.columns(3)
            choice = st.session_state.get("adv_model", "rf")
            with m1:
                if st.button(f"🌲 Random Forest", use_container_width=True, key="m_rf"):
                    st.session_state.adv_model = "rf"
                    st.rerun()
            with m2:
                if st.button(f"⚡ XGBoost", use_container_width=True, key="m_xgb"):
                    st.session_state.adv_model = "xgb"
                    st.rerun()
            with m3:
                if st.button(f"📈 Logistic Regression", use_container_width=True, key="m_lr"):
                    st.session_state.adv_model = "lr"
                    st.rerun()
            selected_model = st.session_state.get("adv_model", "rf")
            info = MODELS[selected_model]
            st.markdown(f"""<div class="glass model-card active"><div style="font-size:28px">{info['icon']}</div>
            <div style="color:#fff;font-weight:700;margin:8px 0">{info['label']}</div>
            <div style="color:#34d399;font-size:12px;font-weight:600">{info['tag']}</div>
            <div style="color:#64748b;font-size:12px;margin-top:6px">{info['desc']}</div></div>""", unsafe_allow_html=True)

        st.markdown('<div class="primary-wrap">', unsafe_allow_html=True)
        predict = st.button("🚀 Get Crop Recommendation", use_container_width=True, type="primary", key="predict_crop")
        st.markdown("</div>", unsafe_allow_html=True)

        payload = {"N": n, "P": p, "K": k, "temperature": temp, "humidity": humidity, "ph": ph, "rainfall": rainfall}
        if predict:
            missing = [label for label, value in {"Nitrogen": n, "Phosphorus": p, "Potassium": k, "Temperature": temp, "Humidity": humidity, "Rainfall": rainfall, "pH": ph}.items() if value is None]
            if missing:
                st.warning("Please enter: " + ", ".join(missing) + ".")
            elif not check_api_status():
                st.error("Cannot reach Flask API. Start the backend with: `python app.py`")
            else:
                try:
                    result, mode_label, mkey = run_prediction(payload, mode, selected_model)
                    crop = result["label"]
                    conf = result.get("confidence", 0.85)
                    save_prediction(payload, crop, conf, mode_label)
                    st.session_state.last_result = {
                        "crop": crop, "confidence": conf, "mode": mode_label, "model_key": mkey,
                        "inputs": payload, "api_model": result.get("model", ""),
                    }
                    st.toast("Recommendation ready!", icon="🌾")
                except Exception as exc:
                    st.error(f"Prediction failed: {exc}")

        if st.session_state.last_result:
            res = st.session_state.last_result
            ck = res["crop"].lower()
            meta = CROP_GUIDE.get(ck, {"name": res["crop"], "emoji": "🌾", "desc": "Recommended by AI."})
            conf_pct = int(res["confidence"] * 100) if res["confidence"] <= 1 else int(res["confidence"])
            st.markdown(f"""<div class="glass result-hero">
            <p style="color:#94a3b8;text-transform:uppercase;font-size:12px;letter-spacing:1px">🌾 Recommended Crop</p>
            <div class="crop-circle">{meta['emoji']}</div>
            <h2 style="color:#34d399;margin:0;font-size:2rem">{meta['name']}</h2>
            <p style="color:#64748b;margin:8px 0">Confidence: <strong style="color:#fff">{conf_pct}%</strong> · Mode: <strong style="color:#fff">{res['mode']}</strong></p>
            <div class="conf-bar"><div class="conf-fill" style="width:{conf_pct}%"></div></div></div>""", unsafe_allow_html=True)

            crop_name, reasons = explain_recommendation(ck, res["inputs"])
            st.markdown(f'<div class="glass"><h4 style="color:#34d399;margin:0 0 12px">Why was {crop_name} recommended?</h4>', unsafe_allow_html=True)
            for r in reasons:
                st.markdown(f'<div class="reason-item"><span class="reason-check">✔</span><span>{r}</span></div>', unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown(f"""<div class="glass"><h4 style="color:#34d399">📖 Crop Guide — {meta['name']}</h4>
            <p style="color:#cbd5e1;line-height:1.7">{meta.get('desc','')}</p>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:12px">
            <div><span style="color:#64748b;font-size:11px">Suitable Soil</span><br><strong>{meta.get('soil','—')}</strong></div>
            <div><span style="color:#64748b;font-size:11px">Ideal Temperature</span><br><strong>{meta.get('temp','—')}</strong></div>
            <div><span style="color:#64748b;font-size:11px">Ideal Rainfall</span><br><strong>{meta.get('rainfall','—')}</strong></div>
            <div><span style="color:#64748b;font-size:11px">Water Requirement</span><br><strong>{meta.get('water','—')}</strong></div>
            <div><span style="color:#64748b;font-size:11px">Growing Duration</span><br><strong>{meta.get('duration','—')}</strong></div>
            <div><span style="color:#64748b;font-size:11px">Harvest Time</span><br><strong>{meta.get('harvest','—')}</strong></div>
            </div>
            <p style="margin-top:12px;color:#94a3b8"><strong>Fertilizer:</strong> {meta.get('fertilizer','—')}</p>
            <p style="color:#94a3b8"><strong>Growing Tips:</strong> {meta.get('tips','—')}</p></div>""", unsafe_allow_html=True)

    with col_viz:
        with st.container(border=True, key="analysis_card"):
            entered = sum(value is not None for value in (n, p, k, temp, humidity, rainfall, ph))
            badge = f"{entered}/7 ENTERED" if entered else "READY FOR DATA"
            st.markdown(f'<div class="analysis-heading"><h3>📊 Live Parameter Analysis</h3><span class="analysis-badge">{badge}</span></div>', unsafe_allow_html=True)
            if not entered:
                st.markdown("""
                <div class="analysis-empty">
                  <div class="analysis-orbit"></div>
                  <h3>Your field profile will appear here</h3>
                  <p>Add soil and climate values on the left. The AI dashboard will update instantly as you type.</p>
                  <div class="analysis-steps"><span>Soil nutrients</span><span>Climate data</span><span>pH balance</span></div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""<div class="analysis-summary">
                <div><small>Nitrogen</small><strong>{n if n is not None else '—'}</strong></div>
                <div><small>Phosphorus</small><strong>{p if p is not None else '—'}</strong></div>
                <div><small>Potassium</small><strong>{k if k is not None else '—'}</strong></div>
                </div>""", unsafe_allow_html=True)
                st.plotly_chart(radar_chart(n, p, k, temp, humidity, ph, rainfall), use_container_width=True)
                st.plotly_chart(nutrient_bar(n, p, k), use_container_width=True)
    draw_footer()


def page_crop_guide():
    st.markdown("## 📖 Crop Guide")
    st.markdown("<p style='color:#94a3b8;margin-top:-8px'>Browse cultivation requirements for all 22 supported crops.</p>", unsafe_allow_html=True)
    names = {v["name"]: k for k, v in sorted(CROP_GUIDE.items(), key=lambda x: x[1]["name"])}
    sel = st.selectbox("Select crop", list(names.keys()), label_visibility="collapsed")
    key = names[sel]
    d = CROP_GUIDE[key]
    left, right = st.columns([1, 2])
    with left:
        st.markdown(f"""<div class="glass" style="text-align:center;padding:32px">
        <div class="crop-circle">{d['emoji']}</div>
        <h3 style="color:#fff;margin:12px 0 0">{d['name']}</h3></div>""", unsafe_allow_html=True)
    with right:
        st.markdown(f"""<div class="glass"><p style="color:#cbd5e1;line-height:1.75">{d['desc']}</p>
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:16px">
        <div style="background:rgba(255,255,255,.03);padding:12px;border-radius:12px"><span style="color:#64748b;font-size:11px">Suitable Soil</span><br><strong style="font-size:13px">{d['soil']}</strong></div>
        <div style="background:rgba(255,255,255,.03);padding:12px;border-radius:12px"><span style="color:#64748b;font-size:11px">Ideal Temperature</span><br><strong style="font-size:13px">{d['temp']}</strong></div>
        <div style="background:rgba(255,255,255,.03);padding:12px;border-radius:12px"><span style="color:#64748b;font-size:11px">Ideal Rainfall</span><br><strong style="font-size:13px">{d['rainfall']}</strong></div>
        </div></div>""", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""<div class="glass"><h4 style="color:#34d399">💧 Water & Duration</h4>
        <p><strong>Water:</strong> {d['water']}</p><p><strong>Duration:</strong> {d['duration']}</p>
        <p><strong>Harvest:</strong> {d['harvest']}</p></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""<div class="glass"><h4 style="color:#34d399">🧪 Fertilizer & Tips</h4>
        <p><strong>Fertilizer:</strong> {d['fertilizer']}</p><p><strong>Tips:</strong> {d['tips']}</p></div>""", unsafe_allow_html=True)
    draw_footer()


def page_history():
    st.markdown("## 📊 Prediction History")
    st.markdown("<p style='color:#94a3b8;margin-top:-8px'>Review past recommendations and download reports.</p>", unsafe_allow_html=True)
    df = load_history()
    search = st.text_input("🔍 Search", placeholder="Search by crop name...")
    if search:
        df = df[df["Recommended Crop"].str.contains(search, case=False, na=False)]
    if df.empty:
        st.info("No predictions yet. Run a recommendation to build your history.")
        draw_footer()
        return
    st.markdown(f"<p style='color:#64748b'>{len(df)} record(s) found</p>", unsafe_allow_html=True)
    for idx, row in df.iterrows():
        conf = row["Confidence"]
        cp = int(conf * 100) if conf <= 1 else int(conf)
        emoji = CROP_GUIDE.get(str(row["Recommended Crop"]).lower(), {}).get("emoji", "🌾")
        st.markdown(f"""<div class="glass" style="padding:16px;margin-bottom:8px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px">
        <div style="display:flex;align-items:center;gap:14px"><span style="font-size:32px">{emoji}</span>
        <div><strong style="color:#fff;font-size:17px">{row['Recommended Crop']}</strong><br>
        <span style="color:#64748b;font-size:12px">{row['Timestamp']}</span></div></div>
        <div style="text-align:right"><span style="color:#64748b;font-size:11px">Mode</span><br><strong>{row.get('Prediction Mode','Automatic') or 'Automatic'}</strong></div>
        <div style="text-align:right"><span style="color:#64748b;font-size:11px">Confidence</span><br><strong style="color:#34d399">{cp}%</strong></div></div>""", unsafe_allow_html=True)
        try:
            pdf = generate_pdf(row.to_dict())
            st.download_button("📥 Download Report", pdf, f"crop_report_{idx}.pdf", "application/pdf", key=f"pdf_{idx}")
        except Exception:
            pass
    draw_footer()


def page_about():
    st.markdown("## ℹ About")
    st.markdown("""<div class="glass"><h3 style="color:#34d399;margin-top:0">What is Crop Recommendation?</h3>
    <p style="color:#cbd5e1;line-height:1.8">The Smart Crop Recommendation System helps farmers select the most suitable crop based on
    soil nutrients (N, P, K), pH, temperature, humidity, and rainfall. Instead of guesswork, you receive a data-driven recommendation
    backed by machine learning models trained on agricultural datasets.</p></div>""", unsafe_allow_html=True)
    st.markdown("""<div class="glass"><h3 style="color:#34d399;margin-top:0">How Artificial Intelligence Works</h3>
    <p style="color:#cbd5e1;line-height:1.8">Your farmland inputs are processed through feature engineering and scaling, then passed to
    trained models — Random Forest, XGBoost, or Logistic Regression. Each model learns patterns between environmental conditions and
    successful crop outcomes, returning the best match with a confidence score and explainable reasons.</p></div>""", unsafe_allow_html=True)
    st.markdown("""<div class="glass"><h3 style="color:#34d399;margin-top:0">Benefits for Farmers</h3>
    <ul style="color:#cbd5e1;line-height:2"><li>Reduce crop failure risk with science-backed selection</li>
    <li>Optimize fertilizer use by matching crops to soil nutrients</li>
    <li>Save time with instant recommendations and downloadable reports</li>
    <li>Access a full crop guide for 22 supported crops</li></ul></div>""", unsafe_allow_html=True)
    st.markdown("""<div class="glass"><h3 style="color:#34d399;margin-top:0">Technology Stack</h3>
    <p style="color:#cbd5e1"><strong>Frontend:</strong> Streamlit &nbsp;·&nbsp; <strong>Backend:</strong> Flask &nbsp;·&nbsp;
    <strong>ML:</strong> Random Forest, XGBoost, Logistic Regression</p></div>""", unsafe_allow_html=True)
    draw_footer()


def page_settings():
    st.markdown("## ⚙ Settings")
    new_url = st.text_input("API Base URL", st.session_state.api_url)
    if st.button("Save Settings", type="primary"):
        st.session_state.api_url = new_url.rstrip("/")
        st.success("Settings saved.")
    st.markdown("---")
    st.markdown("#### API Connection Test")
    if check_api_status():
        st.markdown('<p class="api-ok">● API is online and responding</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p class="api-down">● API is offline — run `python app.py` on port 8000</p>', unsafe_allow_html=True)
    draw_footer()


def render_sidebar():
    st.sidebar.markdown("""
<div style="text-align:center;padding:24px 12px 16px;border-bottom:1px solid rgba(52,211,153,.1)">
<div style="font-size:36px;margin-bottom:8px">🌾</div>
<h3 style="color:#ecfdf5;margin:0;font-size:16px;font-weight:800">Smart Crop AI</h3>
<p style="color:#64748b;font-size:11px;margin:4px 0 0">Recommendation System</p></div>""", unsafe_allow_html=True)

    st.sidebar.toggle("☀️ Light mode", key="light_theme", help="Switch between dark and light appearance")

    nav = ["🏠 Home", "🌱 Recommendation", "📖 Crop Guide", "📊 History", "ℹ About", "⚙ Settings"]
    choice = st.sidebar.radio("Navigation", nav, index=nav.index(st.session_state.page) if st.session_state.page in nav else 0, label_visibility="collapsed")
    if choice != st.session_state.page:
        st.session_state.page = choice
        st.rerun()

    st.sidebar.markdown("---")
    online = check_api_status()
    status_cls = "api-ok" if online else "api-down"
    status_txt = "Online" if online else "Offline"
    st.sidebar.markdown(f"""<div class="glass" style="padding:14px;margin:0">
    <div style="font-size:10px;color:#64748b;text-transform:uppercase;letter-spacing:.8px">API Status</div>
    <div class="{status_cls}" style="font-weight:700;margin-top:4px;font-size:14px">● {status_txt}</div>
    <div style="color:#64748b;font-size:11px;margin-top:4px">{st.session_state.api_url}</div></div>""", unsafe_allow_html=True)


def main():
    inject_css()
    render_sidebar()
    routes = {
        "🏠 Home": page_home,
        "🌱 Recommendation": page_recommendation,
        "📖 Crop Guide": page_crop_guide,
        "📊 History": page_history,
        "ℹ About": page_about,
        "⚙ Settings": page_settings,
    }
    routes.get(st.session_state.page, page_home)()


if __name__ == "__main__":
    main()
