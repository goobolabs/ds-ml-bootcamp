# Phishing Website Detection API

A machine learning system that classifies websites as **phishing** or **legitimate** using 30 structural features pulled from a URL and page, no live crawling involved. Built as a final capstone project covering the whole pipeline: dataset prep, model comparison, a deployed API, and a live UI.

**Repository:** https://github.com/Kacabdev/pishing-detection-api2

**Live Demo (UI):** https://kacabdev.github.io/pishing-detection-api2/

## Overview

Phishing sites copy trusted domains to steal credentials, but the structure tends to give them away: unusual URL length, a raw IP address instead of a domain, too many subdomains, a shaky SSL certificate, a domain that's a few weeks old. This project trains three classifiers on those signals using the UCI Phishing Websites dataset (11,055 rows, cleaned down to 5,849 after dropping exact duplicates), tests them on the same held-out split, and puts the best one behind a FastAPI `/predict` endpoint with a simple UI in front.

## Results

| Algorithm | Accuracy | Precision | Recall | F1-Score |
|---|---|---|---|---|
| **XGBoost (deployed)** | 0.948 | 0.959 | 0.939 | **0.949** |
| Random Forest | 0.940 | 0.957 | 0.926 | 0.941 |
| Logistic Regression | 0.918 | 0.925 | 0.916 | 0.920 |

Models were ranked by F1-Score, with recall as the tiebreaker: missing an actual phishing site costs more than a false alarm does, so recall wins when scores are close. XGBoost came out ahead on both.

## Tech Stack

Python, pandas, scikit-learn, XGBoost, FastAPI, vanilla HTML/CSS/JS.

## Try It

The [live demo](https://kacabdev.github.io/pishing-detection-api2/) runs a sample analysis right in the browser. Full setup instructions and API docs are in the [repository README](https://github.com/Kacabdev/pishing-detection-api2#readme).
