The idea is based on smart home system. If the smart phone is connected to home WiFi, it means the man is at home. If the man is at home and it's at night, the night mode is on. If the man turn on the lights, it should be warm lights. If the screen is off, and it is detected that the man is on bed, and night mode is on, the man is sleeping. Then, all the lights should be turned off.

Example:

kb> load a4_q2_kb.txt
at_home <-- connected_to_home_wifi
night_mode <-- at_home & night
warm_lights <-- night_mode & turn_on_lights
sleeping <-- screen_off & night_mode & on_bed
turn_off_lights <-- sleeping

5 new rule(s) added

kb> tell night
"night" added to KB
kb> tell connected_to_home_wifi turn_on_lights
"connected_to_home_wifi" added to KB
"turn_on_lights" added to KB

kb> infer_all
Newly inferred atoms:
   at_home, night_mode, warm_lights
Atoms already known to be true
   night, connected_to_home_wifi, turn_on_lights

kb> tell screen_off on_bed
"screen_off" added to KB
"on_bed" added to KB

kb> infer_all
Newly inferred atoms:
   sleeping, turn_off_lights
Atoms already known to be true
   night, connected_to_home_wifi, turn_on_lights, at_home, night_mode, warm_lights, screen_off, on_bed