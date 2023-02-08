#!/bin/python3:

import re

def validate_html(html):
    tag_stack = []
    tags = _extract_tags(html)

    for tag in tags:
        if not tag.startswith("<") or not tag.endswith(">"):
            return False
        if tag[1] == '/':
            if not tag_stack or tag_stack.pop() != tag[2:-1]:
                return False
        else:
            if not tag.endswith("/>"):
                tag_stack.append(tag[1:-1])
    return not tag_stack

def _extract_tags(html):
    return re.findall(r'<\/?\w+[^<]*>', html)
