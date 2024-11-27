# Read x lines looping over the file object

import timeit

file = 'sshd.cnf'
x1 = 20
b1 = 600

def read_x_lines(filenm, x):
    result = ''
    with open(filenm, 'r', encoding='utf-8') as f:
        for i, ln in enumerate(f):
            # print(i, '->', ln, end='')      # e/line contains an EOL
            result += (str(i) + ' -> ' + ln)
            if i == x:
                break
    return result


def read_x_bytes(filenm, bytes):
    with open(filenm, 'r', encoding='utf-8') as f:
        return f.readlines(bytes)
        

# Measure the time of both functions
t_read_x_lines = timeit.timeit('rln = read_x_lines(file, x1)', globals=globals(), number=1000)
t_read_x_bytes = timeit.timeit('rby = read_x_bytes(file, b1)', globals=globals(), number=1000)

print(f"Execution time of read_x_lines(): {t_read_x_lines} s.")
print(f"Execution time of read_x_bytes(): {t_read_x_bytes} s.")

rln = read_x_lines(file, x1)
print(rln)
rby = read_x_bytes(file, b1)
print(rby)



### Comparing times - fastened - velocity



# # Rutina 1: Usando un bucle for          
# def rutina_1():
#     result = []
#     for i in range(1000):
#         result.append(i * 2)
#     return result

# # Rutina 2: Usando lista por comprensión
# def rutina_2():
#     return [i * 2 for i in range(1000)]


# # Medir el tiempo de la rutina 1
# tiempo_rutina_1 = timeit.timeit('rutina_1()', globals=globals(), number=10000)

# # Medir el tiempo de la rutina 2
# tiempo_rutina_2 = timeit.timeit('rutina_2()', globals=globals(), number=10000)

# print(f"Tiempo de ejecución de rutina 1: {tiempo_rutina_1} segundos")
# print(f"Tiempo de ejecución de rutina 2: {tiempo_rutina_2} segundos")





# # Esto lo puedes usar directamente en un entorno como IPython o Jupyter Notebook

# # Medir el tiempo de ejecución de rutina_1
# %timeit rutina_1()

# # Medir el tiempo de ejecución de rutina_2
# %timeit rutina_2()
