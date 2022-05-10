from pywebio.input import input, FLOAT
from pywebio.output import put_text

def bmi():
    height = input("Coloque sua altura(cm)：", type=FLOAT)
    weight = input("Coloque seu peso(kg)：", type=FLOAT)

    BMI = weight / (height / 100) ** 2

    top_status = [(16, 'Muito abaixo do peso'), (18.5, 'Abaixo do peso'),
                  (25, 'Normal'), (30, 'Sobrepeso'),
                  (35, 'Moderadamente obeso'), (float('inf'), 'Obeso mórbido')]

    for top, status in top_status:
        if BMI <= top:
            put_text('Seu IMC: %.1f. Categoria: %s' % (BMI, status))
            break

if __name__ == '__main__':
    bmi()