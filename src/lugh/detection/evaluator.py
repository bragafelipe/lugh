def evaluate_underutilized(cpu_avg_percent: float, mem_avg_percent: float, cpu_threshold: float = 10.0, mem_threshold: float = 20.0) -> bool:
    """Return True when both CPU and memory are below configured thresholds."""
    return cpu_avg_percent < cpu_threshold and mem_avg_percent < mem_threshold
