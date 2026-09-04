# -*- coding: utf-8 -*-
from Types import DataType


class CalcDebtors:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.debtors_count: int = 0

    def calc(self) -> int:
        """Подсчитывает количество студентов с задолженностями (балл < 61)"""
        self.debtors_count = 0
        for student in self.data:
            has_debt = False
            for subject, score in self.data[student]:
                if score < 61:
                    has_debt = True
                    break
            if has_debt:
                self.debtors_count += 1
        return self.debtors_count
