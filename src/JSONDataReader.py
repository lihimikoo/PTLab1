# -*- coding: utf-8 -*-
from Types import DataType
from DataReader import DataReader
import json


class JSONDataReader(DataReader):
    def __init__(self) -> None:
        self.data: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            json_data = json.load(file)

        for student_name, subjects in json_data.items():
            self.data[student_name] = []
            for subject, score in subjects.items():
                self.data[student_name].append(
                    (subject, int(score))
                )

        return self.data
