def default():
    print("Groundfruit Cereal (cereal)\n")
    print("Usage:\n   cereal <command>\n")
    print("Available Commands:")
    print("  ports     Get a list of all the available COM ports.")
    print("  serial\tStart a serial monitor.")
    print("  version\tShows the CLI version number")

def serial():
    print("Usage: cereal serial <port> <baud_rate>")
    print("Example: cereal serial COM3 9600")