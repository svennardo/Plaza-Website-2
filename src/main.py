import http.server
import os
import webbrowser
from http.server import ThreadingHTTPServer

PORT = 8080
PUBLIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "public")


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=PUBLIC_DIR, **kwargs)

    def log_message(self, format, *args):  # noqa: A002
        print(f"  {self.address_string()} {format % args}")


def main() -> None:
    # ThreadingHTTPServer serves requests concurrently, so many image
    # requests don't queue up serially behind one another.
    with ThreadingHTTPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}"
        print(f"\n  Plaza e.V. Website")
        print(f"  Running at {url}\n")
        webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n  Server stopped.")


if __name__ == "__main__":
    main()
