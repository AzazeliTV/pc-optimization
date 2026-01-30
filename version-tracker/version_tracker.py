#!/usr/bin/env python3
"""
Version Tracker - Desktop App für Software/Treiber Updates
Erstellt für AzazeliTV's Gaming PC Setup
"""

import sys
import json
import webbrowser
from pathlib import Path
from datetime import datetime, timedelta
from typing import Optional

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTableWidget, QTableWidgetItem, QPushButton, QLabel, QLineEdit,
    QHeaderView, QMessageBox, QSystemTrayIcon, QMenu, QStyle,
    QDialog, QFormLayout, QComboBox, QFrame
)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QIcon, QColor, QAction, QFont

# Standardmäßige Software-Liste für Gaming PC
DEFAULT_SOFTWARE = [
    {
        "name": "NVIDIA Treiber",
        "category": "Treiber",
        "version": "",
        "url": "https://www.nvidia.com/Download/index.aspx",
        "last_checked": ""
    },
    {
        "name": "AMD Chipset",
        "category": "Treiber",
        "version": "",
        "url": "https://www.amd.com/en/support",
        "last_checked": ""
    },
    {
        "name": "BIOS (X870E Hero)",
        "category": "Firmware",
        "version": "",
        "url": "https://rog.asus.com/de/motherboards/rog-crosshair/rog-crosshair-x870e-hero/helpdesk_bios/",
        "last_checked": ""
    },
    {
        "name": "Samsung Magician",
        "category": "Software",
        "version": "",
        "url": "https://semiconductor.samsung.com/consumer-storage/support/tools/",
        "last_checked": ""
    },
    {
        "name": "Samsung 9100 PRO Firmware",
        "category": "Firmware",
        "version": "",
        "url": "https://semiconductor.samsung.com/consumer-storage/support/tools/",
        "last_checked": ""
    },
    {
        "name": "Wootility",
        "category": "Peripherie",
        "version": "",
        "url": "https://wooting.io/wootility",
        "last_checked": ""
    },
    {
        "name": "Razer Synapse",
        "category": "Peripherie",
        "version": "",
        "url": "https://www.razer.com/synapse-3",
        "last_checked": ""
    },
    {
        "name": "SteelSeries GG",
        "category": "Peripherie",
        "version": "",
        "url": "https://steelseries.com/gg",
        "last_checked": ""
    },
    {
        "name": "Elgato Wave Link",
        "category": "Streaming",
        "version": "",
        "url": "https://www.elgato.com/downloads",
        "last_checked": ""
    },
    {
        "name": "Elgato Stream Deck",
        "category": "Streaming",
        "version": "",
        "url": "https://www.elgato.com/downloads",
        "last_checked": ""
    },
    {
        "name": "OBS Studio",
        "category": "Streaming",
        "version": "",
        "url": "https://obsproject.com/download",
        "last_checked": ""
    },
    {
        "name": "Discord",
        "category": "Kommunikation",
        "version": "",
        "url": "https://discord.com/download",
        "last_checked": ""
    },
    {
        "name": "iCUE (Corsair)",
        "category": "Peripherie",
        "version": "",
        "url": "https://www.corsair.com/icue",
        "last_checked": ""
    },
    {
        "name": "ASUS Armoury Crate",
        "category": "Software",
        "version": "",
        "url": "https://www.asus.com/supportonly/armoury-crate/",
        "last_checked": ""
    },
    {
        "name": "DisplayWidget (OLED)",
        "category": "Monitor",
        "version": "",
        "url": "https://rog.asus.com/",
        "last_checked": ""
    }
]

DATA_FILE = Path(__file__).parent / "versions.json"


class AddSoftwareDialog(QDialog):
    """Dialog zum Hinzufügen neuer Software"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Software hinzufügen")
        self.setMinimumWidth(400)

        layout = QFormLayout(self)

        self.name_input = QLineEdit()
        self.category_combo = QComboBox()
        self.category_combo.addItems(["Treiber", "Firmware", "Software", "Peripherie", "Streaming", "Kommunikation", "Monitor", "Sonstiges"])
        self.category_combo.setEditable(True)
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("https://...")

        layout.addRow("Name:", self.name_input)
        layout.addRow("Kategorie:", self.category_combo)
        layout.addRow("Download-URL:", self.url_input)

        btn_layout = QHBoxLayout()
        save_btn = QPushButton("Hinzufügen")
        save_btn.clicked.connect(self.accept)
        cancel_btn = QPushButton("Abbrechen")
        cancel_btn.clicked.connect(self.reject)
        btn_layout.addWidget(save_btn)
        btn_layout.addWidget(cancel_btn)
        layout.addRow(btn_layout)

    def get_data(self):
        return {
            "name": self.name_input.text(),
            "category": self.category_combo.currentText(),
            "version": "",
            "url": self.url_input.text(),
            "last_checked": ""
        }


class VersionTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Version Tracker - Gaming PC")
        self.setMinimumSize(900, 600)

        # Daten laden
        self.software_list = self.load_data()

        # UI erstellen
        self.init_ui()

        # Timer für Erinnerungen (alle 4 Stunden prüfen)
        self.reminder_timer = QTimer()
        self.reminder_timer.timeout.connect(self.check_reminders)
        self.reminder_timer.start(4 * 60 * 60 * 1000)  # 4 Stunden

        # Beim Start einmal prüfen
        QTimer.singleShot(2000, self.check_reminders)

    def init_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setSpacing(10)
        layout.setContentsMargins(15, 15, 15, 15)

        # Header
        header = QLabel("🖥️ Version Tracker")
        header.setFont(QFont("Segoe UI", 18, QFont.Weight.Bold))
        header.setStyleSheet("color: #00ff88;")
        layout.addWidget(header)

        subtitle = QLabel("Behalte deine Software & Treiber im Blick")
        subtitle.setStyleSheet("color: #888; margin-bottom: 10px;")
        layout.addWidget(subtitle)

        # Status-Leiste
        self.status_frame = QFrame()
        self.status_frame.setStyleSheet("""
            QFrame {
                background: #1a1a2e;
                border-radius: 8px;
                padding: 10px;
            }
        """)
        status_layout = QHBoxLayout(self.status_frame)
        self.status_label = QLabel()
        status_layout.addWidget(self.status_label)
        layout.addWidget(self.status_frame)

        # Tabelle
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "Software", "Kategorie", "Meine Version", "Zuletzt geprüft", "Status", "Aktionen"
        ])

        # Spaltenbreiten
        header_view = self.table.horizontalHeader()
        header_view.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header_view.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header_view.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header_view.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        header_view.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)
        header_view.setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)

        self.table.setStyleSheet("""
            QTableWidget {
                background-color: #0f0f19;
                border: 1px solid #2a2a4a;
                border-radius: 8px;
                gridline-color: #2a2a4a;
            }
            QTableWidget::item {
                padding: 8px;
                border-bottom: 1px solid #1a1a2e;
            }
            QTableWidget::item:selected {
                background-color: #00ff8833;
            }
            QHeaderView::section {
                background-color: #14142a;
                color: #00ff88;
                padding: 10px;
                border: none;
                font-weight: bold;
            }
        """)

        layout.addWidget(self.table)

        # Buttons
        btn_layout = QHBoxLayout()

        add_btn = QPushButton("➕ Software hinzufügen")
        add_btn.clicked.connect(self.add_software)
        add_btn.setStyleSheet(self.get_button_style("#3b82f6"))

        check_all_btn = QPushButton("🔄 Alle prüfen (Links öffnen)")
        check_all_btn.clicked.connect(self.check_all_updates)
        check_all_btn.setStyleSheet(self.get_button_style("#00ff88"))

        save_btn = QPushButton("💾 Speichern")
        save_btn.clicked.connect(self.save_data)
        save_btn.setStyleSheet(self.get_button_style("#aa44ff"))

        btn_layout.addWidget(add_btn)
        btn_layout.addWidget(check_all_btn)
        btn_layout.addStretch()
        btn_layout.addWidget(save_btn)

        layout.addLayout(btn_layout)

        # Tabelle füllen
        self.refresh_table()
        self.update_status()

        # Styling
        self.setStyleSheet("""
            QMainWindow {
                background-color: #0a0a0f;
            }
            QLabel {
                color: #ffffff;
            }
            QLineEdit {
                background-color: #14142a;
                border: 1px solid #2a2a4a;
                border-radius: 4px;
                padding: 5px;
                color: #ffffff;
            }
            QLineEdit:focus {
                border-color: #00ff88;
            }
        """)

    def get_button_style(self, color):
        return f"""
            QPushButton {{
                background-color: {color}33;
                color: {color};
                border: 1px solid {color};
                border-radius: 6px;
                padding: 8px 16px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {color}66;
            }}
        """

    def refresh_table(self):
        self.table.setRowCount(len(self.software_list))

        for row, software in enumerate(self.software_list):
            # Name
            name_item = QTableWidgetItem(software["name"])
            name_item.setFlags(name_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            self.table.setItem(row, 0, name_item)

            # Kategorie
            cat_item = QTableWidgetItem(software.get("category", ""))
            cat_item.setFlags(cat_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            cat_item.setForeground(QColor("#888"))
            self.table.setItem(row, 1, cat_item)

            # Version (editierbar)
            version_input = QLineEdit(software.get("version", ""))
            version_input.setPlaceholderText("z.B. 572.16")
            version_input.textChanged.connect(lambda text, r=row: self.update_version(r, text))
            self.table.setCellWidget(row, 2, version_input)

            # Zuletzt geprüft
            last_checked = software.get("last_checked", "")
            last_item = QTableWidgetItem(last_checked if last_checked else "Nie")
            last_item.setFlags(last_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            self.table.setItem(row, 3, last_item)

            # Status
            status = self.get_status(last_checked)
            status_item = QTableWidgetItem(status["text"])
            status_item.setForeground(QColor(status["color"]))
            status_item.setFlags(status_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            self.table.setItem(row, 4, status_item)

            # Aktionen
            action_widget = QWidget()
            action_layout = QHBoxLayout(action_widget)
            action_layout.setContentsMargins(4, 4, 4, 4)
            action_layout.setSpacing(4)

            check_btn = QPushButton("🔗")
            check_btn.setToolTip("Download-Seite öffnen")
            check_btn.setFixedSize(30, 30)
            check_btn.clicked.connect(lambda _, url=software["url"], r=row: self.open_url(url, r))
            check_btn.setStyleSheet("""
                QPushButton {
                    background: #00ff8833;
                    border: 1px solid #00ff88;
                    border-radius: 4px;
                }
                QPushButton:hover {
                    background: #00ff8866;
                }
            """)

            delete_btn = QPushButton("🗑️")
            delete_btn.setToolTip("Entfernen")
            delete_btn.setFixedSize(30, 30)
            delete_btn.clicked.connect(lambda _, r=row: self.delete_software(r))
            delete_btn.setStyleSheet("""
                QPushButton {
                    background: #ff446633;
                    border: 1px solid #ff4466;
                    border-radius: 4px;
                }
                QPushButton:hover {
                    background: #ff446666;
                }
            """)

            action_layout.addWidget(check_btn)
            action_layout.addWidget(delete_btn)
            self.table.setCellWidget(row, 5, action_widget)

    def get_status(self, last_checked: str) -> dict:
        if not last_checked:
            return {"text": "⚠️ Nie geprüft", "color": "#ffaa00"}

        try:
            last_date = datetime.strptime(last_checked, "%d.%m.%Y")
            days_ago = (datetime.now() - last_date).days

            if days_ago > 30:
                return {"text": f"🔴 {days_ago} Tage", "color": "#ff4466"}
            elif days_ago > 14:
                return {"text": f"🟡 {days_ago} Tage", "color": "#ffaa00"}
            else:
                return {"text": f"🟢 {days_ago} Tage", "color": "#00ff88"}
        except:
            return {"text": "⚠️ Ungültig", "color": "#ffaa00"}

    def update_version(self, row: int, text: str):
        if row < len(self.software_list):
            self.software_list[row]["version"] = text

    def update_status(self):
        total = len(self.software_list)
        outdated = 0
        never_checked = 0

        for software in self.software_list:
            last_checked = software.get("last_checked", "")
            if not last_checked:
                never_checked += 1
            else:
                try:
                    last_date = datetime.strptime(last_checked, "%d.%m.%Y")
                    if (datetime.now() - last_date).days > 30:
                        outdated += 1
                except:
                    pass

        ok_count = total - outdated - never_checked

        status_text = f"📊 {total} Software | ✅ {ok_count} OK | ⚠️ {never_checked} nie geprüft | 🔴 {outdated} überfällig (>30 Tage)"
        self.status_label.setText(status_text)

        if outdated > 0:
            self.status_frame.setStyleSheet("""
                QFrame {
                    background: #ff446622;
                    border: 1px solid #ff4466;
                    border-radius: 8px;
                    padding: 10px;
                }
            """)
        elif never_checked > 0:
            self.status_frame.setStyleSheet("""
                QFrame {
                    background: #ffaa0022;
                    border: 1px solid #ffaa00;
                    border-radius: 8px;
                    padding: 10px;
                }
            """)
        else:
            self.status_frame.setStyleSheet("""
                QFrame {
                    background: #00ff8822;
                    border: 1px solid #00ff88;
                    border-radius: 8px;
                    padding: 10px;
                }
            """)

    def open_url(self, url: str, row: int):
        webbrowser.open(url)
        # Datum aktualisieren
        today = datetime.now().strftime("%d.%m.%Y")
        self.software_list[row]["last_checked"] = today
        self.refresh_table()
        self.update_status()
        self.save_data()

    def check_all_updates(self):
        reply = QMessageBox.question(
            self,
            "Alle prüfen",
            f"Möchtest du alle {len(self.software_list)} Download-Seiten öffnen?\n\n"
            "Dies öffnet viele Browser-Tabs!",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            today = datetime.now().strftime("%d.%m.%Y")
            for i, software in enumerate(self.software_list):
                webbrowser.open(software["url"])
                self.software_list[i]["last_checked"] = today

            self.refresh_table()
            self.update_status()
            self.save_data()

            QMessageBox.information(
                self,
                "Fertig",
                f"✅ {len(self.software_list)} Download-Seiten geöffnet!\n\n"
                "Prüfe die Versionen und aktualisiere sie hier."
            )

    def add_software(self):
        dialog = AddSoftwareDialog(self)
        if dialog.exec():
            data = dialog.get_data()
            if data["name"]:
                self.software_list.append(data)
                self.refresh_table()
                self.update_status()
                self.save_data()

    def delete_software(self, row: int):
        if row < len(self.software_list):
            name = self.software_list[row]["name"]
            reply = QMessageBox.question(
                self,
                "Löschen",
                f"'{name}' wirklich entfernen?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )

            if reply == QMessageBox.StandardButton.Yes:
                del self.software_list[row]
                self.refresh_table()
                self.update_status()
                self.save_data()

    def check_reminders(self):
        """Prüft ob Updates überfällig sind"""
        outdated = []
        for software in self.software_list:
            last_checked = software.get("last_checked", "")
            if last_checked:
                try:
                    last_date = datetime.strptime(last_checked, "%d.%m.%Y")
                    if (datetime.now() - last_date).days > 30:
                        outdated.append(software["name"])
                except:
                    pass

        if outdated and len(outdated) <= 5:
            # Nur anzeigen wenn Fenster sichtbar ist
            if self.isVisible():
                self.statusBar().showMessage(
                    f"⚠️ {len(outdated)} Software überfällig: {', '.join(outdated[:3])}{'...' if len(outdated) > 3 else ''}",
                    10000
                )

    def load_data(self) -> list:
        if DATA_FILE.exists():
            try:
                with open(DATA_FILE, "r", encoding="utf-8") as f:
                    return json.load(f)
            except:
                pass
        return DEFAULT_SOFTWARE.copy()

    def save_data(self):
        try:
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(self.software_list, f, indent=2, ensure_ascii=False)
            self.statusBar().showMessage("✅ Gespeichert!", 3000)
        except Exception as e:
            QMessageBox.warning(self, "Fehler", f"Speichern fehlgeschlagen: {e}")

    def closeEvent(self, event):
        self.save_data()
        event.accept()


def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    # Dark Palette
    from PyQt6.QtGui import QPalette
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor("#0a0a0f"))
    palette.setColor(QPalette.ColorRole.WindowText, QColor("#ffffff"))
    palette.setColor(QPalette.ColorRole.Base, QColor("#14142a"))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor("#1a1a2e"))
    palette.setColor(QPalette.ColorRole.Text, QColor("#ffffff"))
    palette.setColor(QPalette.ColorRole.Button, QColor("#14142a"))
    palette.setColor(QPalette.ColorRole.ButtonText, QColor("#ffffff"))
    palette.setColor(QPalette.ColorRole.Highlight, QColor("#00ff88"))
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor("#000000"))
    app.setPalette(palette)

    window = VersionTracker()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
