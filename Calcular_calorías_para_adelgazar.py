def consumo_calorias_recomendado_para_adelgazar(peso: float,altura: float,edad: int,valor_genero: float) -> str:
  
    tmb = (10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero

    minimo = round(tmb * 0.80, 2)
    maximo = round(tmb * 0.85, 2)


    return (
        f"Para adelgazar es recomendado que consumas "
        f"entre: {minimo} y {maximo} calorías al día."
    )

