import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.extract_prices import *


def test_save_to_json():
    """Test saving events creates a file and writes correctly."""
    test_file = "test_events.json"
    events = [{"coin":"bitcoin","usd_price":40000,"eur_price":37000,"timestamp":"2025-12-19T15:00:00"}]
    save_to_json(events, filename=str(test_file))
    
    # Check file exists
    assert test_file.exists()