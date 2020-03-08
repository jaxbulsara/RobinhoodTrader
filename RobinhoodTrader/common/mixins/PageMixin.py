from __future__ import absolute_import

from ...RobinhoodSession import RobinhoodSession
from ...exceptions import RecordNotFoundError
from ...datatypes import Page
from ...exceptions import PageError

from .ArgumentCheckingMixin import ArgumentCheckingMixin

import math, requests


class PageMixin(ArgumentCheckingMixin):
    session: RobinhoodSession

    def get_pages(
        self, page, start_page_number=0, limit=math.inf,
    ):
        self.check_argument("page", page, (Page))
        self.check_argument("start_page_number", start_page_number, (int))
        self.check_argument("limit", limit, int, float)

        pages = [page]
        start_page_number = start_page_number
        limit = limit
        current_page = 0

        def _limit_not_reached():
            limit_not_reached = current_page < limit + start_page_number

            return limit_not_reached

        def _run_conditions():
            next_page_exists = self.next_page_exists(page)
            limit_not_reached = _limit_not_reached()

            return [next_page_exists, limit_not_reached]

        def _page_is_in_range():
            return current_page >= start_page_number

        while False not in _run_conditions():
            page = self.get_next_page(page)

            if _page_is_in_range():
                pages.append(page)
            current_page += 1

        return pages

    def find_record(self, page, record_key, record_value):
        page = page
        record_key = record_key
        record_value = record_value

        records = None
        found_record = None

        def _run_conditions():
            next_page_exists = self.next_page_exists(page)
            record_is_not_found = found_record is None

            return [next_page_exists, record_is_not_found]

        def found_record_or_none():
            found_record_or_none = None

            for record in records:
                if record[record_key] == record_value:
                    found_record_or_none = record
                    break

            return found_record_or_none

        records = page.results
        found_record = found_record_or_none()

        while False not in _run_conditions():
            page = self.get_next_page(page)
            records = page.results  # pylint: disable=no-member
            found_record = found_record_or_none()

        if found_record is None:
            raise RecordNotFoundError()

        return found_record

    def next_page_exists(self, page):
        return page.next is not None

    def get_next_page(self, page):
        try:
            nextUrl = page.next
            data = self.session.get_data(nextUrl, timeout=15)
            return Page(data)
        except requests.exceptions.MissingSchema:
            raise PageError("Next page does not exist.")
