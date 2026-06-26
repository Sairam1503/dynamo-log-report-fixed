An Apache-style access log is at `/app/access.log`. Parse it and write a JSON summary to `/app/report.json`.

Each non-empty line is one request. Count how many lines there are, how many distinct client IP addresses appear (the first token on each line), and which request path was hit most often. Extract paths from the HTTP request in quotes (for example, `GET /index.html` yields `/index.html`). Only count paths from GET, POST, PUT, DELETE, HEAD, or PATCH requests. If two paths tie for the highest count, choose the one that appears first in the log.

Write `/app/report.json` as a JSON object with these keys:
- `"total_requests"`: integer, number of non-empty log lines
- `"unique_ips"`: integer, number of distinct client IPs
- `"top_path"`: string, the most frequent path

1. `/app/report.json` exists.
2. `/app/report.json` is valid JSON and contains the keys `total_requests`, `unique_ips`, and `top_path`.
3. `total_requests` equals the number of non-empty lines in `/app/access.log`.
4. `unique_ips` equals the number of distinct client IP addresses in `/app/access.log`.
5. `top_path` is the most frequently requested path in `/app/access.log` (ties broken by first appearance in the log).

You have 120 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.
