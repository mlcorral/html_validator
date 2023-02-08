#!/bin/python3:

import re

def validate_html(html):
    tag_stack = []
    tags = _extract_tags(html)

    for tag in tags:
        if not tag.startswith("<") or not tag.endswith(">"):
            return False
        if tag[1] == '/':
            if not tag_stack or tag_stack.pop() != tag[2:-1].split()[0]:
                return False
        else:
            if tag.endswith("/>"):
                continue
            tag_name = tag[1:].split()[0].rstrip(">")
            if not tag_name.endswith("/"):
                tag_stack.append(tag_name)
    return not tag_stack

def _extract_tags(html):
    return re.findall(r'<\/?\w+[^<]*>', html)
