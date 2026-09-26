FROM python:3.11-slim

WORKDIR /app/src

COPY src .

CMD ["python", "persistent_auditor.py"]
