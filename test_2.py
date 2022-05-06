"""
The program is trying to display the number of grades, the average grade, 
and the percentage of grades that are above the average grade in a final exam.
We first read in text file final.txt
then from the text file, we create a list of integer from each lines of the text file
We create a dictionary from the list.
Once the text file has been read into memory, we close the file.
The grades in text file will be imported to the program.
The program will read the input text file to assign the grades to a list of integer.

We then define a function that calculate the number of grades
then, calculate the average grade which take the total grade / number of grades
we convert the output of average grade to float
then, we define a function that calculate the percentage of grades that are above the average grade
we convert the output of the  percentage of grades that are above the average grade to float and add percentage

Print out the calculated value to the assigned variable.
"""


"""
import final.txt
main():
  set dictionary = create_dictionary ("final.txt")
  num_grades = formListofGrades (dictionary)
  avg_grade = createAverageGrade (num_grades)
  calculate_percent_above_average = createPercentAboveAverage (avg_grade)

def create_dictionary("final.txt"):
  read in final.txt
  create list = each line from the text file
  close the file
  create dict off the list
  return dict

def num_grades(dictionary):
    calculate the total number
    print number of grades

def avg_grade(num_grades):
    calculate avg = total grade / number of grades
    print avg grade

def calculate_percent_above_average(avg_grade):
    calculate percentage = (total grades > avg) / number of grades
    print percentage grade above the avg 

main()
"""



def main():
  file = "Final.txt"
  calculate_percent_above_average(file)

def calculate_percent_above_average(file):
    infile = open(file, 'r')
    listGrades = [int(line.rstrip()) for line in infile]
    infile.close()
    length = len(listGrades)
    sum1= sum(listGrades)
    avg = sum1 / length
    print("Number of grades: ", length)
    print("Average grade: ", avg)
    counter = 0
    for item in listGrades:
        if item > avg:
            counter += 1
    percentHigher = counter / length
    print("Percentage of grades above the average grade: ", end= " ")
    print("{0:.2%}".format(percentHigher))

main()