# Frequenz channels Release Notes

## Summary

The main change in this release is the introduction of the `OneshotChannel` and `BroadcastChannel` classes, and the deprecation of the `Broadcast` and `Anycast` classes.

## Upgrading

- `LatestValueCache` now closes the receiver when it is stopped.

- Fetching values from stopped `LatestValueCache` instances is now disallowed.

- The old `Broadcast` class is deprecated in favour of the new auto-closing `BroadcastChannel`.

- The `Anycast` class is deprecated, because of the lack of use-cases and the maintenance cost.

## New Features

- There's a new `OneshotChannel`, which returns a sender and a receiver.  A single message can be sent using the sender, after which it will be closed.  And the receiver will close as soon as the message is received.

- `Sender`s now have an `aclose`, which must be called, when they are no-longer needed.

- There's a new `BroadcastChannel`, which returns a broadcast sender and a broadcast receiver.  The channel is auto-closing, meaning when all the senders or all the receivers are closed, the channel is closed.
