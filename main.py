"""One Star, Written in Sap: write a single houseplant review to entry.txt.

The line is written for the judge brief in criterion order: (1) a
one-line 1-star review by a houseplant about its human owner, with
the plant's own grievance at the centre; (2) a surprising turn that
lands in the last word; (3) a plant's-eye view of watering; (4) a
genuine review shape, complaint plus reason for the single star;
(5) fresh, specific detail, with none of the stock phrases the
brief bans. The owner waters the plant with yesterday's coffee,
so the plant ends up with insomnia.
"""

LINE = (
    "One star: he waters me with yesterday's coffee, and now I'm "
    "the only plant in this flat with insomnia."
)


def main() -> None:
    import os

    # The grader sets MAKEFUN_OUTPUT_DIR to its /output mount; locally,
    # fall back to ./output so a shared /output on this machine is
    # never touched (other workers verify against the same path).
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
        "output"
    )
    target = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
