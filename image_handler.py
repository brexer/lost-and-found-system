from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

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
    self.labelImagePreview.setPixmap(pixmap)
