#!/bin/bash
set -e

REPO_NAME="ai-agent-portfolio"
BASE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "=== Pushing to GitHub: $REPO_NAME ==="
cd "$BASE"

git init
git checkout -b main
git config user.email "mythrip11@gmail.com"
git config user.name "Mythri Potluri"
git add .
git commit -m "Initial commit: AI Agent Portfolio - 9 n8n workflow agents across Healthcare, Transportation, Construction"

gh repo create "$REPO_NAME" \
  --public \
  --description "AI Agent Portfolio - 9 n8n workflow agents powered by Claude across Healthcare, Transportation and Construction, tested with fictional data" \
  --source=. \
  --remote=origin \
  --push

echo ""
echo "Done! Repo live at: https://github.com/mythrip11/$REPO_NAME"
echo ""
echo "=== Enabling GitHub Pages ==="
gh api \
  --method PUT \
  -H "Accept: application/vnd.github+json" \
  "/repos/mythrip11/$REPO_NAME/pages" \
  -f "source[branch]=main" \
  -f "source[path]=/" 2>/dev/null || \
gh api \
  --method POST \
  -H "Accept: application/vnd.github+json" \
  "/repos/mythrip11/$REPO_NAME/pages" \
  -f "source[branch]=main" \
  -f "source[path]=/" 2>/dev/null || true

echo ""
echo "GitHub Pages will be live in ~60 seconds at:"
echo "  https://mythrip11.github.io/$REPO_NAME/"
echo ""
echo "Optional: Also deploy the Streamlit app"
echo "  1. Go to https://share.streamlit.io"
echo "  2. Click 'New app'"
echo "  3. Select repo: mythrip11/$REPO_NAME"
echo "  4. Branch: main   |   Main file: app.py"
echo "  5. Click Deploy"
