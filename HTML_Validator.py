#!/bin/python3:


def extract_tags(html):
    tag_list = []
    tag = ''
    in_tag = False

    for char in html:
        if char == '<':
            in_tag = True
        elif char == '>':
            if in_tag:
                tag_list.append(tag)
                tag = ''
                in_tag = False
        elif in_tag:
            tag += char

    if tag:
        raise ValueError('found < without matching >')

    return tag_list


def validate_html(html):
    tag_list = extract_tags(html)
    stack = []
    for tag in tag_list:
        if tag[1] != '/':
            stack.append(tag)
        else:
            if not stack:
                return False
            open_tag = stack.pop()
            if open_tag[1:] != tag[2:]:
                return False
    return not stack
