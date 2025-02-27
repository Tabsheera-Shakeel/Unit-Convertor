#THIS IS MY UNIT CONVERTOR WHICH CAN ALSO SUPPORT MULTI LANGAUES 

import streamlit as st
import forex_python.converter as forex
from datetime import datetime
import pytz

# So I am Designing UI with Custom CSS 
st.markdown(
    """
    <style>
    body {
        background-color: #12121f;
        color: white !important;
    }
    
    .stApp {
        background: linear-gradient(231deg, #1b1d2b, #2a2c42);
        padding: 40px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.4);
        margin-bottom: 20px;
    }
    
    h1, label, span {
        text-align: center;
        font-size: 38px;
        font-weight: bold;
        background: linear-gradient(90deg, cyan, #00ff7f); /* Cyan to Blue-Green */
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        transition: 0.3s;
        text-shadow: 2px 2px 15px rgba(0, 201, 255, 0.4);
    }
    
/* Sidebar background */
    .stSidebar {
        background-color: #1b1d2b !important;
        padding: 20px;
        border-radius: 15px;
    }

    /* Sidebar text color */
    .stSidebar, .stSidebar div, .stSidebar span, .stSidebar label {
        color: #12121f !important;
        font-size: 16px;
        font-weight: bold;
        }
       .description {
        font-size: 18px;
        font-weight: bold;
        color:white;
        text-align: center;
        padding: 10px;
    } 
    .stButton>button {
        background: linear-gradient(45deg, #00c9ff, #00ff7f);
        color: white !important;
        border: none;
        border-radius: 8px;
        padding: 12px 24px;
        font-size: 18px;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease-in-out;
        box-shadow: 0px 4px 15px rgba(0, 201, 255, 0.4);
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        background: linear-gradient(45deg, #00ff7f, #00c9ff);
        box-shadow: 0px 6px 20px rgba(0, 255, 200, 0.6);
    }
.result-box {
    font-size: 22px;
    font-weight: bold;
    text-align: center;
    color: #ffffff; /* Ensures text is readable on any background */
    background: rgba(255, 255, 255, 0.15); /* Slightly more visible */
    padding: 20px 30px; /* Balanced padding */
    border-radius: 15px; /* Smoother rounded corners */
    margin-top: 30px;
    box-shadow: 0px 8px 25px rgba(0, 201, 255, 0.5); /* Softer glow */
    width: max-content; /* Adapts to content width */
    max-width: 90%; /* Prevents overflow */
    margin-left: auto;
    margin-right: auto; /* Centers the box */
    backdrop-filter: blur(8px); /* Glassmorphism effect */
    border: 2px solid rgba(255, 255, 255, 0.2); /* Subtle border */
    transition: all 0.3s ease-in-out; /* Smooth animations */
}
.result-box:hover {
    box-shadow: 0px 10px 30px rgba(0, 201, 255, 0.7);
    transform: translateY(-3px);
}  
    .footer {
        text-align: center;
        margin-top: 60px;
        font-size: 16px;
        color: white !important;
        opacity: 0.8;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# This will Multi-language support
language = st.sidebar.selectbox("Choose Language / اختر اللغة / 选择语言 / زبان منتخب کریں", 
                                ["English", "Arabic", "Chinese", "Urdu","Spanish", "French", "German"])

# Translation dictionary
translations = {
    "English": {
        "title": "Unit Master: Convert Anything, Anytime",
        "description": "Easily convert between different units of length, weight, temperature, currency, time zones, data storage, speed, energy, and volume.",
        "conversion_type": "Choose Conversion Type",
        "enter_value": "Enter Value",
        "convert": "Convert",
        "result": "Great! {} {} is equal to {:.4f} {}. That’s your converted value!",
        "footer": "Created by Tabsheera Shakeel"
    },
    "Arabic": {
        "title": "سيد الوحدات: حوّل أي شيء، في أي وقت",
        "description": "قم بالتحويل بسهولة بين وحدات الطول، الوزن، درجة الحرارة، العملة، المناطق الزمنية، تخزين البيانات، السرعة، الطاقة، والحجم.",
        "conversion_type": "اختر نوع التحويل",
        "enter_value": "أدخل القيمة",
        "convert": "تحويل",
        "result": "رائع! {} {} يساوي {:.4f} {}. هذا هو القيمة المحولة الخاصة بك!",
        "footer": "تم الإنشاء بواسطة Tabsheera Shakeel"
    },
    "Chinese": {
        "title": "单位大师：随时转换任何东西",
        "description": "轻松转换长度、重量、温度、货币、时区、数据存储、速度、能量和体积的不同单位。",
        "conversion_type": "选择转换类型",
        "enter_value": "输入值",
        "convert": "转换",
        "result": "太棒了！{} {} 等于 {:.4f} {}。这是你的转换值！",
        "footer": "由 Tabsheera Shakeel 创建"
    },
    "Urdu": {
        "title":"یونٹ ماسٹر: کسی بھی چیز کو کسی بھی وقت تبدیل کریں",
        "description": "لمبائی، وزن، درجہ حرارت، کرنسی، ٹائم زونز، ڈیٹا اسٹوریج، سپیڈ، توانائی، اور حجم کے مختلف یونٹس کے درمیان آسانی سے تبدیل کریں۔",
        "conversion_type": "تبادلوں کی قسم منتخب کریں",
        "enter_value": "ویلیو درج کریں",
        "convert": "تبدیل کریں",
        "result": "زبردست! {} {} {:.4f} {} کے برابر ہے۔ یہ آپ کی تبدیل شدہ قدر ہے!",
        "footer": "Tabsheera Shakeel کے ذریعہ بنایا گیا"
    },"Spanish": {
        "title": "Maestro de Unidades: Convierte Cualquier Cosa, en Cualquier Momento",
        "description": "Convierte fácilmente entre diferentes unidades de longitud, peso, temperatura, moneda, zonas horarias, almacenamiento de datos, velocidad, energía y volumen.",
        "conversion_type": "Elige el Tipo de Conversión",
        "enter_value": "Ingresa el Valor",
        "convert": "Convertir",
       "result": "¡Genial! {} {} es igual a {:.4f} {}. ¡Ese es tu valor convertido!",
        "footer": "Creado por Tabsheera Shakeel"
    },
    "French": {
        "title": "Maître des Unités : Convertissez Tout, à Tout Moment",
        "description": "Convertissez facilement entre différentes unités de longueur, poids, température, devise, fuseaux horaires, stockage de données, vitesse, énergie et volume.",
        "conversion_type": "Choisissez le Type de Conversion",
        "enter_value": "Entrez la Valeur",
        "convert": "Convertir",
        "result": "Super ! {} {} est égal à {:.4f} {}. C’est votre valeur convertie !",
        "footer": "Créé par Tabsheera Shakeel"
    },
    "German": {
        "title": "Einheitenmeister: Wandle Alles, Jederzeit Um",
        "description": "Einfach zwischen verschiedenen Einheiten für Länge, Gewicht, Temperatur, Währung, Zeitzonen, Datenspeicher, Geschwindigkeit, Energie und Volumen umrechnen.",
        "conversion_type": "Wählen Sie den Umrechnungstyp",
        "enter_value": "Wert eingeben",
        "convert": "Umrechnen",
        "result": "Großartig! {} {} ist gleich {:.4f} {}. Das ist dein umgerechneter Wert!",
        "footer": "Erstellt von Tabsheera Shakeel"
    }
}

# Title and description
st.markdown(f"<h1>{translations[language]['title']}</h1>", unsafe_allow_html=True)
st.markdown(f'<p class="description">{translations[language]["description"]}</p>', unsafe_allow_html=True)


# Sidebar menu
conversion_type = st.sidebar.selectbox(
    translations[language]['conversion_type'],
    ["Length", "Weight", "Temperature", "Currency", "Time Zones", "Data Storage", "Speed", "Energy", "Volume"]
)
value = st.number_input(translations[language]['enter_value'], value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

#This is Hardcoded exchange rates (update as needed)
exchange_rates = {
    "USD": 1,         # Base currency
    "EUR": 0.91,      # Example: 1 USD = 0.91 EUR
    "GBP": 0.78,      # Example: 1 USD = 0.78 GBP
    "INR": 83.50,     # Example: 1 USD = 83.50 INR
    "PKR": 280.75,    # Example: 1 USD = 280.75 PKR
    "CAD": 1.35,      # Example: 1 USD = 1.35 CAD
    "AUD": 1.52,      # Example: 1 USD = 1.52 AUD
    "JPY": 145.3,     # Example: 1 USD = 145.3 JPY
    "CNY": 7.2,       # Example: 1 USD = 7.2 CNY
}

# Conversion units
if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
elif conversion_type == "Currency":
    with col1:
        from_unit = st.selectbox("From", list(exchange_rates.keys()))
    with col2:
        to_unit = st.selectbox("To", list(exchange_rates.keys()))
elif conversion_type == "Time Zones":
    with col1:
        from_unit = st.selectbox("From", pytz.all_timezones)
    with col2:
        to_unit = st.selectbox("To", pytz.all_timezones)
elif conversion_type == "Data Storage":
    with col1:
        from_unit = st.selectbox("From", ["Bytes", "Kilobytes", "Megabytes", "Gigabytes", "Terabytes"])
    with col2:
        to_unit = st.selectbox("To", ["Bytes", "Kilobytes", "Megabytes", "Gigabytes", "Terabytes"])
elif conversion_type == "Speed":
    with col1:
        from_unit = st.selectbox("From", ["km/h", "m/s", "mph", "knots"])
    with col2:
        to_unit = st.selectbox("To", ["km/h", "m/s", "mph", "knots"])
elif conversion_type == "Energy":
    with col1:
        from_unit = st.selectbox("From", ["Joules", "Calories", "Kilowatt-hours"])
    with col2:
        to_unit = st.selectbox("To", ["Joules", "Calories", "Kilowatt-hours"])
elif conversion_type == "Volume":
    with col1:
        from_unit = st.selectbox("From", ["Liters", "Gallons", "Cubic Meters", "Milliliters"])
    with col2:
        to_unit = st.selectbox("To", ["Liters", "Gallons", "Cubic Meters", "Milliliters"])

# Conversion functions
def length_converter(value, from_unit, to_unit):
    length_units = {
        'Meters': 1, 'Kilometers': 0.001, 'Centimeters': 100, 'Millimeters': 1000,
        'Miles': 0.000621371, 'Yards': 1.09361, 'Feet': 3.28084, 'Inches': 39.3701
    }
    return value / length_units[from_unit] * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'Kilograms': 1, 'Grams': 1000, 'Milligrams': 1000000, 'Pounds': 2.20462, 'Ounces': 35.274
    }
    return value / weight_units[from_unit] * weight_units[to_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return value * 9/5 + 32
        elif to_unit == "Kelvin":
            return value + 273.15
        else:
            return value
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        else:
            return value
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value

def currency_converter(value, from_unit, to_unit):
    return forex.convert(from_unit, to_unit, value)

def time_zone_converter(value, from_unit, to_unit):
    from_tz = pytz.timezone(from_unit)
    to_tz = pytz.timezone(to_unit)
    dt = datetime.now()
    from_dt = from_tz.localize(dt)
    to_dt = from_dt.astimezone(to_tz)
    return to_dt.strftime("%Y-%m-%d %H:%M:%S")

def data_storage_converter(value, from_unit, to_unit):
    data_units = {
        'Bytes': 1, 'Kilobytes': 1024, 'Megabytes': 1024**2, 'Gigabytes': 1024**3, 'Terabytes': 1024**4
    }
    return value / data_units[from_unit] * data_units[to_unit]

def speed_converter(value, from_unit, to_unit):
    speed_units = {
        'km/h': 1, 'm/s': 0.277778, 'mph': 0.621371, 'knots': 0.539957
    }
    return value / speed_units[from_unit] * speed_units[to_unit]

def energy_converter(value, from_unit, to_unit):
    energy_units = {
        'Joules': 1, 'Calories': 0.239006, 'Kilowatt-hours': 0.000000277778
    }
    return value / energy_units[from_unit] * energy_units[to_unit]

def volume_converter(value, from_unit, to_unit):
    volume_units = {
        'Liters': 1, 'Gallons': 0.264172, 'Cubic Meters': 0.001, 'Milliliters': 1000
    }
    return value / volume_units[from_unit] * volume_units[to_unit]

def currency_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    amount_in_usd = value / exchange_rates[from_unit]
    return round(amount_in_usd * exchange_rates[to_unit], 2)

# Button for conversion
if st.button(translations[language]['convert']):
    if conversion_type == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temperature_converter(value, from_unit, to_unit)
    elif conversion_type == "Currency":
        result = currency_converter(value, from_unit, to_unit)
    elif conversion_type == "Time Zones":
        result = time_zone_converter(value, from_unit, to_unit)
    elif conversion_type == "Data Storage":
        result = data_storage_converter(value, from_unit, to_unit)
    elif conversion_type == "Speed":
        result = speed_converter(value, from_unit, to_unit)
    elif conversion_type == "Energy":
        result = energy_converter(value, from_unit, to_unit)
    elif conversion_type == "Volume":
        result = volume_converter(value, from_unit, to_unit)

    st.markdown(f"""<div class='result-box'>🎉 {translations[language]['result'].format(value, from_unit, result, to_unit)}</div>""",unsafe_allow_html=True)
    st.markdown(f"<div class='footer'>{translations[language]['footer']}</div>", unsafe_allow_html=True)