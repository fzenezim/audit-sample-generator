# Audit Sample Generator 📊

A professional, lightweight application to generate random audit samples with reproducibility support via seeds.

## 🚀 Features
- **Random Sampling:** Selects a specific number of items from a provided list.
- **Seed Support:** Use a seed to replicate the exact same sample for the same universe of items (essential for audit trails).
- **Modern UI:** Dark-themed interface built with `customtkinter`.
- **One-Click Copy:** Quickly copy results to your clipboard for Excel/Reports.

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/fzenezim/audit-sample-generator.git
cd audit-sample-generator
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
python main.py
```

## 📦 Creating the Executable (.exe)

To convert this script into a standalone Windows executable, use **PyInstaller**:

```bash
pip install pyinstaller
pyinstaller --noconsole --onefile --collect-all customtkinter main.py
```

The executable will be located in the `dist/` folder.

## 📋 How to use
1. Enter the **Sample Size** (how many items you want to draw).
2. Enter a **Seed** (optional, but recommended for audit reproducibility).
3. Paste your **Item List** (one item per line).
4. Click **Generate Sample**.
5. Copy the result and paste it into your audit report.
