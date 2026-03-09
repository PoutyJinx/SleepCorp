# SleepCorp — SIN Corporation Sleep Tracking Cog

SleepCorp is a themed sleep tracking cog for **Red Discord Bot** that allows users to log when they go to bed and when they wake up.  
The bot calculates total sleep time and generates a **SIN Corporation style sleep report** with star ratings and humorous corporate comments.

Instead of boring sleep logs, SleepCorp turns your community's sleep habits into a **corporate incident report from the depths of SIN Corp**.

---

## Features

• `/sleep` — Log when you went to bed  
• `/awake` — Log when you woke up and receive a sleep report  
• `/bedtime` — Check the last recorded bedtime for a user  

The bot calculates:

- total sleep duration
- a 0–5 star sleep rating
- a randomized SIN Corp evaluation message

All responses are written in **SIN Corporation style**, including HR commentary, castle status updates, and corporate sleep evaluations.

---

## Example Output

🌙 **SIN CORP SLEEP EVALUATION**

Employee: @User  
Bedtime: 04:37  
Wake Time: 11:52  
Duration: 7.2 hours  

Rating: ★★★☆☆  

"Questionable timing, acceptable recovery."

HR Notes:  
Castle bats confirm irregular sleep cycles.  
Coffee reserves have been authorized.

---

## Requirements

- Red Discord Bot
- Downloader cog enabled

---

## Installation

Run the following commands in your Discord server where your Red Discord Bot is installed.

[p]repo add sleepcorp https://github.com/PoutyJinx/SleepCorp
[p]repo install sleepcorp sleepcorp
[p]load sleepcorp
[p]slash enablecog SleepCorp
[p]slash sync
