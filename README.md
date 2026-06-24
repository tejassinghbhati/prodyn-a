# log-report

A Harbor task where the agent reads an Apache access log and writes a JSON summary.

The agent gets `/app/access.log` and has to produce `/app/report.json` with three fields: total number of requests, count of unique IPs, and the most-visited path.

```
harbor run -p log-report -a oracle
```

Verified with pytest. Reward 1 if all five checks pass, 0 otherwise.
