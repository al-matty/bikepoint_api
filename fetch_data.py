"""
Fetch and store Amplitude event data for a specified date range.
Data is fetched from the Amplitude EU residency server.
Data goes to the data/ directory as JSON files named with timestamps.
Logging is configured to output to a file in the logs/ directory.
"""

import time
import logging
#import os
from dotenv import load_dotenv
#from datetime import datetime, timedelta
from logging_config import setup_logging
#from utils import unzip
from utils import fetch, write_to_local, push_to_s3

# Load .env file
load_dotenv()

# Configuration
log_outpath = "logs"
log_level = logging.INFO    # or logging.ERROR
data_outpath = "data"
data_outfile = "bp_dump"
max_attempts = 5
delay_seconds = 1

# Set up logging
setup_logging(log_outpath, log_level)

# Get secrets from .env
#api_key = os.getenv("AMP_API_KEY")
#secret_key = os.getenv("AMP_SECRET_KEY")

# Format the start and end time (YYYYMMDDTHH)
#yesterday = datetime.now() - timedelta(days=1)
#start_time = yesterday.strftime("%Y%m%dT00")
#end_time = yesterday.strftime("%Y%m%dT23")

# API endpoint is the EU residency server
url = "https://api.tfl.gov.uk/BikePoint/"

# Fetch data
data = fetch(
    url,
    #api_key,
    #secret_key,
    delay_seconds,
    #start_time,
    #end_time,
    max_attempts
    )

events = data.json()
print(f"Parsed {len(events)} events")

# Write to local file
write_to_local(events, data_outpath, data_outfile)

# Wait a moment to ensure file is closed
time.sleep(3)

# Upload to S3
push_to_s3(data_outpath)
