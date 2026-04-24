#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,
                        page_size: int = 10) -> Dict:
        """
        Return a deletion-resilient hypermedia page.

        Starting from ``index``, collect up to ``page_size`` items,
        skipping positions that were removed from the indexed dataset.
        The returned ``next_index`` is the first position after the
        last returned item, so a follow-up call with that value never
        misses rows even if deletions happened in between.

        Args:
            index (int): starting position (0-indexed). Must be a
                valid index of the original dataset.
            page_size (int): number of items to return.

        Returns:
            Dict: keys ``index``, ``next_index``, ``page_size``,
            ``data``.
        """
        indexed = self.indexed_dataset()
        assert index is not None and 0 <= index < len(indexed)

        data: List[List] = []
        current = index
        total = len(self.dataset())

        while len(data) < page_size and current < total:
            row = indexed.get(current)
            if row is not None:
                data.append(row)
            current += 1

        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': current,
        }
