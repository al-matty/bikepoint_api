# BikePoint API

Fetches London bike point data from the TfL API and stores it to AWS S3.

## Setup

```bash
pip install -r requirements.txt
```

Create a `.env` file with your AWS credentials.

## Usage

```bash
python main.py
```

Data is fetched from TfL, saved locally to `data/`, uploaded to S3, then deleted locally.
