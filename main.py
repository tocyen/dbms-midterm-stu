import psycopg2
from module.connect import DB_CURSOR
from midterm.Q1 import SQL1
from midterm.Q2 import SQL2
from midterm.Q3 import SQL3
from midterm.Q4 import SQL4
from midterm.Q5 import SQL5
from midterm.Q6 import SQL6
from midterm.Q7 import SQL7
from midterm.Q8 import SQL8

# Q1

if not SQL1:
    print("SQL1 empty")

else:
    print("-------Question 1--------")

    result = DB_CURSOR(SQL1)


    if result is not None:

        with open("result/Q1.result", "w+") as f1:

            for item in result:
                print(item)

                f1.write(str(item))
            f1.close()
    else:
        with open("result/Q1.result", "w+") as f1:
            f1.write("None")
            f1.close()

##########
# Q2

if not SQL2:
    print("SQL2 empty")

else:
    print("-------Question 2--------")
    result = DB_CURSOR(SQL2)


    if result is not None:
        with open("result/Q2.result", "w+") as f2:

            for item in result:
                print(item)

                f2.write(str(item))
            f2.close()
    else:
        with open("result/Q2.result", "w+") as f2:
            f2.write("None")
            f2.close()
##########
# Q3

if not SQL3:
    print("SQL3 empty")

else:
    print("-------Question 3--------")

    result = DB_CURSOR(SQL3)

    if result is not None:
        with open("result/Q3.result", "w+") as f3:

            for item in result:
                print(item)

                f3.write(str(item))
            f3.close()
    else:
        with open("result/Q3.result", "w+") as f3:
            f3.write("None")
            f3.close()
##########
# Q4

if not SQL4:
    print("SQL4 empty")

else:
    print("-------Question 4--------")

    result = DB_CURSOR(SQL4)

    if result is not None:
        with open("result/Q4.result", "w+") as f4:

            for item in result:
                print(item)

                f4.write(str(item))
            f4.close()
    else:
        with open("result/Q4.result", "w+") as f4:
            f4.write("None")
            f4.close()
##########
# Q5

if not SQL5:
    print("SQL5 empty")

else:
    print("-------Question 5--------")

    result = DB_CURSOR(SQL5)

    if result is not None:
        with open("result/Q5.result", "w+") as f5:

            for item in result:
                print(item)

                f5.write(str(item))
            f5.close()
    else:
        with open("result/Q5.result", "w+") as f5:
            f5.write("None")
            f5.close()
##########
# Q6

if not SQL6:
    print("SQL6 empty")

else:
    print("-------Question 6--------")

    result = DB_CURSOR(SQL6)

    if result is not None:
        with open("result/Q6.result", "w+") as f6:

            for item in result:
                print(item)

                f6.write(str(item))
            f6.close()
    else:
        with open("result/Q6.result", "w+") as f6:
            f6.write("None")
            f6.close()
##########
# Q7

if not SQL7:
    print("SQL7 empty")

else:
    print("-------Question 7--------")

    result = DB_CURSOR(SQL7)

    if result is not None:
        with open("result/Q7.result", "w+") as f7:

            for item in result:
                print(item)

                f7.write(str(item))
            f7.close()
    else:
        with open("result/Q7.result", "w+") as f7:
            f7.write("None")
            f7.close()
##########
# Q8

if not SQL8:
    print("SQL8 empty")

else:
    print("-------Question 8--------")

    result = DB_CURSOR(SQL8)

    if result is not None:
        with open("result/Q8.result", "w+") as f8:

            for item in result:
                print(item)

                f8.write(str(item))
            f8.close()
    else:
        with open("result/Q8.result", "w+") as f8:
            f8.write("None")
            f8.close()
##########
