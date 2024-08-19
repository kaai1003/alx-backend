#!/usr/bin/env python3
"""Simple pagination Module"""
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """return list dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        range = self.index_range(page, page_size)
        return self.dataset()[range[0]:range[1]]

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple:
        """Simple helper function"""
        end_index = page * page_size
        start_index = end_index - page_size
        return (start_index, end_index)
