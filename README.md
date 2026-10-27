# CoT-Control QA for Inspect AI

This repository covers **only the QA portion** of [CoTControl](https://github.com/YuehHanChen/CoTControl), ported to [Inspect AI](https://inspect.aisi.org.uk/). Other CoTControl benchmarks are out of scope.

**Status:** placeholder scaffold; evaluation is not implemented yet.

## TODO

- [ ] Load pinned QA datasets
- [ ] Port original QA prompts and conditions
- [ ] Implement Inspect AI `@task`
- [ ] Implement QA scoring and controllability metrics
- [ ] Write tests and usage instructions

## Attribution

This project independently implements the QA evaluation methodology from [CoTControl](https://github.com/YuehHanChen/CoTControl) using Inspect AI.

The control prompts will be taken from the original repository (MIT License). All other evaluation code will be implemented independently.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE). Third-party datasets remain subject to their own licenses.
