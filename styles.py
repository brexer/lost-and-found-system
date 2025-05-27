MAIN_WINDOW_STYLE = """
    /* Main window background */
    QMainWindow {
        background-color: #2c3e50;
        font-family: 'Century Gothic';
    }
    
    /* ===== NAVIGATION BUTTONS ===== */
    /* Style for ALL navigation buttons */
    QPushButton#reviewItemsButton,
    QPushButton#homeButton,
    QPushButton#manageItemsButton,
    QPushButton#managePersonsButton,
    QPushButton#itemHistoryButton,
    QPushButton#claimItemButton,
    QPushButton#reportItemButton,
    QPushButton#surrenderItemButton {
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
        min-width: 160px;
        max-width: 160px;
    }
    
    /* Hover and pressed states for ALL */
    QPushButton#reviewItemsButton,
    QPushButton#homeButton:hover,
    QPushButton#manageItemsButton:hover,
    QPushButton#managePersonsButton:hover,
    QPushButton#itemHistoryButton:hover,
    QPushButton#claimItemButton:hover,
    QPushButton#reportItemButton:hover,
    QPushButton#surrenderItemButton:hover {
        background-color: rgba(255, 255, 255, 0.3);
    }
    QPushButton#reviewItemsButton,
    QPushButton#homeButton:pressed,
    QPushButton#manageItemsButton:pressed,
    QPushButton#managePersonsButton:pressed,
    QPushButton#itemHistoryButton:pressed,
    QPushButton#claimItemButton:pressed,
    QPushButton#reportItemButton:pressed,
    QPushButton#surrenderItemButton:pressed {
        background-color: rgba(255, 255, 255, 0.1);
    }
    
    /* Active state for ALL */
    QPushButton#reviewItemsButton[active="true"],
    QPushButton#homeButton[active="true"],
    QPushButton#manageItemsButton[active="true"],
    QPushButton#managePersonsButton[active="true"],
    QPushButton#itemHistoryButton[active="true"],
    QPushButton#claimItemButton[active="true"],
    QPushButton#reportItemButton[active="true"],
    QPushButton#surrenderItemButton[active="true"] {
        background-color: #ffc107;
        color: #2c3e50;
        font-weight: 700;
    }
    
        QPushButton#reportItem,
    QPushButton#surrenderItem {
        min-width: 110px;
        max-width: 110px;
        min-height: 20px;
        max-height: 20px;
        padding: 20px 20px;
        font-size: 14px;
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
        background-color: #ffc107;
        color: #2c3e50;
        padding: 6px;
        border: none;
        font-size: 13px;
        font-weight: bold;
    }
    QPushButton#reportItem,
    QPushButton#surrenderItem {
    color: white;
    border: none;
    min-width: 110px;
    max-width: 110px;
    min-height: 20px;
    max-height: 20px;
    padding: 6px 12px;  /* Reduced padding for compact look */
    border-radius: 10px;  /* Increased for rounder buttons */
    background-color: rgba(255, 255, 255, 0.2);
    font-family: 'Century Gothic';  /* Matching home button font */
    font-weight: 600;  /* Matching home button weight */
    font-size: 12px;  /* Smaller than home button's 15px */
    letter-spacing: 0.5px;  /* Matching home button letter spacing */
    text-align: center;  /* Centered for compact buttons */
}
    
    QPushButton#reportItem:hover,
    QPushButton#surrenderItem:hover {
        background-color: rgba(255, 255, 255, 0.3);
    }
    
    QPushButton#reportItem:pressed,
    QPushButton#surrenderItem:pressed {
        background-color: rgba(255, 255, 255, 0.1);
    }
    
    QPushButton#reportItem[active="true"],
    QPushButton#surrenderItem[active="true"] {
        background-color: #ffc107;
        color: #2c3e50;
        font-weight: 700;
    }

"""