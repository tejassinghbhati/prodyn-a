import json
from pathlib import Path

_REPORT = Path("/app/report.json")


def _load():
    return json.loads(_REPORT.read_text())


def test_report_exists():
    """Criterion 1: /app/report.json exists."""
    assert _REPORT.exists(), "report.json not found"


def test_report_is_json_object():
    """Criterion 2: the file contains valid JSON with a top-level object."""
    data = _load()
    assert isinstance(data, dict), "report.json must be a JSON object"


def test_total_requests():
    """Criterion 3: total_requests equals the number of lines in the log."""
    data = _load()
    assert data.get("total_requests") == 6, (
        f"expected total_requests=6, got {data.get('total_requests')!r}"
    )


def test_unique_ips():
    """Criterion 4: unique_ips equals the number of distinct client IPs."""
    data = _load()
    assert data.get("unique_ips") == 3, (
        f"expected unique_ips=3, got {data.get('unique_ips')!r}"
    )


def test_top_path():
    """Criterion 5: top_path equals the URL path with the highest request count."""
    data = _load()
    assert data.get("top_path") == "/index.html", (
        f"expected top_path='/index.html', got {data.get('top_path')!r}"
    )
