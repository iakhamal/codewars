#You have been hired by a major MP3 player manufacturer to implement a new music compression standard. In this kata you will implement the ENCODER, and its companion kata deals with the DECODER. It can be considered a harder version of Range Extraction.



def compress(numbers):
    result = []
    i = 0
    while i < len(numbers):
        start = numbers[i]
        end = start
        count = 1
        step = None
        j = i + 1
        while j < len(numbers):
            if numbers[j] == end + 1:
                end = numbers[j]
            elif step is None and numbers[j] == end:
                count += 1
            elif step is None and count > 1:
                result.append(str(start) + ',' + str(start + count - 1))
                i = j - 1
                break
            elif step is None and count == 1:
                result.append(str(start))
                i = j - 1
                break
            elif numbers[j] == end - step:
                end = numbers[j]
            else:
                if count > 1:
                    result.append(str(start) + '-' + str(end))
                else:
                    result.append(str(start))
                if step is not None:
                    result[-1] += '/' + str(step)
                i = j - 1
                break
            j += 1
        else:
            if count > 1:
                result.append(str(start) + '-' + str(end))
            else:
                result.append(str(start))
            if step is not None:
                result[-1] += '/' + str(step)
            i = j
    return ','.join(result)



"""Specification
The input signal is represented as an array of integers. Several cases of regularities can be shortened.

A sequence of 2 or more identical numbers is shortened as number*count
A sequence of 3 or more consecutive numbers is shortened as first-last. This is true for both ascending and descending order
A sequence of 3 or more numbers with the same interval is shortened as first-last/interval. Note that the interval does NOT need a sign
Compression happens left to right
Examples
[1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20] is compressed to "1,3-5,7-11,14,15,17-20"
[0, 2, 4, 5, 7, 8, 9] is compressed to "0-4/2,5,7-9"
[0, 2, 4, 5, 7, 6, 5] is compressed to "0-4/2,5,7-5"
[0, 2, 4, 5, 7, 6, 5, 5, 5, 5, 5] is compressed to "0-4/2,5,7-5,5*4"
Input
A non-empty array of integers

Output
A string of comma-separated integers and sequence descriptors"""

