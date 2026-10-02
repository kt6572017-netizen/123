cd "c:\Users\Riya\OneDrive\Desktop\srm"

# Stage all updated files
git add app.py vercel.json requirements.txt .vercelignore index.html attendance.csv README.md

# Commit the changes
git commit -m "Fix Vercel deployment: Expose top-level app WSGI variable and configure vercel.json"

# Push to your repository
git push -u origin main
