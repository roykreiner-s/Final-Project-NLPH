import sys


def run_text(text):
    # todo handle it
    return "passed through python successfully" + text


def main():
    print(run_text(sys.argv[1]))


if (len(sys.argv) < 1):
    raise Exception("No Arguments")
main()
