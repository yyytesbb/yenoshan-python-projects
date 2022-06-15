import random
import string

def passwords(text, length, amount):
    # password = ""
    file = ""
    for x in range(amount):
        password = f"".join(random.sample(text, length)) 
        file += f"{x+1}-> {password} \n"
    return file


letters = string.ascii_letters
symbols = "!@#$%^&*()_+|*<>?[]{}~`\\:';/.,=-"
nums = string.digits

text = "".join(letters+symbols+nums)

length = int(input("Length of each password: "))
amount = int(input("Total number of passwords: "))
print("\nGenerated Passwords.....\n")
print(passwords(text, length, amount))

save = input("Save to a file? [Y/N]: ").lower()
file_exists = False

if save in ['y', "yes"]:
    file_name = input("File name: ")

    try:
        open(file_name, "x")
    except FileExistsError:
        print(f"\nFile '{file_name}' already exists.")
        print("what do you want to do: ")
        print(f"\t[1]: Overwrite file {file_name}\n\t\t>> WARNING: All data in {file_name} will be erased.\n\t[2]: Append file {file_name}")
        try:
            do = int(input(">> "))
        except ValueError:
            print("Enter a valid digit..")
            exit()

        match do:
            case 1:
                file = open(file_name, 'w')
                file.write(passwords(text, length, amount))
                file.close()
                print("Writing complete")
            case 2:
                file = open(file_name, 'a')
                file.write(passwords(text, length, amount))
                file.close()
                print("Done appending")
            case default:
                exit()

        file_exists = True
else:
    file_exists = True

if file_exists == False:

    file = open(file_name, "w")
    file.write(passwords(text, length, amount))
    file.close()
    print("Password(s) stored in \'" + file_name + "\'\n")
    