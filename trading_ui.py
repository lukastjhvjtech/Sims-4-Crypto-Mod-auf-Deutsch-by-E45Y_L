from PIL import Image, ImageDraw
import os
import services
from trading_core import TradingAccount, MOD_DATA_DIR

CHART_DIR = os.path.join(MOD_DATA_DIR, "charts")
os.makedirs(CHART_DIR, exist_ok=True)

def generate_chart(stock_name, history, width=300, height=120):
    if not history or len(history) < 2:
        return None
    path = os.path.join(CHART_DIR, f"{stock_name}.png")
    img = Image.new("RGB", (width, height), "#1e1e1e")
    draw = ImageDraw.Draw(img)
    min_val, max_val = min(history), max(history)
    scale = height / max(1, max_val - min_val)
    points = []
    for i, val in enumerate(history):
        x = int((i / (len(history) - 1)) * width)
        y = height - int((val - min_val) * scale)
        points.append((x, y))
    draw.line(points, fill="#4ade80" if history[-1] >= history[0] else "#ef4444", width=2)
    img.save(path)
    return path
