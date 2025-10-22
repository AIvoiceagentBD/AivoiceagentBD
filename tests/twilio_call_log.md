# Twilio Call Test Log - October 22, 2025

## Activities Done
- Created Twilio account and received free credits.
- Set up Twilio project and verified number.
- Wrote Python script to initiate a voice call.
- First call succeeded.
- Second call failed — likely due to rapid repeated call triggering Bangladesh carrier spam filter.

## Observations
- Twilio successfully connects to Bangladeshi carriers.
- Rapid repeated calls can be blocked; adding delay or retry logic needed.

## Next Steps
- Add retry logic with `time.sleep(30)` between calls.
- Log each call attempt and response.
- Test with more varied phone numbers.
