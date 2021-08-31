from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class SATInstance:
    variables: List[str]
    variable_table: Dict[str, int]
    clauses: List[int]

    def parse_and_add_clause(self, line):
        pass

    @classmethod
    def from_file(cls, file):
        pass

    def literal_tor_string(self, literal):
        pass

    def clause_to_string(self, clause):
        pass

    def assignment_to_string(self, assignment, brief=False, starting_with=""):
        pass
