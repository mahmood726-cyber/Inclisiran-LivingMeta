"""Minimal smoke test for the Inclisiran-LivingMeta dashboard.

Run from the repo root:  python test_smoke.py
No third-party dependencies. Validates that the shipped single-file HTML
review is structurally intact and that the core statistics engine functions
are present. This is a regression guard, not a full unit suite.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(ROOT, "INCLISIRAN_REVIEW.html")
INDEX = os.path.join(ROOT, "index.html")

failures = []


def check(cond, msg):
    if not cond:
        failures.append(msg)


def main():
    check(os.path.exists(HTML), "INCLISIRAN_REVIEW.html missing")
    check(os.path.exists(INDEX), "index.html missing")

    with open(HTML, "rb") as fh:
        raw = fh.read()
    # No UTF-8 BOM in shipped asset.
    check(not raw.startswith(b"\xef\xbb\xbf"), "INCLISIRAN_REVIEW.html has a UTF-8 BOM")

    text = raw.decode("utf-8", errors="replace")

    # No unfilled template placeholders. Build the sentinel tokens at runtime so
    # this test file does not itself contain the literal placeholder strings.
    tokens = ("REPLACE" + "_ME", "__PLACE" + "HOLDER__", "TODO" + "_FILL")
    for tok in tokens:
        check(tok not in text, "unfilled placeholder token present: " + tok)
    check(re.search(r"\{\{\s*[a-zA-Z_]+\s*\}\}", text) is None,
          "unfilled mustache token present")

    # No hardcoded local user paths in the shipped HTML.
    check("C:\\Users" not in text and "/home/" not in text,
          "hardcoded local path present in shipped HTML")

    # Core statistics engine functions are present (regression guard against
    # accidental deletion of the pooling engine).
    for fn in ("computeOR", "computeRR", "computeRD"):
        check(("function " + fn) in text, "missing engine function: " + fn)
    check("qProfileTau2CI" in text, "missing engine function: qProfileTau2CI")

    # The OR continuity correction must be conditional (add 0.5 only on a zero
    # cell), per the meta-analysis correctness rule.
    check("a === 0 || b === 0 || c === 0 || d === 0" in text,
          "OR continuity correction is no longer conditional on a zero cell")

    # Prediction interval uses the Cochrane v6.5 t_{k-1} convention.
    check("k - 1" in text and "qProfileTau2CI" in text,
          "prediction-interval / tau2 CI engine markers missing")

    if failures:
        print("SMOKE FAIL:")
        for f in failures:
            print("  - " + f)
        sys.exit(1)
    print("SMOKE PASS: structural + engine checks OK")


if __name__ == "__main__":
    main()
