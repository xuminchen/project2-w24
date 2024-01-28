from DictionaryBST import *
import time, random
import matplotlib.pyplot as plt
print("\n Welcome to Dictionary Application 2")
print("======================================\n")

# instantiate new BST database
dict = DictionaryBST()

# load dictionaries into BST
while True:
    name = input("Enter dictionary name (english,french,spanish,short,tiny,etc.): ")
    if name == "": break
    dict.load(name)  # add dictionary to the BST

# display some info
print("\nThe size of the BST is " + str(dict.getSize()) + " with " + str(dict.getMaxLevel()) + " level(s)")

# extract list of Word objects
mylist = dict.extractInOrder()
time_M_result = []
time_N_result = []

random.seed(7)  # initialize the seed for random reproducibility

plot_type = input("plot type:")
if str(plot_type) == 'M':
    for nrnd in range(10000,99171):
        # Generate nrnd random list of words
        rndlist = []
        for i in range(nrnd): rndlist.append(random.choice(mylist).getWord())

        # BST search
        print()
        startTime = time.process_time()  # capture time
        i = 0
        for w in rndlist:  # randomly search words and display the first 10
            word = dict.search(w)
            if i < 10: print("<<%s>> found in BST: %s" % (w, word))
            i += 1
        endTime = time.process_time()  # capture time
        ms = (endTime - startTime) * 1000
        time_M_result.append(ms)
        print("Time: " + str(ms) + " ms to search " + str(nrnd) + " words")


    plt.plot(range(10000,99171), time_M_result)
    plt.xlabel('M-random words')
    plt.ylabel('Times')
    plt.title('Time vs M PLOT')
    plt.show()

elif str(plot_type) == 'N':
    nrnd = int(input("How many random words would you like to search?: "))
    