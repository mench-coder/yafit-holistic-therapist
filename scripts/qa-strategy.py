from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
url = (ROOT / "presentation" / "strategy-doc.html").resolve().as_uri()
qa = ROOT / "_qa"
qa.mkdir(exist_ok=True)

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 820, "height": 1160}, device_scale_factor=2)
    pg.goto(url, wait_until="networkidle")
    pg.wait_for_timeout(3000)
    pg.screenshot(path=str(qa / "strategy-cover.png"))
    top = pg.evaluate("document.querySelectorAll('.page')[3].offsetTop")
    pg.evaluate(f"window.scrollTo(0, {top})")
    pg.wait_for_timeout(800)
    pg.screenshot(path=str(qa / "strategy-questions.png"))
    b.close()
print("ok")
