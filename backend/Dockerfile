FROM python:3.11.7-bookworm

WORKDIR /app

COPY ./app/ .

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

ENV SUPABASE_URL='https://ocqssqkjzmnmxxfdtdzb.supabase.co'
ENV SUPABASE_SECRET_KEY ='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9jcXNzcWtqem1ubXh4ZmR0ZHpiIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcyMDUxMDQ0OCwiZXhwIjoyMDM2MDg2NDQ4fQ.zzO1x39YncRXSRIVQauSBIzYL6tSdxcQO2uqmQbdWIs'
ENV GOOGLE_API_KEY ='AIzaSyCozqIzVfFdFfvJgmxAlN8g5ETeuyJkxUQ'

EXPOSE 5000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]