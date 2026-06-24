An Apache-style access log is available at `/app/access.log`.

Analyze the log and write a JSON report to `/app/report.json` containing exactly these three keys:

- `total_requests` — integer, total number of log lines
- `unique_ips` — integer, number of distinct client IP addresses
- `top_path` — string, the URL path that appears most often in requests

**Success criteria:**

1. `/app/report.json` exists.
2. The file contains valid JSON with a top-level object.
3. `total_requests` is an integer equal to the total number of lines in the log.
4. `unique_ips` is an integer equal to the number of distinct client IP addresses.
5. `top_path` is a string equal to the URL path with the highest request count.
