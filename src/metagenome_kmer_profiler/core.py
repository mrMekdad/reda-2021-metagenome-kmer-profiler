"""Core workflow for Metagenome Kmer Profiler by Red@."""

PROJECT_NAME = "Metagenome Kmer Profiler"
DOMAIN_THEME = "bioinformatics"


def build_snapshot() -> dict[str, str]:
    return {"project": PROJECT_NAME, "author": "Red@", "theme": DOMAIN_THEME}
