from utils import get_input

input = get_input('input.txt')[0]

def get_memory_representation(input):
    input = input
    length = len(input)
    print(f"Input: {input} \nLength: {length}")
    memory = []
    for idx, i in enumerate(input):
        block_id = 0 if idx == 0 else idx // 2
        if idx % 2 == 0:
            memory.append(str(block_id)*int(i))
        else:
            if not (i == '0' or i == 0):
                memory.append('.'*int(i))
    return memory

memory_representation = "".join(get_memory_representation(input))
print(f"Memory Representation: {memory_representation} \n")

memory_representation_list = list(memory_representation)

while "." in memory_representation_list:
    last_element = memory_representation_list.pop()
    ptr_dot = memory_representation_list.index(".")
    memory_representation_list[ptr_dot] = last_element

memory_representation = "".join(memory_representation_list)
print(f"Memory Representation: {memory_representation} \n")

total = 0

for idx, mem in enumerate(list(map(int, memory_representation_list))):
    total +=idx*mem
print(f"Total: {total}")
