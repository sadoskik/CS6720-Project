Internet Architecture and Protocols Project
# Summary
This project simulates three packet scheduling algorithms WFQ, WF2Q, and WRR. Each algorithm is fed packets by the orchestrator.py file. The intention is to standarize the testing of these algorithms, so that they may be directly compared.

# Algorithms
## WFQ - Weighted Fair Queueing
## WF2Q - Worst-case Fair Weighted Fair Queueing
## WRR - Weighted Round Robin

# Use
Parameters should only be modified in orchestrator. The current capabilities limits the number of simulated input ports (queues) to four. Run the project as such `python orchestrator.py`.