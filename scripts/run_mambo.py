#!/usr/bin/env python3
import os
import sys
import pathmagic
import json

from sympy import cofactors
with pathmagic.context():
    from MamboControllerInterface import MamboControllerInterface


if __name__ == "__main__":
    # load mambo index from command line arguments
    if len(sys.argv) == 2:
        mambo_idx = sys.argv[1]
    else:
        mambo_idx = 1

    # load the configuration as a dictionary

    # for Real-time-Task-Allocation-and-Path-Planning
    # config_file_name = "config_aimslab.json"

    # # for learning from directional correction
    # config_file_name = os.path.expanduser("~") + \
    #     "/Learning-from-Directional-Corrections/experiments/config_aimslab.json"
    
    # For Formation Control
    # config_file_name = "config_aimslab_" + mambo_idx + ".json"
    # realtime
    config_file_name = os.path.expanduser("~") + \
        "/tianyu/Reinforcement-Learning-for-Multi-agent-Formation-Control/experiment/config_aimslab_" + \
        str(mambo_idx) + ".json"

    # config_file_name = os.path.expanduser("~") + \
    #     "/github/DrMaMP-Distributed-Real-time-Multi-agent-Mission-Planning-Algorithm/experiment/config_aimslab_ex_" + \
    #     str(mambo_idx) + ".json"

    mocap_string = "QUALISYS"

    Controller = MamboControllerInterface(config_file_name, mocap_string)
    Controller.run_controller()
