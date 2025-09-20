set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]

venv:
	python -m venv venv
	Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
	.\venv\Scripts\Activate.ps1

init: 
	python -m pip install -r requirements.txt

run:
	python main.py

test:
	pytest
