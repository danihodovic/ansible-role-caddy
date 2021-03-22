def test_http(host):
    res = host.ansible("uri", "url=http://localhost return_content=true", check=False)
    assert "Hello, world!" in res["content"]
