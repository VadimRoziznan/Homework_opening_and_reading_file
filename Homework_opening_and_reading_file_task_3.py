import os

with open('1.txt', encoding='utf-8') as file_1,\
     open('2.txt', encoding='utf-8') as file_2,\
     open('3.txt', encoding='utf-8') as file_3:

     file_1 = file_1.read()
     file_2 = file_2.read()
     file_3 = file_3.read()

def sort_and_save(file_1, file_2, file_3):
     with open('4.txt', 'w'):
          pass
     sorted_list1 = sorted([file_1, file_2, file_3], reverse=True)
     with open('4.txt', 'a') as common_file:
          for file in sorted_list1:
               if file == file_1:
                    name = os.path.basename(r'1.txt')
                    len_file = file_1.count('\n') + 1
               elif file == file_2:
                    name = os.path.basename(r'2.txt')
                    len_file = file_2.count('\n') + 1
               elif file == file_3:
                    name = os.path.basename(r'3.txt')
                    len_file = file_3.count('\n') + 1
               common_file.write(f"{name}\n\n{len_file}\n\n{file}\n\n")
     return f'Операции выполнена'

print(sort_and_save(file_1, file_2, file_3))


