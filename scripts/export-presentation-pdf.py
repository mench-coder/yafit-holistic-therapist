"""Export presentation/business-plan.html to PDF via Playwright."""
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "presentation" / "business-plan.html"
OUT = ROOT / "exports" / "yafit-business-plan-2026.pdf"


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    url = HTML.resolve().as_uri()

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 720})
        page.goto(url, wait_until="networkidle", timeout=120_000)
        page.wait_for_timeout(3500)
        page.emulate_media(media="print")
        page.pdf(
            path=str(OUT),
            format="A4",
            landscape=True,
            print_background=True,
            prefer_css_page_size=False,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
        )
        browser.close()

    print(f"Wrote {OUT} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
