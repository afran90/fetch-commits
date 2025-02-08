FROM python

WORKDIR /app

COPY fetch_commits.py .

RUN pip install requests

CMD ["python", "fetch_commits.py"]
