from IPython.display import clear_output

def display_progress(ind, tot, limiter): 
    if ind % limiter == 0: 
        bar = ["-" for spc in range(10)]
        fill = int(ind / tot * 10) 
        if fill > 0: 
            for f in range(fill): 
                bar[f] = "x"
        clear_output(wait=True)
        print("[" + "".join(bar) + "]")
    elif (ind) == tot: 
        print("[" + "".join(["x" for x in range(10)]) + "]")
