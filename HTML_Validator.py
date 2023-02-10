#!/bin/python3:

import re

def validate_html(html):
    """
    Validate the HTML string by checking if all the tags are properly nested and closed.
    """
    tag_stack = [] # stack to store the opened tags
    tags = _extract_tags(html) # extract the tags from HTML string
    if not tags or not re.match(r'<\/?\w+[^<]*>', tags[0]):
        return False 
    for tag in tags:
        # if the tag doesn't start with "<" or doesn't end with ">", return False
        if not tag.startswith("<") or not tag.endswith(">"):
            return False
        if tag[1] == '/':
            # if the stack is empty or the top of the stack is not the same as the closing tag, return False
            if not tag_stack or tag_stack.pop() != tag[2:].split()[0].rstrip(">"):
                return False
        else:
            # if the tag ends with "/>", continue to the next iteration
            if tag.endswith("/>"):
                continue
            # get the tag name and add it to the stack if it's not a self-closing tag
            tag_name = tag[1:].split()[0].rstrip(">")
            if not tag_name.endswith("/"):
                tag_stack.append(tag_name)
    # return False if there are still tags in the stack, True otherwise
    return not tag_stack

def _extract_tags(html):
    """
    Extract all the tags from the HTML string using regular expression.
    """
    return re.findall(r'<\/?\w+[^<]*>', html)
