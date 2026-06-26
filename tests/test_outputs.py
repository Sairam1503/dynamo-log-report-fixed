import json
import re
from collections import Counter
from pathlib import Path


def _expected_report() -> dict:
    paths, ips, total = Counter(), set(), 0
    with open("/app/access.log") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            total += 1
            ips.add(line.split()[0])
            match = re.search(r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ', line)
            if match:
                paths[match.group(1)] += 1
    return {
        "total_requests": total,
        "unique_ips": len(ips),
        "top_path": paths.most_common(1)[0][0],
    }


def test_report_exists():
    """Success criterion 1: /app/report.json exists."""
    assert Path("/app/report.json").exists(), "report.json not found at /app/report.json"


def test_report_schema():
    """Success criterion 2: /app/report.json is valid JSON with keys total_requests, unique_ips, and top_path."""
    data = json.loads(Path("/app/report.json").read_text())
    assert isinstance(data, dict)
    assert {"total_requests", "unique_ips", "top_path"} <= set(data.keys())
    assert isinstance(data["total_requests"], int)
    assert isinstance(data["unique_ips"], int)
    assert isinstance(data["top_path"], str)


def test_total_requests():
    """Success criterion 3: total_requests equals the number of non-empty lines in /app/access.log."""
    data = json.loads(Path("/app/report.json").read_text())
    expected = _expected_report()
    assert data["total_requests"] == expected["total_requests"]


def test_unique_ips():
    """Success criterion 4: unique_ips equals the number of distinct client IP addresses in /app/access.log."""
    data = json.loads(Path("/app/report.json").read_text())
    expected = _expected_report()
    assert data["unique_ips"] == expected["unique_ips"]


def test_top_path():
    """Success criterion 5: top_path is the most frequently requested path (ties broken by first appearance in the log)."""
    data = json.loads(Path("/app/report.json").read_text())
    expected = _expected_report()
    assert data["top_path"] == expected["top_path"]
