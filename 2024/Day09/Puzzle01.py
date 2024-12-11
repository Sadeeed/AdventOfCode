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
            # memory.append(str(block_id)*int(i))
            for _ in range(int(i)):
                memory.append(str(block_id))
        else:
            if not (i == '0' or i == 0):
                # memory.append('.'*int(i))
                for _ in range(int(i)):
                    memory.append(".")
                    
    return memory

# memory_representation = "".join(get_memory_representation(input))
memory_representation = get_memory_representation(input)
print(f"Memory Representation: {"".join(memory_representation)} \n")

# memory_representation_list = list(memory_representation)

while "." in memory_representation:
    try:
        last_element = memory_representation.pop()
        ptr_dot = memory_representation.index(".")
        memory_representation[ptr_dot] = last_element
    except ValueError:
        break

# memory_representation = "".join(memory_representation)
print(f"Memory Representation: {"".join(memory_representation)} \n")

total = 0
for idx, mem in enumerate(list(map(int, memory_representation))):
    total += idx*mem
print(f"Total: {total}")
