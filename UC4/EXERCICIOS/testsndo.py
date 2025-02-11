def senso_academia():
    clientes = {}
    print("Digite os dados dos clientes (Código, Altura e Peso). Digite 0 no código para encerrar.")

    while True:
        codigo = int(input("Código do cliente: "))
        if codigo == 0:
            break
        altura = float(input("Altura do cliente (em metros): "))
        peso = float(input("Peso do cliente (em kg): "))
        clientes[codigo] = {'altura': altura, 'peso': peso}

    if not clientes:
        print("Nenhum dado foi inserido.")
        return

    # Encontrar o mais alto, mais baixo, mais gordo e mais magro
    mais_alto = max(clientes.items(), key=lambda x: x[1]['altura'])
    mais_baixo = min(clientes.items(), key=lambda x: x[1]['altura'])
    mais_gordo = max(clientes.items(), key=lambda x: x[1]['peso'])
    mais_magro = min(clientes.items(), key=lambda x: x[1]['peso'])

    # Calcular médias
    total_altura = sum(cliente['altura'] for cliente in clientes.values())
    total_peso = sum(cliente['peso'] for cliente in clientes.values())
    media_altura = total_altura / len(clientes)
    media_peso = total_peso / len(clientes)

    # Exibir resultados
    print("\nResultados do Senso:")
    print(f"Mais alto: Código {mais_alto[0]}, Altura {mais_alto[1]['altura']}m")
    print(f"Mais baixo: Código {mais_baixo[0]}, Altura {mais_baixo[1]['altura']}m")
    print(f"Mais gordo: Código {mais_gordo[0]}, Peso {mais_gordo[1]['peso']}kg")
    print(f"Mais magro: Código {mais_magro[0]}, Peso {mais_magro[1]['peso']}kg")
    print(f"Média de altura: {media_altura:.2f}m")
    print(f"Média de peso: {media_peso:.2f}kg")

# Executar o programa
senso_academia()
