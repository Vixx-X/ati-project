"""
Starting script for the flask app
"""
# Run a test server.

from backend import init_app

app = init_app()

if __name__ == "__main__":
    import config
    from sys import argv

    host, port = "0.0.0.0", 8080

    if len(argv) > 2:
        port = int(argv[2])
    if len(argv) > 1:
        host = argv[1]

    app.run(host=host, port=port, debug=config.DEBUG)
