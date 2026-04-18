from PIL import Image, ImageDraw, ImageFont
import os
import services
from trading_core import TradingAccount, MOD_DATA_DIR, get_account

CHART_DIR = os.path.join(MOD_DATA_DIR, "charts")
os.makedirs(CHART_DIR, exist_ok=True)

def generate_chart(crypto_name, history, width=300, height=150, show_labels=True):
    """Generiere einen Kursverlauf-Chart für eine Kryptowährung"""
    if not history or len(history) < 2:
        return None
    
    path = os.path.join(CHART_DIR, f"{crypto_name}.png")
    
    # Hintergrund erstellen (dunkles Theme wie bei Trading-Apps)
    img = Image.new("RGB", (width, height), "#1e1e1e")
    draw = ImageDraw.Draw(img)
    
    # Achsen zeichnen
    draw.line([(0, height-10), (width, height-10)], fill="#404040", width=1)  # X-Achse
    draw.line([(10, 0), (10, height)], fill="#404040", width=1)  # Y-Achse
    
    # Preiswerte berechnen
    min_val = min(history)
    max_val = max(history)
    range_val = max(0.01, max_val - min_val)
    
    # Punkte für die Linie berechnen
    points = []
    chart_width = width - 20
    chart_height = height - 20
    
    for i, val in enumerate(history):
        x = 10 + int((i / max(1, len(history) - 1)) * chart_width)
        y = height - 10 - int(((val - min_val) / range_val) * chart_height)
        points.append((x, y))
    
    # Farbe bestimmen (grün wenn steigend, rot wenn fallend)
    line_color = "#4ade80" if history[-1] >= history[0] else "#ef4444"
    
    # Hauptlinie zeichnen
    if len(points) > 1:
        draw.line(points, fill=line_color, width=2)
    
    # Gefüllte Fläche unter der Linie (Gradient-Effekt)
    if len(points) > 1:
        fill_points = points.copy()
        fill_points.append((points[-1][0], height - 10))
        fill_points.append((points[0][0], height - 10))
        
        # Semi-transparente Füllung
        overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        overlay_draw = ImageDraw.Draw(overlay)
        overlay_draw.polygon(fill_points, fill=(74, 222, 128, 40) if history[-1] >= history[0] else (239, 68, 68, 40))
        img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
        draw = ImageDraw.Draw(img)
        draw.line(points, fill=line_color, width=2)
    
    # Aktuelle Preise anzeigen
    if show_labels:
        current_price = history[-1]
        start_price = history[0]
        change_pct = ((current_price - start_price) / start_price * 100) if start_price > 0 else 0
        
        # Preis-Label oben rechts
        price_text = f"{current_price:.2f}§"
        try:
            font = ImageFont.truetype("arial.ttf", 14)
        except:
            font = ImageFont.load_default()
        
        text_bbox = draw.textbbox((0, 0), price_text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        draw.text((width - text_width - 5, 5), price_text, fill="#ffffff", font=font)
        
        # Veränderungs-Prozent
        change_color = "#4ade80" if change_pct >= 0 else "#ef4444"
        change_sign = "+" if change_pct >= 0 else ""
        change_text = f"{change_sign}{change_pct:.1f}%"
        draw.text((width - text_width - 5, 22), change_text, fill=change_color, font=font)
    
    img.save(path)
    return path


def generate_portfolio_chart(portfolio_summary, prices, width=400, height=200):
    """Generiere einen Übersichtscharts für das gesamte Portfolio"""
    if not portfolio_summary:
        return None
    
    path = os.path.join(CHART_DIR, "portfolio_overview.png")
    img = Image.new("RGB", (width, height), "#1e1e1e")
    draw = ImageDraw.Draw(img)
    
    # Titel
    try:
        title_font = ImageFont.truetype("arial.ttf", 16)
    except:
        title_font = ImageFont.load_default()
    draw.text((10, 10), "Portfolio Übersicht", fill="#ffffff", font=title_font)
    
    # Liste der Assets mit Werten
    y_offset = 40
    total_value = sum(item["value"] for item in portfolio_summary)
    
    colors = ["#4ade80", "#60a5fa", "#f472b6", "#fbbf24", "#a78bfa"]
    
    for i, item in enumerate(portfolio_summary):
        color = colors[i % len(colors)]
        name = item["name"]
        qty = item["quantity"]
        value = item["value"]
        price = item["price"]
        
        # Prozentualer Anteil
        pct = (value / total_value * 100) if total_value > 0 else 0
        
        # Balkenbreite basierend auf Prozentsatz
        bar_width = int((pct / 100) * (width - 100))
        
        # Asset-Name
        draw.text((10, y_offset), f"{name}", fill="#ffffff")
        
        # Menge und Preis
        draw.text((10, y_offset + 12), f"{qty:.2f} @ {price:.2f}§", fill="#888888")
        
        # Wertbalken
        draw.rectangle([
            (150, y_offset + 5),
            (150 + bar_width, y_offset + 15)
        ], fill=color)
        
        # Gesamtwert des Assets
        draw.text((width - 80, y_offset), f"{value:.0f}§", fill="#ffffff")
        
        y_offset += 35
    
    img.save(path)
    return path


def get_crypto_icon(crypto_name):
    """Gib den Pfad zum Crypto-Icon zurück (falls vorhanden)"""
    icon_path = os.path.join(CHART_DIR, f"icons", f"{crypto_name}.png")
    if os.path.exists(icon_path):
        return icon_path
    return None
