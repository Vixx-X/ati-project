"""
Main file for testing procedures
"""

# import backend.app as app


# def test_hello():
#     """
#     Test the main hello page
#     """
#     app.app.testing = True
#     client = app.app.test_client()
#     resp = client.get("/")
#     assert resp.status == "200 OK"
#     assert resp.data == b"Hello World!\n"


def test_just_werks():
    """Dummy test"""

    a = "I use Arch btw"
    assert "Arch" in a
