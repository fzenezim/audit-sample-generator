# Audit Sample Generator 📊

A professional, lightweight application to generate random audit samples with reproducibility support via seeds and professional evidence generation.

## 🚀 Features (v2.1)
- **Numerical Sampling:** Simply enter the total universe size and the desired sample size.
- **Seed Support:** Use a seed to replicate the exact same sample for the same universe of items (essential for audit trails).
- **Random Seed Generator:** One-click button to generate a unique random seed.
- **Digital Evidence (Certificates):** Generates a professional `.png` report with a timestamp, seed, and the sorted list of items. This report is generated digitally, ensuring perfect quality regardless of screen resolution or monitor scaling.
- **Modern UI:** Dark-themed, responsive interface built with `customtkinter`.
- **One-Click Copy:** Quickly copy results to your clipboard for Excel or official reports.

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

## 📦 Creating the Professional Executable (.exe)

To convert this script into a standalone Windows executable with a professional name, use **PyInstaller**:

```bash
pip install pyinstaller
pyinstaller --noconsole --onefile --collect-all customtkinter --name "AuditSampleGenerator" main.py
```

The executable will be located in the `dist/` folder as `AuditSampleGenerator.exe`.

## 📋 How to use
1. Enter the **Universe Size** (Total number of items in your population).
2. Enter the **Sample Size** (How many items you need to draw).
3. **Seed (Optional):** Enter a specific number to lock the result or click the 🎲 button for a random one.
4. Click **Generate Sample**.
5. **Save Evidence:** Click the 📸 button to generate a digital certificate of the sampling process for your audit papers.
6. **Copy Result:** Copy the list and paste it into your working papers.
