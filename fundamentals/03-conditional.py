# Lecture 03
# Conditional

""" Determines the correct HTTP response code."""

http_resp_code = "200"

if http_resp_code == "200":
  meaning = "ok"
elif http_resp_code == "400":
  meaning = "bad request"
elif http_resp_code == "404":
  meaning = "not found"
elif http_resp_code == "500":
  meaning = "internal server error"
else: 
  meaning = "unknown"


if http_resp_code != "unknown":
  print(f"It's a valid HTTP response code.")
else:
  print(f"Error: The HTTP response code is invalid.")
