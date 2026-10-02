import pypdf
import re
import pandas as pd

reader = pypdf.PdfReader('ATTENDANCE 290926.pdf')
all_lines = []
for i, page in enumerate(reader.pages):
    text = page.extract_text()
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith('CONSOLIDATED') or 'Overall Percentage' in line:
            continue
        all_lines.append(line)

pattern = re.compile(r'^(\d+)\s+(RA\w+)\s+(.*?)\s+(MBG\w+)\s+(.*?)(?:\s+)?(\d+\.\d{2})$')

records = []
for line in all_lines:
    m = pattern.match(line)
    if not m:
        raise ValueError(f"Line didn't match: {line}")
    sno, reg, name, code, title, pct = m.groups()
    records.append({
        'S.No': int(sno),
        'Register_No': reg.strip(),
        'Student_Name': name.strip(),
        'Course_Code': code.strip(),
        'Course_Title': title.strip(),
        'Attendance_Percentage': pct.strip()
    })

df = pd.DataFrame(records)

# Check sequence of S.No
expected_snos = list(range(1, 175))
actual_snos = df['S.No'].tolist()
assert actual_snos == expected_snos, f"S.No mismatch: {actual_snos[:10]}"

# Check percentages
df['Attendance_Percentage_Num'] = pd.to_numeric(df['Attendance_Percentage'])
assert df['Attendance_Percentage_Num'].isna().sum() == 0, "Null percentages found"

# Calculate Status: mark "Shortage" if percentage < 75%, otherwise "Eligible"
df['Status'] = df['Attendance_Percentage_Num'].apply(lambda x: 'Shortage' if x < 75.0 else 'Eligible')

output_df = df[['S.No', 'Register_No', 'Student_Name', 'Course_Code', 'Course_Title', 'Attendance_Percentage', 'Status']]

# Save to CSV
output_df.to_csv('attendance.csv', index=False, encoding='utf-8')
print("Successfully generated attendance.csv!")
print(f"Total rows: {len(output_df)}")
print(f"Status distribution:\n{output_df['Status'].value_counts()}")
print("\nUnique Course Codes:", output_df['Course_Code'].nunique())
print("Unique Students:", output_df['Register_No'].nunique())
