import math
import os


shuffled_log = "comparisons/sample/logn_shuffled_list_%.2d.pkl"
shuffled = "comparisons/sample/shuffled_list_%.2d.pkl"

kths = {'5': lambda n: 5,
       'logn': lambda n: int(math.log(n)),
       'sqrt': lambda n: int(math.sqrt(n)),
       'n/2': lambda n: n/2}

data = {"n": [2000, 4000, 8000, 16000, 32000, 64000, 128000, 256000, 512000, 1024000, 2048000, 4096000, 8192000, 16384000, 32768000],
        "kth_by_extreme": [],
        "kth_by_sorting": [],
        "kth_by_mom": [],
        "kth_by_quickselect": []}

final_data = {}

for shuffle_type in [shuffled_log, shuffled]:
    print "\n\n\n##################\nshuffle type %s" % shuffle_type
    final_data[shuffle_type] = {}
    for kth in kths:
        final_data[shuffle_type][kth] = data
        print "\n\n-----------------\nkth %s" % kth
        for method in ["kth_by_extreme", "kth_by_sorting", "kth_by_mom", "kth_by_quickselect"]:
            print "\nmethod: %s" % method
            for i in xrange(1, 16):
                n = (1000 * 2 ** i)
                k = kths[kth](n)
                cmd = "python -m comparisons.compare_selection %d %s %s" % (k, shuffle_type % i, method)
                stdout_handle = os.popen(cmd, "r")
                text = stdout_handle.read().strip("\n")
                print "%d, %s" % (n, text)
                time = float(text)
                final_data[shuffle_type][kth][method].append(time)

print "--------------"
print final_data

