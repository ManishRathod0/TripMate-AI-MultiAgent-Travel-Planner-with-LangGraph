# TripMate-AI-MultiAgent-Travel-Planner-with-LangGraph

## How to run 

1. Create Virtual Environment
# python -m venv venv

2. Activate the Virtual Environment 
# venv\Scripts\Activate.ps1

3. Install the dependincies from requirements.txt 
# pip install -r requirements.txt


# postgresql://tripagentmemory_wref_user:9ftbljFutbFNasfmgFPFKYgX3Fg0iT3Q@dpg-dav9rr97lnhs73bil260-a.oregon-postgres.render.com/tripagentmemory_wref

## Git Flow 

git reset --soft origin/main
echo .env >> .gitignore
git rm --cached .env
git add .
git status
git commit -m "folder structure added"
git push origin main