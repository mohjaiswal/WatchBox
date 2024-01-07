#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import the libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import HTML
import ipywidgets as widgets
from IPython.display import display, clear_output
from flask import Flask, render_template_string
import pandas as pd

app = Flask(__name__)

import pandas as pd
from IPython.display import display  # Import the display function

# Sample DataFrame setup (please replace this with your actual DataFrame)
watch_data = {
    "Brand": ["Tissot", "Casio", "Titan", "Casio", "Mido", "Citizen", "Apple", "Fossil", "Titan"],
    "Series": ["Couturier", "Edifice", "Classique", "Edifice", "Ocean Star Tribute", "Eco-Drive", "Watch Series 1", "Replica/Fake", "Classique"],
    "Model Number": ["T0356171105100", "ECB950MP-1A", "ND1490SL01", "EF-558D-7AV", "M026.830.17.421.00", "AT0550-11X", "N/A", "CH2519", "EB-218-K95"],
    "Description": [
        "Chronograph Watch", 
        "Motorsports-inspired watch with Bluetooth, speed indicator, and urethane band", 
        "Analog Black Dial Men's Watch with leather strap", 
        "Classic and modern style, silver dial, luminous hands, water-resistant up to 100 meters",
        "Smokey red gradient dial, stainless steel case, water-resistant up to 200 meters", 
        "42mm stainless steel case, brown dial, brown leather strap, Eco-Drive technology", 
        "Available in 38mm and 42mm, dual-core processor, 8GB storage, OLED Retina display",
        "Replica of Fossil CH2519, black dial, stainless steel, water-resistant, and PRICELESS TO ME!", 
        "Pre-owned, gold finish, classic luxurious style"],
    "Movement": ["Swiss Quartz", "Tough Solar (solar powered)", "Quartz", "Quartz", "Automatic Mido Caliber 80", "Eco-Drive", "Dual-core processor", "Quartz", "Quartz"],
    "Crystal": ["Sapphire", "Mineral", "N/A", "Mineral", "Sapphire", "Mineral", "Ion-X", "Mineral", "Mineral"],
    "Case Material": ["Stainless Steel", "Stainless Steel", "", "Stainless Steel", "Stainless Steel", "Stainless Steel", "Aluminum", "Stainless Steel (replica)", "Stainless Steel"],
    "Strap Material": ["Stainless Steel", "Resin (Urethane)", "Leather", "Stainless Steel", "Rubber", "Leather", "Varies", "Bracelet-style (replica)", "Leather"],
    "Clasp Type": ["Butterfly", "Pin Buckle", "Pin Buckle", "Double-Lock, 1-Press, 3-Fold", "Pin Buckle", "Pin Buckle", "Pin-and-Tuck Buckle", "Tang Buckle", "Pin Buckle"],
    "Water Resistance": ["100 meters", "100 meters", "30 meters", "100 meters", "200 meters", "100 meters", "IPX7 - Splash-resistant", "N/A (replica)", "10 meters"],
    "Case Size: Length x Width x Thickness": ["41 mm × 41 mm × 11 mm", "51.2 mm × 48 mm × 13.9 mm", "48 mm × 30 mm × 9 mm", "49.3 mm × 49.3 mm × 14.1 mm", "40.5 mm × 40.5 mm × 13.4 mm", "42 mm × 42 mm × 13 mm", "38.6 mm × 33.3 mm × 10.5 mm", "45 mm × 45 mm × 14.4 mm", "33 mm × 33 mm × 4.4 mm"],
    "Dial Color": ["Black", "Black-Brown dial with colorful touches", "Anthracite Black", "White with Bronze touches", "Smokey red gradient", "Silver", "OLED Retina display with Force Touch (450 nits)", "Black", "Black"],
    "Functions": [
        "Central 60-seconds chronograph hand, 30-minutes and 1/10 of a second counters, ADD and SPLIT functions", 
        "Water Resistance, Smartphone Link Feature, World Time, Timer, Led Back-Light, Calendar, Energy Saver, Stopwatch, Alarm, Hourly Signal, Mute Feature, Battery Display/Alert", 
        "Analog", 
        "Chronograph, Tachymeter, Day and Date Display", 
        "80 Hour Power Reserve, Day and Date Display", 
        "1-second chronograph, 12/24 hour time, Date Display", 
        "Splash resistant, Heart rate sensor, Accelerometer, Gyroscope, Ambient light sensor", 
        "Chronograph, Date (replica)", 
        "Analog"],
    "Release Year": ["2015", "N/A", "~2010-2012", "2011", "N/A", "2011", "2016", "N/A", "2010"],
    "RetailPriceUSD": ["595.00", "250.00", "60.97", "258.98", "990.00", "375.00", "349.00", "45.00", "112.95"],
    "Links": ["https://www.tissotwatches.com/en-us/t0356171105100.html",
    "https://www.casio.com/us/watches/edifice/product.ECB-950MP-1A/",
    "https://www.titan.co.in/product/titan-anthracite-dial-analog-watch-for-men-1490sl01.html",
    "https://www.citywatches.co.uk/product/casio-edifice-chronograph-ef-558d-7av/",
    "https://www.midowatches.com/en/ocean-star-tribute-gradient-m0268301742100.html",
    "https://www.citizenwatch.com/us/en/product/AT0550-11X.html",
    "https://support.apple.com/kb/SP745?locale=en_US",
    "https://www.amazon.com/Fossil-Watch-Stainless-Bracelet-CH2519/dp/B001EDTSNW/ref=cm_cr_arp_d_product_top?ie=UTF8",
    "https://www.ebay.com/itm/335099068790"]
}

watches_df = pd.DataFrame(watch_data)
# Define the list of HTML code for the 9 thumbnail-linked image sources
image_html_sources = [
    '<a href="https://ibb.co/db4MSc9"><img src="https://i.ibb.co/db4MSc9/T0356171105100.png" alt="T0356171105100" border="0"></a>','<a href="https://ibb.co/T87sWGn"><img src="https://i.ibb.co/T87sWGn/ECB950-MP-1-A.png" alt="ECB950-MP-1-A" border="0"></a>','<a href="https://ibb.co/Y2bcr0y"><img src="https://i.ibb.co/Y2bcr0y/ND1490-SL01.png" alt="ND1490-SL01" border="0"></a>','<a href="https://ibb.co/h84JXnw"><img src="https://i.ibb.co/h84JXnw/EF-558-D-7-AV.png" alt="EF-558-D-7-AV" border="0"></a>','<a href="https://ibb.co/5hxGnkP"><img src="https://i.ibb.co/5hxGnkP/M026-830-17-421-00.png" alt="M026-830-17-421-00" border="0"></a>','<a href="https://ibb.co/dbx15q5"><img src="https://i.ibb.co/dbx15q5/AT0550-11-X.png" alt="AT0550-11-X" border="0"></a>','<a href="https://ibb.co/vX3Dtpt"><img src="https://i.ibb.co/vX3Dtpt/N-A.png" alt="N-A" border="0"></a>','<a href="https://ibb.co/Cnqj94C"><img src="https://i.ibb.co/Cnqj94C/CH2519.png" alt="CH2519" border="0"></a>','<a href="https://ibb.co/Bgyx58t"><img src="https://i.ibb.co/Bgyx58t/EB-218-K95.png" alt="EB-218-K95" border="0"></a>'
                     ]

# Create a new column 'Thumbnails' in the DataFrame
watches_df['Thumbnails'] = image_html_sources
# Get the list of columns in the DataFrame
columns = list(watches_df.columns)

# Reorder the columns. Insert 'Links' at index 1 and 'Thumbnails' at index 2
columns.insert(1, columns.pop(columns.index('Links')))
columns.insert(2, columns.pop(columns.index('Thumbnails')))

# Reassign the reordered columns to the DataFrame
watches_df = watches_df[columns]

# Rename the 'Links' column to 'Watch Name'
watches_df.rename(columns={'Links': 'Watch Names'}, inplace=True)

# Function to calculate brightness of a color (used for contrast)
def brightness(hex_color):
    hex_color = hex_color.lstrip('#')
    rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return (0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]) / 255

# Function to map color descriptions to color codes
def color_mapper(color_description):
    color_map = {
        'black': '#000000', 'white': '#FFFFFF', 'red': '#FF0000', 
        'blue': '#0000FF', 'green': '#008000', 'yellow': '#FFFF00', 
        'silver': '#C0C0C0', 'gold': '#FFD700', 'bronze': '#CD7F32',
        'gray': '#808080', 'grey': '#808080', 'pink': '#FFC0CB',
        'purple': '#800080', 'orange': '#FFA500', 'brown': '#A52A2A',
        'anthracite': '#303030', 'smokey red': '#B22222', # Add other colors as needed
    }
    for color_word, hex_color in color_map.items():
        if color_word in color_description.lower():
            return hex_color
    return '#FFFFFF'  # Default color

# Function to format the 'Watch Names' column with smart names
def format_watch_names(val):
    # Retrieve the brand and series based on the 'val' link
    brand = watches_df.loc[watches_df['Watch Names'] == val, 'Brand'].iloc[0]
    series = watches_df.loc[watches_df['Watch Names'] == val, 'Series'].iloc[0]
    label = f"{brand} {series}" if series else brand
    return f'<a href="{val}" target="_blank">{label}</a>'

# Function to apply styling to 'Dial Color' column
def style_dial_color(row):
    dial_color = row['Dial Color']
    bg_color = color_mapper(dial_color)
    if bg_color:
        text_color = "#FFFFFF" if brightness(bg_color) < 0.5 else "#000000"
        return [f'background-color: {bg_color}; color: {text_color}']
    return [''] * len(row)

# Check if 'Dial Color' column exists in the DataFrame
if 'Dial Color' not in watches_df.columns:
    print("Column 'Dial Color' not found in DataFrame.")
else:
    # Apply styling to the DataFrame
        styled_df = watches_df.style.apply(
            lambda row: style_dial_color(row), axis=1, subset=['Dial Color']
        ).format(
            {'Watch Names': format_watch_names}  # Updated to use the 'Watch Names' column
        ).set_table_styles([
            {'selector': 'th', 'props': [('background-color', '#f4f4f4'), ('color', 'black'), ('font-family', 'Arial')]},
            {'selector': 'td', 'props': [('font-family', 'Arial')]}
        ]).set_properties(**{
            'border-color': 'black',
            'border-width': '1px',
            'border-style': 'solid'
        }).background_gradient(cmap='Blues', subset=['RetailPriceUSD'])

# Display the styled DataFrame - display(styled_df)
html_data = styled_df.render()

@app.route('/')
def display_table():
    return render_template_string('<html><body>{{table|safe}}</body></html>', table=html_data)

if __name__ == '__main__':
    app.run(debug=True)

