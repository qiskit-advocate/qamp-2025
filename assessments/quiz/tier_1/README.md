# Tier 1 Tools (Grades 6–8)

These scripts support **Tier 1** classroom printables / assets.

| Tier 1 Week | Activity | Tool | What it generates |
|---|---|---|---|
| Week 4 | Teleportation Mini-Project | 	eleportation_cards/teleport_cards.py | Team cards + teacher legend |
| Week 5 | Static on the Signal | signal_studio_audio/signal_set_maker.py | clean.wav + 
oisy.wav + worksheet stub |
| Week 6 | Quantum Courier | quantum_courier_maps/city_map_maker.py | Sample map text description |

## Quick run examples

`ash
python tools/tier_1/teleportation_cards/teleport_cards.py --pairs 12 --outdir teleport_class_set
python tools/tier_1/signal_studio_audio/signal_set_maker.py --outdir signal_set
python tools/tier_1/quantum_courier_maps/city_map_maker.py
