#!/bin/python3:
def validate_html(html):
    '''
    This function returns True if every opening tag has a corresponding closing tag in the given html string, and False otherwise.

    >>> validate_html('<strong>Python</strong>')
    True
    >>> validate_html('<strong>Python</em>')
    False
    '''
    tags = _extract_tags(html)
    opening_tags = []
    closing_tags = []
    for tag in tags:
        if tag[1] == '/':
            closing_tags.append(tag)
        else:
            opening_tags.append(tag)
    return len(opening_tags) == len(closing_tags)

def _extract_tags(html):
    '''
    This function returns a list of all the html tags contained in the input string, stripping out all text not contained within angle brackets.

    >>> _extract_tags('<strong>Python</strong>')
    ['<strong>', '</strong>']
    >>> _extract_tags('<strong>Python</em>')
    ['<strong>', '</em>']
    '''
    tags = []
    start = 0
    while start < len(html):
        start = html.find('<', start)
        if start == -1:
            break
        end = html.find('>', start + 1)
        if end == -1:
            break
        tags.append(html[start:end + 1])
        start = end + 1
    return tags
