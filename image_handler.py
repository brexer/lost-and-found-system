from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os
import shutil

def upload_image(self):
    file_path, _ = QFileDialog.getOpenFileName(
        self,
        "Select Image",
        "",
        "Images (*.png *.jpg *.jpeg *.bmp)"
    )
    if file_path:
        self.display_image(file_path)
        self.current_image_path = file_path  # save item

def display_image(self, image_path):
    pixmap = QPixmap(image_path).scaled(
        self.labelImagePreview.size(),
        Qt.KeepAspectRatio,
        Qt.SmoothTransformation
    )
    self.labelImagePreview.setPixmap(pixmap) # change to QLabel sa kung asa ang preview

def save_uploaded_image(source_path, item_id):
    rel_path = f"assets/itemimg/{item_id}.png"
    abs_path = os.path.abspath(rel_path)
    os.makedirs(os.path.dirname(abs_path), exist_ok=True)
    shutil.copy(source_path, abs_path)
    return rel_path


