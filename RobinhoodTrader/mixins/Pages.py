from ..RobinhoodSession import RobinhoodSession
from typing import Union, List, Optional
import math


class Pages:
    session: RobinhoodSession

    def getPages(
        self,
        page: dict,
        startPageNumber: int = 0,
        limit: Union[int, float] = math.inf,
    ) -> List[dict]:

        pages = [page]
        startPageNumber = startPageNumber
        limit = limit
        currentPage = 0

        def _limitNotReached() -> bool:
            limitNotReached = currentPage < limit + startPageNumber

            return limitNotReached

        def _runConditions() -> List[bool]:
            nextPageExists = self.nextPageExists(page)
            limitNotReached = _limitNotReached()

            runConditions = [nextPageExists, limitNotReached]

            return runConditions

        def _pageIsInRange() -> bool:
            pageIsInRange = currentPage >= startPageNumber

            return pageIsInRange

        def _appendNextPage() -> None:
            page = self.getNextData(page)

            if _pageIsInRange():
                pages.append(page)

        while False not in _runConditions():
            _appendNextPage()
            currentPage += 1

        return pages

    def searchForRecord(
        self, page: dict, searchKey: str, searchValue: str
    ) -> dict:
        page = page
        searchKey = searchKey
        searchValue = searchValue

        records: List[dict] = None
        foundRecord: dict = None

        def _runConditions() -> List[bool]:
            nextPageExists = self.nextPageExists(page)
            recordIsNotFound = foundRecord is None

            runConditions = [nextPageExists, recordIsNotFound]

            return runConditions

        def _foundRecordOrNone() -> Optional[dict]:
            foundRecordOrNone = None

            for record in records:
                if record[searchKey] == searchValue:
                    foundRecordOrNone = record
                    break

            return foundRecordOrNone

        records = page["results"]
        foundRecord = _foundRecordOrNone()

        while False not in _runConditions():
            page = self.getNextData(page)
            records = page["results"]
            foundRecord = _foundRecordOrNone()

        return foundRecord

    def nextPageExists(self, responseData: dict) -> bool:
        nextPageExists = responseData["next"] is not None
        return nextPageExists

    def getNextData(self, page: dict) -> dict:
        nextUrl = page["next"]
        response = self.session.get(nextUrl, timeout=15)
        response.raise_for_status()
        data = response.json()

        return data
