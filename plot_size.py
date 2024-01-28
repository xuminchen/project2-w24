from DictionaryBST import *
import time, random
import matplotlib.pyplot as plt

print("\n Welcome to Dictionary Application 2")
print("======================================\n")

dict_size = []
time_result = []
ds = {
    "english": ["english"],
    "french": ["french"],
    "spanish": ["spanish"],
    "english+french": ["english","french"],
    "english+spanish": ["english","spanish"],
    "french+spanish": ["french","spanish"],
    "english+french+spanish":["english", "french", "spanish"]
}


for d in ds.keys():

    # instantiate new BST database
    dict = DictionaryBST()

# load dictionaries into BST
# while True:
#     name = input("Enter dictionary name (english,french,spanish,short,tiny,etc.): ")
#     if name == "": break
    for name in ds[d]:
        dict.load(name)  # add dictionary to the BST
    dict_size.append(f"{d}({str(dict.getSize())})")
# display some info
# print("\nThe size of the BST is " + str(dict.getSize()) + " with " + str(dict.getMaxLevel()) + " level(s)")

# extract list of Word objects
    mylist = dict.extractInOrder()
#     nrnd = int(input("How many random words would you like to search?: "))
    nrnd = 50000
# Generate nrnd random list of words
    random.seed(7)  # initialize the seed for random reproducibility
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
    time_result.append((endTime - startTime) * 1000)
    print("Time: " + str((endTime - startTime) * 1000) + " ms to search " + str(nrnd) + " words")
# plt.plot(dict_size, time_result)

# plt.show()

fig, ax = plt.subplots()
ax.plot(dict_size, time_result)
plt.subplots_adjust(bottom=0.5)
plt.xlabel('dictionary and size')
plt.xticks(rotation=45)
plt.ylabel('Times')
plt.title('Time vs N-size PLOT')

plt.show()