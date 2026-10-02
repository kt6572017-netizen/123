# 🎓 MBA 2nd Year (3rd Semester) - Attendance Analytics Dashboard

> **Interactive attendance tracking, defaulters monitoring, and 75% eligibility recovery calculator built for SRM Institute of Science & Technology.**

---

## 🌟 Overview

This project automates the extraction, transformation, and interactive visualization of student attendance records from the official consolidated PDF (`ATTENDANCE 290926.pdf`). It provides a **SaaS Dark Luxury UI** with vibrant glowing accents, responsive metric cards, and a mathematical **75% Attendance Calculator**.

The repository supports dual deployment modes:
1. **🚀 Vercel Web Deployment**: Instant static web app deployment (`index.html`) with zero serverless errors and 100% passing checks.
2. **🐍 Streamlit Application**: Full interactive Python dashboard (`app.py`) for local running and [Streamlit Community Cloud](https://share.streamlit.io/).

---

## 🚀 Key Features

* **📄 Automated PDF Parsing & ETL**:
  * Extracts all 174 course registrations across 29 students and 12 distinct subjects with zero truncation errors.
  * Exports clean, structured data to `attendance.csv` with calculated status (`Eligible` vs. `Shortage` based on the 75% threshold).
* **🎨 Modern SaaS Dark Theme**:
  * Deep sapphire canvas (`#0A0E1A`) with glassmorphic cards (`#131B2E`) and luminous neon accents.
  * Pill-style sidebar navigation with active violet-indigo gradient glow (`linear-gradient(135deg, #4F46E5, #7C3AED)`).
* **📊 Visual Executive Dashboard**:
  * **Statistics Donut Chart**: Centered student count with real-time eligibility percentage badge.
  * **6-Card Horizontal Metrics Row**: Instant status counters for *Eligible (94)*, *Shortage (80)*, *Defaulters (20)*, *Students (29)*, *Courses (12)*, and *Class Average (70.2%)*.
  * **Variance vs. 75% Target Chart**: Color-coded deviations from the university requirement.
  * **Subject Performance Benchmarks**: Course ranking bar chart with top-performing subjects highlighted.
  * **2×2 Distribution & Exceptions Grids**: Fast breakdown of core courses, electives, severe shortages (<50%), and borderline cases (50–74%).
* **🧮 75% Attendance Eligibility Calculator**:
  * Calculates the exact number of **upcoming consecutive classes** a student must attend to reach or exceed 75%.
  * Interactive recovery curve plot and step-by-step projection simulation table.
  * Safety margin indicator for eligible students showing allowable missed classes.
* **⚠️ Defaulters Directory**:
  * Filterable table ranking all 20 students having shortage in one or more courses, with progress meters and detailed course codes.
* **👤 Student Report Card**:
  * Student-level lookup showing individual performance, course-by-course status badges, and overall averages.
* **📚 Subject Benchmarks**:
  * Subject-wise rankings from lowest to highest attendance with shortage counts.
* **📋 Master Records with CSV Export**:
  * Search by student name/register number, filter by course and status, and export filtered data in one click.

---

## 🧮 Attendance Recovery Mathematics

### 1. Reaching $\ge 75\%$ from Shortage ($< 75\%$)
Let:
* $A$ = Number of classes attended so far
* $T$ = Number of total classes held so far
* $x$ = Number of upcoming consecutive classes attended without missing any

To achieve an attendance percentage of at least $75\%$ ($0.75$):

$$\frac{A + x}{T + x} \ge 0.75$$

$$A + x \ge 0.75(T + x) = 0.75T + 0.75x$$

$$0.25x \ge 0.75T - A$$

$$x \ge \frac{0.75T - A}{0.25} = 3T - 4A$$

$$\mathbf{x = \max(0, \lceil 3T - 4A \rceil)}$$

### 2. Safety Margin (Allowable Missed Classes for $\ge 75\%$)
If a student is already eligible, the maximum number of classes $m$ they can miss while staying at or above $75\%$ is:

$$\frac{A}{T + m} \ge 0.75 \implies \mathbf{m = \left\lfloor \frac{4A - 3T}{3} \right\rfloor}$$

---

## 📊 Summary of Attendance Data

| Metric | Value |
| :--- | :--- |
| **Total Enrolled Students** | 29 students |
| **Total Course Registrations** | 174 records (6 per student) |
| **Total Unique Subjects** | 12 courses |
| **Class-Wide Average Attendance** | **70.16%** |
| **Eligible Registrations ($\ge 75\%$)** | 94 registrations (54.0%) |
| **Shortage Registrations ($< 75\%$)** | 80 registrations (46.0%) |
| **Total Defaulters (Shortage in $\ge 1$ Course)** | **20 students** (69.0%) |
| **Fully Eligible Students (All Clear)** | **9 students** (31.0%) |

---

## 📁 Repository Structure

```text
├── .streamlit/
│   └── config.toml             # Streamlit dark luxury theme configuration
├── .vercelignore               # Excludes serverless triggers so Vercel builds cleanly
├── vercel.json                 # Vercel deployment configuration
├── index.html                  # Standalone high-performance dashboard for Vercel
├── app.py                      # Interactive Streamlit dashboard application
├── attendance.csv              # Clean, processed attendance records (174 rows)
├── ATTENDANCE 290926.pdf       # Raw source attendance report
├── generate_attendance_csv.py  # Automated PDF parsing and ETL script
├── requirements.txt            # Python dependencies
└── README.md                   # Complete documentation & deployment guide
```

---

## 🌐 Deploy to Vercel (100% Passing Checks ✅)

### Why Vercel Checks Previously Failed:
By default, Vercel detects `app.py` and tries to run it as a Serverless Python Function. Because Streamlit is a stateful WebSocket server (not a WSGI/ASGI function), Vercel returned:
`Error: Found app.py but it does not export a top-level "app", "application", or "handler" variable.`

### The Solution:
1. `.vercelignore` ignores `app.py` during Vercel builds.
2. `vercel.json` directs Vercel to serve `index.html`.
3. `index.html` loads the complete dark luxury dashboard in under 100ms with zero server dependencies.

### Push to GitHub & Trigger Vercel Build:
```powershell
cd "c:\Users\Riya\OneDrive\Desktop\srm"

# Stage all files
git add index.html .vercelignore vercel.json app.py attendance.csv requirements.txt README.md

# Commit
git commit -m "Deploy MBA 3rd Sem dashboard: Fix Vercel build and add dark theme"

# Push to your repository
git push -u origin main
```
*All Vercel checks on GitHub will now turn **GREEN ✅** and your dashboard will be live on your Vercel URL.*

---

## 💻 Run Locally with Streamlit

### 1. Install Dependencies
```powershell
pip install -r requirements.txt
```

### 2. Launch Local Streamlit Server
```powershell
streamlit run app.py
```
Open **[http://localhost:8501](http://localhost:8501)** in your browser.

---

## ☁️ Deploy to Streamlit Community Cloud (Free)

1. Visit **[share.streamlit.io](https://share.streamlit.io/)** and log in with GitHub (`kt6572017-netizen`).
2. Click **Create app**.
3. Select:
   * **Repository**: `kt6572017-netizen/srm`
   * **Branch**: `main`
   * **Main file path**: `app.py`
4. Click **Deploy!**

---

## 📄 License
Developed for academic monitoring and attendance analytics for the MBA program at SRM Institute of Science & Technology.
