# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.JSONDataReader import JSONDataReader


class TestJSONDataReader:
    @pytest.fixture()
    def json_content_and_data(self) -> tuple[str, DataType]:
        json_text = '''{
            "Иванов Иван Иванович": {
                "математика": 80,
                "программирование": 90,
                "литература": 76
            },
            "Петров Петр Петрович": {
                "математика": 100,
                "социология": 90,
                "химия": 61
            }
        }'''

        data: DataType = {
            "Иванов Иван Иванович": [
                ("математика", 80),
                ("программирование", 90),
                ("литература", 76)
            ],
            "Петров Петр Петрович": [
                ("математика", 100),
                ("социология", 90),
                ("химия", 61)
            ]
        }

        return json_text, data

    @pytest.fixture()
    def filepath_and_data(
        self,
        json_content_and_data: tuple[str, DataType],
        tmpdir
    ) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.json")
        p.write_text(json_content_and_data[0], encoding='utf-8')
        return str(p), json_content_and_data[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        reader = JSONDataReader()
        result = reader.read(filepath_and_data[0])
        assert result == filepath_and_data[1]

    def test_init(self) -> None:
        reader = JSONDataReader()
        assert reader.data == {}
