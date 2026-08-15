from lugh.detection.evaluator import evaluate_underutilized


def test_underutilized_true_when_both_below_thresholds():
    assert evaluate_underutilized(5.0, 10.0) is True


def test_underutilized_false_when_cpu_high():
    assert evaluate_underutilized(25.0, 10.0) is False
