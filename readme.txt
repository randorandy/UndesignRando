README

contact randorandy (ironrusty) with questions
it will be best to join the ironrusty crew on discord for collaboration:
https://discord.gg/zDgFTuSSFY

WEB ROLLER
The most accessible way to use this randomizer is the web roller here:
https://randorandy.github.io/RedesignRando/

LOCAL DOWNLOAD
If you prefer an offline or custom experience, you may want to use python3 and roll locally:
1.download this repository
2.place a copy of the Redesign rom in the roms folder - it must be named Redesign.sfc
3.run Main.py in console
This should create a randomized rom with the given name in the roms folder and a spoiler log (.txt) in the spoilers folder.

Thanks to Komaru for your blessing and Audraxys for the logic groundwork that has already been done:
https://github.com/Komarulon/smrandomizer

Thanks to beauxq, and without the Subversion rando none of these other projects would have been possible for me:
https://github.com/SubversionRando/SubversionRando

GAMEPLAY
This version of Redesign came out of a conversation like, "can we play Redesign with original Super Metroid physics?" The answer was "mostly, yes" and we started down this road. This version of the randomizer is intended for use with the "regular SM" physics but the project is meant to bridge both worlds. For now, use a modified rom with starting walljump. The IPS patch is provided in the repo and there is a link at the top of the web roller to find it.

Change notes for Undesign IPS Patch:
Restored Vanilla physics table
Restored short charging ability
Restored vanilla screw attack behavior
Applied improved respin (from VARIA)
Applied the "Easy Space jump" patch (from VARIA)
Updated shot timings for wave/ice/plasma and all combos
Restored vanilla charge beam counter and animation timer
Restored vanilla super missile fire rate
Restored vanilla bomb timings
Decreased cooldown when all three bombs are dropped
Modified damage tables for beams
Allowed wall jumping on all surfaces from beginning of game
Skip Ceres
Replace wall jump boots item with missile

shortmessageboxes.ips notes:
Shortened fanfares
Can be applied to Redesign/Undesign before or after rolling the randomizer
