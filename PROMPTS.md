# How This Was Built: Prompt Summary

This doc captures the design spec and the prompts used to build the Hurry Up Chicken Butt timer, plus short summaries of what each step produced. Use it to see how small, incremental prompts can grow a working app quickly.

---

## Design spec (DESIGN.md)

> # Hurry Up Chicken Butt Timer
>
> This is a timer for the game what's up chicken butt. We didn't have a battery for the real timer. Let's create a timer that is 60 seconds, and randomly plays one of the sound files throughout the timer. When the audio is done pick another one to play, and when the timer goes off play the singe click sound.
>
> Sounds are from pixabay.com
>
> For the UI just a simple webpage with a button to start the timer (but don't show how much time is left). Can play a light click every second to ensure it's working.

---

## Prompt 1

**Prompt:** “Look at @DESIGN.md and build the thang.”

**Result:** Single-file `index.html` with: 60s timer (no countdown), Start button, tick every second (Web Audio sine + small visual dot), random clucks from `clucks/` during the round, finish alarm when time’s up. Styling and layout in the same file.

---

## Prompt 2

**Prompt:** “Create a script I can run to access this on the local wifi from my phone via ip address”

**Result:** `serve.py` — Python HTTP server on `0.0.0.0:8000` that prints the machine’s local IP so you can open the app from a phone on the same Wi‑Fi. Uses `SimpleHTTPRequestHandler` with basic CORS/cache headers.

---

## Prompt 3

**Prompt:** “Oops I undid it, bring serve.py back - and add a way to restart the timer while it's running ("stop")”

**Result:** `serve.py` recreated as above. Timer UI: Stop button that appears while the timer is running; Stop clears the timer, stops ticks/clucks, and returns to “Ready to play?” so you can start again.

---

## Prompt 4

**Prompt:** “Also make the background flash red when it's done, and make the volume of the final sound 100% while the clucks during is 60%”

**Result:** When time’s up, `body` gets a class that runs a CSS animation alternating red backgrounds. Clucks use `audio.volume = 0.6`; finish alarm uses `volume = 1`.

---

## Prompt 5

**Prompt:** “also make the final one play 5 times to signify it's done”

**Result:** Finish alarm plays 5 times in sequence (each play waits for the previous to end). After the 5th, the usual “Ready to play again?” flow runs.

---

## Prompt 6

**Prompt:** “Make the timer easy to reconfigure by putting variable up top somewhere in the script”

**Result:** A `CONFIG` object at the top of the script with: timer duration, tick interval, cluck/finish volumes, finish play count, cluck delay range, and “ready again” delay. All behavior reads from `CONFIG` instead of literals.

---

## Prompt 7

**Prompt:** “Randomly pick betwen 45 sconds and 90 seconds instead of always 60”

**Result:** `CONFIG` now has `timerSecondsMin: 45` and `timerSecondsMax: 90`. On Start, duration is a random integer in that range (inclusive). Countdown still hidden.

---

## Prompt 8

**Prompt:** “Play a ding ding ding before the 5 clucks”

**Result:** When time’s up: three synthesized dings (Web Audio sine at 880 Hz) with configurable duration and gap, then the existing 5× finish clucks. New CONFIG keys: `dingCount`, `dingFrequency`, `dingDurationMs`, `dingGapMs`.

---

## Prompt 9

**Prompt:** “Write a simple README.md, then summarize this conversation (including DESIGN.md) into a PROMPTS.md (with quoted prompts and summarized LLM results) including this prompt so others can learn how we built this so quickly”

**Result:**  
- **README.md:** Short project description, feature list, how to run locally and via `serve.py`, where to change behavior (CONFIG), and note that sounds are from Pixabay.  
- **PROMPTS.md:** This file — DESIGN.md excerpt plus each prompt in quotes and a one-paragraph summary of what was built or changed, so others can see the step-by-step flow and reuse the pattern.

---

## Prompt 10

**Prompt:** “Change the alarm sound (not clucks but the sound before) to a buzzer sound like at a hockey game, but only one time for 2 seconds”

**Result:** The three dings were replaced with a single 2-second hockey-style buzzer: Web Audio square wave at 250 Hz for a harsh, arena-horn tone. CONFIG now has `buzzerDurationMs: 2000`, `buzzerFrequency: 250`, and `buzzerVolume: 0.4`. Flow is: buzzer (2 s) → 5 finish clucks (later changed to alarm.mp3 once — see Prompt 11).

---

## Prompt 11

**Prompt:** “OK new plan - use `alarm.mp3` instead of the 5 alarm sounds and chicken cluck”

**Result:** End-of-round sound is now a single play of `clucks/alarm.mp3` instead of 5× `cluck-alarm-finish.mp3`. Removed `finishPlays` from CONFIG. Flow is: buzzer (2 s) → alarm.mp3 once → “Ready to play again?” Chicken clucks during the round are unchanged.

---

## Prompt 12

**Prompt:** “Great. Let's make it mobile friendly and so it won't turn off the screen, update prompts.md and readme.md and we're good to go”

**Result:** **Mobile-friendly:** viewport-fit=cover, theme-color and apple-mobile-web-app meta tags; safe-area padding; responsive typography and padding with `clamp()`; touch-friendly buttons (min-height 48px, touch-action: manipulation, -webkit-tap-highlight-color: transparent); -webkit-fill-available for min-height on iOS. **Screen wake lock:** when the timer starts, `navigator.wakeLock.request('screen')` keeps the display on; released when the round ends (alarm finished or Stop). Visibility-change listener re-requests the lock when the user returns to the tab and the timer is still running. README and PROMPTS updated (features, Quick start, Prompt 12, Takeaway).

---

## Takeaway

One design doc plus twelve short, focused prompts produced a working game timer with: random duration, ticks, clucks during the round, single alarm (alarm.mp3), red flash, Stop button, CONFIG-driven behavior, a script to use it on a phone, mobile-friendly layout, and screen wake lock so the display stays on during a round. Keeping each prompt to a single concern made it easy to iterate and extend without rewriting the whole app.
