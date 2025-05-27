from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from src.backend.utils.image_utils import ClickableImageLabel
import os

def create_item_card(item):
    frame = QFrame()
    frame.setFixedSize(200, 300)
    frame.setStyleSheet("""
        QFrame {
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 6px;
        }
        QLabel {
            font-size: 11px;
        }
        QLabel#statusLabel {
            font-weight: bold;
            color: white;
            background-color: #3a7bd5;
            border-radius: 4px;
            padding: 2px 4px;
            margin-bottom: 4px;
        }
    """)

    layout = QVBoxLayout(frame)

    # === Image path resolution ===
    default_path = os.path.abspath("assets/icons/placeholder.png")
    img_path = item.get("ImagePath")
    img_path = os.path.abspath(img_path) if img_path and os.path.exists(img_path) else default_path

    # === Clickable image ===
    image_label = ClickableImageLabel(img_path)
    image_label.setAlignment(Qt.AlignCenter)
    pixmap = QPixmap(img_path)
    image_label.setPixmap(pixmap.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation))

    # === Status Label ===
    status = item.get("Status", "Unknown")
    status_label = QLabel(status.upper())
    status_label.setObjectName("statusLabel")
    status_label.setAlignment(Qt.AlignCenter)

    # === Info Labels ===
    name_label = QLabel(f"Name: {item.get('Name', '')}")
    category_label = QLabel(f"Category: {item.get('Category', '')}")
    date_label = QLabel(f"Date: {item.get('DateLost') or item.get('DateFound', '')}")
    location_label = QLabel(f"Location: {item.get('LocationLost') or item.get('LocationFound', '')}")

    for lbl in (status_label, name_label, category_label, date_label, location_label):
        lbl.setWordWrap(True)
        lbl.setAlignment(Qt.AlignCenter)
        layout.addWidget(lbl)

    layout.insertWidget(0, image_label)
    return frame

def load_recent_items(container_layout, recent_items):
    # Clear existing widgets
    for i in reversed(range(container_layout.count())):
        widget = container_layout.itemAt(i).widget()
        if widget:
            widget.setParent(None)

    # Add new items
    columns = 3
    for index, item in enumerate(recent_items):
        row = index // columns
        col = index % columns
        card = create_item_card(item)
        container_layout.addWidget(card, row, col)