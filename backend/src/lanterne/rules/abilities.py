"""
Implementation of common D&D mechanics
"""


def ability_modifier(score: int) -> int:
    return (score - 10) // 2
