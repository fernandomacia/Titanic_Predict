# Base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy files
COPY app.py /app
COPY requirements.txt /app
COPY model.pkl /app
COPY request.py /app
COPY templates /app/templates
COPY static /app/static

# Install dependencies
RUN pip install -r requirements.txt
RUN pip install gunicorn

# Run the application
EXPOSE 8000
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000", "--access-logfile", "-", "--error-logfile", "-", "--timeout", "120"]
CMD ["app:app"]