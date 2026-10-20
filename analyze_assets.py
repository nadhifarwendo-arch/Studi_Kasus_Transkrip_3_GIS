"""Analisis sederhana data aset berkoordinat untuk latihan GIS."""
from pathlib import Path
import csv
import json
from collections import Counter

HERE = Path(__file__).resolve().parents[1]
DATA = HERE / "data" / "assets.csv"
OUT = HERE / "output"
OUT.mkdir(exist_ok=True)

with DATA.open(newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

for row in rows:
    row["latitude"] = float(row["latitude"])
    row["longitude"] = float(row["longitude"])

category_counts = Counter(row["category"] for row in rows)
status_counts = Counter(row["status"] for row in rows)

with (OUT / "summary_by_category.csv").open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["category", "count"])
    writer.writerows(sorted(category_counts.items()))

with (OUT / "summary_by_status.csv").open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["status", "count"])
    writer.writerows(sorted(status_counts.items()))

# GeoJSON Point coordinates must be [longitude, latitude].
geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {
                "asset_id": row["asset_id"],
                "name": row["name"],
                "category": row["category"],
                "status": row["status"],
            },
            "geometry": {
                "type": "Point",
                "coordinates": [row["longitude"], row["latitude"]],
            },
        }
        for row in rows
    ],
}
(OUT / "assets.geojson").write_text(
    json.dumps(geojson, indent=2, ensure_ascii=False), encoding="utf-8"
)

print(f"Jumlah aset: {len(rows)}")
print("Ringkasan kategori:")
for category, count in sorted(category_counts.items()):
    print(f"  - {category}: {count}")
print("Ringkasan status:")
for status, count in sorted(status_counts.items()):
    print(f"  - {status}: {count}")
print(f"Output tersimpan di: {OUT}")
