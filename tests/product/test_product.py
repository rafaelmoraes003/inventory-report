from inventory_report.inventory.product import Product


def test_cria_produto():
    chocolate = Product(
        id=1,
        nome_da_empresa="Nestlé",
        nome_do_produto="Chocolate",
        data_de_fabricacao="2023-01-01",
        data_de_validade="2025-01-01",
        numero_de_serie="12345678",
        instrucoes_de_armazenamento="In a cool and dry place",
    )

    assert (chocolate.id) == 1
    assert (chocolate.nome_da_empresa) == "Nestlé"
    assert (chocolate.nome_do_produto) == "Chocolate"
    assert (chocolate.data_de_fabricacao) == "2023-01-01"
    assert (chocolate.data_de_validade) == "2025-01-01"
    assert (chocolate.numero_de_serie) == "12345678"
    assert (chocolate.instrucoes_de_armazenamento) == "In a cool and dry place"

    assert (chocolate.data_de_fabricacao) != "01/01/2023"
    assert (chocolate.data_de_validade) != "01/01/2025"
