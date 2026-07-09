# Audit Sample Generator 📊

A professional, lightweight application to generate random audit samples with reproducibility support via seeds.

## 🚀 Features (v1.2)
- **Numerical Sampling:** Simply enter the total universe size and the desired sample size.
- **Seed Support:** Use a seed to replicate the exact same sample for the same universe of items (essential for audit trails).
- **Random Seed Generator:** One-click button to generate a unique random seed.
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
1. Enter the **Universe Size** (Total number of items in your population).
2. Enter the **Sample Size** (How many items you need to draw).
3. **Seed (Optional):** Enter a specific number to lock the result or click the 🎲 button for a random one.
4. Click **Generate Sample**.
5. Copy the result (Format: `1 - item X`) and paste it into your audit report.
