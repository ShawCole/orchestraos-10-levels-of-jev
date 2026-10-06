"""
Test suite verifying all 10 Levels of Jev for OrchestraOS
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.orchestra_jev_evaluator import OrchestraJevEvaluator

@pytest.fixture
def evaluator():
    return OrchestraJevEvaluator()

def test_level_1_precondition_gate(evaluator):
    res = evaluator.evaluate_level_1({
        "is_canonical_session_live": True,
        "is_wal_delta_drained": True
    })
    assert res["verdict"] == "APPROVED"
    assert res["action"] == "spawn_green()"
    assert res["latency_ms"] < 350

def test_level_6_tmux_sanitizer(evaluator):
    res = evaluator.evaluate_level_6("tmux kill-session -t P-g1")
    assert res["collision_hazard_detected"] is True
    assert res["sanitized_command"] == "tmux kill-session -t =P-g1"
