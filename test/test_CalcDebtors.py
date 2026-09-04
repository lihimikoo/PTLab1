# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.CalcDebtors import CalcDebtors


class TestCalcDebtors:
    @pytest.fixture()
    def test_data(self) -> DataType:
        return {
            "Иванов Иван Иванович": [
                ("математика", 80),
                ("программирование", 90),
                ("литература", 76)
            ],
            "Петров Петр Петрович": [
                ("математика", 50),  # задолженность
                ("социология", 90),
                ("химия", 61)
            ],
            "Сидоров Сидор Сидорович": [
                ("математика", 40),  # задолженность
                ("физика", 30),      # задолженность
                ("химия", 80)
            ]
        }

    def test_init(self, test_data: DataType) -> None:
        calc_debtors = CalcDebtors(test_data)
        assert calc_debtors.data == test_data
        assert calc_debtors.debtors_count == 0

    def test_calc_no_debtors(self) -> None:
        data: DataType = {
            "Студент1": [("математика", 80), ("физика", 90)]
        }
        calc_debtors = CalcDebtors(data)
        assert calc_debtors.calc() == 0

    def test_calc_one_debtor(self) -> None:
        data: DataType = {
            "Студент1": [("математика", 80), ("физика", 90)],
            "Студент2": [("математика", 50), ("физика", 90)]
        }
        calc_debtors = CalcDebtors(data)
        assert calc_debtors.calc() == 1

    def test_calc_multiple_debtors(self, test_data: DataType) -> None:
        calc_debtors = CalcDebtors(test_data)
        assert calc_debtors.calc() == 2 
