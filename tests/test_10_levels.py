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

def test_level_3_context_tiers(evaluator):
    # Tier 1: Normal (<70%) -> HOLD_BLUE
    res_normal = evaluator.evaluate_level_3({"context_saturation_pct": 45, "git_uncommitted_lines": 20})
    assert res_normal["verdict"] == "HOLD_BLUE"
    assert res_normal["context_tier_zone"] == "NORMAL (<70%)"

    # Tier 2: Elevated (70-80%) -> PREWARM_GREEN
    res_elevated = evaluator.evaluate_level_3({"context_saturation_pct": 74, "git_uncommitted_lines": 20})
    assert res_elevated["verdict"] == "PREWARM_GREEN"
    assert res_elevated["context_tier_zone"] == "ELEVATED (70-80%)"

    # Tier 3: Critical (>80%) -> SWAP_MANDATORY
    res_critical = evaluator.evaluate_level_3({"context_saturation_pct": 85, "git_uncommitted_lines": 20})
    assert res_critical["verdict"] == "SWAP_MANDATORY"
    assert res_critical["context_tier_zone"] == "CRITICAL (>80%)"

