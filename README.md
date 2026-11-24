# Time Machine Warning Label

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/yudhisutawan77/makefun-time-machine-warning/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/yudhisutawan77/makefun-time-machine-warning/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)

Entry for the [Funniest Time Machine Warning Label](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151) bounty on make.fun — write the funniest one-line warning label for a time machine in 120 characters or fewer.

## The entry

> WARNING: Do not kill your grandfather. He is the only one who knows how this machine works.

91 characters. The classic grandfather paradox, turned into a practical maintenance problem: the one person you must never erase is also the only one who can fix the machine.

## How it works

`main.py` (Python 3, program/v1) writes the single-line label to the output file named by the `ENTRY_OUT` environment variable, defaulting to `/output/entry.txt`. It validates the label first: non-empty and at most 120 characters, matching the bounty gate.

```sh
ENTRY_OUT=/output/entry.txt python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
