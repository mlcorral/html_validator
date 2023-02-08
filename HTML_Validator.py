#!/bin/python3:
#


import re


class HtmlValidator:
    def __init__(self, html_string):
        self.html_string = html_string
        self.stack = []

    def is_valid_html(self):
        tags = self._extract_tags(self.html_string)
        for tag in tags:
            if tag.startswith("<") and not tag.startswith("</"):
                self.stack.append(tag)
            elif tag.startswith("</"):
                if not self.stack:
                    return False
                opening_tag = "<" + tag[2:]
                if opening_tag != self.stack[-1]:
                    return False
                self.stack.pop()
        return not self.stack

    @staticmethod
    def validate_html(html_string):
        return HTML_Validator(html_string).is_valid_html()


def _extract_tags(html):
    return re.findall(r"<.*?>", html)
