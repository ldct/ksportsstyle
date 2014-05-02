#!/usr/bin/env python

template = """
<li class="isotope-item item-junior">
    <img src="static/SUPERGA/Junior/%s" width="200" />
    <div class="description-container"><div class="description-text">%s</div></div>            
</li>
"""

with open("list") as f:
	for line in f.readlines():
		name = line[:-1]
		print template % (name, name.replace('_', " ")[:-4])