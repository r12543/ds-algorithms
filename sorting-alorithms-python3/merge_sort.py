def MergeSort(array):
  """ Function to sort an array using merge sort algorithm """
  if len(array) == 0 or len(array) == 1:
    return array
  else:
    middle = len(array)//2
    array1 = MergeSort(array[:middle])
    array2 = MergeSort(array[middle:])
    return merge(array1, array2)

def merge(array1, array2):
  """ Function to merge two arrays """
  temp = []
  while len(array1) != 0 and len(array2) != 0:
    if array1[0] < array2[0]:
      temp.append(array1[0])
      array1.remove(array1[0])
    else:
      temp.append(array2[0])
      array2.remove(array2[0])
  if len(array1) == 0:
    temp += array2
  else:
    temp += array1
  return temp
