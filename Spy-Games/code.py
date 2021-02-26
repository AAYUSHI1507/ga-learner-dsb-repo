# --------------

def read_file(path):
    # open file in read mode
    file = open(path,mode ='r')

    # iterate over the file object
    for i in file.readlines():
        sentence = i
    # close the file
    file.close()
    return sentence

sample_message = read_file(file_path)


# --------------
#Code starts here
message_1 = read_file(file_path_1)
message_2 = read_file(file_path_2)

#Display message 1 and 2
print(message_1)
print(message_2)

# Creating function...fuse_msg
def fuse_msg(message_a,message_b):
    message_a = int(message_a)
    message_b = int(message_b)
    quotient = message_b//message_a
    quotient = str(quotient)
    return quotient

secret_msg_1 = fuse_msg(message_1,message_2)


# --------------
#Code starts here

# Creating substitute_msg function...
def substitute_msg(message_c):
    if message_c == 'Red':
        sub = 'Army General'
    elif message_c == 'Green':
        sub = 'Data Scientist'
    elif message_c == 'Blue':
        sub = 'Marine Biologist'
    return sub

message_3 = read_file(file_path_3)
print(message_3)

secret_msg_2 = substitute_msg(message_3)
print(secret_msg_2)


# --------------
# File path for message 4  and message 5
file_path_4
file_path_5

#Code starts here

# Creating Function compare_msg()...
def compare_msg(message_d,message_e):
    a_list = message_d.split()
    b_list = message_e.split()
    c_list = [i for i in a_list if i not in b_list]
    final_msg = " ".join(c_list)
    return final_msg

# storing the message
message_4 = read_file(file_path_4)
message_5 = read_file(file_path_5)

# Display message_4 and 5
print(message_4)
print('='*50)
print(message_5)
print('='*50)

# display secret_msg_3
secret_msg_3 = compare_msg(message_4,message_5)
print(secret_msg_3)


# --------------
#Code starts here

# Creating a Function extract_msg 
def extract_msg(message_f):
    a_list = message_f.split()

    even_word = lambda x : (len(x) % 2 == 0)
    # splitting the message in to list
    b_list = (filter(even_word, a_list))
    final_msg = " ".join(b_list)
    return final_msg

# message_6 = file_path_6
message_6 = read_file(file_path_6)
print(message_6)
print('='*50)

# Storing the return value in secret_msg_4
secret_msg_4 = extract_msg(message_6)

# Displaying the secret msg
print(secret_msg_4)


# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]
secret_msg = " ".join(message_parts)

# create function write_file
def write_file(secret_msg,path):

    #opening the file for appending
    file = open(path,mode ='a+')

    #writing in the file 
    file.write(secret_msg)

    #closing the file
    file.close()

final_path= user_data_dir + '/secret_message.txt'
write_file(secret_msg,final_path)
print(secret_msg)


