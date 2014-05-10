#!/usr/bin/env python

template = """
<li class="isotope-item item-male">
    <img src="static/BSC/Male/%s" width="400" />
    <div class="description-container"><div class="description-text">%s</div></div>            
</li>
"""

with open("list") as f:
	for line in f.readlines():
		name = line[:-1]
		print template % (name, name.replace('_', " ")[:-4]),