import pytest
from unittest.mock import Mock
import requests
from call_apis import call_api

def test_call_api():
    def mock_post(*args, **kwargs):
        return {"text": "hello"}
        
    requests.post = Mock(side_effect=mock_post)
    
    url = "https://text-translator2.p.rapidapi.com/translate"

    payload = {
        "source_language": "en",
        "target_language": "id",
        "text": "What is your name?"
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "a1d1519551msh0be91d8c02a5155p1bfb4ajsnf52f4f692d5b",
        "X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
    }

    
    assert call_api(url, payload, headers) == "hello"