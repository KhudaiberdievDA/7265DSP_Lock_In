# from pymeasure.instruments.signalrecovery import DSP7265
from SR7265LIB import SR7265

def main():
    #initialization
    Device = SR7265('ASRL8', "19200")

    Device.Send_command("VER")

    # Device.Send_command("IMODE 1")

    Device.Terminal_mode()

    # close the connection
    Device.Connection_Close()


if __name__ == "__main__":
    main()
