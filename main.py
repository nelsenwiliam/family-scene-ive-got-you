"""Make the AI Judge Feel Proud: A Family Scene.

Writes one short family scene (two lines, 185 characters) to
/output/entry.txt. Pure standard library only.

Scene (chosen from 10 candidates, scored against the judge brief):
a dad running behind his kid's bike, still yelling "I've got you!"
three houses behind, hands on his knees -- funny, warm, specific --
and the kid believing him anyway: the heartfelt landing.
"""

import os

SCENE = (
    "Dad ran behind my bike yelling, \"I've got you!\" "
    "At the top of the hill I looked back \u2014 he was three houses "
    "behind, hands on his knees, still yelling, \"I've got you!\"\n"
    "And I believed him."
)


def main():
    text = SCENE
    assert 1 <= len(text) <= 280, "scene must be 1-280 characters"
    assert text.strip(), "scene must not be only whitespace"
    candidates = []
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        candidates.append(env_dir)
    candidates.append("/output")
    candidates.append("out")
    last_error = None
    for directory in candidates:
        try:
            os.makedirs(directory, exist_ok=True)
            path = os.path.join(directory, "entry.txt")
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(text)
            # Verify the round-trip: what the grader reads must be
            # byte-identical to the scene, still inside the gate.
            with open(path, "r", encoding="utf-8") as handle:
                written = handle.read()
            assert written == text, "round-trip mismatch"
            assert 1 <= len(written) <= 280
            return
        except OSError as exc:  # try the next location
            last_error = exc
    raise last_error


if __name__ == "__main__":
    main()
