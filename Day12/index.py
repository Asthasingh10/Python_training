
def average_marks(marks:list[float])->float:
    count=0
    for i in marks:
        count+=i
    avg=count/len(marks)
    return avg
print(average_marks([1,2,3]))