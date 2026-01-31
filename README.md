# Hurry Up Chicken Butt Timer

A web timer for the “What’s Up Chicken Butt?” game. No battery required—run it in a browser. Works great on phones: mobile-friendly layout and screen stays on while the timer is running.

## Features

- Random duration between 45–120 seconds (no countdown shown)
- Light tick every second so you know it’s running
- Random chicken clucks during the round
- Alarm sound (`alarm.mp3`) when time’s up
- Red flashing background when the timer ends
- Stop button to reset and start again
- **Mobile-friendly:** responsive layout, touch-friendly buttons, safe-area padding for notched devices
- **Screen wake lock:** display stays on during a round (when supported by the browser)

## Quick start

**Local:** Open `index.html` in a browser.

**On your phone (same Wi‑Fi):** Run the server on your computer, then open the URL it prints in your phone’s browser (e.g. `http://192.168.1.x:8000`). The screen will stay on while the timer is running.

```bash
python3 serve.py
```

Stop the server with `Ctrl+C`.

## Reconfiguring

Edit the `CONFIG` object at the top of the `<script>` in `index.html` to change:

- `timerSecondsMin` / `timerSecondsMax` — duration range
- `cluckVolume` / `finishVolume` — volume levels
- `buzzerDurationMs`, `buzzerFrequency`, `buzzerVolume` — buzzer before alarm
- `cluckDelayMinMs` / `cluckDelayMaxMs` — delay between clucks
- `readyAgainDelayMs` — delay before “Ready to play again?”

## Sounds

Cluck and alarm files live in `clucks/` (including `alarm.mp3` for the end-of-round sound). Sounds are from [Pixabay](https://pixabay.com).
