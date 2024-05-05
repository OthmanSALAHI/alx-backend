#!/usr/bin/env python3

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of size two containing a start index and an end index
    """
    start_page = (page - 1) * page_size
    end_page = page * page_size
    return (start_page, end_page)
