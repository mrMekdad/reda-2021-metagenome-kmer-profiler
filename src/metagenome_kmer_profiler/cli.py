import argparse
from metagenome_kmer_profiler.core import build_snapshot


def main() -> None:
    parser = argparse.ArgumentParser(description="Exploration project for k-mer profiles and sample-level comparative summaries.")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    if args.summary:
        print(build_snapshot())


if __name__ == "__main__":
    main()
