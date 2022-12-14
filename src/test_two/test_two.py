"""
Write a function that takes as arguments two arrays of integers. 
Your function needs to determine whether the second array is contained in the first one, returning true or false;
"""

def contains_second_array(array_one, array_two):
        
        for item in array_two:
            try:
                array_one.index(item)
            except ValueError:
                return False
        return True



if __name__=="__main__":

        array_one = [5, 1, 22, 25, 6, -1, 8, 10]
        array_two = [1, 6, -1, 10]

        print(contains_second_array(array_one, array_two))