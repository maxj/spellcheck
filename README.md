
# Spell:heavy_check_mark: Service

Simple HTTP server to check word spelling.

# Requirements

* Python
* Flask
* Requests

```sh
pip install flask
pip install requests
```

# Start the service

```sh
python spellService.py
```

# Run some test

Assuming the service started on localhost, ```spellRequest.py``` shows
two example requests to make against the HTTP server.  The first will
return a 200 response indicating the word is spelled correctly, the
second will return a 303 response with a suggested spelling.
