// --------------------------------------------------------------------------------------------------------------------
// Copyright (C) Microsoft Corporation.  All rights reserved.
// --------------------------------------------------------------------------------------------------------------------

// Local:
#include "WorldState.h"

namespace malmo
{
    WorldState::WorldState()
        : is_mission_running( false )
        , number_of_video_frames_since_last_state(0)
        , number_of_rewards_since_last_state(0)
        , number_of_observations_since_last_state(0)
    {
    }
    
    void WorldState::clear()
    {
        this->is_mission_running = false;
        this->number_of_observations_since_last_state = 0;
        this->number_of_rewards_since_last_state = 0;
        this->number_of_video_frames_since_last_state = 0;
        this->observations.clear();
        this->rewards.clear();
        this->video_frames.clear();
        this->mission_control_messages.clear();
        this->errors.clear();
    }
}