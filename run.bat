@echo off
if not exist "check.txt" (
	echo Installing python requirements...
	pip install -r requirements.txt
	echo installed requirements>"check.txt"
) 

py main.py