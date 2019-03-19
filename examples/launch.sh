#!/bin/sh

chmod a+rx launch.sh

echo python3 -m SimpleHTTPServer 8181
echo google-chrome http://localhost:8181/Documents/GitHub/arxiv-topic-graph/arxiv-topic-graph/graph.html

