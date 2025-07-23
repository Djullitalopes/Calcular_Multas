def calcular_multa_localidade(velocidade):
    if velocidade >= 120:
        return 320
    elif velocidade >= 90:
        return 120
    elif velocidade > 50:
        return 60
    else:
        return 0


def verificar_velocidade():
    print("Verificador de Velocidade")
    
    print("\nonde circula o veiculo:")
    print("1 - Localidade ")
    print("2 - Fora da localidade")
    print("3 - Autoestrada")

    tipo_zona = input("Digite o número correspondente: ")

    if tipo_zona == "1":
        limite = 50
        zona = "Localidade"
    elif tipo_zona == "2":
        limite = 90
        zona = "Fora da localidade"
    elif tipo_zona == "3":
        limite = 120
        zona = "Autoestrada"
    else:
        print("Opção inválida.")
        return

    try:
        velocidade = float(input(f"\nIntroduza a velocidade do carro na {zona}: "))
    except ValueError:
        print("Por favor, insira um número válido para a velocidade.")
        return

    print(f"\nZona: {zona}")
    print(f"Velocidade registada: {velocidade:.1f} km/h")
    print(f"Limite permitido: {limite} km/h")

    if velocidade > limite:
        excesso = velocidade - limite
        print(f"Excedeu o limite de velocidade em {excesso:.1f} km/h. vais receber uma multa!")

        if zona == "Localidade":
            multa = calcular_multa_localidade(velocidade)
            if multa > 0:
                print(f"Multa a pagar: {multa}€")
    else:
        print("Está dentro do limite permitido.")


verificar_velocidade()