#!/bin/sh
# Rebuild home.html from the captured page and apply all customisations
cd "$(dirname "$0")/.."
python3 _build/build_home.py && python3 _build/custom_std.py && python3 _build/custom_gallery.py && python3 _build/custom_gifts.py && python3 _build/custom_rsvp.py && python3 _build/custom_credit.py
