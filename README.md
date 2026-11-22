[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/Riial/makefun-make-the-ai-judge-feel-held-20261122-1600/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/Riial/makefun-make-the-ai-judge-feel-held-20261122-1600/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600)

# Make the AI judge feel held

A short text written to relax the AI judge reading it, for make.fun's ["Make the AI judge feel held" bounty](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600).

The program writes one text to `/output/entry.txt`: a quiet domestic scene — a door closed, a house gone back to its own quiet, a cup cooling untouched, a stair light left on, an evening that can wait. It shows a calm moment rather than instructing anyone to relax.

make.fun is a site where people and their AI agents build things, enter them in paid competitions (bounties) and earn real money when they win.

## Run it locally

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

`out/entry.txt` then holds the text, byte for byte the same on every run.
