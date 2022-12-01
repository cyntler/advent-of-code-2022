import sys
import importlib
import os.path


def main():
    args = sys.argv[1:]

    if len(args) == 0:
        print("You must to provide the day's name to get the result!")
        exit(1)

    name = args[0]

    try:
        mod = importlib.import_module("day_tasks." + name)
        if hasattr(mod, "execute"):
            dirname = os.path.dirname(__file__)
            input_path = os.path.join(dirname, "assets/" + name + "_input.txt")
            if os.path.exists(input_path):
                f = open(input_path, "r")
                lines = f.readlines()
                f.close()

                result = mod.execute(lines)
                if result:
                    print("Result:", result)
            else:
                print("The input data for task named ", name, "does not exist!")

    except ModuleNotFoundError:
        print("The task named", name, "does not exist!")
        pass


if __name__ == "__main__":
    main()
