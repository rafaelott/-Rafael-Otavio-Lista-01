import random


def insertionSort(arr):
    deslocamentos = 0
    n = len(arr)

    print("Array de entrada:", arr)
    print("Passos:")

    for i in range(1, n):
        valor_atual = arr[i]
        j = i - 1
        deslocamento_local = 0

        while j >= 0 and arr[j] > valor_atual:
            arr[j + 1] = arr[j]
            j -= 1
            deslocamentos += 1
            deslocamento_local += 1

        arr[j + 1] = valor_atual

        if deslocamento_local > 0:
            print("→", arr, f"→ deslocamento {deslocamento_local}")

    print(f"Total: {deslocamentos} deslocamentos\n")
    return deslocamentos


def gerenate_random_array(size, min_val=1, max_val=100):
    return [random.randint(min_val, max_val) for _ in range(size)]


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        result = insertionSort(arr)
        print("Deslocamentos realizados:", result)


if __name__ == '__main__':
    main()
