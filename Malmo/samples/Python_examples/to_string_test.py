# --------------------------------------------------------------------------------------------------------------------
# Copyright (C) Microsoft Corporation.  All rights reserved.
# --------------------------------------------------------------------------------------------------------------------
# Similar to run_mission.py, but tests the Python _str_ bindings.

import MalmoPython
import os
import random
import sys
import time

sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately

agent_host = MalmoPython.AgentHost()
print agent_host

try:
    agent_host.parse( sys.argv )
except RuntimeError as e:
    print 'ERROR:',e
    print agent_host.getUsage()
    exit(1)
if agent_host.receivedArgument("help"):
    print agent_host.getUsage()
    exit(0)

my_mission = MalmoPython.MissionSpec()
my_mission.timeLimitInSeconds( 10 )
my_mission.requestVideo( 320, 240 )
my_mission.rewardForReachingPosition( 19, 0, 19, 100.0, 1.1 )
print my_mission

my_mission_record = MalmoPython.MissionRecordSpec("./saved_data.tgz")
my_mission_record.recordCommands()
my_mission_record.recordMP4(20, 400000)
my_mission_record.recordRewards()
my_mission_record.recordObservations()
print my_mission_record

try:
    agent_host.startMission( my_mission, my_mission_record )
except RuntimeError as e:
    print "Error starting mission:",e
    exit(1)

print "Waiting for the mission to start",
world_state = agent_host.getWorldState()
while not world_state.is_mission_running:
    time.sleep(0.1)
    world_state = agent_host.getWorldState()
    print world_state
    for error in world_state.errors:
        print "Error:",error.text
print

# main loop:
while world_state.is_mission_running:
    agent_host.sendCommand( "move 1" )
    agent_host.sendCommand( "turn " + str(random.random()*2-1) )
    time.sleep(0.5)
    world_state = agent_host.getWorldState()
    print world_state
    for reward in world_state.rewards:
        print reward
    for frame in world_state.video_frames:
        print frame
    for obs in world_state.observations:
        print obs
    for error in world_state.errors:
        print "Error:",error.text

print "Mission has stopped."