class Coins:
    def moedas(n):
        moeda1 = n // 1
        n = n - moeda1*1
        moeda1=float('%.2f'% moeda1)
        n=float('%.2f'% n)

        moeda50 = n // 0.5
        n = n - moeda50*0.5
        moeda50=float('%.2f'% moeda50)
        n=float('%.2f'% n)

        moeda25 = n // 0.25
        n = n - moeda25*0.25
        moeda25=float('%.2f'% moeda25)
        n=float('%.2f'% n)

        moeda10 = n // 0.10
        n = n - moeda10*0.10
        moeda10=float('%.2f'% moeda10)
        n=float('%.2f'% n)

        moeda5 = n // 0.05
        n = n - moeda5*0.05
        moeda5=float('%.2f'% moeda5)
        n=float('%.2f'% n)

        moeda1c = n * 100
        moeda1c=float('%.2f'% moeda1c)
        n=float('%.2f'% n)
        return ('{} moeda(s) de R$ 1.00 {} moeda(s) de R$ 0.50 {} moeda(s) de R$ 0.25 {} moeda(s) de R$ 0.10 {} moeda(s) de R$ 0.05 {} moeda(s) de R$ 0.01'.format(int(moeda1), int(moeda50), int(moeda25), int(moeda10), int(moeda5), int(moeda1c)))
        

if __name__ == "__main__":
    n = input("Digite um valor para trocar: \n")
    try:
        n = float(n)
        Coins.moedas(n)
    except ValueError:
        n = n.replace(",", '.')
        Coins.moedas(float(n))
