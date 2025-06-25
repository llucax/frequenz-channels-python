# License: MIT
# Copyright © 2024 Frequenz Energy-as-a-Service GmbH

"""Tests for the RelaySender class."""

from contextlib import ExitStack

from frequenz.channels import Broadcast
from frequenz.channels.experimental import RelaySender


async def test_tee_sender(stack: ExitStack) -> None:
    """Test tee sender."""
    channel1: Broadcast[int] = Broadcast(name="channel1")
    channel2: Broadcast[int] = Broadcast(name="channel2")
    channel3: Broadcast[int] = Broadcast(name="channel3")

    sender = RelaySender(
        channel1.new_sender(), channel2.new_sender(), channel3.new_sender()
    )

    receiver1 = stack.enter_context(channel1.new_receiver())
    receiver2 = stack.enter_context(channel2.new_receiver())
    receiver3 = stack.enter_context(channel3.new_receiver())

    await sender.send(42)
    assert (
        await receiver1.receive()
        == await receiver2.receive()
        == await receiver3.receive()
        == 42
    )

    await sender.send(-2)
    assert (
        await receiver1.receive()
        == await receiver2.receive()
        == await receiver3.receive()
        == -2
    )
