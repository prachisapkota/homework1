print("What type of calculator do you want to use? ")
print("A. Basic calculator ")
print("B. Scientific calculator ")

input1 = input("\tSelect what type of operation you want to use \tA\tB\t")

if input1 == 'A':
    print("Please select the operation. ")
    print("\t1. Addition.")
    print("\t2. Subtraction.")
    print("\t3. Division.")
    print("\t4. Multiplication.")
    print("\t5. Calculation of powers.")
    print("\t6. Square roots.")
    print("\t7. Cube roots.")
    print("\t8. Modulus.\n")

    input2 = input("What type of operation do you want to perform? \t1\t2\t3\t4\t5\t6\t7\t\n")

    if input2 == '1':
        print("\tFor Addition operation: \n")
        first_num = float(input("\tEnter the first one"))
        second_num = float(input("\tEnter the second one"))
        add = float(first_num + second_num)
        print("\t",first_num, "+", second_num, "=", add)
    elif input2 == '2':
        print("\tFor Subtraction operation: \n")
        first_num = float(input("\tEnter the first one"))
        second_num = float(input("\tEnter the second one"))
        subtract = float(first_num - second_num)
        print("\t",first_num, "-", second_num, "=", subtract)
    elif input2 == '3':
        print("\tFor Division operation: \n")
        first_num = float(input("\tEnter the first one"))
        second_num = float(input("\tEnter the second one"))
        division = float(first_num / second_num)
        print("\t",first_num, "/", second_num, "=", division)
    elif input2 == '4':
        print("\tFor Multiplication operation: \n")
        first_num = float(input("\tEnter the first one"))
        second_num = float(input("\tEnter the second one"))
        multiply = float(first_num * second_num)
        print("\t",first_num, "*", second_num, "=", multiply)
    elif input2 == '5':
        print("\tFor Calculation of power form: \n")
        first_num = float(input("\tEnter the first one"))
        second_num = float(input("\tEnter the second one"))
        power = float(first_num.__pow__(second_num))
        print("\t",first_num, "^", second_num, "=", power)
    elif input2 == '6':
        print("\tFor Square root operation: \n")
        num = float(input("\tEnter the number"))
        sq_root = float((num.__pow__(2)))
        print("\tThe square root of %s is %s " %(num, sq_root))
    elif input2 == '7':
        print("\tFor Cube root operation: \n")
        num = float(input("\tEnter the number"))
        cube_root = float(num.__pow__(3))
        print("\tThe cube root of %s is %s " %(num, cube_root))
    elif input2 == '8':
        print("\tFor Modulus operation: \n")
        first_num = float(input("\tEnter the first one"))
        second_num = float(input("\tEnter the second one"))
        mod = float(first_num.__mod__(second_num))
        print("\t",first_num, "%", second_num, "=", mod)
    else:
        print("\tYou have entered wrong format ")
elif input1 == 'B':
    print("Please select the operation.")
    print("1. HCF")
    print("2. LCM")
    print("3. Celsius to Fahrenheit.")
    print("4. Fahrenheit to Celsius.\n")

    input3 = input("What type of operation do you want to perform? \t1\t2\t3\t4\t5\t6\t7\t\n ")
    if input3 == '1':
        print("\tFor HCF: \n")
        num1 = int(input("\tEnter the first number"))
        num2 = int(input("\tEnter the second number"))
        while num1%num2 !=0:
            rem=num1%num2
            num1=num2
            num2=rem

        print("\tThe required HCF is: ", num2)
    elif input3 == '2':
        print("\tFor LCM: \n")
        num1 = int(input("\tEnter the first number"))
        num2 = int(input("\tEnter the second number"))
        for m in range (1, num1 *num2):
            if m%num1 ==0 and m%num2 ==0:
                print("The required LCM is", m)
                break
    elif input3 == '3':
        print("\tFor Conversion: \n")
        print("Celsius to Fahrenheit ")
        celsius=int(input("enter the temperature in celsius"))
        f=(celsius*1.8)+32
        print("Temperature in fahrenheit is:", f)
    elif input3 == '4':
        print("\tFor Conversion: \n")
        print("Fahrenheit to celsisus ")
        fe=int(input("enter the temperature in Fahrenheit"))
        ce=(fe-32)/1.8
        print("Temperature in celsius is:", ce)