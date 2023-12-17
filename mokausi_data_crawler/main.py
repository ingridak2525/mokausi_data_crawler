import cProfile, pstats


def creat_list():
    return list(range (10000))

def main():
     print ("hello")
# This is a sample Python script.
cProfile.run("main()")
profiler=cProfile.Profile()
profiler.enable()
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
main()
profiler.disable()
stats=pstats.Stats(profiler).sort_stats()
stats.print_stats()
#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
 #   print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
