from prefect import task

@task(name="Calculo de factorial")
def factorial_task(numero):
    factorial = 1
    for i in range(1, numero+1):
        factorial = factorial*i
    return factorial

@task(name="Suma")
def suma_task(factorial):
    suma = factorial + 10
    return suma


