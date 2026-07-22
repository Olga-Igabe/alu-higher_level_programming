# python-network_0

This project covers the basics of HTTP networking using `curl` from Bash
scripts: measuring response body size, filtering by status code, sending
different HTTP methods, discovering allowed methods, sending custom
headers, and sending POST form parameters.

## Files

- `0-body_size.sh` — displays the byte size of a response body
- `1-body.sh` — displays the response body, only for a 200 status code
- `2-delete.sh` — sends a DELETE request and displays the response body
- `3-methods.sh` — displays all HTTP methods a server accepts for a URL
- `4-header.sh` — sends a GET request with a custom header
- `5-post_params.sh` — sends a POST request with email/subject parameters

## Usage

Each script takes a URL as its first argument:
