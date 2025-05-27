from PyQt5.QtWidgets import QFileDialog, QLabel, QDialog, QVBoxLayout, QPushButton, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os
import shutil

class ImageHandler:
    def __init__(self, label_preview):
        self.labelImagePreview = label_preview
        self.current_image_path = None

    def upload_image(self, parent=None):
        file_path, _ = QFileDialog.getOpenFileName(
            parent,
            "Select Image",
            "",
            "Images (*.png *.jpg *.jpeg *.bmp)"
        )
        if file_path:
            self.display_image(file_path)
            self.current_image_path = file_path

    def display_image(self, image_path):
        pixmap = QPixmap(image_path).scaled(
            self.labelImagePreview.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.labelImagePreview.setPixmap(pixmap)
        
    @staticmethod
    def save_uploaded_item_image(source_path, item_id):
        rel_path = f"assets/itemimg/{item_id}.png"
        abs_path = os.path.abspath(rel_path)
        os.makedirs(os.path.dirname(abs_path), exist_ok=True)
        shutil.copy(source_path, abs_path)
        return rel_path

    @staticmethod
    def save_uploaded_proof_id(source_path, person_id):
        rel_path = f"assets/proofid/{person_id}.png"
        abs_path = os.path.abspath(rel_path)
        os.makedirs(os.path.dirname(abs_path), exist_ok=True)
        shutil.copy(source_path, abs_path)
        return rel_path
    
class ClickableLabel(QLabel):
    def __init__(self, image_path, item_id=None, on_remove_callback=None, parent=None):
        super().__init__(parent)
        self.image_path = image_path
        self.item_id = item_id  # optional: link to DB ID
        self.on_remove_callback = on_remove_callback  # function to run when removed
        self.setCursor(Qt.PointingHandCursor)

    def mousePressEvent(self, event):
        if self.image_path:
            self.show_preview_dialog()

    def show_preview_dialog(self):
        dialog = QDialog()
        dialog.setWindowTitle("Proof Preview")
        layout = QVBoxLayout()

        image_label = QLabel()
        pixmap = QPixmap(self.image_path)
        if not pixmap.isNull():
            image_label.setPixmap(pixmap.scaled(400, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            image_label.setText("Image not found")
        image_label.setPixmap(pixmap.scaled(400, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        image_label.setAlignment(Qt.AlignCenter)

        remove_btn = QPushButton("Remove Image")
        remove_btn.clicked.connect(lambda: self.remove_image(dialog))

        layout.addWidget(image_label)
        layout.addWidget(remove_btn)
        dialog.setLayout(layout)
        dialog.exec_()

    def remove_image(self, dialog):
        reply = QMessageBox.question(
            self,
            "Remove Image",
            "Are you sure you want to remove this image?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            if os.path.exists(self.image_path):
                os.remove(self.image_path)

            if self.on_remove_callback:
                self.on_remove_callback(self.item_id, self.image_path)

            dialog.accept()