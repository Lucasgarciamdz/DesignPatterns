from power import Device, TurnOnCommand, TurnOffCommand
from remote_control import RemoteControl


def main():
    device = Device()
    turn_on = TurnOnCommand(device)
    turn_off = TurnOffCommand(device)

    remote = RemoteControl()

    print(remote.submit(turn_on))
    print(remote.submit(turn_off))


if __name__ == "__main__":
    main()
