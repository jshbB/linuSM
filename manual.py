class what:
    def cmd(cmd):
        cmd = str(cmd)
        if cmd.startswith("ls"):
            return "Shows files present in the directory"
        elif cmd.startswith("shout"):
            return "Shout, a print statement in linuSM"
            return "(See our documentation on github to know more on how to use shout)"
        elif cmd.startswith("neofh"):
            return "Neofetch, Shortened for ease. Uses neofetch.";
            return "(See our documentation on github to know more on how to use neofh)"
        elif cmd.startswith("clear"):
            return "Clear\n- Clear the terminal instance"
            return "(See our documentation on github to know more on how to use clear)"
        elif cmd.startswith("cls"):
            return "Clear the terminal instance"
        return f"LSM: unknown command {cmd}"