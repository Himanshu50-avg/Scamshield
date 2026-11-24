



import re


def detect_warnings(text):  #receives text
    text = text.lower()     #lowecase conversation
    warnings = []           #empty list for detected warnings


     #here we are predefining keywords
    checks = [
        ("urgent", "Urgent language"),
        ("immediately", "Pressure to act quickly"),
        ("prize", "Possible prize claim"),
        ("winner", "Possible fake prize claim"),
        ("otp", "OTP mentioned"),
        ("password", "Password mentioned"),
        ("pay now", "Payment request"),
        ("bank", "Bank-related wording"),
        ("verify", "Verification request"),
        ("click here", "Request to click a link"),
        ("account suspended", "Account suspension warning"),
        ("send money", "Request to send money"),
        ("free gift", "Possible free gift scam"),
    ]

    for phrase, warning in checks:
        if phrase in text and warning not in warnings:
            warnings.append(warning)

    return warnings




def check_url(url):
    warnings = []
    url = url.strip()
    lower_url = url.lower()

    if not url:
        return ["Please enter a URL"]

    if not (
        lower_url.startswith("https://")
        or lower_url.startswith("http://")
        or lower_url.startswith("www.")
    ):
        return ["URL format is not recognised"]

    if lower_url.startswith("http://"):
        warnings.append("Link uses HTTP instead of HTTPS")

    if "@" in url:
        warnings.append("URL contains an @ symbol")

    if len(url) > 100:
        warnings.append("URL is unusually long")

    return warnings


def check_sender(sender):
    warnings = []
    sender = sender.strip().lower()

    if not sender:
        return ["Sender email address was not provided"]

    if sender.count("@") != 1:
        return ["Sender email address appears invalid"]

    parts = sender.split("@")
    name = parts[0]
    domain = parts[1]

    if not name or not domain or "." not in domain:
        warnings.append("Sender email address appears invalid")

    return warnings


def find_urls(text):
    pattern = r'https?://[^\s<>"\']+|www\.[^\s<>"\']+'
    urls = re.findall(pattern, text, re.IGNORECASE)
    clean_urls = []

    for url in urls:
        url = url.rstrip(".,!?;:)]}")

        if url not in clean_urls:
            clean_urls.append(url)

    return clean_urls


def calculate_score(warnings):
    return min(len(warnings) * 20, 100)


def analyse_message(message):
    warnings = detect_warnings(message)
    urls = find_urls(message)

    for url in urls:
        for warning in check_url(url):
            if warning not in warnings:
                warnings.append(warning)

    return warnings, urls, calculate_score(warnings)


def analyse_email(subject, sender, body):
    email_text = subject + " " + body
    warnings = detect_warnings(email_text)

    for warning in check_sender(sender):
        if warning not in warnings:
            warnings.append(warning)

    urls = find_urls(email_text)

    for url in urls:
        for warning in check_url(url):
            if warning not in warnings:
                warnings.append(warning)

    return warnings, urls, calculate_score(warnings)


def analyse_standalone_url(url):
    warnings = check_url(url)   #function call  
    urls = [url.strip()] if url.strip() else []

    return warnings, urls, calculate_score(warnings)


