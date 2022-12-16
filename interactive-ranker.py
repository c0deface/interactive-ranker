import sys
import tkinter as tk

window = tk.Tk(className='Interactive Ranker')
window.geometry("1000x500")

startFrame = tk.Frame(window)
startFrame.pack()

intro = tk.Label(startFrame, text="Pick which one you like more each time", font=("Helvetica", 32))
intro.pack()

LEFT_CLICKED = False
RIGHT_CLICKED = False
var = tk.IntVar()

def leftClicked():
    global LEFT_CLICKED
    global RIGHT_CLICKED
    LEFT_CLICKED = True
    RIGHT_CLICKED = False
    var.set(var.get()+1)

def rightClicked():
    global LEFT_CLICKED
    global RIGHT_CLICKED
    RIGHT_CLICKED = True
    LEFT_CLICKED = False
    var.set(var.get()+1)

def defaultButtons():
    LEFT_CLICKED = False
    RIGHT_CLICKED = False

def betterThanGUI(a, b):
    decisionFrame = tk.Frame(window)
    decisionFrame.pack()
    
    left = tk.Button(
        decisionFrame,
        text=a,
        width=25,
        height=25,
        command=leftClicked
    )
    left.pack(side=tk.LEFT)

    right = tk.Button(
        decisionFrame,
        text=b,
        width=25,
        height=25,
        command=rightClicked
    )
    right.pack(side=tk.LEFT)

    defaultButtons()

    decisionFrame.wait_variable(var)
    decisionFrame.destroy()

    if LEFT_CLICKED:
        return True
    else:
        return False
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2 # Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves
        
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if betterThanGUI(L[i], R[j]):
                arr[k] = L[i] 
                i+= 1
            else:
                arr[k] = R[j] 
                j+= 1
            k+= 1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+= 1
            k+= 1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+= 1
            k+= 1

def startProgram():
    startFrame.destroy()

    intro = tk.Label(window, text="Which one do you like more?", font=("Helvetica", 32))
    intro.pack()

    filename = sys.argv[1]
    f = open(filename, "r")
    arr = f.read().splitlines()

    import random
    random.shuffle(arr)
    
    mergeSort(arr)

    intro.destroy()
    output = ""
    colArr = []
    index = 1
    resultFrame = tk.Frame(window)
    resultFrame.pack()
    
    for i in arr:
        output += "{0}. {1}\n".format(index, i)
        if index % 20 == 0:
            col = tk.Label(
                resultFrame,
                text=output,
                anchor='w',
                font=("Helvetica", 16)
            )
            col.pack(side=tk.LEFT)
            output = ""
        index += 1

    if output != "":
        col = tk.Label(
            resultFrame,
            text=output,
            anchor='w',
            font=("Helvetica", 16)
        )
        col.pack(side=tk.LEFT)
    
start = tk.Button(
    startFrame,
    text="Start!",
    width=50,
    height=25,
    command=startProgram
)
start.pack()

window.mainloop()
