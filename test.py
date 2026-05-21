from rich import print

# for style in [0, 1]:  # 0: normal, 1: bold/bright
#     for fg in range(30, 38):
#         for bg in range(40, 48):
#             code = f"{style};{fg};{bg}"
#             print(f"\033[{code}m {code} \033[0m", end=" ")
#         print()  # Newline after each row
#     print()  # Extra newline between normal and bold


print(
    "[bold red] Hey there!! this is some text ![/bold red] \n [black on white] is this black on white eH? ![/black on white]"
)
