"""Pulls your published games from itch.io and updates games.json.
Keeps anything you set by hand (category, home flag, local cover images)."""
import json, os, sys, urllib.request

KEY = os.environ.get("ITCH_API_KEY", "").strip()
if not KEY:
    print("No ITCH_API_KEY secret set, skipping.")
    sys.exit(0)

req = urllib.request.Request("https://itch.io/api/1/%s/my-games" % KEY,
                             headers={"User-Agent": "lazerz-site-updater"})
try:
    data = json.load(urllib.request.urlopen(req, timeout=30))
except Exception as e:
    print("itch.io request failed:", e)
    sys.exit(1)

if "games" not in data:
    print("Unexpected response from itch.io:", list(data))
    sys.exit(1)

old = json.load(open("games.json")) if os.path.exists("games.json") else []
byid = {g["id"]: g for g in old}
PAL = ["#5b93cc", "#3fae62", "#d9a92b", "#8f7ad8", "#e27b5e", "#5cc5a2"]
ROT = ["-1deg", ".8deg", "-.6deg", "1deg"]
out = []
for gm in data["games"]:
    if gm.get("published") is False:
        continue
    url = gm.get("url", "")
    slug = url.rstrip("/").split("/")[-1]
    if not slug:
        continue
    n = len(out)
    g = byid.get(slug) or {"id": slug, "c": PAL[n % len(PAL)], "r": ROT[n % len(ROT)], "type": "unsorted"}
    g["n"] = gm.get("title") or slug
    g["u"] = url
    date = (gm.get("published_at") or gm.get("created_at") or "")[:10]
    if date:
        g["date"] = date
    cover = gm.get("still_cover_url") or gm.get("cover_url")
    if cover and not g.get("img_locked"):
        g["img"] = cover  # itch.io cover always wins unless you locked a custom one
    out.append(g)

ids = {g["id"] for g in out}
for g in old:
    if g.get("manual") and g["id"] not in ids:
        out.append(g)

if not out:
    print("itch.io returned no published games, leaving games.json alone.")
    sys.exit(0)

new = json.dumps(out, indent=2) + "\n"
if not os.path.exists("games.json") or open("games.json").read() != new:
    open("games.json", "w").write(new)
    print("games.json updated with", len(out), "games")
else:
    print("No changes")
