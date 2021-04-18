from subprocess import check_output, CalledProcessError, STDOUT

def turnTVOn():
    command = ["./turnTVOn.sh"]
    try:
        output = check_output(command, stderr=STDOUT).decode()
        success = True
        return str(output)
    except CalledProcessError as e:
        output = e.output.decode()
        success = False