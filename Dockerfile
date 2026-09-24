FROM python:3.11-slim
WORKDIR /app
COPY presistent_auditor.py .
COPY inventory.txt .
CMD ["python", "presistent_auditor.py"]
##docker mount and run
## docker run --rm -it -v "${PWD}:/usr/src/app" -w /usr/src/app python:3.11-slim python presistent_auditor.py
##docker build -t inf1003-labs-smart-auditor .
##docker run --rm -it inf1003-labs-smart-auditor