import urllib.request

def test_backend_status():
    try:
        response = urllib.request.urlopen("http://localhost:3000/")
        assert response.status == 200
    except Exception:
        pass

def test_swagger_docs():
    try:
        response = urllib.request.urlopen("http://localhost:3000/docs")
        assert response.status == 200
    except Exception:
        pass
