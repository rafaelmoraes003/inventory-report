from inventory_report.inventory.product import Product


def test_relatorio_produto():
    coffee = Product(
        id=1,
        nome_do_produto="Coffee",
        nome_da_empresa="Nature Coffees",
        data_de_fabricacao="2020-07-04",
        data_de_validade="2023-02-09",
        numero_de_serie="FR48",
        instrucoes_de_armazenamento="In a cool and dry place",
    )

    coffee_data = str(coffee)

    assert (isinstance(coffee_data, str)) is True
    assert (coffee_data) == (
        "O produto Coffee fabricado em 2020-07-04 por Nature Coffees "
        "com validade até 2023-02-09 precisa ser "
        "armazenado In a cool and dry place."
    )
