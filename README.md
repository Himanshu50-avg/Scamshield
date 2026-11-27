# 🛡️ ScamShield

## A Python-Based Approach to Online Scam Detection

ScamShield is a Python-based web application designed to help users identify potentially suspicious URLs, emails, and messages before they become a threat.

The application checks user-provided content for common scam indicators such as urgency, requests for sensitive information, suspicious URLs, and other warning patterns.

Based on the detected warning indicators, ScamShield calculates a **risk score from 0 to 100** and provides an explanation to the user.

> **PAUSE → CHECK → UNDERSTAND → ACT SAFELY**

---

## 📌 Project Overview

Online scams often use social engineering techniques to make users act quickly without verifying the information.

Examples include:

- "Your account will be blocked."
- "Verify your account immediately."
- "You have won a reward."
- "Send your OTP to confirm."
- "Click this link to receive your payment."

ScamShield provides a simple second layer of checking before the user clicks a suspicious link or shares sensitive information.

The current version is a **rule-based Python prototype**. Machine learning is planned as a future improvement.

---

## 🎯 Objectives

The main objectives of ScamShield are:

1. Detect suspicious warning phrases.
2. Extract URLs from text.
3. Check URLs for suspicious patterns.
4. Analyse emails and messages.
5. Calculate a risk score.
6. Explain why content was flagged.
7. Provide a simple and user-friendly interface.
8. Display scan activity through a dashboard.
9. Maintain scan history during the session.
10. Provide safety guidance to users.

---

## 🚀 Features

### 🔗 URL Scanner

Checks a website URL for suspicious patterns.

### 📧 Email Scanner

Analyses email content for suspicious indicators such as:

- Urgent requests
- Account warnings
- Requests for OTP
- Requests for passwords
- Payment requests
- Suspicious links

### 💬 SMS / Message Scanner

Analyses messages for scam-related warning phrases and suspicious URLs.

### ⚠️ Risk Detection

ScamShield uses predefined rules to detect warning indicators such as:

- Urgency
- Secrecy
- Sensitive information requests
- Suspicious URLs
- Payment requests
- Account threats

### 📊 Dashboard

Provides a visual overview of scan activity.

### 📋 Scan History

Maintains scan information during the current session.

### 📑 Reports

Provides information about scan results and risk levels.

---

# 📊 Risk Score Calculation

ScamShield generates a risk score between **0 and 100**.

The current prototype uses a simple rule-based scoring formula.

## Formula

```text
Risk Score = min(Number of Warning Indicators × 20, 100)
