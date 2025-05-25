MAIN_WINDOW_STYLE = """
    /* Main window background */
    QMainWindow {
        background-color: #2c3e50;  /* Dark background for contrast */
        font-family: 'Century Gothic', 'Segoe UI', sans-serif;
    }
    
    /* ===== SIDEBAR BUTTONS ===== */
    QPushButton {
        color: white;
        border: none;
        padding: 8px 15px;
        border-radius: 4px;
        background-color: rgba(255, 255, 255, 0.2);
        font-family: 'Century Gothic';
        font-weight: 600;
        font-size: 15px;
        letter-spacing: 0.5px;
        text-align: left;
        min-width: 160px;  /* Wider for sidebar */
    }
    
    QPushButton:hover {
        background-color: rgba(255, 255, 255, 0.3);
    }
    
    QPushButton:pressed {
        background-color: rgba(255, 255, 255, 0.1);
    }
    
    /* Active page indicator */
    QPushButton[active="true"] {
        background-color: #ffc107;  /* Yellow to match tables */
        color: #2c3e50;  /* Dark text for contrast */
        font-weight: 700;
    }
    
    /* ===== ACTION BUTTONS (Delete/Update/etc) ===== */
    QPushButton[actionButton="true"] {
        background-color: #ffc107;  /* Yellow */
        color: #2c3e50;  /* Dark text */
        text-align: center;
        min-width: 80px;
        padding: 6px 12px;
        margin: 2px;
        font-size: 14px;
    }
    
    QPushButton[actionButton="true"]:hover {
        background-color: #ffca28;  /* Lighter yellow */
    }
    
    QPushButton[danger="true"] {
        background-color: #e53935;  /* Red for delete */
        color: white;
    }
    
    /* ===== YELLOW-THEMED TABLES ===== */
    QTableWidget {
        background-color: white;
        border: 1px solid #e0e0e0;
        gridline-color: #e0e0e0;
        font-size: 13px;
        selection-background-color: #fff9e6;
        selection-color: black;
    }
    
    QHeaderView::section {
        background-color: #ffc107;  /* Yellow */
        color: #2c3e50;  /* Dark text */
        padding: 6px;
        border: none;
        font-size: 13px;
        font-weight: bold;
    }
    
    /* ===== CONTENT AREAS ===== */
    QWidget[page="true"] {
        background-color: white;
        border-radius: 8px;
        margin: 10px;
        padding: 15px;
        border: 1px solid #e0e0e0;
    }
    
    /* ===== SCROLLBARS ===== */
    QScrollBar:vertical {
        border: none;
        background: #f0f0f0;
        width: 10px;
    }
    
    QScrollBar::handle:vertical {
        background: #95a5a6;
        min-height: 20px;
        border-radius: 5px;
    }
"""
