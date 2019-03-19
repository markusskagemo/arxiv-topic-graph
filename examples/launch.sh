#!/bin/sh

cd ..
google-chrome http://localhost:7676/arxiv-topic-graph/graph.html
python3 -m http.server 7676

