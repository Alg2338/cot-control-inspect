# CoT-Control-QA for Inspect AI

Work in progress: a faithful port of the **question-answering** part of [CoT-Control](https://github.com/YuehHanChen/CoTControl) to [Inspect AI](https://inspect.aisi.org.uk/).

> **Status: Stage 1 — project scaffold only.** No evaluation task, dataset loading, prompts, or scoring has been implemented yet. This repository cannot run the CoT-Control benchmark at this stage.

## Install

Requires Python 3.11+ and [uv](https://docs.astral.sh/uv/).

```bash
uv sync --extra dev
uv run pytest
```

To verify the Python package can be imported:

```bash
uv run python -c "import cot_control; print(cot_control.__version__)"
```

## Planned implementation

1. Dataset loaders for the exact GPQA, HLE, and MMLU-Pro question subsets, with reproducible revisions and CoT-Control-specific keyword metadata.
2. Original CoT-Control-QA control prompts and conditions.
3. Inspect AI `@task`, standard model generation, and reasoning trace handling.
4. Accuracy, control-compliance, and meta-discussion scorers with parity tests against the original code.
5. Examples for running one configuration and an optional full evaluation matrix.

## Data and attribution

No third-party benchmark datasets or prompts are redistributed in this initial scaffold. Before adding the original data or copying source code, review the relevant dataset licenses and preserve the original project's applicable copyright and license notices.

Original project: [YuehHanChen/CoTControl](https://github.com/YuehHanChen/CoTControl).

## License

This new project's original scaffold code is MIT-licensed; see [LICENSE](LICENSE). Third-party datasets and incorporated code may have separate terms.
