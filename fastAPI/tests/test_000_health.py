import httpx

def test_health_check(base_url):
    response = httpx.get(f"{base_url}/health")
    assert response.status_code == 200
    assert response.json() == {"status":"ok"}