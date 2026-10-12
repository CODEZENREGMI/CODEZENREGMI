"""Write Kathmandu local time and the 'billionaire before 2045' day count into README.md."""
import datetime
import re
from pathlib import Path
from zoneinfo import ZoneInfo

DAY_ONE = datetime.date(2026, 5, 4)  # day 1 of posting daily
CLOCKS = "🕛🕐🕑🕒🕓🕔🕕🕖🕗🕘🕙🕚"

now = datetime.datetime.now(ZoneInfo("Asia/Kathmandu"))
day = (now.date() - DAY_ONE).days + 1
time_str = now.strftime("%I:%M %p").lstrip("0")

block = (
    "<!--LOCAL-TIME:START-->\n"
    f"{CLOCKS[now.hour % 12]} **{time_str}** in Kathmandu (NPT, UTC+5:45) · "
    f"📅 Day **{day}** of becoming a billionaire before 2045<br>\n"
    "<sub>Updates automatically every 15 minutes</sub>\n"
    "<!--LOCAL-TIME:END-->"
)

readme = Path("README.md")
text = readme.read_text(encoding="utf-8")
readme.write_text(
    re.sub(r"<!--LOCAL-TIME:START-->.*?<!--LOCAL-TIME:END-->", block, text, flags=re.S),
    encoding="utf-8",
)
