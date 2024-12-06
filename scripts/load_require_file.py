# -*- coding: utf-8 -*-

with open(requireFile, "r", encoding = "utf-8") as rrf:
    requireList = f"# list of requirements\n{rrf.read().strip()}\n"
